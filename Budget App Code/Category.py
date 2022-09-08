import Expense

class Category:

    totalExpenseAmount = .00
    totalExpenseCount = 0
    expenseList = []
    expenseTypeName = ""

    def __init__(self, expenseTypeName):
        self.expenseTypeName = expenseTypeName

    def addExpense(self, expense):
        self.expenseList.append(expense)
        self.totalExpenseCount += 1
        self.totalExpenseAmount += expense.expenseCost

    def removeExpense(self, listIndex):
        removedExpense = self.expenseList.pop(listIndex)
        self.totalExpenseCount -= 1
        self.totalExpenseAmount -= removedExpense.expenseCost

    def editExpense(self, listIndex, newAmount, newDescription):
        editedExpense = self.expenseList[listIndex]
        if (newAmount != None):
            self.totalExpenseAmount -= editedExpense.expenseCost
            editedExpense.expenseCost = newAmount
            self.totalExpenseAmount += editedExpense.expenseCost
        if (newDescription != None):
            editedExpense.expenseDescription = newDescription
        