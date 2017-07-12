# making a list of multiples of 3
threes_multiples = list(range(3,31,3))
for three in threes_multiples:
    print("{}".format(three.bit_length()))