from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = ['python']
favorite_languages['sarah'] = ['c','ruby']
favorite_languages['phil'] = ['javascript','haskell']
favorite_languages['edward'] = ['c','c++']

for name,languages in favorite_languages.items():
    print('{}\'s favorite languages are:'.format(name.title()))
    for language in languages:
        print('- {}'.format(language.title()))