import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

data = pd.read_csv('all_data.csv')

data.rename(columns={'Country': 'country',
                     'Year': 'year',
                     'Life expectancy at birth (years)': 'life_expectancy',
                     'GDP': 'gdp'}, inplace=True)

print(data.head())