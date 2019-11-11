# db check
from datetime import date as date1

import dbconnect as db


def editDate():
    dat = date1.today()
    dat = dat.strftime('%Y-%m-%d')
    return dat


def sendTODB(ip, state, ports, portstate, scantype):
    conn = db.getcon()
    cursor = conn.cursor()
    scabType = scantype
    daten = editDate()

    try:
        query = "INSERT INTO scan_results (scan_type, scanned_ip, state, ports_open, ports_state, datentime) VALUES (" \
                "%s, %s, %s, %s, %s, %s) "
        values = (scabType, ip, state, ports, portstate, daten)
        cursor.execute(query, values)
        conn.commit()

        if cursor.lastrowid:
            print('last insert id: ', cursor.lastrowid)
        else:
            print('no last insert id found')

        print("Data Sent to database")
    except db.Error as error:
        print(error)
    finally:
        db.destroyConn()


ip = '192.168.1.6'
state = 'open'
ports = '32, 64,.65'
date = editDate()
print(date)

# sendTODB(ip, state, ports, date)
