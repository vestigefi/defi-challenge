# Limit Order System Challenge Solution

## 🥅 Objective

Your task is to build an **on-chain limit order system** that can interact with a decentralized exchange (DEX), specifically **Tinyman** or **Pact**, to fill its orders. This system should enable users to create limit orders that are executed when specific conditions are met, such as price or time thresholds. This foundational tool aims to enhance decentralized trading and has the potential to become a valuable product in the **Algorand DeFi landscape**. The system should be primarily decentralized, allowing orders to be filled through DEXes or by arbitrageurs, with all orders managed on-chain.

## ✅ Completed Requirements

- [x] I used **AlgoKit** for the smart contract development.
- [x] I used **Puya** as the language for the smart contract development.
- [x] I target **Tinyman** as the DEX to interact with via their python SDK.

## 🚧 In-Progress

Due to time constraints, I was unable to deliver a fully functional system. However, I have implemented the core functionality/ logic of limit order execution, which allows users to create and execute orders. Here's what I have so far:

- The smart contract **AtomTrade** allows users to register via a **register()** method.
- On registration, the user can place an order via the **place_order()** method.

  - The order includes the limit price, amount, asset ID, and stop price.
  - At the time of placement, an abi call is to be made to **Tinyman** to check the current price of the asset. The current price is then compared to the limit price and stop price.

    - If the current price is lower than the limit price, the order will be filled immediately as that is a limit order.
    - If the current price is higher than the stop price, the order will be canceled which is a stop-loss order.

  - If the order is not filled or canceled, the status of the order is initially set to "open".

- Once the order has been placed, the offchain agent periodically calls the **exec_order()** method to ensure that the order can get the best price from the DEX.

## 📌 Next Step

As a next step, I plan to add the **exec_order()** method to the smart contract, which will be called by the offchain agent to ensure that the order can get the best price from the DEX and integrate with the **Tinyman** smart contract onchain.
