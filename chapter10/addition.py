def add():
    """Add a and b."""
    while True:
        print('Enter \'q\' to quit anytime.')
        a = input('Number1: ')
        if a == 'q':
            break
        b = input('Number2: ')
        if b == 'q':
            break
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print('Input should contain only numbers.')
        else:
            print('{} + {} = {}'.format(a, b, a + b))

if __name__ == '__main__':
    add()