# generating a list of cubes using list comprehension

cubes = [num ** 3 for num in range(1,11)]
for cube in cubes:
    print("{}".format(cube))