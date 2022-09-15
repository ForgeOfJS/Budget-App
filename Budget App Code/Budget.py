import Expense as exp
import Category as cat

count = 0

#Main Class for the Application
class Budget:

    netIncome = 0.00
    availableIncome = 0.00
    totalBudget = 0.00
    categoryList = []

    #object creation method, system keeps a count of budgets.
    def __init__(self, budgetName = "Enter a name for your Budget", percentageSavings= .00):
        global count
        count = count + 1
        self.budgetName = budgetName
        self.percentageSavings = percentageSavings

    #debugging tool
    def display(self):
        print("This budget is: " + self.budgetName + "!\n The total budget is: " + str(self.totalBudget) + "!\n The total amount of budgets is: " + str(count))
        print("\nYour categories are:")
        categoryCount = 1
        for i in self.categoryList:
            print(str(categoryCount) + ". " + i.expenseTypeName + ", Total Expense: " + str(i.totalExpenseAmount))

        print("----------------------------------------\n")

    
    #adds a category to a budget
    #TODO 1 Adding amounts to category after initial use of this method will not reflect in the amount in the total budget FIX THIS
    def addCategory(self, categoryToAdd):
        self.categoryList.append(categoryToAdd)
        self.totalBudget += categoryToAdd.totalExpenseAmount

    #temp FIX for TODO 1
    #Checks through every category's total in budget and recalculates totalBudget.
    def refreshBudget(self):
        actualBudget = 0.00
        for i in self.categoryList:
            actualBudget += i.totalExpenseAmount
        self.totalBudget = actualBudget

    #allows user to set available income to a budget.
    def setAvailableIncome(self, newNetIncome):
        self.netIncome = newNetIncome
        self.availableIncome = self.netIncome - self.totalBudget

    #check and apply investment ratio to give user available income to invest
    def setInvestableIncome(self, investRatio):
        if investRatio >= 1:
            raise Exception("Invest Ratio must be less than 1")
        return self.availableIncome * investRatio

            
#for debugging purposes.
def main():
    budget = Budget("Budget 1")
    food = cat.Category("Food")
    bread = exp.Expense(1.99, "Bread")
    food.addExpense(bread)
    budget.addCategory(food)
    budget.display()

    rent = cat.Category("Rent")
    budget.addCategory(rent)
    apartment = exp.Expense(2000.00, "Apartment")
    rent.addExpense(apartment)
    budget.refreshBudget()
    budget.display()
    
#for debugging purposes.
if __name__ == "__main__":
    main()