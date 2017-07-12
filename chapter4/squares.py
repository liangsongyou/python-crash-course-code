# generating squares of numbers
squares = []
for num in range(1,11):
    squares.append(num ** 2)

print("{}".format(squares))

# Using list comprehensions to generate the same list

squares = [value ** 2 for value in range(1,11)]
print("{}".format(squares))