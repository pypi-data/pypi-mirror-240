from abc import ABC, abstractmethod
import decimal
from decimal import Decimal
from enum import Enum
import math

ASSET_SEPARATOR = "-"


class OrderSide(Enum):
    BUY = 0
    SELL = 1

    def __json__(self):
        return self.name

    def __neg__(self):
        if self == self.BUY:
            return OrderSide.SELL
        return OrderSide.BUY


class OrderType(Enum):
    UNSUPPORTED = 0
    MARKET = 1
    LIMIT = 2
    STOP_LOSS = 3

    def __json__(self):
        return self.name


class MarketPosition(Enum):
    FLAT = 0
    LONG = 1
    SHORT = 2

    def __neg__(self):
        if self == self.LONG:
            return MarketPosition.SHORT
        elif self == self.SHORT:
            return MarketPosition.LONG
        return MarketPosition.FLAT

    def __json__(self):
        return self.name


class BasicTradingIndicator:
    def __init__(
        self,
        time: float,
        direction: MarketPosition,
        price: float = None,
        leverage: float = 1,
        averaging_factor: float = 1,
        take_profit: float = 0,
        meta_data: dict = None,
    ):
        if leverage <= 0:
            raise ValueError("leverage must be greater than 0.")
        if averaging_factor <= 0:
            raise ValueError("averaging_factor must be greater than 0.")
        if (take_profit < 0) or (take_profit > 1):
            raise ValueError("take_profit must be between 0 and 1 inclusive.")
        self.time = time
        self.direction = direction
        self.price = price
        self.leverage = leverage
        self.averaging_factor = averaging_factor
        self.take_profit = take_profit
        self.meta_data = meta_data

    def __eq__(self, other):
        if other is self:
            return True
        if isinstance(other, BasicTradingIndicator):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    def __json__(self):
        return self.__dict__


class BasicTradingIndicatorSource(ABC):
    INDICATOR_SOURCE_NAME = None

    def __init__(self):
        super().__init__()
        if self.INDICATOR_SOURCE_NAME is None:
            raise TypeError(
                f"Cannot instantiate class {self.__class__.__name__} "
                "without INDICATOR_SOURCE_NAME."
            )

    @abstractmethod
    def get_indicator(
        self,
        sample_time: float,
        base_asset: str,
        quote_asset: str,
    ) -> BasicTradingIndicator | None:
        pass

    def get_indicators(
        self,
        sample_time: float,
        asset_pairs: list[tuple[str, str]],
    ) -> dict[tuple[str, str], BasicTradingIndicator] | None:
        results = {}
        for asset_pair in asset_pairs:
            base_asset, quote_asset = asset_pair
            indicator = self.get_indicator(sample_time, base_asset, quote_asset)
            if indicator:
                results[asset_pair] = indicator
        return results

    @abstractmethod
    async def get_indicator_async(
        self,
        sample_time: float,
        base_asset: str,
        quote_asset: str,
    ) -> BasicTradingIndicator | None:
        pass

    async def get_indicators_async(
        self,
        sample_time: float,
        asset_pairs: list[tuple[str, str]],
    ) -> dict[tuple[str, str], BasicTradingIndicator] | None:
        results = {}
        for asset_pair in asset_pairs:
            base_asset, quote_asset = asset_pair
            indicator = await self.get_indicator_async(
                sample_time, base_asset, quote_asset
            )
            if indicator:
                results[asset_pair] = indicator
        return results


