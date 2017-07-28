def print_models(unprinted,completed):
    """
    Simulate printing each design, until none are left.
    Move each desing to completed after it has been printed.
    """
    while unprinted:
        current = unprinted.pop()
        # simulate printing each desing
        print("Printing model: {}".format(current))
        completed.append(current)

def show_completed(completed):
    """
    Show all the models that were printed
    """
    print("The following models have been printed")
    for model in completed:
        print("{}".format(model))
