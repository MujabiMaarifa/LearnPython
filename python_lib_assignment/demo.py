from ucimlrepo import fetch_ucirepo
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

# fetch dataset from the csv iris
data = pd.read_csv('iris/iris.data')
#display the first five records to work with afte loading data from iris data set
print("The first five rows:\n", data.head())

# the data types
print("\nThe data types in the data are as follows:\n", data.dtypes)

# finding missing values
print("\nMissing values")
print(data.isnull().sum())

print(f"\nThe data shape for the complete data set before cleaning is:\n {data.shape}")

#droping the empty fields
new_data = data.dropna()
print("\nThe new clean data: \n", new_data) # print(f"\nThe new clean data\n: {new_data.shape}")

# descriptive statistics
print("\nThe descriptive statistics for the new data: \n", new_data.describe())

#print new data columns
print("\nnew data columns: ")
print(new_data.columns)

# group the data set based on either species or department
group_means = new_data.groupby('Iris-setosa').mean(numeric_only=True)
print("\nThe grouped means for the species group:\n")
print(group_means)

#observations made on the data analysis
print("\nObesrvations made:")
print("->> Iris-virginica 5.1 are the highest number of species in the region with an aggregate mean of (6.588000).")
print("->> Iris-setosa 0.2 are the least number of species in the region with a mean of (0.244898).")

#simple bar chart
group_means.plot(kind='bar')
plt.title('Average Measurements per Iris Species')
plt.xlabel('Species')
plt.ylabel('Measurement Value')
plt.xticks(rotation=0)
plt.legend(loc='upper right')
plt.show()

#line chart
group_means.plot(kind='line')
plt.title('Average Measurements per Iris Species')
plt.xlabel('Species')
plt.ylabel('Measurement Value')
plt.xticks(rotation=0)
plt.legend(loc='upper right')
plt.show()

#histogram
plt.hist(group_means, bins=4, edgecolor='black')
plt.title("Histogram of Scores")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

#scatter
"""plot based on the given values"""

plt.scatter(new_data['sepal length'], new_data['petal length'], color='red', marker='o') 
plt.title("sepal length vs. petal length")
plt.xlabel("sepal length (cm)")
plt.ylabel("petal length (cm)")
plt.grid(True)
plt.show()

