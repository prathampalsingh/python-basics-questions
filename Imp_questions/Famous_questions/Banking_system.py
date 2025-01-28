# create account class with 2 attribute - balance & account no
# create method for debit , credit & print the balance

class Account():
    def __init__(self,balance,acc_no):
        self.bal = balance 
        self.acc = acc_no
    
    def debit_bal(self,debit):
        self.debit = debit
        if self.debit < self.bal:
            self.bal = self.bal - self.debit
            # self.bal -= self.debit
            print(f"total balance : {self.print_bal()}")
        else:
            print(f"Insufficant balance. you have only {self.bal} in our account")

    def credit_bal(self,credit):
        # self.credit = credit
        self.bal = self.bal + credit
        # self.bal += credit
        print(f"total balance : {self.print_bal()}")

    def print_bal(self):
        return self.bal



c1 = Account(1000,555)
c1.print_bal()
print("")
c1.debit_bal(int(input("enter the amount to be deducted: ")))
c1.print_bal()
print("")
c1.credit_bal(int(input("enter the amount to be deducted: ")))
c1.print_bal()
print("")
