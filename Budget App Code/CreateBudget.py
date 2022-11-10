import wx
import Budget as B

class CreateBudgetFrame(wx.Frame):    
    def __init__(self, frameName = "Create New Budget"):
        super().__init__(parent=None, title= frameName)
        panel = wx.Panel(self)        
        my_sizer = wx.BoxSizer(wx.VERTICAL)       
        #Name Entry for new Budget 
        self.nameEntry = wx.TextCtrl(panel)
        my_sizer.Add(self.nameEntry, 0, wx.ALL | wx.EXPAND, 5)   
        #Percentage to save Entry
        self.percEntry = wx.TextCtrl(panel)
        my_sizer.Add(self.percEntry, 0, wx.ALL | wx.EXPAND, 5)         
        my_btn = wx.Button(panel, label='Create Budget')
        my_btn.Bind(wx.EVT_BUTTON, self.uiSaveBudget)
            
        
        my_sizer.Add(my_btn, 0, wx.ALL | wx.CENTER, 5)        
        panel.SetSizer(my_sizer)        
        self.Show()

    def uiSaveBudget(self, event):
        value = self.nameEntry.GetValue()
        value2 = self.percEntry.GetValue()
        newBudget = B.Budget(budgetName = value, percentageSavings= value2)
        newBudget.save()
    

        

if __name__ == '__main__':
    app = wx.App()
    frame = CreateBudgetFrame()
    app.MainLoop()