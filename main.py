import numpy as np

from var import ValueAtRisk

if __name__ == "__main__":
    period = "5y"

    sp = ValueAtRisk(period=period)

    # Obtain a visual of the return for the given time period
    sp.return_distribution_visual()

    # Get the VaR
    percentile = 0.01
    var = sp.value_at_risk(percentile = percentile)
    print('For a ' + str((1 - percentile) * 100)+ '% CI, the VaR is: ' + str(np.round(var,3)) +
          ', indicating that with ' + str((1 - percentile) * 100)+
          '% confidence we can be sure that the daily losses will not exceed '
          + str(abs(np.round(var * 100,2))) + '%.')



