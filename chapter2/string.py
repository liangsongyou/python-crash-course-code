# Simple strings
foo = 'I told my friend, "Python is my favorite Language"'
bar = "The language 'Python' is named after BBC's own Monty Python"
baz = "One of Python's strength is its diverse and vibrant community"

print("{}".format(foo.title()))
print("{}".format(bar.title()))
print("{}".format(baz.title()))

# Using variables and methods
name = "ada lovelace"
print("{}".format(name.title()))

first_name = "ada"
middle_name = "byron"
last_name = "lovelace"
print("Hell {}!".format((first_name + " " + middle_name  + " " + last_name).title()))

# Whitespaces
print("{}".format("Python"))
print("{}".format("\tPython"))
print("{}".format("Languages:\nC\nJavascript\nPython"))
print("{}".format("Languages:\n\tC\n\tJavascript\n\tPython".strip()))