'''
Lecture on inheritance
Multiple Inheritance - inherit from more than 1 parent
where the parents do not inherit from eachother
'''


class Parent_1():
    def method_1(self):
        print('I am method 1')

    def method_2(self):
        print('I am method 2')


class Parent_2:

    def method_3(self):
        print('I am method 3')

    def method_4(self):
        print('I am method 4')


class Child(Parent_1, Parent_2):
    def method_5(self):
        print('I am method 5')

    def method_6(self):
        print('I am method 6')


obj = Child()
print(obj.method_1())
print(obj.method_4())
print(obj.method_6())
