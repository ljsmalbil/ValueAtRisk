import numpy as np

from var import ValueAtRisk

if __name__ == "__main__":
    period = "5y"

    sp = ValueAtRisk(period=period)

    # Obtain a visual of the return for the given time period
    sp.return_distribution_visual()

    # Get the VaR
    var = sp.value_at_risk()
    print('For a 95% CI, the VaR is: ' + str(np.round(var,3)) + ', indicating that with 95% confidence we can be sure that the daily returns will not exceed ' + str(np.round(var * 100,2)) + '%.')



