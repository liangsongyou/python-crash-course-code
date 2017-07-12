bicycles = ['trek','canondale','redline','specialized']
print("{}".format(bicycles))
print("{}".format("#Accessing Elements in a list"))

print("{}".format(bicycles[0]))
print("{}".format(bicycles[0].encode()))
print("{}".format(bicycles[0].upper()))
print("Length of list is : {}".format(bicycles.index(bicycles[-1]) + 1))
print("{}".format("#Displaying Message"))
message = "My first bicycle was a " + bicycles[0].title() + "."
print("{}".format(message))