from tkinter import *
from datetime import datetime,date
from pickle import dump,load
from sys import exit



class welcomeWindow():
    def __init__(self,windowhight,windowWidth,welcomeText) -> None:
        self.windowHight = windowhight
        self.windowwidth = windowWidth
        self.welcomeText = welcomeText

        root = Tk()
        root.geometry(f"{self.windowHight}x{self.windowwidth}")
        root.resizable(0,0)
        root.title(self.welcomeText)
        mainText = Label(root,text=self.welcomeText,fg="white",bg="black",font=("Ubuntu-Medium.ttf",45))
        mainText.pack(fill="both",expand=1)
        root.mainloop()
       



class Main():
    def __init__(self) -> None:
        lastWishdata = self.loadLastDayData()
        today = datetime.now().strftime(r'%d-%m-%Y').split('-')
        timegap = self.getTimegap(today,lastWishdata)

        if timegap == 0:
            welcomeWindow1 = welcomeWindow(600,400,"welcome back sir :)")
            self.storeLastDate()
            exit()
        else:
            self.storeLastDate()
            exit()

        
    def storeLastDate(self):

        date = datetime.now().strftime(r'%Y,%m,%d').split(",")
        dateObj = date
        f = open("data.pkl",'wb')

        dump(dateObj,f)
        print(dateObj)
        f.close()

    def loadLastDayData(self):
        try:
            f = open("data.pkl","rb")
            data = load(f)
            return data
        except Exception as e:
            self.storeLastDate()
            exit()
            

    def getTimegap(self,today=list,lastDate=list) -> list:
        lastDay = date(int(lastDate[0]),int(lastDate[1]),int(lastDate[2]))
        today = date(int(today[2]),int(today[1]),int(today[0]))
        return (today-lastDay).days
            







if __name__ =="__main__":

    # window = welcomeWindow(600,300,"Welcome back sir")
    main = Main()