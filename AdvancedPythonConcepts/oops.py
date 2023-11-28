'''
Object oriented programming and classes
'''


class Student:
    '''
    Class to build students
    '''

    def __init__(self, name, age, roll_number):
        '''
        Initialise the class variables
        '''

        self.name = name
        self.age = age
        self.roll_number = roll_number

    def details(self):
        '''
        to Print the details to terminal
        '''
        print(self.name)
        print(self.age)
        print(self.roll_number)


obj = Student('Roy', 58, 12589)
print(obj.details())
