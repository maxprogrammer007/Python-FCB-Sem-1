import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Your data
data = {
    'Name': [f'Student_{i}' for i in range(1, 74)],
    'FCB Marks': [29, 35, 35, 21, 33, 20, 17, 39, 10, 19, 35, 30, 27, 9, 33, 34, 31, 14, 38, 23, 17, 11, 31, 15, 40, 28, 20, 28, 26, 32, 29, 27, 23, 20, 38, 12, 32, 26, 32, 39, 30, 17, 23, 21, 23, 35, 36, 19, 0, 16, 35, 10, 24, 39, 10, 19, 18, 29, 16, 33, 24, 38, 32, 4, 40, 32, 30, 34, 10, 21, 38, 31, 33],
}

# Convert data to a DataFrame
df = pd.DataFrame(data)

# Descriptive statistics
statistics = df['FCB Marks'].describe()

# Print descriptive statistics
print("Descriptive Statistics:")
print(statistics)

# Histogram
plt.figure(figsize=(10, 6))
plt.hist(df['FCB Marks'], bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of FCB Marks')
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.show()

# Box plot
plt.figure(figsize=(8, 5))
plt.boxplot(df['FCB Marks'])
plt.title('Box Plot of FCB Marks')
plt.ylabel('Marks')
plt.show()

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df.index, df['FCB Marks'], color='orange', alpha=0.7)
plt.title('Scatter Plot of FCB Marks')
plt.xlabel('Index')
plt.ylabel('Marks')
plt.show()

# KDE plot
plt.figure(figsize=(10, 6))
sns.kdeplot(df['FCB Marks'], shade=True, color='green')
plt.title('Kernel Density Estimate (KDE) Plot of FCB Marks')
plt.xlabel('Marks')
plt.ylabel('Density')
plt.xlim(0, 40)  # Set x-axis limits to reflect the actual range of marks
plt.show()


# Violin plot
plt.figure(figsize=(10, 6))
sns.violinplot(x=df['FCB Marks'], color='purple')
plt.title('Violin Plot of FCB Marks')
plt.xlabel('Marks')
plt.xlim(0, 40)  # Set x-axis limits to reflect the actual range of marks
plt.show()

# Pair plot
sns.pairplot(df[['FCB Marks']], height=3)
plt.suptitle('Pair Plot of FCB Marks', y=1.02)
plt.show()

# ECDF plot
plt.figure(figsize=(10, 6))
sns.ecdfplot(df['FCB Marks'])
plt.title('Empirical Cumulative Distribution Function (ECDF) Plot of FCB Marks')
plt.xlabel('Marks')
plt.ylabel('Cumulative Probability')
plt.show()

# Pie Chart (Pass/Fail)
pass_threshold = 14
pass_fail_counts = [len(df[df['FCB Marks'] >= pass_threshold]), len(df[df['FCB Marks'] < pass_threshold])]
labels = ['Pass', 'Fail']
colors = ['lightgreen', 'lightcoral']

plt.figure(figsize=(8, 8))
plt.pie(pass_fail_counts, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Pass/Fail Distribution')
plt.show()

# Swarm plot
plt.figure(figsize=(10, 6))
sns.swarmplot(x=df['FCB Marks'], color='red')
plt.title('Swarm Plot of FCB Marks')
plt.xlabel('Marks')
plt.show()

# Line plot
plt.figure(figsize=(12, 6))
plt.plot(df['Name'], df['FCB Marks'], marker='o', linestyle='-', color='purple')
plt.title('Line Plot of FCB Marks for Each Student')
plt.xlabel('Student')
plt.ylabel('Marks')
plt.xticks(rotation=45, ha='right')
plt.show()

# Error bar plot
plt.figure(figsize=(10, 6))
plt.bar(df['Name'], df['FCB Marks'], color='skyblue', alpha=0.7, yerr=3)
plt.title('Bar Plot with Error Bars')
plt.xlabel('Student')
plt.ylabel('Marks')
plt.xticks(rotation=45, ha='right')
plt.show()

