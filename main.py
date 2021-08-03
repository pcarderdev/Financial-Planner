from account import Account
from accountList import AccountList

def main():
    s = Account('Savings', 10, goal=750, max=1000)
    c = Account('Checking', 20)

    a = AccountList("My Accounts")
    a.addAccounts([s, c])
    a.printAllAccounts()

    # TO-DO
    # 1. Turn into webpage
    # 2. Create user class

if __name__ == "__main__":
    main()