import wx
import pandas as pd
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from oauth2client.service_account import ServiceAccountCredentials
import gspread



SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']



class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="",
            pos=wx.DefaultPosition, size=(800,1000),
            style=wx.DEFAULT_FRAME_STYLE
            ,name="MyFrame"):
        super(MyFrame, self).__init__(parent, id, title,pos, size, style, name)
        self.panel = wx.Panel(self)


        # Setting first
        filemenu=wx.Menu()

        # first file menu
        menuAbout=filemenu.Append(wx.ID_ABOUT,"&About","Information about this program")
        filemenu.AppendSeparator()
        menuExit=filemenu.Append(wx.ID_EXIT, "&Exit", " Terminate the program")



        # Creating the menubar
        menuBar = wx.MenuBar()
        menuBar.Append(filemenu, "&File")  # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.



        # add Events to the tool bar
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU,self.OnExit,menuExit)


        # add buttens to the application
        self.btn1 = wx.Button(self.panel, label="Push Me to Log in")
        self.btn2 = wx.Button(self.panel, label="I wanna Know which Course we have on the big drive")
        self.btn3 = wx.Button(self.panel, label="I wanna Know which Course we have on the big drive")
        self.btn4 = wx.Button(self.panel,label="I wanna add new Curse")


       # self.btn2 = wx.Button(self.panel, label="")

        # add sizer
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(self.btn1, 0, wx.ALL, 10)
        sizer.Add(self.btn2, 0, wx.ALL, 10)
        sizer.Add(self.btn3, 0, wx.ALL, 10)
        sizer.Add(self.btn4, 0, wx.ALL, 10)
        self.panel.SetSizer(sizer)
        # Connect the buttuns to the libary

        self.Bind(wx.EVT_BUTTON, self.OnButtonInit, self.btn1)
        self.Bind(wx.EVT_BUTTON, self.OnKnowWitchCourse, self.btn2)
        self.Bind(wx.EVT_BUTTON, self.readFiles, self.btn3)
        self.Bind(wx.EVT_BUTTON, self.OnCreateCourse,self.btn4)



    def OnOpen(self,event):
        """Open a file"""


    def OnAbout(self,event):
        print("mmmmm about buttun mmmmm")

    def OnExit(self,event):
        self.Close(True)


    def OnCreateCourse(self,event):
        print("yes")



    def readFiles(self,event):
        self.service.files()
        # gsheet = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()

    def OnKnowWitchCourse(self,event):
        results = self.service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])
        print(results)

    def OnButtonInit(self, event):
        event_id = event.GetId()
        event_obj = event.GetEventObject()
        print("Button 1 Clicked:")
        print("ID=%d" % event_id)
        print("object=%s" % event_obj.GetLabel)
        creds = None
          # The file token.pickle stores the user's access and refresh tokens, and is
          # created automatically when the authorization flow completes for the first
          # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                  creds.refresh(Request())
            else:
                  flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                  creds = flow.run_local_server(port=0)
              # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                  pickle.dump(creds, token)

        self.service = build('drive', 'v3', credentials=creds)



class MyApp(wx.App):
    def OnInit(self):
        self.frame = MyFrame(None,title="Technio")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

if __name__ == '__main__':
    app = MyApp(False)
    app.MainLoop()






