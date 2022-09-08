#Each expense should have both a cost and a description, should be grouped together.
class Expense:

    def __init__(self, expenseCost, expenseDescritption):
        self.expenseCost = expenseCost
        self.expenseDescription = expenseDescritption