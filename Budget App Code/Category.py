import Expense

#Definition for each possible category.
class Category:

    totalExpenseAmount = .00
    totalExpenseCount = 0
    expenseList = []
    expenseTypeName = ""

    def __init__(self, expenseTypeName):
        self.expenseTypeName = expenseTypeName

    #Add/remove expense, adjust total count and amount
    def addExpense(self, expense):
        self.expenseList.append(expense)
        self.totalExpenseCount += 1
        self.totalExpenseAmount += expense.expenseCost

    def removeExpense(self, listIndex):
        removedExpense = self.expenseList.pop(listIndex)
        self.totalExpenseCount -= 1
        self.totalExpenseAmount -= removedExpense.expenseCost

    #Requires knowledge of index and desired changes.
    #TODO 2 Test if this method can take in only 2 parameters.
    def editExpense(self, listIndex, newAmount, newDescription):
        editedExpense = self.expenseList[listIndex]
        if (newAmount != None):
            self.totalExpenseAmount -= editedExpense.expenseCost
            editedExpense.expenseCost = newAmount
            self.totalExpenseAmount += editedExpense.expenseCost
        if (newDescription != None):
            editedExpense.expenseDescription = newDescription
    
    #Returns a percentage based on the name of category.
    def recommendPercentage(self):
        if self.expenseTypeName == "Food":
            return 0.10
        elif self.expenseTypeName == "Housing":
            return 0.40
        #TODO 2: input additional categories here
        return 0.00
        
