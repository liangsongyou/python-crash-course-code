def build_sandwich(*items):
    """
    Print items the user provides for sandwiches.
    """
    print("Adding following items to your sandwich:")
    for item in items:
        print('- {}'.format(item))


build_sandwich('peanut','butter')
build_sandwich('mayonnaise','chilli sauce')
build_sandwich('eggs','bread','chillie','jam')