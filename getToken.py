# -*- coding: utf-8 -*-
import psutil
import os

# Get Process pID
def getProcessPID(processName):
    # check process
    for process in psutil.process_iter():
        try:
            processInfo = process.as_dict(attrs=['pid', 'name', 'create_time'])
            if processInfo['name'] is None:
                continue
            # Check if process name contains the given name string.
            if processName.lower() in processInfo['name'].lower():
                listOfProcessObjects = processInfo
                break
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listOfProcessObjects['pid']


def getToken():
    token = None
    # waiting for the process endlessly
    while True:
        try:
            token = psutil.Process(getProcessPID('EscapeFromTarkov_BE.exe')).cmdline()[3][7:]
            pID = getProcessPID('EscapeFromTarkov_BE.exe')
            command = 'taskkill /PID ' + str(pID)
            os.system(command)
        except:
            pass
        if token is not None:
            p = psutil.Process(pID)
            p.kill
            return token


if __name__ == '__main__':
    print(getToken())
