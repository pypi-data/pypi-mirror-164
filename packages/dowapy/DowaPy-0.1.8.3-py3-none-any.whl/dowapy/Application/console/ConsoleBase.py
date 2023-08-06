import os
import sys
import inspect
import tempfile
import subprocess
from threading import Thread
from queue import Queue, Empty
from .CommandBase import CommandBaseClass


class ConsoleBaseClass:
    def __init__(self):
        self.Process = None
        self.ProcessOutputQueue = Queue()
        self.ProcessLogQueue = Queue()
        self.CommandFilter = ''
        self.LogFilter = '[Console Log]'
        self.InitializeCommand = ''
    
    def Boot(self, ExecutePath, RequireModules, CommandClass, CommandFilter='>>'):
        self.CommandFilter = CommandFilter
        InitCode = self.BuildInitializeCode(RequireModules, CommandClass)
        # @TODO : 임시 파일 지워지는 지 확인 필요.
        f, fpath = tempfile.mkstemp()
        os.write(f, InitCode.encode('utf-8'))
        Execute = 'py' if ExecutePath == '' else ExecutePath
        self.Process = subprocess.Popen(f'{Execute} {fpath}', stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True, shell=False)
        self.ReadThread = Thread(target=self.LiveOutput, args=(self.Process.stdout,))
        self.ReadThread.daemon = True
        self.ReadThread.start()
    
    def LiveOutput(self, out):
        for line in iter(out.readline, b''):
            if self.LogFilter in line:
                self.ProcessLogQueue.put(line)
            self.ProcessOutputQueue.put(line)
        out.close
        
    def GetProcessOutput(self):
        Result=[]
        try:
            while True:
                Result.append(self.ProcessOutputQueue.get_nowait())
        except Empty:
            if len(Result) > 0: 
                return Result

    def GetProcessLog(self):
        Result=[]
        try:
            while True:
                Result.append(self.ProcessLogQueue.get_nowait())
        except Empty:
            if len(Result) > 0:
                return Result
        
    def SendMsg(self, Msg):
        if self.Process.poll() is None:
            self.Process.stdin.write(Msg)
            self.Process.stdin.flush()
        else:
            print('[Error]')
            print('    - The sub process is not running')
            
    def SendCommand(self, Cmd):
        self.SendMsg(f'{self.CommandFilter} {Cmd}')
        
    def BuildModuleImportCode(self, Module):
        ResultImportCode = ''
        ResultPath = ''
        if inspect.ismodule(Module):
            split = Module.__name__.split('.')
            PathSplit = os.path.dirname(Module.__file__).split('\\')
            if len(split) > 1:
                RootModule = split[0]
                ModuleHeirachy = '.'.join(split[:-1])
                ImportModule = split[-1]
                ResultImportCode = f'from {ModuleHeirachy} import {ImportModule}'
                ResultPath = '\\'.join(PathSplit[:PathSplit.index(RootModule)])
            else:
                ResultImportCode = f'import {Module.__name__}'
                ResultPath = os.path.dirname(Module.__file__)
        return ResultImportCode, ResultPath

    def BuildClassImportCode(self, Class):
        ResultImportCode = ''
        ResultPath = ''
        if inspect.isclass(Class):
            ModuleReference = sys.modules[Class.__module__]
            _, ResultPath = self.BuildModuleImportCode(ModuleReference)
            ResultImportCode = f'from {ModuleReference.__name__} import {Class.__name__}'
        
        return ResultImportCode, ResultPath

    def BuildImportCode(self, RequireModules:list, CommandClass):
        PathList = []
        ImportCode = ''
        for Module in RequireModules:
            if inspect.ismodule(Module):
                ImportCodeTemp, Path = self.BuildModuleImportCode(Module)
                ImportCode += ImportCodeTemp +'\n'
                if Path not in PathList:
                    PathList.append(Path)
                
        if CommandBaseClass in CommandClass.__bases__:
            ImportCodeTemp, Path = self.BuildClassImportCode(CommandClass)
            ImportCode += ImportCodeTemp + '\n'
            if Path not in PathList:
                PathList.append(Path)
        
        return PathList, ImportCode

    def BuildInitializeCode(self, RequireModules:list, CommandClass):
        RequirePath, ImportCode = self.BuildImportCode(RequireModules, CommandClass)
        ResultCode = f'''
import sys
sys.path += {RequirePath}
{ImportCode}
CommandIns = {CommandClass.__name__}()
try:
    for line in sys.stdin:
        CommandIns.Read(line)
except KeyboardInterrupt:
    print('    - Process terminated')
    exit()
'''
        return ResultCode