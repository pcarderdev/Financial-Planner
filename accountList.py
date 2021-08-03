from account import Account

class AccountList:
    def __init__ (self, name, accounts=[]):
        self.name = name
        self.accountList = accounts

    def addAccounts(self, accounts):
        for account in accounts:
            self.accountList.append(account)

    def printAllAccounts(self):
        for account in self.accountList:
            print(account.getName() + ": $" + str(account.getBalance()))

    def printTotalBalance(self):
        total = 0
        for account in self.accountList:
            total += account.getBalance()
        print("Total balance: ${}".format(total))
