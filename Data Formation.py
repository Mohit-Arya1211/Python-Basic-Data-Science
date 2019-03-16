import numpy as np
from scipy import stats

incomes = np.random.randint(1, 1000, 501, int)
print(incomes)

Mean = np.mean(incomes)
print(Mean)

Median = np.median(incomes)
print(Median)

Mode = stats.mode(incomes)
print(Mode)
