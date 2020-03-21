import wx
import wx.grid as grid
import pandas as pd
import numpy as np



df=pd.DataFrame(np.random.normal(0, 1, (5, 2)), columns=["A", "C"])

class PandasGUI:

    def __init__(self,data_pandas):
        global df
        df =data_pandas

        app = MyApp()
        app.MainLoop()



class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(parent=None, title="Grid In WxPython")
        self.frame.Show()
        return True

class MyFrame(wx.Frame):
    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(800, 600))
        self.panel = MyPanel(self)


class MyPanel(wx.Panel):
    def __init__(self, parent):
        super(MyPanel, self).__init__(parent)
        mygrid = grid.Grid(self)
        mygrid.CreateGrid(df.shape[0], df.shape[1])
        for i in range(len(df.columns)):
            mygrid.SetColLabelValue(i, df.columns[i])
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                mygrid.SetCellValue(i, j, str(df.iat[i, j]))
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(mygrid, 1, wx.EXPAND)
        self.SetSizer(sizer)




