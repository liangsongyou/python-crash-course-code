ordinals = [1,2,3,4,5,6,7,8,9]

for ordinal in ordinals:
    if ordinal == 1:
        print("{}st".format(ordinal))
    if ordinal == 2:
        print("{}nd".format(ordinal))
    if ordinal == 3:
        print("{}rd".format(ordinal))
    elif ordinal > 3 and ordinal < 10:
        print("{}th".format(ordinal))