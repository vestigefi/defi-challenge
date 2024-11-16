from typing import TypeAlias

from algopy import ARC4Contract, BoxMap, Txn, Account
from algopy.arc4 import Struct, UInt16, UInt64, abimethod, DynamicArray, String, Address


class Order(Struct):
    amount: UInt64
    asset_id: UInt16
    limit_price: UInt16
    stop_price: UInt16
    status: String


User: TypeAlias = Account


class AtomTrade(ARC4Contract):
    orders: BoxMap[User, DynamicArray[Order]]
    tinyman_app_id: UInt16

    def __init__(self) -> None:
        self.orders = BoxMap(User, DynamicArray[Order], key_prefix="orders")

    @abimethod(create="require")
    def init(self, tinyman_app_id: UInt16) -> None:
        self.tinyman_app_id = tinyman_app_id

    @abimethod
    def register(self) -> None:
        """
        Registers the user for AtomTrade.

        If the user is already registered, does nothing.
        """
        if self.orders.maybe(Txn.sender)[1]:
            self.orders[Txn.sender] = DynamicArray[Order]()

    @abimethod
    def place_order(
        self, limit_price: UInt16, amount: UInt64, asset_id: UInt16, stop_price: UInt16
    ) -> UInt16:
        """
        Places a new order for the user.

        The order will be added with the specified limit price, amount, asset ID, and stop price.
        The status of the order is initially set to "open". If the current price is checked
        and found to be lower than the limit price, the order will be filled. If the current
        price is higher than the stop price, the order will be canceled.

        Returns:
            UInt16: The ID of the newly placed order.

        Raises:
            AssertionError: If the user is not registered.
        """
        assert self.orders.maybe(Txn.sender)[1], "User not registered"

        order = Order(
            limit_price=limit_price,
            amount=amount,
            asset_id=asset_id,
            stop_price=stop_price,
            status=String("open"),
        )

        # TODO: We check current price in tinyman or offchain if needed

        # TODO: If current price is lower than limit_price, fill the order

        # TODO: If current price is higher than stop_price, cancel the order

        # Save the order to the user.
        self.orders[Txn.sender].append(order.copy())

        # Return the order id
        return UInt16(self.orders[Txn.sender].length - 1)

    @abimethod
    def exec_order(self, order_id: UInt64, user: Address) -> None:
        """
        Executes the order with the specified order ID for the given user.

        If the user has no orders, does nothing. If the user has an order with the specified order ID,
        checks current price in tinyman directly in contract or offchain if needed, and if the
        current price is lower than the limit price, fills the order. If the current price is higher
        than the stop price, cancels the order.

        :param order_id: The ID of the order to execute
        :param user: The user to execute the order for
        :return: None
        """
        if not self.orders.maybe(user.native)[1]:
            return

        order = self.orders[user.native][order_id.native].copy()

        # TODO: We check current price in tinyman or offchain if needed

        # TODO: If current price is lower than limit_price, fill the order

        # TODO: If current price is higher than stop_price, cancel the order

        # Update the order status
        order.status = String("closed")

        # Remove the order from the user
        self.orders[user.native][order_id.native] = order.copy()
