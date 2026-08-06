import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("data/RELIANCE.csv", skiprows=[1,2])

df.rename(columns={"Price": "Date"}, inplace=True)

df["Date"] = pd.to_datetime(df["Date"])

df["Close"] = pd.to_numeric(df["Close"])

df["Daily Return"] = df["Close"].pct_change()

# Calculate Moving Averages
df["MA20"] = df["Close"].rolling(window=20).mean()
df["MA50"] = df["Close"].rolling(window=50).mean()

# Create Buy Signal
df["Signal"] = 0
df.loc[df["MA20"] > df["MA50"], "Signal"] = 1

#Shift the Signal
df["Position"] = df["Signal"].shift(1)

#Calculate Strategy Return
df["Strategy Return"] = df["Position"] * df["Daily Return"]

#Buy & Hold Return
df["Buy & Hold Return"] = df["Daily Return"]

#Calculate Cumulative Returns
df["Strategy Cumulative"] = (1 + df["Strategy Return"]).cumprod()
df["BuyHold Cumulative"] = (1 + df["Buy & Hold Return"]).cumprod()

# Daily stock return
df["Daily_Return"] = df["Close"].pct_change()

# 20-day rolling volatility
df["Rolling_Volatility"] = (
    df["Daily_Return"]
      .rolling(window=20)
      .std()
)

# Annualize volatility
df["Rolling_Volatility"] = (
    df["Rolling_Volatility"] * np.sqrt(252)
)


print(df[[
    "Date",
    "Strategy Return",
    "Buy & Hold Return",
    "Strategy Cumulative",
    "BuyHold Cumulative"
]].tail())

plt.figure(figsize=(15,7))

plt.plot(
    df["Date"],
    df["Strategy Cumulative"],
    label="Moving Average Strategy",
    linewidth=2
)

plt.plot(
    df["Date"],
    df["BuyHold Cumulative"],
    label="Buy & Hold",
    linewidth=2
)

plt.title("Strategy vs Buy & Hold")

plt.xlabel("Date")

plt.ylabel("Portfolio Growth")

plt.legend()

plt.grid(True)

plt.tight_layout()

plt.savefig("plots/strategy_vs_buy_hold.png", dpi=300)

plt.show()

# ================================
# Performance Metrics
# ================================

#We are storing two columns separately.
strategy = df["Strategy Return"].dropna()
buyhold = df["Buy & Hold Return"].dropna()

#Total Return.
strategy_total_return = (
    df["Strategy Cumulative"].iloc[-1] - 1
) * 100

buyhold_total_return = (
    df["BuyHold Cumulative"].iloc[-1] - 1
) * 100

#annual return/252 trading days
years = len(df) / 252

annual_return = (
    (df["Strategy Cumulative"].iloc[-1]) ** (1 / years) - 1
) * 100

#calculate volatility/ high volatility higher risk
volatility = strategy.std() * (252 ** 0.5) * 100

#Calculate Sharpe Ratio/ low risk high sharpe ratio
sharpe_ratio = (
    strategy.mean() / strategy.std()
) * (252 ** 0.5)

#max drawdown
rolling_max = df["Strategy Cumulative"].cummax()

drawdown = (
    df["Strategy Cumulative"] - rolling_max
) / rolling_max

max_drawdown = drawdown.min() * 100

print("\n==============================")
print("Performance Report")
print("==============================")

print(f"Strategy Return      : {strategy_total_return:.2f}%")
print(f"Buy & Hold Return    : {buyhold_total_return:.2f}%")
print(f"Annual Return        : {annual_return:.2f}%")
print(f"Volatility           : {volatility:.2f}%")
print(f"Sharpe Ratio         : {sharpe_ratio:.2f}")
print(f"Maximum Drawdown     : {max_drawdown:.2f}%")

# ===================================
# Save Performance Report
# ===================================

with open("reports/performance_metrics.txt", "w") as file:

    file.write("Performance Report\n")
    file.write("============================\n\n")

    file.write(f"Strategy Return   : {strategy_total_return:.2f}%\n")
    file.write(f"Buy & Hold Return : {buyhold_total_return:.2f}%\n")
    file.write(f"Annual Return     : {annual_return:.2f}%\n")
    file.write(f"Volatility        : {volatility:.2f}%\n")
    file.write(f"Sharpe Ratio      : {sharpe_ratio:.2f}\n")
    file.write(f"Maximum Drawdown  : {max_drawdown:.2f}%\n")
    
    # ===================================
# Cumulative Returns Plot
# ===================================

plt.figure(figsize=(15,6))

plt.plot(
    df["Date"],
    df["Strategy Cumulative"],
    label="Strategy",
    linewidth=2,
    color="green"
)

plt.plot(
    df["Date"],
    df["BuyHold Cumulative"],
    label="Buy & Hold",
    linewidth=2,
    color="blue"
)

plt.title("Cumulative Returns")

plt.xlabel("Date")

plt.ylabel("Portfolio Growth")

plt.legend()

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig("plots/cumulative_returns.png", dpi=300)

plt.show()


# ===================================
# Drawdown Plot
# ===================================

plt.figure(figsize=(15,6))

plt.fill_between(
    df["Date"],
    drawdown * 100,
    color="red",
    alpha=0.4
)

plt.plot(
    df["Date"],
    drawdown * 100,
    color="darkred"
)

plt.title("Strategy Drawdown")

plt.xlabel("Date")

plt.ylabel("Drawdown (%)")

plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig("plots/drawdown.png", dpi=300)

plt.show()

plt.close()

# -----------------------------
# Rolling Volatility Graph
# -----------------------------

plt.figure(figsize=(16,6))

plt.plot(
    df["Date"],
    df["Rolling_Volatility"],
    color="purple",
    linewidth=2,
    label="20-Day Rolling Volatility"
)

plt.title("20-Day Rolling Volatility", fontsize=16)

plt.xlabel("Date", fontsize=12)

plt.ylabel("Volatility", fontsize=12)

plt.legend()

plt.grid(True, linestyle="--", alpha=0.5)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("plots/rolling_volatility.png", dpi=300)

plt.show()

plt.close()




