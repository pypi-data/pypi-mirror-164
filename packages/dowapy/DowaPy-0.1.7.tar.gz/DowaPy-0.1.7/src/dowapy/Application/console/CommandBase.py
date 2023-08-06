class CommandStructure:
    def __init__(self, FuncPtr):
        self.Initialize()
        self.BuildCommand(FuncPtr)
        
    def Initialize(self):
        self.Name = ''
        self.args = {}
        self.desc = ''
        self.Func = None
    
    def BuildCommand(self, FuncPtr):
        if FuncPtr:
            if callable(FuncPtr):
                self.Name = FuncPtr.__name__
                ArgsTemp = FuncPtr.__code__.co_varnames[:FuncPtr.__code__.co_argcount]
                for Current in ArgsTemp:
                    if Current == 'self': continue 
                    self.args[Current] = FuncPtr.__annotations__[Current]
                self.desc = FuncPtr.__doc__
                self.Func = FuncPtr
    
    def Execute(self, kwargs):
        try:
            if len(kwargs.keys()) > 0:
                print(kwargs)
                self.Func(**kwargs)
            else:
                self.Func()
        except ValueError:
            print('Run Fail')
            

class CommandBaseClass:
    def __init__(self, CommandFilter='>>'):
        self.CommandFilter = CommandFilter
        self.CommandDict = {}

    def Help(self, CommandName:str=''):
        '''Show description of console'''
        if CommandName:
            RefineCommandName = CommandName.strip().lstrip('-')
            if RefineCommandName in self.CommandDict.keys():
                print(self.CommandDict[RefineCommandName].desc)
            elif RefineCommandName == 'Exit':
                print(f'Exit')
                print(f'    - {self.Exit.__doc__}')
            else:
                print('wrong input')
        else:
            print(f'Help')
            print(f'    - {self.Help.__doc__}')
            print(f'Exit')
            print(f'    - {self.Exit.__doc__}')
            for Command in self.CommandDict.keys():
                print(f'{self.CommandDict[Command].Name}')
                print(f'    - {self.CommandDict[Command].desc}')
            
    
    def Exit(self):
        '''terminate the console'''
        raise KeyboardInterrupt
    
    def AddCommand(self, FuncPtr):
        NewCommand = CommandStructure(FuncPtr)
        CommandName = NewCommand.Name
        if CommandName not in self.CommandDict.keys() and CommandName != '':
            self.CommandDict[CommandName] = NewCommand
        
    def AddCommands(self, *args):
        for Func in args:
            self.AddCommand(Func)
    
    def DeleteCommand(self, FuncName):
        try:
            self.CommandDict.pop(FuncName)
        except KeyError:
            print('Invalid Key')

    def AnalyzeCommand(self, line:str):
        Result = False
        ResultCommand = None
        ResultCommandArgs = None
        split = line.split(' ')
        if len(split) > 0:
            CommandTemp = split[0]
            # Check Command inputted correctly
            if CommandTemp == '':
                print(f'    [Error] :  command input error')
                print(f'        - Command not inputted.')
            elif CommandTemp == 'Help':
                args = ''
                if len(split) > 1:
                    args = split[1]
                self.Help(args)
            elif CommandTemp == 'Exit':
                self.Exit()
            else: 
                # Check Command is in command list
                if CommandTemp not in self.CommandDict.keys():
                    print(f'    [Error] : command not exists')
                    print(f'        - "{CommandTemp}" command is not in command list.')
                    print(f'        - for more information. use the command "Help"')
                else:
                    ResultCommand = self.CommandDict[CommandTemp]
                    ResultCommandArgs = {}
                    RawArgs = split[1:]
                    
                    # Check arguments
                    index = 0
                    while index < len(RawArgs) and len(RawArgs) > 0:
                        if RawArgs[index][0] == '-':
                            if RawArgs[index][1:] in ResultCommand.args.keys():
                                CommandArgsType = ResultCommand.args[RawArgs[index][1:]]
                                if index < len(RawArgs):
                                    try:
                                        ResultCommandArgs[RawArgs[index][1:]] = CommandArgsType(RawArgs[index+1])
                                    except ValueError:
                                        print(f'[Error] : argument type error')
                                        print(f'    - "{RawArgs[index]}" argument value type is incorrect')
                                        print(f'    - expected value type : {CommandArgsType}')
                                        print(f'    - inputted : {RawArgs[index+1]}')
                                        print(f'    - for more information, use the command "Help -{CommandTemp}"')
                                        break
                            else:
                                print(f'[Error] : argument not exists')
                                print(f'    - The "{RawArgs[index]}" argument is not in arguments list of the "{CommandTemp}" command.')
                                print(f'    - for more information, use the command "Help -{CommandTemp}"')
                                break
                        index+=1
                    if index >= len(RawArgs):
                        Result = True
        return Result, ResultCommand, ResultCommandArgs
        
    def Read(self, Line):
        if len(Line) > len(self.CommandFilter):
            if Line[:len(self.CommandFilter)] == self.CommandFilter:
                CommandLine = Line.replace(self.CommandFilter, '').rstrip('\n').strip()
                print(f'- CommandLine : "{CommandLine}"')
                Succed, Command, Kwargs = self.AnalyzeCommand(CommandLine)
                if Succed:
                    Command.Execute(Kwargs)
                # else:
                #     print(f'    - Command execute failed')
