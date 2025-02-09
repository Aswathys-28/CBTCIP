# -*- coding: utf-8 -*-
"""Iris Flower Classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1OFP8CctRiP6ZycoVfcG0C09bBsCL76pB

**IRIS FLOWER CLASSIFICATON**


*Data Science Project*
"""

# Importing Dependencies
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import warnings
warnings.filterwarnings('ignore')

# Load the dataset
df = pd.read_csv('IRIS.csv')

# Display the first few rows of the dataset
df.head()

df.info()

rows, columns = df.shape
print(f"Number of rows are: {rows}")
print(f"Number of columns are: {columns}")

# Missing Values/Null Values Count
df.isnull().sum()

df.describe()

# Count the occurrences of each species
species_counts = df['species'].value_counts()

# Print the counts
print(species_counts)

df.groupby('species').mean()

# Create the scatterplot
plt.figure(figsize=(10, 6))
sns.scatterplot(x='sepal_length', y='sepal_width', hue='species', data=df, palette='deep', s=100, edgecolor='k')

# Add titles and labels
plt.title('Sepal Length vs Sepal Width by Species', fontsize=16)
plt.xlabel('Sepal Length', fontsize=14)
plt.ylabel('Sepal Width', fontsize=14)

# Show the plot
plt.legend(title='Species')
plt.show()

# Create the line plot
plt.figure(figsize=(10, 6))
sns.lineplot(data=df.drop(['species'], axis=1), palette='tab10', linewidth=2.5)

# Add titles and labels
plt.title('Line Plot of Iris Dataset Features', fontsize=16)
plt.xlabel('Index', fontsize=14)
plt.ylabel('Value', fontsize=14)

# Show the plot
plt.legend(labels=['Sepal Length', 'Sepal Width', 'Petal Length', 'Petal Width'], title='Features')
plt.show()

# Drop the 'species' column as it is not numerical
df_numeric = df.drop(['species'], axis=1)

# Plot histograms for each feature
df_numeric.plot.hist(subplots=True, layout=(2, 2), figsize=(10, 10), bins=20, edgecolor='black')

# Add a title to the entire figure
plt.suptitle('Histograms of Iris Dataset Features', fontsize=16)

# Show the plot
plt.show()

# Calculate the correlation matrix
correlation_matrix = df_numeric.corr()

# Set the plot size
plt.figure(figsize=(5, 5))

# Create the heatmap
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", cbar=False, square=True,
            xticklabels=correlation_matrix.columns, yticklabels=correlation_matrix.columns)

# Add titles and labels
plt.title("Correlation Matrix of Iris Dataset Features", fontsize=16)
plt.xticks(rotation=45, ha='right', fontsize=12)
plt.yticks(rotation=0, fontsize=12)

# Show the plot
plt.show()

g = sns.FacetGrid(df, col='species')

# Map the KDE plot to the grid
g = g.map(sns.kdeplot, 'sepal_length', shade=True, color="r")

# Add a title
plt.subplots_adjust(top=0.85)
g.fig.suptitle('Kernel Density Estimate of Sepal Length by Species')

# Show the plot
plt.show()

g = sns.FacetGrid(df, col='species')

# Map the KDE plot to the grid
g = g.map(sns.kdeplot, 'petal_length', shade=True, color="b")

# Add a title
plt.subplots_adjust(top=0.85)
g.fig.suptitle('Kernel Density Estimate of petal Length by Species')

# Show the plot
plt.show()

# Create a pairplot
sns.pairplot(df, hue='species', palette='Set2', diag_kind='kde')

# Show the plot
plt.show()

# Create histograms for all numerical columns in the Iris dataset
df.hist(color='#9CDBA6', edgecolor='black', figsize=(10, 10))

# Add a title to the overall plot
plt.suptitle('Histograms of Iris Dataset Features', fontsize=16)

# Show the plot
plt.show()

x = df.drop('species', axis=1)
y= df.species

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=5)

from sklearn.linear_model import LogisticRegression
# Assuming x and y are already defined
logreg = LogisticRegression()
logreg.fit(x, y)
y_pred = logreg.predict(x)

# Calculate accuracy
accuracy = metrics.accuracy_score(y, y_pred)

# Print accuracy in percentage
print("Accuracy: {:.2f}%".format(accuracy * 100))

from sklearn.neighbors import KNeighborsClassifier
# Create and fit the KNN classifier
knn = KNeighborsClassifier(n_neighbors=5, p=2, metric='minkowski')
knn.fit(x_train, y_train)

# Calculate accuracy on the test set
accuracy = knn.score(x_test, y_test)

# Print the accuracy in percentage
print("Accuracy: {:.2f}%".format(accuracy * 100))

from sklearn.svm import SVC
# Create and fit the SVC model
svm = SVC(kernel='rbf', random_state=0, gamma=0.10, C=1.0)
svm.fit(x_train, y_train)

# Calculate accuracy on the test set
accuracy = svm.score(x_test, y_test)

# Print the accuracy in percentage
print("Accuracy: {:.2f}%".format(accuracy * 100))