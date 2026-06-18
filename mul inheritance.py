class Bank:
    def bank_name(self):
        print("Bank Name:State Bank of India")


class Account:
    def account_details(self):
        print("Account Holder:Sanika")
        print("Account Number:12353657")


class SavingsAccount(Bank,Account):
    def savings_details(self):
        print("Account type:Saving Account")
        print("Interset Rate:5%")

s = SavingsAccount()

s.bank_name()
s.account_details()
s.savings_details()


