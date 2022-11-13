# Создать не менее двух дескрипторов для атрибутов классов, которые вы создали ранее в ДЗ

class Verify:
    @classmethod
    def int_check(cls, value):
        if type(value) != int:
            raise TypeError('Значение не является цифрой!')

    def __get__(self, instance, owner):
        return instance.__dict__[self.variable]

    def __set__(self, instance, value):
        self.int_check(value)
        instance.__dict__[self.variable] = value

    def __delete__(self, instance):
        del instance.__dict__[self.variable]

    def __set_name__(self, owner, variable):
        self.variable = variable

class CheckLenth:
    def __set_name__(self, owner, name):
        self.name = '**//lenth'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

class ProtectAndVerify:
    @classmethod
    def int_check(cls, value):
        if type(value) != int:
            raise TypeError('Значение не является цифрой!')

    def __get__(self, instance, owner):
        return instance.__dict__[self.variable]

    def __set__(self, instance, value):
        self.int_check(value)
        instance.__dict__[self.variable] = value

    def __delete__(self, instance):
        del instance.__dict__[self.variable]

    def __set_name__(self, owner, variable):
        self.variable = '//**' + variable

class Road:
    lenth = ProtectAndVerify()
    width = ProtectAndVerify()
    weight = Verify()
    thickness = Verify()
    random_check = CheckLenth()

    def __init__(self, lenth, width, weight, thickness):
        self.lenth = lenth
        self.width = width
        self.weight = weight
        self.thickness = thickness
        result = lenth * width * weight * thickness
        print(f'{lenth}м * {width}м * {weight}кг * {thickness}м = {result}кг = {result/1000}т')

road = Road(150, 60, 15, 10)
road.random_check = 1500
print(road.__dict__)
