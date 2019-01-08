import os, sys
from win32com.client import GetObject

def getProcessList():
    psList = []
    getObj = GetObject('winmgmts:')
    process = getObj.InstancesOf('Win32_Process')
    for ps in process:
        psList.append(ps.Properties_('name').Value)
    return psList

print(getProcessList())