def show_magicians(magicians):
    """
    Print the name of each item in the provided list
    """
    print("Magician>>>")
    for magician in magicians:
        print("{}".format(magician))

def make_great(magicians,great_magicians):
    while magicians:
        current = magicians.pop()
        great_magicians.append('Great ' + current)

magicians = ['rob','alice','candice']
great_magicians = []
make_great(magicians,great_magicians)
show_magicians(great_magicians)