def describe_pet(type, name, age=None):
    """Display information about a per"""
    print("I have a {0}.".format(type))
    print("My {0}'s name is {1}.".format(type,name.title()))
    if age:
        print("{} is {} years old.".format(name.title(), age))

describe_pet('cat','zooor',3)
describe_pet('dog','willie')

# the arguments to functions can also be provided in keyword form like the following
describe_pet(type='dog',name='scooby',age=4)