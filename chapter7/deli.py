sandwich_orders = ['tuna','pbj','jam','mayonnaise','chocolate spong']
finished_sandwiches = []

for sandwich in sorted(sandwich_orders):
    print("I made your {} sandwich.".format(sandwich.title()))
    idx = sandwich_orders.index(sandwich)
    finished = sandwich_orders.pop(idx)
    finished_sandwiches.append(finished)

print('The following sandwiches have been made:')
for sw in finished_sandwiches:
    print("\t {}".format(sw.title()))