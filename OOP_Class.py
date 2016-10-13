class Robot:
    __counter = 0

    def __init__(self):
        Robot.__counter += 1

    def say_hi(self):
        if self.__name:
            print("Hi, I am " + self.__name)
        else:
            print("Hi, I am a robot without a name")

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_build_year(self, by):
        self.__build_year = by

    def get_build_year(self):
        return self.__build_year

    def __repr__(self):
        return "Robot('" + self.__name + "', " + str(self.__build_year) + ")"

    def __str__(self):
        return "Name: " + self.__name + ", Build Year: " + str(self.__build_year)

    def __del__(self):
       print ("Robot has been destroyed")

    @classmethod
    def RobotInstances(cls):
        return cls, Robot.__counter


if __name__ == "__main__":
    x = Robot()
    x.set_name("Marvin")
    x.set_build_year(1979)
    y = Robot()
    y.set_name("Caliban")
    y.set_build_year(1943)
    print(x.RobotInstances())
    for rob in [x, y]:
        rob.say_hi()
        if rob.get_name() == "Caliban":
            rob.set_build_year(1993)
        print("I was built in the year " + str(rob.get_build_year()) + "!")
