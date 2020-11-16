import seaborn as sns
import numpy as np
import yfinance as yf

import matplotlib.pyplot as plt

from scipy.stats import t

class ValueAtRisk:
    def __init__(self, default = '^GSPC', period = "1y", percentile = 0.01):
        self.default = default
        self.period = period
        self.percentile = percentile

    def return_distribution_num(self):
        # Get S&P500 Index data
        index_data = yf.Ticker(self.default)
        index_data = index_data.history(period=self.period)

        # Convert to returns and remove nan columns
        index_data = index_data.pct_change(1)
        index_data = index_data['Close']
        index_data = index_data.dropna(axis=0)

        return index_data

    def return_distribution_visual(self):
        """
        # Get S&P500 Index data
        market = yf.Ticker(self.default)
        market_data = market.history(period=self.period)

        # Convert to returns and remove nan columns
        market_data = market_data.pct_change(1)
        market_data = market_data['Close']
        market_data = market_data.dropna(axis=0)
        """

        current_portfolio = ValueAtRisk(default=self.default, period=self.period)
        index_data = current_portfolio.return_distribution_num()

        sns.histplot(index_data)
        plt.title('S&P500 returns')
        plt.ylabel('Frequency')
        plt.xlabel('Returns (in %)')

        return plt.show()

    def value_at_risk_hist(self):
        """
        N.B. This VaR computation uses the historical method

        :param percentile: VaR percentile, CI
        :return: VaR value
        """

        current_portfolio = ValueAtRisk(default=self.default, period=self.period)
        index_data = current_portfolio.return_distribution_num()

        return np.quantile(index_data, self.percentile)

    def value_at_risk_var_covar(self):
        """
        This VaR computation uses the variance-covariance method

        N.B. A t-score is used instead of a z-score to account for uncertainties in smaller data sets.

        :param percentile: VaR percentile, CI
        :return: VaR value
        """

        current_portfolio = ValueAtRisk(default=self.default, period=self.period)
        index_data = current_portfolio.return_distribution_num()

        alpha = t.ppf(1 - self.percentile, df = len(index_data))
        var_vc = alpha * np.std(index_data)

        return var_vc

    def value_at_risk_monte_carlo(self, repetitions = 1000):
        """
        This VaR computation uses the Monte Carlo method

        N.B. This method assumes a underlying Student's t-distribution.

        :param repetitions: number of sample points drawn, sample size
        :param percentile: VaR percentile, CI
        :return:
        """
        current_portfolio = ValueAtRisk(default=self.default, period=self.period)

        index_data = current_portfolio.return_distribution_num()
        mu, sigma = np.mean(index_data), np.std(index_data)  # mean and standard deviation
        monte_carlo = np.random.normal(mu, sigma, repetitions)

        alpha = t.ppf(1 - self.percentile, df=len(monte_carlo))
        var_mc = alpha * np.std(monte_carlo)

        return var_mc