class TradingPolicy:
    def __init__(
        self,
        minimum_order_quantity: Decimal | float,
        maximum_order_quantity: Decimal | float = None,
        minimum_order_value: Decimal | float = None,
        maximum_order_value: Decimal | float = None,
        quantity_decimals: int = None,
        quantity_precision: Decimal = None,
        price_decimals: int = None,
        price_precision: Decimal = None,
    ):
        if quantity_precision is not None:
            quantity_precision = Decimal(quantity_precision)

        if price_precision is not None:
            price_precision = Decimal(price_precision)

        if (quantity_decimals is None) and quantity_precision:
            quantity_decimals = int(-math.log10(quantity_precision))
        self._quantity_decimals = quantity_decimals

        if (price_decimals is None) and price_precision:
            price_decimals = int(-math.log10(price_precision))
        self._price_decimals = price_decimals

        self._minimum_order_quantity = self.align_quantity(
            minimum_order_quantity, decimal.ROUND_UP
        )

        if maximum_order_quantity is not None:
            maximum_order_quantity = self.align_quantity(
                maximum_order_quantity, decimal.ROUND_DOWN
            )
        self._maximum_order_quantity = maximum_order_quantity

        if minimum_order_value is None:
            minimum_order_value = Decimal(0)
        else:
            minimum_order_value = self.align_price(
                minimum_order_value, decimal.ROUND_UP
            )
        self._minimum_order_value = minimum_order_value

        if maximum_order_value is not None:
            maximum_order_value = self.align_price(
                maximum_order_value, decimal.ROUND_DOWN
            )
        self._maximum_order_value = maximum_order_value

    @staticmethod
    def _align(value: Decimal | float | int, decimals: int | None, rounding) -> Decimal:
        value = Decimal(value)
        if decimals is not None:
            with decimal.localcontext() as ctx:
                ctx.rounding = rounding
                value = round(value, decimals)
        return value

    def align_quantity(
        self, quantity: Decimal | float | int, rounding=decimal.ROUND_DOWN
    ) -> Decimal:
        return self._align(quantity, self._quantity_decimals, rounding)

    def get_minimum_order_quantity(self, price: Decimal) -> Decimal:
        # Adjust slightly to prevent errors due to price fluctuations
        minimum_by_value = (self._minimum_order_value / price) * Decimal("1.01")

        if minimum_by_value > self._minimum_order_quantity:
            return self.align_quantity(minimum_by_value, decimal.ROUND_UP)
        else:
            return self._minimum_order_quantity

    def limit_quantity_maximum(
        self, quantity: Decimal | float | int, price: Decimal
    ) -> Decimal:
        if self._maximum_order_value is not None:
            # Adjust slightly to prevent errors due to price fluctuations
            maximum_by_value = (self._maximum_order_value / price) * Decimal("0.99")
            if quantity > maximum_by_value:
                quantity = maximum_by_value

        if (self._maximum_order_quantity is not None) and (
            quantity > self._maximum_order_quantity
        ):
            quantity = self._maximum_order_quantity

        return self.align_quantity(quantity)

    def align_price(
        self, price: Decimal | float | int, rounding=decimal.ROUND_HALF_EVEN
    ) -> Decimal:
        return self._align(price, self._price_decimals, rounding)

    def limit_value(self, value: Decimal) -> Decimal:
        if value < self._minimum_order_value:
            value = self._minimum_order_value
        if self._maximum_order_value is not None:
            if value > self._maximum_order_value:
                value = self._maximum_order_value
        return value

    def __json__(self):
        return self.__dict__


class Order:
    def __init__(
        self,
        base_asset: str,
        quote_asset: str,
        side: OrderSide,
        order_type: OrderType,
        creation_time: float,
        quantity: Decimal = None,
        amount: Decimal = None,
        price: Decimal = None,
        filled_quantity: Decimal = Decimal(0),
        meta_data: dict = None,
    ):
        if (quantity is None) and (amount is None):
            raise ValueError("quantity and amount cannot both be None.")
        if (quantity is not None) and (amount is not None):
            raise ValueError("quantity and amount both specified.")
        if quantity is not None:
            quantity = Decimal(quantity)
        if amount is not None:
            amount = Decimal(amount)
        if price is not None:
            price = Decimal(price)
        if filled_quantity is None:
            filled_quantity = Decimal(0)
        else:
            filled_quantity = Decimal(filled_quantity)
        self.base_asset = base_asset
        self.quote_asset = quote_asset
        self.side = side
        self.order_type = order_type
        self.creation_time = float(creation_time)
        self._quantity = quantity
        self._amount = amount
        self.price = price
        self.filled_quantity = filled_quantity
        self.meta_data = meta_data

    def get_quantity(self, quote_price: Decimal):
        if self._quantity is None:
            if self.price is None:
                return self._amount / quote_price
            else:
                return self._amount / self.price
        return self._quantity

    def __json__(self):
        return self.__dict__


