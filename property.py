#property用法1：
'''
class Test(object):
    def __init__(self):
        self.__num = 100

    def setNum(self, newNum):
        self.__num = newNum

    def getNum(self):
        return self.__num

    num = property(getNum, setNum)

t = Test()
print(t.getNum())
t.setNum(20)
print(t.getNum())
print("."*50)
t.num = 1000
print(t.num)
'''

#property用法2：
class Test(object):
    def __init__(self):
        self.__num = 100

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, newNum):
        self.__num = newNum

t = Test()
print(t.num)
t.num = 1000
print(t.num)