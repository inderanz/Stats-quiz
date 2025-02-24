import matplotlib.pyplot as plt

# Given dataset
data = [45, 50, 55, 60, 65, 70, 75, 80, 85, 90]

# Creating the box plot
plt.figure(figsize=(6, 4))
plt.boxplot(data, vert=False, patch_artist=True, boxprops=dict(facecolor="lightblue"))

# Adding labels
plt.title("Box Plot of Salaries (in $1000s)")
plt.xlabel("Salary ($1000s)")
plt.grid(axis="x", linestyle="--", alpha=0.7)

plt.show()
