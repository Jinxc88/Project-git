import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("scores.csv")

# Group by breakfast
grouped = df.groupby("Breakfast")["Score on Test"].mean()

# Plot
grouped.plot(kind="bar", color=["skyblue", "orange"])
plt.title("Average Test Score by Breakfast")
plt.ylabel("Average Test Score")
plt.xlabel("Breakfast Status")
plt.tight_layout()
plt.savefig("breakfast_vs_score.png")
plt.show()

# Scatter plot: Sleep Hours vs Test Score
plt.figure(figsize=(10, 6))
plt.scatter(df['SleepHours'], df['Score'], alpha=0.7, color='teal')
plt.xlabel('Hours of Sleep')
plt.ylabel('Test Score')
plt.title('Test Score vs. Sleep Hours')
plt.grid(True)
plt.show()
