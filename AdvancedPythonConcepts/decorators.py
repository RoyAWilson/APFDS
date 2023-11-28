'''
Lecture about function decorators
'''


def welcome(func):
    def inner():
        print('Welcome')
        func()
        print('Thanks for choosing us')
    return inner()


@welcome
def selfcode():
    print('Selfcode Academy')


print(selfcode)
