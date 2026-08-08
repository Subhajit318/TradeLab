# TradeLab

## Overview
This project is a Python-based trading strategy backtester that analyzes historical stock market data using a Moving Average Crossover strategy. It compares the performance of the strategy with a simple Buy & Hold approach and generates visualizations and performance metrics.

## Features
- Historical stock price analysis
- 20-day and 50-day Moving Average calculation
- Buy & Sell signal generation
- Strategy backtesting
- Performance comparison with Buy & Hold
- Rolling volatility analysis
- Drawdown analysis
- Performance metrics report
- Graph generation

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib

## Project Structure

```
Trading-Strategy-Backtester/
│
├── data/
│   ├── RELIANCE.csv
│   ├── HDFCBANK.csv
│   ├── ICICIBANK.csv
│   ├── INFY.csv
│   ├── NIFTY50.csv
│   └── TCS.csv
│
├── plots/
│   ├── reliance_price.png
│   ├── moving_average_strategy.png
│   ├── buy_sell_strategy.png
│   ├── strategy_vs_buy_hold.png
│   ├── cumulative_returns.png
│   ├── drawdown.png
│   └── rolling_volatility.png
│
├── reports/
│   └── performance_metrics.txt
│
├── src/
│   ├── analysis.py
│   ├── visualize.py
│   └── backtest.py
│
├── main.py
├── requirements.txt
└── README.md
```

## How to Run

1. Clone the repository.
2. Install the required libraries:

```bash
pip install -r requirements.txt
```

3. Run the project:

```bash
python main.py
```

## Output
The project generates:
- Closing Price Graph
- Moving Average Strategy Graph
- Buy & Sell Signal Graph
- Strategy vs Buy & Hold Graph
- Cumulative Returns Graph
- Drawdown Graph
- Rolling Volatility Graph
- Performance Metrics Report

## Author
Subhajit Khan
