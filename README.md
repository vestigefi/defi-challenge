# Limit Order System Challenge

## Challenge Overview

Your task is to build an **on-chain limit order system** that can interact with a decentralized exchange (DEX), specifically **Tinyman** or **Pact**, to fill its orders. This system should enable users to create limit orders that are executed when specific conditions are met, such as price or time thresholds. This foundational tool aims to enhance decentralized trading and has the potential to become a valuable product in the **Algorand DeFi landscape**. The system should be primarily decentralized, allowing orders to be filled through DEXes or by arbitrageurs, with all orders managed on-chain.

### Bonus Features
Extra points will be awarded if additional trading strategies, such as **Dollar Cost Averaging (DCA)** or **Stop-loss**, are implemented.

---

## Requirements

### Working Environment
- Participants must use **AlgoKit** to build the smart contracts and/or SDKs necessary to complete the challenge.

### Challenge Tools
- The system should utilize **Algorand-based smart contracts**.
- While discouraged, a non-decentralized proof of concept will be accepted but will receive lower scores.

### Development Languages
- The primary development language should be **Python**, specifically the **Puya library**.

### Functional Requirements
1. **Limit Order Execution**: The system should allow users to set limit orders to buy/sell assets once the specified conditions (e.g., price limits or time limits) are met.
2. **Automated Strategies (Optional)**: Implement optional features like:
   - **DCA System**: Allows users to periodically buy/sell a specified asset at set intervals.
   - **Stop-Loss Order**: Enables users to sell an asset if its price falls below a certain threshold.

### Time Allotment
- Participants have **4 days** to complete the challenge.

---

## Evaluation Criteria

1. **Functionality**: The limit order system must meet the outlined requirements, including executing limit orders and any optional trading strategies if implemented.
2. **Decentralization**: Solutions that leverage smart contracts over simple SDKs are strongly preferred.
3. **Code Quality**: Code readability, adherence to best practices, and documentation will be evaluated.
4. **User Experience**: The system should offer simple, intuitive interactions. Although a UI is not required due to time constraints, including one will result in extra points. A **Command-Line Interface (CLI)** is sufficient, provided the commands are well documented in this README.
5. **Test Net Proof of Concept**: The system should be deployed on a testnet, with participants encouraged to deploy ASA/ASA pools to demonstrate the system's intended functionality.

**SUBMISSIONS SHOULD BE A PR FOR THIS REPO***
