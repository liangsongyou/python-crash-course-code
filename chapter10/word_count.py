def word_count(file_p):
    """Count the number of words in given file path."""
    try:
        with open(file_p) as file:
            text = file.read()
    except FileNotFoundError:
        #print('The file "{}" can\'t be opened.'.format(file_p))
        pass
    else:
        # split the entire text into words
        words = text.split()
        num_words = len(words)
        print('The file "{}" has approximately {} words.'.format(file_p,num_words))

# take the file path from user
file = input('Enter the file path to count words: ')

if __name__ == '__main__':
    word_count(file)