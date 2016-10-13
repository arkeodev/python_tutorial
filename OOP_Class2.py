class Counter(object):
    number = 0

    def __init__(self):
        type(self).number += 1
        print(type(self).number)

    def __del__(self):
        type(self).number -= 1
        print(type(self).number)

class Account(Counter):
    def __init__(self, holder, number, balance,credit_line=1500):
        self.Holder = holder
        self.Number = number
        self.Balance = balance
        self.CreditLine = credit_line
        Counter.__init__(self)

    def deposit(self, amount):
        self.Balance = amount

    def withdraw(self, amount):
        if(self.Balance - amount < -self.CreditLine):
            # coverage insufficient
            return False
        else:
            self.Balance -= amount
            return True

    def balance(self):
        return self.Balance

    def transfer(self, target, amount):
	if(self.Balance - amount < -self.CreditLine):
            # coverage insufficient
            return False
        else:
            self.Balance -= amount
            target.Balance += amount
            return True

if __name__ == "__main__":
    k = Account("Guido", 345267, 10009.78)
    print(k.balance())
    # 10009.780000000001
    k2 = Account("Sven", 345289, 3800.03)
    print(k2.balance())
    # 3800.0300000000002
    print(k.transfer(k2, 1000))
    # True
    print(k2.balance())
    # 4800.0300000000007
    print(k.balance())
    # 9009.7800000000007
