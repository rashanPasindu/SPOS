# retrieving data as a file
import time

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
    QUERY = 'SELECT * FROM scan_results;'

    connection = db.getcon()
    cur = connection.cursor()
    cur.execute(QUERY)
    result = cur.fetchall()

    c = csv.writer(open('c:/Users/Rashan/Desktop/NmapScanResults_' + editDate() + '.csv', 'wb'))
    global filename
    filename = 'NmapScanResults_' + editDate() + '.csv'
    for x in result:
        c.writerow(x)

