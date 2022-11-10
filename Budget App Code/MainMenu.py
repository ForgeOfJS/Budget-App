import pickle
import os
import wx  

	
class Mywin(wx.Frame): 
            
    def __init__(self, parent, title): 
        super(Mywin, self).__init__(parent, title = title) 
		
        panel = wx.Panel(self) 
        box = wx.BoxSizer(wx.HORIZONTAL)
		
        self.list = wx.ListCtrl(panel, -1, style = wx.LC_REPORT) 
        self.list.InsertColumn(0, 'Budget Name', width = 100) 
        self.list.InsertColumn(1, 'Total Budget Amount', wx.LIST_FORMAT_RIGHT, 100) 
        self.list.InsertColumn(2, 'Available Cash', wx.LIST_FORMAT_RIGHT, 100) 
        self.list.InsertColumn(3, '# of Categories', wx.LIST_FORMAT_RIGHT, 100) 
        
        budgetList = Mywin.populateBudgets()

        for i in budgetList: 
            index = self.list.InsertItem(1000, i.budgetName) 
            self.list.SetItem(index, 1, str(i.totalBudget)) 
            self.list.SetItem(index, 2, str(i.availableIncome))
            self.list.SetItem(index, 3, str(len(i.categoryList)))
		
        self.indexEntry = wx.TextCtrl(panel)
        button = wx.Button(panel, wx.ID_ANY, 'Test', (10, 10))
        button.Bind(wx.EVT_BUTTON, Mywin.deleteBudget(self.indexEntry))
        

        box.Add(self.list,1,wx.ALL | wx.CENTER, 5) 
        box.Add(self.indexEntry, 1, wx.ALL | wx.CENTER, 5)
        box.Add(button, 1, wx.ALL | wx.CENTER, 5)
        panel.SetSizer(box) 
        panel.Fit() 
        self.Centre() 
         
        self.Show(True)  
    
    def populateBudgets():
        budgetList = []

        for file in os.listdir(os.curdir+'/BudgetCollection'):
            if file.endswith('.pickle'):
                with open('BudgetCollection/' + file, 'rb') as budget:
                    budgetList.append(pickle.load(budget))

        return budgetList

    def deleteBudget(index):
        for file in os.listdir(os.curdir+'/BudgetCollection'):
            if file.endswith(str(index) + '.pickle'):
                print("Done!")
                os.remove(file)
                break
        
     
ex = wx.App() 
Mywin(None,'ListCtrl Demo') 
ex.MainLoop()