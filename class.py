#!/usr/bin/python

class Parent:  # define parent class
    parentAttr = 100

    def __init__(self):
        print("Calling parent constructor")

    def parentMethod(self):
        print('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent attribute :", Parent.parentAttr)


class Child(Parent):  # define child class
    def __init__(self):
        print("Calling child constructor")

    def childMethod(self):
        print('Calling child method')

    def parentMethod(self):
        print('Overriding parent method')


c = Child()  # instance of child
c.childMethod()  # child calls its method
c.parentMethod()  # calls parent's method
c.setAttr(200)  # again call parent's method
c.getAttr()  # again call parent's method


class JustCounter:
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter._JustCounter__secretCount)