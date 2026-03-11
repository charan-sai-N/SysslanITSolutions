'''Seaborn is a Python library used for statistical data visualization.
It helps create attractive, informative, and easy-to-understand graphs for analyzing datasets.

Seaborn is built on top of two important Python libraries: matplot and pandas
Developers and data analysts use Seaborn to:

Visualize datasets clearly

Identify patterns and relationships in data

Analyze distributions and correlations

Create professional statistical plots'''



import seaborn as sns
import matplotlib.pyplot as plt
data = [10, 20, 12 , 40, 50 , 56 , 69 , 88 , 99]

sns.lineplot(x=[1,2,3,4,5,6,7,8,9], y=data)### the data sets must have same length

plt.show() # it shows a graph like structure 