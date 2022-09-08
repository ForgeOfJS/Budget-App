from unicodedata import category
import Expense as exp
import Category as cat

count = 0

class Budget:

    totalBudget = 0.00
    categoryList = []

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

    
    def addCategory(self, categoryToAdd):
        self.categoryList.append(categoryToAdd)
        self.totalBudget += categoryToAdd.totalExpenseAmount

    def refreshBudget(self):
        actualBudget = 0.00
        for i in self.categoryList:
            actualBudget += i.totalExpenseAmount
        self.totalBudget = actualBudget
            

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
    

if __name__ == "__main__":
    main()