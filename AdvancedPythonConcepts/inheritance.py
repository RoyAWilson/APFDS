'''
Lecture on inheritance
inheritance and multilevel inheritance
'''


class GrandParent():
    def method_1(self):
        print('I am method 1')

    def method_2(self):
        print('I am method 2')


class Parent(GrandParent):

    def method_3(self):
        print('I am method 3')

    def method_4(self):
        print('I am method 4')


class Child(Parent):
    def method_5(self):
        print('I am method 5')

    def method_6(self):
        print('I am method 6')


obj = GrandParent()
obj2 = Parent()
obj3 = Child()

print(obj.method_1())
print(obj2.method_3())
print(obj2.method_2())
print(obj3.method_1())
