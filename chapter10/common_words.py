def common(file_p, word):
    """Count occurrence of word in file."""
    try:
        with open(file_p) as file:
            text = file.read()
    except FileNotFoundError:
        print('File doesn\'t exist.')
    else:
            text = text.lower()
            num = text.count(word)
            return num

print('Hello, I count "words" in "files".')
file = input("File Path: ")
word = input("What you are looking for: ")

if __name__ == '__main__':
    print('"{}" occurs {} times in "{}"'.format(word,common(file,word),file))
