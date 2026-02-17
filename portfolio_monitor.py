import pandas as pd
import yfinance as yf

class PortfolioMonitor:
    def __init__(self, log_file="trade_log.csv"):
        self.log_file = log_file

    def get_live_price(self, symbol):
        # Fetch only the last 1 day of data for speed
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d")
        return data['Close'].iloc[-1]

    def calculate_pnl(self):
        df = pd.read_csv(self.log_file)
        if df.empty: return
        
        # Calculate Current Holdings
        # 1. Net Quantity per stock
        df['Net_Qty'] = df.apply(lambda x: x['Quantity'] if x['Type'] == 'BUY' else -x['Quantity'], axis=1)
        holdings = df.groupby('Symbol')['Net_Qty'].sum()
        
        # 2. Average Buy Price (Simplified)
        buys = df[df['Type'] == 'BUY']
        avg_prices = buys.groupby('Symbol')['Price'].mean()

        print("--- 📈 LIVE PAPER PORTFOLIO MONITOR ---")
        for symbol, qty in holdings.items():
            if qty > 0:
                live_price = self.get_live_price(symbol)
                avg_price = avg_prices[symbol]
                
                # Formula: (Current Price - Entry Price) * Quantity
                unrealized_pnl = (live_price - avg_price) * qty
                
                print(f"Stock: {symbol}")
                print(f"  Qty: {qty} | Avg Buy: ₹{avg_price:.2f}")
                print(f"  Current: ₹{live_price:.2f} | PnL: ₹{unrealized_pnl:.2f}")
                print("-" * 30)

# --- Execution ---
monitor = PortfolioMonitor()
monitor.calculate_pnl()