import seaborn as sns
import pandas as pd
import numpy as np
import yfinance as yf

import matplotlib.pyplot as plt

class ValueAtRisk:
    def __init__(self, default = '^GSPC', period = "1y"):
        self.default = default
        self.period = period

    def return_distribution_num(self):
        # Get S&P500 Index data
        market = yf.Ticker(self.default)
        market_data = market.history(period=self.period)

        # Convert to returns and remove nan columns
        market_data = market_data.pct_change(1)
        market_data = market_data['Close']
        market_data = market_data.dropna(axis=0)

        return market_data

    def return_distribution_visual(self):
        # Get S&P500 Index data
        market = yf.Ticker(self.default)
        market_data = market.history(period=self.period)

        # Convert to returns and remove nan columns
        market_data = market_data.pct_change(1)
        market_data = market_data['Close']
        market_data = market_data.dropna(axis=0)

        sns.histplot(market_data)
        plt.title('S&P500 returns')
        plt.ylabel('Frequency')
        plt.xlabel('Returns (in %)')

        return plt.show()

