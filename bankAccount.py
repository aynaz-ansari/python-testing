class BankAccount:
    def __init__ (self,initial_balance=0):
        self.balance = initial_balance #موجودی اولیه حساب

    def deposit(self,amount):
        if amount > 0 :
            self.balance += amount #اضافه کردن مبلغ به حساب

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount  #برداشت از حساب در صورتی که موجودی کافی باشد
            return True
        return False  #اگر موحودی کافی نباشد،برداشت انجام نمی شود

    def get_balance(self):
        return self.balance # گرفتن موحودی فعلی