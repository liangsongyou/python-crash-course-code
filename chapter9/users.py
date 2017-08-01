from admin import Admin

me = Admin('muhammad','ramzan','lightify','ramzanm461@gmail.com',['can add user','can create database','can delete database','can modify users'])
you = Admin('muhammad','ali','charlie','mali@mail.com')

me.describe_user()
me.greet_user()
me.priviliges.show_priviliges()

you.describe_user()
you.greet_user()
you.priviliges.show_priviliges()
