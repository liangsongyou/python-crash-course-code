while True:
    topping = input("Enter your pizza topping ('quit' to end): ")

    if topping.lower() == 'quit':
        break
    else:
        print("Adding {} to your pizza.".format(topping))