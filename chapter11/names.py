from name_function import get_formatted_name

print('Enter "q" to quit any time.')
while True:
    first = input('First Name: ')
    if first == 'q':
        break
    last = input('Last Name: ')
    if last == 'q':
        break

    formatted_name = get_formatted_name(first,last)
    print('Neatly formatted name: {}'.format(formatted_name))