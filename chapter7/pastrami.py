sandwich_orders = ['pastrami','tuna','pbj','jam','pastrami','mayonnaise','chocolate spong','pastrami']
finished_sandwiches = []

print("Deli have run out of pastramis")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich in sorted(sandwich_orders):
    print("I made your {} sandwich.".format(sandwich.title()))
    idx = sandwich_orders.index(sandwich)
    finished = sandwich_orders.pop(idx)
    finished_sandwiches.append(finished)

print('The following sandwiches have been made:')
for sw in finished_sandwiches:
    print("\t {}".format(sw.title()))