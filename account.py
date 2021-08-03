class Account:
    def __init__(self, name, balance, max=None, goal=None, goalDate=None):
        self.name = name
        self.balance = balance
        self.max = max
        self.goal = goal
        self.goalDate = goalDate

    def getBalance(self):
        return self.balance
    
    def getName(self):
        return self.name
    
    def getMax(self):
        return self.max

    def getGoal(self):
        return self.goal

    def getGoalDate(self):
        return self.goalDate

    def setMax(self, max):
        self.max = max

    def setGoal(self, goal):
        self.goal = goal

    def setGoalDate(self, goalDate):
        self.goalDate = goalDate
    
    def changeBalance(self, amount):
        if (amount + self.balance < 0):
            print("You cannot withdrawal that much money. Max withdrawal is: {}".format(self.balance))
        else: self.balance += amount

    def moveBalance(self, destAccount, amount):
        self.changeBalance(-amount)
        destAccount.changeBalance(amount)
        
    