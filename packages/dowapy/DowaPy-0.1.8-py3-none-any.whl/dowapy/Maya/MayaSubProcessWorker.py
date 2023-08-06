import subprocess
from queue import Queue, Empty
from threading import Thread
import os
from ..Process.Multiprocess.SubProcessWorker import SubProcessWorkerClass
from ..File import Path

BootUpCommand = f'''
import sys
import maya.standalone
import maya.mel as mel
import maya.cmds as cmds
import epic.internal.mayaTaskServer

maya.standalone.initialize( name='python' )
cmds.upAxis(ax='z') # Sets the up axis to Z

for InputLine in sys.stdin:
    print(InputLine)
'''
class MayaSubProcessWorker(SubProcessWorkerClass):
    def __init__(self, cpuID, MayaVersion, LogFilter, CommandFilter):
        MayaPath = Path.GetMayaPath(MayaVersion)
        if MayaPath:
            MayaPyPath = os.path.join(MayaPath, '/bin/mayapy.exe')
        super(MayaSubProcessWorker, self).__init__(cpuID, MayaPyPath, '', LogFilter, CommandFilter)
    
    def BootUp(self):
        self.SubProcess = subprocess.Popen(f'{self.ExcutePath} {BootUpCommand}', stdin=subprocess.PIPE, stdout=subprocess.PIPE, bufsize=1, text=True, shell=False)
        self.SubProcessOutputQueue = Queue()
        self.ReadThread = Thread(target=self.LiveOutput, args=(self.SubProcess.stdout, self.SubProcessOutputQueue))
        self.ReadThread.daemon = True
        self.ReadThread.start()
        