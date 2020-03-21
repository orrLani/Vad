import wx
import pandas as pd
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from oauth2client.service_account import ServiceAccountCredentials
import gspread
<<<<<<< HEAD
import re
import PyPDF2

=======
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import sys
from PandasGUI import PandasGUI
from PyQt5.QtWidgets import QApplication, QTableView

from PyQt5.QtCore import QAbstractTableModel, Qt
>>>>>>> 5beb395d44d408c15023a35511cd346d8ef6c164

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']



class MyFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title="",
            pos=wx.DefaultPosition, size=(800,1000),
            style=wx.DEFAULT_FRAME_STYLE
            ,name="MyFrame"):
        super(MyFrame, self).__init__(parent, id, title,pos, size, style, name)
        self.panel = wx.Panel(self)

        # Setting  menu
        file_menu=wx.Menu()

        # first file menu
        menu_about=file_menu.Append(wx.ID_ABOUT,"&About","Information about this program")
        file_menu.AppendSeparator()

        menu_witch_courses=file_menu.Append(wx.ID_ANY,"Know what courses we have in big drive")
        file_menu.AppendSeparator()
        
        menu_exit=file_menu.Append(wx.ID_EXIT, "&Exit", " Terminate the program")


        # Creating the menubar
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")  # Adding the "file_menu" to the MenuBar
        self.SetMenuBar(menu_bar)  # Adding the MenuBar to the Frame content.



        # add Events to the tool bar
        self.Bind(wx.EVT_MENU, self.OnAbout, menu_about)
        self.Bind(wx.EVT_MENU,self.OnExit,menu_exit)
        self.Bind(wx.EVT_MENU,self.onMenuWitchCourses,menu_witch_courses)


        # add buttens to the application
<<<<<<< HEAD
        self.btn1 = wx.Button(self.panel, label="Push Me to Log in")
        self.btn2 = wx.Button(self.panel, label="I wanna Know which Course we have on the big drive")
        self.btn3 = wx.Button(self.panel, label="I wanna Know which Course we have on the big drive")
        self.btn4 = wx.Button(self.panel,label="I wanna add new Curse")
        self.btn10 = wx.Button(self.panel,label="מבחנים לפי מרצה")
=======
        self.btn1 = wx.Button(self.panel,-1 ,label="Push Me to Log in")

>>>>>>> 5beb395d44d408c15023a35511cd346d8ef6c164

        # show all course
        self.course_namese = wx.StaticText(self.panel,-1, label="")
        self.course_namese.SetForegroundColour(wx.RED)

       # self.btn2 = wx.Button(self.panel, label="")

        # add sizer
        sizer = wx.BoxSizer(wx.VERTICAL)
<<<<<<< HEAD
        sizer.Add(self.btn1, 0, wx.ALL, 10)
        sizer.Add(self.btn2, 0, wx.ALL, 10)
        sizer.Add(self.btn3, 0, wx.ALL, 10)
        sizer.Add(self.btn4, 0, wx.ALL, 10)
        sizer.Add(self.btn10, 0, wx.ALL, 10)
=======
        sizer.Add(self.btn1,3,0,0)

        sizer.Add(self.course_namese,2,0,0)

        sizer.SetSizeHints(self.panel)
>>>>>>> 5beb395d44d408c15023a35511cd346d8ef6c164
        self.panel.SetSizer(sizer)
        # Connect the buttuns to the libary

        self.Bind(wx.EVT_BUTTON, self.OnButtonInit, self.btn1)
<<<<<<< HEAD
        self.Bind(wx.EVT_BUTTON, self.OnKnowWitchCourse, self.btn2)
        self.Bind(wx.EVT_BUTTON, self.readFiles, self.btn3)
        self.Bind(wx.EVT_BUTTON, self.OnCreateCourse,self.btn4)
        self.Bind(wx.EVT_BUTTON, self.NameSearchTest,self.btn10)
        self.panel.Layout()
=======



    def onMenuWitchCourses(self,event):
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

        cred = ServiceAccountCredentials.from_json_keyfile_name('onedrive.json', scope)

        gc = gspread.authorize(cred)

        wks = gc.open('Courses').sheet1

        data = wks.get_all_values()
        head = data.pop(0)

        data_pandas = pd.DataFrame(data=data, columns= head)
        PandasGUI(data_pandas)

       # wx.MessageBox(data_pandas.to_string(), 'Info', wx.OK | wx.ICON_INFORMATION)

     #   self.course_namese.SetLabel(data_pandas.to_string())



>>>>>>> 5beb395d44d408c15023a35511cd346d8ef6c164


    def OnOpen(self,event):
        """Open a file"""


    def OnAbout(self,event):
        print("mmmmm about buttun mmmmm")

    def OnExit(self,event):
        self.Close(True)


    def OnCreateCourse(self,event):
<<<<<<< HEAD
        print("yes")

    def NameSearchTest(self,event):
        for root,dirs,files in os.walk("C:/Users/itke/Documents/6RD_SEMESTER/GIT/Vad") :
                for folder in dirs:
                    if (folder.find("236703") >-1 ):
                        name = os.path.join(root,folder)
                        for tmp in os.walk(name):
                            for tests in tmp[2]:
                                    if(tests.find(".pdf")<0):
                                        continue
                                    print(name)
                                    currpath = os.path.join(name, tests)
                                    print(currpath)
                                    file = open(currpath,'rb')

                                    reader = PyDF2.PdfFileReader(file)
                                    lecturer = "יוסי גיל"
                                    for i in range(0,1):
                                        page=reader.getpage(i)
                                        text=page.extracttext()
                                        if(re.search(lecturer,text)):
                                            print(tests)


=======
        scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
        cred = ServiceAccountCredentials.from_json_keyfile_name('onedrive.json', scope)
        gc = gspread.authorize(cred)
        wks = gc.open('Courses').sheet1
        mydata = wks.get_all_values()
        myHead = mydata.pop(0)
        df = pd.DataFrame(data=mydata, columns=myHead)
>>>>>>> 5beb395d44d408c15023a35511cd346d8ef6c164


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






