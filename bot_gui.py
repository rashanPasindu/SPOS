from tkinter import *

from bot import getResponse

typed_request = ""

bot_Reply = ""

bot_template = "SPOS : {0}"
user_template = "USER : {0}"


def getText():
    typed_request = str(userEntry.get())

    return typed_request


def sendRequest():
    req = getText()
    response = getResponse(req)
    clear_Text()
    ShowChat(user_template.format(req))
    print(req)
    print(response)
    ShowChat(response)


def clear_Text():
    userEntry.delete(first=0, last=100)


def ShowChat(msg):
    displayBox.configure(state=NORMAL)
    displayBox.insert(END, msg + '\n')
    displayBox.configure(state=DISABLED)


# showData():
    # ShowChat(user_template.format(getText()))
    # print(user_template.format(getText()))
    # bot_Reply = str(sendRequest())
    # bot_Reply = bot_template.format(bot_Reply)
    # ShowChat(bot_Reply)


def showMenu(e):
    rightclickMenu.post(e.x_root, e.y_root)


def onExit():
    quit()


def onReset():
    # reset msg box
    # quit()
    clear_Text()
    displayBox.delete(0, END)


root = Tk()
root.geometry("320x410")
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

scrollbar = Scrollbar(frame1)
displayBox = Text(frame1, wrap='word', yscrollcommand=scrollbar.set, state=DISABLED)
scrollbar.configure(command=displayBox.yview)
displayBox.pack(side=LEFT, fill=BOTH)

frame2 = Frame(root)
frame2.pack(side=BOTTOM, fill=X)

userEntry = Entry(frame2, textvariable=typed_request)
userEntry.pack(side=LEFT, fill=X, expand=YES)
submitButton = Button(frame2, text='Send', command=sendRequest)
submitButton.pack(side=RIGHT, fill=X, expand=YES)

root.mainloop()
