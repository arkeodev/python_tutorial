class P:

    """
    def __init__(self,x):
        self.setX(x)

    def getX(self):
        return self.__x

    def setX(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x
    """

    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        print("Burada")
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x

if __name__ == "__main__":
    p1 = P(1001)
    print(p1.x)
    # 1000
    p2 = P(15)
    print(p2.x)
    # 15
    p3 = P(-1)
    print(p3.x)
    # 0
    p1 = P(42)
    p1.x = 1030
    print(p1.x)
