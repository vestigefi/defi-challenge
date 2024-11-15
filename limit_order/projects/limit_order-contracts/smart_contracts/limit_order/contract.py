from algopy import *
from algopy.arc4 import abimethod

class LimitOrder(ARC4Contract):
    # Define contract state variables
    assetID: UInt64
    limitPrice: UInt64
    orderAmount: UInt64
    expiryTime: UInt64
    isActive: bool

    @abimethod(allow_actions=["NoOp"], create="require")
    def createApplication(self, assetID: Asset, limitPrice: UInt64, orderAmount: UInt64, expiryTime: UInt64) -> None:
        """
        Create the limit order contract with specified parameters.
        """
        assert limitPrice > UInt64(0), "Limit price must be positive"
        assert expiryTime > Global.latest_timestamp, "Expiry must be in the future"

        self.assetID = assetID.id
        self.limitPrice = limitPrice
        self.orderAmount = orderAmount
        self.expiryTime = expiryTime
        self.isActive = True

    @abimethod()
    def executeOrder(self, currentPrice: UInt64) -> None:
        """
        Execute the limit order if the price conditions are met.
        """
        assert self.isActive, "Order is inactive"
        assert currentPrice >= self.limitPrice, "Current price is below the limit price"
        assert Global.latest_timestamp <= self.expiryTime, "Order has expired"

        # Execute asset transfer
        itxn.AssetTransfer(
            xfer_asset=self.assetID,
            asset_receiver=Txn.sender,
            asset_amount=self.orderAmount,
        ).submit()

        self.isActive = False  # Mark order as executed

    @abimethod()
    def cancelOrder(self) -> None:
        """
        Cancel an active limit order.
        """
        assert self.isActive, "Order is already inactive"
        self.isActive = False  # Mark order as inactive

    @abimethod()
    def updateOrder(self, newLimitPrice: UInt64, newExpiryTime: UInt64) -> None:
        """
        Update the parameters of an active limit order.
        """
        assert self.isActive, "Cannot update an inactive order"
        assert newLimitPrice > UInt64(0), "Limit price must be positive"
        assert newExpiryTime > Global.latest_timestamp, "Expiry must be in the future"

        self.limitPrice = newLimitPrice
        self.expiryTime = newExpiryTime
