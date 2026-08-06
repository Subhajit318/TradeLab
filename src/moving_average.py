

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Read the CSV
df = pd.read_csv("data/RELIANCE.csv", skiprows=[1,2])

# Rename first column
df.rename(columns={"Price": "Date"}, inplace=True)
df["Date"] = pd.to_datetime(df["Date"])

# Convert Close column to numeric
df["Close"] = pd.to_numeric(df["Close"])

# Calculate 20-day Moving Average
df["MA20"] = df["Close"].rolling(window=20).mean()

# Calculate 50-day Moving Average
df["MA50"] = df["Close"].rolling(window=50).mean()

df["Signal"] = 0

df.loc[df["MA20"] > df["MA50"], "Signal"] = 1

df["Position"] = df["Signal"].diff()

plt.figure(figsize=(16,6))

# Closing Price
plt.plot(
    df["Date"],
    df["Close"],
    label="Close Price",
    color="blue",
    linewidth=1.5
)

# 20-Day Moving Average
plt.plot(
    df["Date"],
    df["MA20"],
    label="20-Day Moving Average",
    color="orange",
    linewidth=2
)

# 50-Day Moving Average
plt.plot(
    df["Date"],
    df["MA50"],
    label="50-Day Moving Average",
    color="red",
    linewidth=2
)
#buy green triangle
plt.scatter(
    df[df["Position"] == 1]["Date"],
    df[df["Position"] == 1]["Close"],
    marker="^",
    color="green",
    s=120,
    label="Buy"
)

#sell red triangle
plt.scatter(
    df[df["Position"] == -1]["Date"],
    df[df["Position"] == -1]["Close"],
    marker="v",
    color="red",
    s=120,
    label="Sell"
)

plt.title("Reliance Industries Stock Price with Moving Averages", fontsize=16)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Price (₹)", fontsize=12)

# Display the legend
plt.legend(loc="upper left", fontsize=10)

plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
# plt.savefig("plots/moving_average_strategy.png", dpi=300)
plt.savefig("plots/buy_sell_strategy.png", dpi=300)
plt.legend()
plt.show()
plt.close()
