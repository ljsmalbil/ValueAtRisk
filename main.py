"""
Developed by: L. Smalbil

This script can be used to compute the value at risk (VaR) of a given portfolio.
Three methods have been implemented:

1) Historical method;
2) Variance-covariance method;
3) Monte Carlo method (to be implemented).
"""

import numpy as np
from var import ValueAtRisk


if __name__ == "__main__":
    period = "5y"

    sp = ValueAtRisk(period=period, percentile=0.01)

    # Obtain a visual of the return for the given time period
    sp.return_distribution_visual()

    # Get the VaR
    percentile = 0.01 # CI
    var = sp.value_at_risk_hist()
    print('For a ' + str((1 - percentile) * 100)+ '% CI, the VaR is: ' + str(np.round(var,3)) +
          ', indicating that with ' + str((1 - percentile) * 100) +
          '% confidence we can be sure that the daily losses will not exceed '
          + str(abs(np.round(var * 100,2))) + '%.')

    var_cov = sp.value_at_risk_var_covar()
    print('\nAccording to the variance-covariance method, the VaR for a ' + str((1 - percentile) * 100)+ '% CI' +
          ' is ' + str(abs(np.round(var_cov * 100,2))) + '%.')

    var_monte_carlo = sp.value_at_risk_monte_carlo(repetitions = 1000)
    print('\nAccording to the Monte Carlo method, the VaR for a ' + str((1 - percentile) * 100) + '% CI' +
          ' is ' + str(abs(np.round(var_monte_carlo * 100, 2))) + '%.')

