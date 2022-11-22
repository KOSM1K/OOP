from PersonClass import Person




class Programmer(Person):
    pass


class WebProg(Programmer):
    pass


class DataScientist(Programmer):
    pass


class GameDeveloper(Programmer):
    pass


if __name__ == '__main__':
    p = Person(10, True)
