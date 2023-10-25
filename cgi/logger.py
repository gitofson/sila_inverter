#!/usr/bin/python
from invertor_hr import Invertor
from db import db
from parser import *

if __name__ == '__main__':
    vmiii = Invertor()
    command = 'QPIGS'
    data = parse_resp(command, vmiii.write(command))
    print(data)
    db.dbsave('vmiii_nadejkov_qpigs', data)
