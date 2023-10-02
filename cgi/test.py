#!/usr/bin/python
from invertor_hr import Invertor
from parser import *

if __name__ == '__main__':
    vmiii = Invertor()
    cmds = ['QPIGS', 'QDI', 'QMOD', 'QPIRI']
    for command in cmds:
        out=vmiii.write(command)
        print(out)
        data = parse_resp(command, out)
        print(data)
