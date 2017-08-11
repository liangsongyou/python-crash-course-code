import matplotlib.pyplot as plt

numbers = list(range(1,1001))
squares = [n * n for n in numbers]

plt.scatter(numbers, squares, edgecolor='none', c=squares, cmap=plt.cm.Set1, s=20)
# Set chart title and label axis
plt.title("Scatter Square", fontsize=23)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square", fontsize=14)
# Set size of tick labels
plt.tick_params(axis='x', which='major', labelsize=14)
plt.axis([1,1001,1, 1002001])
#plt.axis('square')
plt.show()