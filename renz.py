#!bin/python3

print('nameDescription is imported')
class Renz:
    def nameDescription(self,name,age):
        if int(age) < 20:
            age_description = 'oh you are just a baby'
        else:
            age_description = 'oh you are old'
        return 'your name is {name}, you are {age_description}'.format(name=name, age_description=age_description)


if __name__=='__main__':
    name = input('please insert your name \n')
    print(' hello {}'.format(name))


    age = input('how old are you \n')
    if int(age) < 20:
        print('oh you are just a baby')
    else:
        print('oh you are old')
