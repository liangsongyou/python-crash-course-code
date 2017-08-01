from collections import OrderedDict

glossary = OrderedDict()

glossary = {
    'def': 'Used to define a new function in Python.',
    'and': 'Binary comparison operator which evaluates to true only if boht conditions are True',
    'list': 'list() is a function in python to define a new list. The arguments to this function are assigned items of list',
    'tuple': 'A data structure similar to lists but immutable(in parts) but mutable as a whole',
    'elif': 'A pun on else if. Used to chech another condition if the previous condition failed',
    'set' : 'A list of unique items. Has almost all the properties of a mathematical Set',
    'sorted': 'A function which takes an iterable and returns the same iterable in stored form.',
    'dict': 'A function to define a new dictionary.',
    'in': 'Checks whether an item is in iterable',
    'not in': 'Checks if the items is not in the iterable',
}

print("Term: Description")
for term,meaning in sorted(glossary.items()):
    print("{} : {}".format(term,meaning))