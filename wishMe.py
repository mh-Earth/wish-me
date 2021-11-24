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
        storeLastDate()



def storeLastDate():

    date = datetime.now().strftime(r'%Y,%m,%d').split(",")
    dateObj = date
    f = open("data.pkl",'wb')

    dump(dateObj,f)


def loadLastDayData():
    try:
        f = open("data.pkl","rb")
        data = load(f)
        return data
    except Exception as e:
        return None


def getTimegap(today=list,lastDate=list) -> list:
    lastDay = date(int(lastDate[0]),int(lastDate[1]),int(lastDate[2]))
    # lastDay = date(2000,5,5)
    today = date(int(today[2]),int(today[1]),int(today[0]))
    return (today-lastDay).days
        


def wishMe():

    lastWishdata = loadLastDayData()
    today = datetime.now().strftime(r'%d-%m-%Y').split('-')
    timegap = getTimegap(today,lastWishdata)

    if timegap > 4:
        welcomeWindow1 = welcomeWindow(600,400,"welcome back sir :)")
        exit()
    else:
        storeLastDate()
        exit()



if __name__ =="__main__":

    wishMe()