# Создать метакласс для паттерна Синглтон (см. конец вебинара)

class Singleton(type):

    def __init__(cls, name, region, country, **kwargs):
        super().__init__(name, region, country)
        cls.__instance = None

    def __call__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__call__(*args, **kwargs)
        return cls.__instance

class Cities(metaclass = Singleton):
    pass

location1 = Cities()
location2 = Cities()
location3 = Cities()

print(location1 is location3)
print(location1 is not location2)
print(location2 is location3)
