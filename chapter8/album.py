def make_album(artist,title,tracks=None):
    album = {'artist': artist,'title': title}
    if tracks:
        album['tracks'] = tracks 
    return album

# print(make_album('taylor swift','1989'))
# print(make_album('justin bieber','purpose',9))
# print(make_album('ellie goulding','burn'))

while True:
    print("Enter Your Albums below")
    print("Enter q to quit anytime.")
    artist = input("Artist: ")
    if artist == 'q':
        break
    title = input("Title: ")
    if title == 'q':
        break

    print("\n {}".format(make_album(artist,title)))