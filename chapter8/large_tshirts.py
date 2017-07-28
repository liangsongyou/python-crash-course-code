def make_shirt(size='large',message='I love Python'):
    """Display the size and message about tshirt"""
    print("Weaving a {} sized shirt for you. With the text: '{}'".format(size.upper(),message))

make_shirt()
make_shirt('medium')
make_shirt('small','Hawk')