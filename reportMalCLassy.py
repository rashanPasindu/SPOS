import dbconnect as db
import csv
from datetime import date as date1


filename = " "


def editDate():
    dat = date1.today()
    dat = dat.strftime('%Y-%m-%d')
    return dat


def returnfilename():
    global filename

    return filename


def run():
    QUERY = 'SELECT * FROM mal_classify;'

    connection = db.getcon()
    cur = connection.cursor()
    cur.execute(QUERY)
    result = cur.fetchall()

    c = csv.writer(open('c:/Users/Rashan/Desktop/Malware_Classification_Results_' + editDate() + '.csv', 'wt'))
    global filename
    filename = 'Malware_Classification_Results_' + editDate() + '.csv'
    for x in result:
        c.writerow(x)
