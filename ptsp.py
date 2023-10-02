import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

uniform_data = stats.uniform.rvs(size=100000, #Generate 100000 numbers
                                 loc=0,       #Form 0
                                 scale=10)    #To 10

pd.DataFrame(unifrom_data).plot(kind="density",  #Plot the distribution
                                figsize=(9,9),
                                xlim=(-1,11))
