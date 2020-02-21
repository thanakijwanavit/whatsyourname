#!bin/python3
name = input('please insert your name \n')
print(' hello {}'.format(name))


age = input('how old are you \n')
if int(age) < 20:
    print('oh you are just a baby')
else:
    print('oh you are old')
