import tkinter as tk
from PIL import Image, ImageTk
import os
import Budget as B
import pickle

def populateBudgets():
        budgetList = []

        for file in os.listdir(os.getcwd()+"\Budget App Code\BudgetCollection"):
            if file.endswith('.pickle'):
                with open(os.getcwd()+"\Budget App Code\BudgetCollection\\" + file, 'rb') as budget:
                    budgetList.append(pickle.load(budget))

        return budgetList


class EntryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Budget Applicaiton")
        self.root.geometry("800x700")
        self.root.minsize(800, 700)

        #bg_image = Image.open("OIP.jpg")  # Replace with your image file
        bg_photo = tk.PhotoImage(file=os.getcwd()+"\Budget App Code\R.png")
        bg_label = tk.Label(root, image=bg_photo)
        bg_label.image = bg_photo
        bg_label.place(relwidth=1, relheight=1)

        # Listbox to display entries with two columns
        self.entry_listbox = tk.Listbox(root, width=40, height=10)
        self.entry_listbox.grid(row=0, column=0, rowspan=4, padx=10, pady=10, columnspan=2)
        budgets = populateBudgets()
        for budget in budgets:
            self.entry_listbox.insert(tk.END, budget.budgetName)

        

        # Entry details labels and text boxes
        label = tk.Label(root, text="Budget Name:").place(relx=0.5, rely=0.3, anchor="center")

        self.entry_name_var = tk.StringVar()
        self.entry_name_entry = tk.Entry(root, textvariable=self.entry_name_var)
        self.entry_name_entry.grid(row=0, column=3, padx=10, pady=5)
        self.entry_name_entry.place(relx=0.45, rely=0.35, anchor="center")

        # Button to add entries
        add_button = tk.Button(root, text="Add Entry", command=self.add_budget)
        add_button.grid(row=2, column=3, pady=10)
        add_button.place(relx=0.6, rely=0.35, anchor="center")

        self.entry_listbox.place(relx=0.5, rely=0.5, anchor="center")
    def add_budget(self):
        # Get entry details from text boxes
        entry_name = self.entry_name_var.get()

        # Add entry to the listbox with two columns
        entry_text = entry_name
        new_budget = B.Budget(budgetName=entry_text)
        new_budget.save()
        self.entry_listbox.insert(tk.END, entry_text)

        # Clear text boxes
        self.entry_name_var.set("")

if __name__ == "__main__":
    root = tk.Tk()
    app = EntryApp(root)
    root.mainloop()
