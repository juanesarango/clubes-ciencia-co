
# Output Strings
print('Hello World!')

# Import python libraries
import time
time.sleep(3)

# Create functions
def say_hello(recipient):
    return 'Hello, ' + recipient '!'

say_hello('Tim')

# Use cells and teach execution orders
import numpy as np

def square(x):
    return x * x

x = np.random.randint(1, 10)
y = square(x)

print('%d squared is %d' % (x, y))


# Fortune 500 exercise

%matplotlib inline

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="darkgrid")


df = pd.read_csv('fortune500.csv')

df.head()
df.tail()

df.columns = ['year', 'rank', 'company', 'revenue', 'profit']

len(df)

df.dtypes
# Profit dtype is object. Probably wrong values

non_numberic_profits = df.profit.str.contains('[^0-9.-]')
df.loc[non_numberic_profits].head()

set(df.profit[non_numberic_profits])
# only {N.A}

len(df.profit[non_numberic_profits])
# 369 only 1.5%

bin_sizes, _, _ = plt.hist(df.year[non_numberic_profits], bins=range(1955, 2006))
# Distribution of missing profit by year
# < 25 always. Worst case is 4% of the data

# remove the missing data
df = df.loc[~non_numberic_profits]
len(df)

# fixing the dtype
df.profit = df.profit.apply(pd.to_numeric)
df.dtypes


# Plotting with Matplotlib
def plot(x, y, ax, title, y_label):
    ax.set_title(title)
    ax.set_ylabel(y_label)
    ax.plot(x, y)
    ax.margins(x=0, y=0)

group_by_year = df.loc[:, ['year', 'revenue', 'profit']].groupby('year')
avgs = group_by_year.mean()
x = avgs.index

# Plot Profits
y1 = avgs.profit
fig, ax = plt.subplots()
plot(x, y1, ax, 'Increase in mean Fortune 500 company profits from 1955 to 2005', 'Profit (millions)')

# Plot Revenues
y2 = avgs.revenue
fig, ax = plt.subplots()
plot(x, y2, ax, 'Increase in mean Fortune 500 company revenues from 1955 to 2005', 'Revenue (millions)')

# Plots with Standard Deviation
def plot_with_std(x, y, stds, ax, title, y_label):
    ax.fill_between(x, y - stds, y + stds, alpha=0.2)
    plot(x, y, ax, title, y_label)

fig, (ax1, ax2) = plt.subplots(ncols=2)
title = 'Increase in mean and std Fortune 500 company %s from 1955 to 2005'
stds1 = group_by_year.std().profit.as_matrix()
stds2 = group_by_year.std().revenue.as_matrix()
plot_with_std(x, y1.as_matrix(), stds1, ax1, title % 'profits', 'Profit (millions)')
plot_with_std(x, y2.as_matrix(), stds2, ax2, title % 'revenues', 'Revenue (millions)')
fig.set_size_inches(14, 4)
fig.tight_layout() 