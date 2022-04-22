class Dog(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __str__(self):
        return self.__name + "今年" + str(self.__age) + "岁了"

    # get方法访问私有变量
    @property
    def name(self):
        return self.__name

    # set方法修改私有变量（注意,get方法名，set方法名，xx.setter方法名要一致）
    @name.setter
    def name(self, name):
        self.__name = name

    def play(self):
        print(self.__name + "再玩游戏")


if __name__ == '__main__':
    dog = Dog('lucky', 8)
    dog.name = 'Nig'
    print(dog.name)

"""
class Dog(object):
    __name = 'lucky'
    __age = 8

    def __init__(self):
        pass

    # classmethod用来访问类私有成员变量
    @classmethod
    def setName(cls, name):
        cls.__name = name

    @classmethod
    def getName(cls):
        return cls.__name

    def play(self):
        print(self.__name + "再玩游戏")


def main():
    dog = Dog()
    print(dog.getName())
    dog.setName('Nig')
    dog.play()


if __name__ == '__main__':
    main()
"""
