# 📈 NSE Portfolio Monitor

A lightweight, real-time paper portfolio tracking tool for the National Stock Exchange (NSE). This tool fetches live stock prices and calculates unrealized Profit and Loss (PnL) based on your trade logs.

## 🚀 Features

- **Live Market Data:** Fetches real-time prices using the `yfinance` API.
- **Automated PnL Calculation:** Automatically calculates holdings and unrealized gains/losses from a CSV trade log.
- **Clean Interface:** Simplified terminal output for quick portfolio snapshots.

## 🛠️ Installation

Clone the repository and install the dependencies:

```bash
# Clone the repository
git clone https://github.com/PranavVetkar/NSE-Portfolio-Monitor.git

# Navigate to the project directory
cd NSE-Portfolio-Monitor

# Install dependencies
pip install -r requirements.txt
```

## 📊 Sample Output

When you run the script, it generates a real-time snapshot of your paper holdings:

```text
--- 📈 LIVE PAPER PORTFOLIO MONITOR ---
Stock: RELIANCE.NS
  Qty: 5 | Avg Buy: ₹1418.80
  Current: ₹1423.00 | PnL: ₹21.00
------------------------------
```

## 📂 Project Structure

- `portfolio_monitor.py`: Core logic for fetching prices and calculating PnL.
- `trade_log.csv`: Your trade history (Symbol, Type, Quantity, Price).
- `requirements.txt`: Project dependencies.

## 📝 Usage

1. Update `trade_log.csv` with your buy/sell transactions.
2. Run the monitor:
   ```bash
   python portfolio_monitor.py
   ```

## 🔧 Dependencies

- [Pandas](https://pandas.pydata.org/)
- [yfinance](https://github.com/ranaroussi/yfinance)

---
Developed by [Pranav Vetkar](https://github.com/PranavVetkar)
