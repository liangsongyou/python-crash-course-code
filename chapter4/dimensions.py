# using tuples 
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

for dimension in dimensions:
    print("{}".format(dimension))

# tuples are mutable as a whole 

dimensions = (1024,920)
for dimension in dimensions:
    print("{}".format(dimension))