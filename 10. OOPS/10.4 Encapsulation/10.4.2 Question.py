class Account:
    def __init__(self, acc_no, balance):
        # Initialize account number and balance attributes
        self.acc_no = acc_no
        self.balance = balance
    
    def debit(self, amount):
        # Method to debit amount from the account
        self.balance -= amount
        print("Rs.", amount , "has been debited")
        print("Total Balance :", self.get_balance())
    
    def credit(self, amount):
        # Method to credit amount to the account
        self.balance += amount
        print("Rs. ", amount, "has been credited")
        print("Total Balance", self.get_balance())
    
    def get_balance(self):
        # Method to retrieve the current balance
        return self.balance

# creating object
acc1 = Account("7633872665", 990000000000)
print(acc1.balance)  # Print initial balance
print(acc1.acc_no)   # Print account number
acc1.debit(1000)     # Debit 1000 from the account
acc1.credit(9999999000000)  # Credit a large amount to the account
