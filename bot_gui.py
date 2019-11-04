from tkinter import *

from bot import getResponse

typed_request = ""

bot_Reply = ""


def getText():
    typed_request = str(userEntry.get())

    return typed_request


def sendRequest():
    req = getText()
    response = getResponse(req)
    clear_Text()

    return response


def clear_Text():
    userEntry.delete(first=0, last=100)


def showData():
    bot_Reply = sendRequest()


def showMenu(e):
    rightclickMenu.post(e.x_root, e.y_root)


def onExit():
    quit()

def onReset():
    # reset msg box
    quit()

root = Tk()
root.geometry("320x450")
root.title('SPOS')

# frame = Frame(root)
# frame.pack(side=TOP, fill=BOTH)

menuBar = Menu(root)
root.config(menu=menuBar)
reportMenu = Menu(menuBar)

submenuReport = Menu(reportMenu)
submenuReport.add_command(label="Nmap Scan Reports")
submenuReport.add_command(label="Metasploit Reports")
submenuReport.add_command(label="System Rating")

reportMenu.add_separator()

reportMenu.add_cascade(label="Scan Report", menu=submenuReport, underline=0)
reportMenu.add_command(label="Detection Report", command='')
reportMenu.add_command(label="DLP Report", command='')
reportMenu.add_command(label="Malware Classifications", command='')
menuBar.add_cascade(label="Reports", menu=reportMenu)
menuBar.add_cascade(label="Reset")

rightclickMenu = Menu(root, tearoff=0)
rightclickMenu.add_command(label="Reset", command=onReset)
rightclickMenu.add_command(label="Exit", command=onExit)
root.bind("<Button-3>", showMenu)

frame1 = Frame(root)
frame1.pack(fill=BOTH, side=TOP)

msgBox = Label(frame1, text=bot_Reply)
msgBox.pack(side=LEFT)

frame2 = Frame(root)
frame2.pack(side=BOTTOM, fill=X)

userEntry = Entry(frame2, textvariable=typed_request)
userEntry.pack(side=LEFT, fill=X, expand=YES)
submitButton = Button(frame2, text='Send', command=sendRequest)
submitButton.pack(side=RIGHT, fill=X, expand=YES)

root.mainloop()
