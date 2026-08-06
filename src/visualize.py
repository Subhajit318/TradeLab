import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# Read the CSV
df = pd.read_csv("data/RELIANCE.csv", skiprows=[1,2])

# Rename first column
df.rename(columns={"Price": "Date"}, inplace=True)

# Convert Close column to number
df["Date"] = pd.to_datetime(df["Date"])
df["Close"] = pd.to_numeric(df["Close"])

# Create the figure
plt.figure(figsize=(16, 6))
plt.plot(df["Date"], df["Close"], color="blue", linewidth=1.5)

plt.title("Reliance Industries Closing Price")
plt.xlabel("Date", fontsize=12)
plt.ylabel("Price (₹)", fontsize=12)

# Show only one label every 6 months
plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Save the graph
plt.savefig("plots/reliance_price.png", dpi=300, bbox_inches="tight")

# Show the graph
plt.show()

# Close the figure
plt.close()