file_p = './alice.txt'

try:
    with open(file_p) as file:
        contents = file.read()
except FileNotFoundError:
    print('File {} not found(404)'.format(file_p))
else:
    # count the approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    print('The file {} has about {} words.'.format(file_p,num_words))
