files = ['cats.txt','dogs.txt','hamsters.txt']

for file in files:
    try:
        with open(file) as fp:
            contents = fp.read()
    except FileNotFoundError:
        #print('File "{}" can\'t be found.'.format(file))
        pass # silently ignore any exceptions
    else:
        print('File: {}'.format(file))
        print(contents)