class Exchange(ABC):
    EXCHANGE_NAME = None

    def __init__(self):
        super().__init__()
        if self.EXCHANGE_NAME is None:
            raise TypeError(
                f"Cannot instantiate class {self.__class__.__name__} "
                "without defining EXCHANGE_NAME."
            )
        self.short_selling_supported = False
        self.stop_loss_orders_supported = False

    @abstractmethod
    def get_quote(self, base_asset: str, quote_asset: str) -> Decimal:
        pass

    def get_quotes(
        self, asset_pairs: list[tuple[str, str]]
    ) -> dict[tuple[str, str], Decimal]:
        quotes = {}
        for asset_pair in asset_pairs:
            base_asset, quote_asset = asset_pair
            price = self.get_quote(base_asset, quote_asset)
            quotes[asset_pair] = price
        return quotes

    @abstractmethod
    def get_policy(self, base_asset: str, quote_asset: str) -> TradingPolicy:
        pass

    def get_policies(
        self, asset_pairs: list[tuple[str, str]]
    ) -> dict[tuple[str, str], TradingPolicy]:
        policies = {}
        for asset_pair in asset_pairs:
            base_asset, quote_asset = asset_pair
            policy = self.get_policy(base_asset, quote_asset)
            policies[asset_pair] = policy
        return policies

    @abstractmethod
    def get_positions(self) -> dict[str, Decimal]:
        """
        :return: dictionary with asset identifiers as keys and quantities as values
        Short positions are negative.
        """
        pass

    @abstractmethod
    def get_open_orders(self, base_asset: str, quote_asset: str) -> list[Order]:
        pass

    @abstractmethod
    def place_order(
        self,
        policy: TradingPolicy,
        base_asset: str,
        quote_asset: str,
        side: OrderSide,
        order_type: OrderType,
        quantity: Decimal,
        price: Decimal = None,
        stop_loss_price: Decimal = None,
        increasing_position: bool = None,
    ):
        """
        :param policy:
        :param base_asset:
        :param quote_asset:
        :param side:
        :param order_type:
        :param quantity:
        :param price: price for limit orders
        :param stop_loss_price: price for stop loss orders. For exchanges that support
        automatic stop losses, the stop loss price to use when market and limit orders
        are filled.
        :param increasing_position:
        """
        pass

    @abstractmethod
    def cancel_order(self, order: Order):
        pass

    def cancel_open_orders(self, base_asset: str, quote_asset: str):
        orders = self.get_open_orders(base_asset, quote_asset)
        for order in orders:
            self.cancel_order(order)


def normalize(value: str | int | float | Decimal) -> Decimal:
    _MAX_NORMALIZED_DIGITS = 6
    value = Decimal(value)
    value = Decimal(round(value, _MAX_NORMALIZED_DIGITS))
    return value.normalize()


def split_asset_pair(asset_pair: str) -> tuple[str, str]:
    assets = asset_pair.split(ASSET_SEPARATOR, 1)
    if len(assets) != 2:
        raise ValueError(
            f"asset_pair must contain two assets separated by {ASSET_SEPARATOR}."
        )
    return assets[0], assets[1]


def join_asset_pair(base_asset: str, quote_asset: str) -> str:
    return ASSET_SEPARATOR.join((base_asset, quote_asset))
