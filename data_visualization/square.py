import matplotlib.pyplot as plt

numbers = [n for n in range(6)]
squares = [n*n for n in range(6)]
plt.plot(numbers, squares, linewidth=4)
# Set chart title and label axis
plt.title("Square Numbers", fontsize=26)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of value", fontsize=14)
# Set size of tick labels
plt.tick_params(axis='both', labelsize=14)
plt.show()