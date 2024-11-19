import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load the dataset with column names
df = pd.read_csv('basic_data_visualiztion.csv')

# Check the data to confirm columns
print(df.head())

# Visualization 1: Bar Chart - Average Session Length vs Yearly Amount Spent
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Avg. Session Length', y='Yearly Amount Spent')
plt.title('Yearly Amount Spent by Average Session Length')
plt.xlabel('Average Session Length')
plt.ylabel('Yearly Amount Spent')
plt.show()

# Visualization 2: Line Chart - Time on App vs Yearly Amount Spent
plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='Time on App', y='Yearly Amount Spent')
plt.title('Yearly Amount Spent by Time on App')
plt.xlabel('Time on App')
plt.ylabel('Yearly Amount Spent')
plt.show()

# Visualization 3: Scatter Plot - Length of Membership vs Yearly Amount Spent
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Length of Membership', y='Yearly Amount Spent')
plt.title('Yearly Amount Spent by Length of Membership')
plt.xlabel('Length of Membership')
plt.ylabel('Yearly Amount Spent')
plt.show()