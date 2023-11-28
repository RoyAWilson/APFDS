'''
Lecture on metaxlasses intro only
'''


class Meta(type):
    pass


class Hi(metaclass=Meta):
    pass


print(type(Hi))
