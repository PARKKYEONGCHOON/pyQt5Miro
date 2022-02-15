from ClsINI import *
from enum import Enum

diretory = os.path.dirname(os.path.abspath(__file__))
os.chdir(diretory)

class GlobalVariable:
    def __init__(self):

        iniFile = Inifile()
        iniFile.InIfile_Set_Path('Setting.ini')
    
        self.MapXsize = Inifile.InIfile_ReadValue(iniFile,'Setting','MapXsize')
        self.MapYsize = Inifile.InIfile_ReadValue(iniFile,'Setting','MapYsize')
        self.MapStartChar = Inifile.InIfile_ReadValue(iniFile,'Setting','StartChar')
        self.MapFinishChar = Inifile.InIfile_ReadValue(iniFile,'Setting','FinishChar')
        self.MapLoadChar = Inifile.InIfile_ReadValue(iniFile,'Setting','LoadChar')
        self.MapWallChar = Inifile.InIfile_ReadValue(iniFile,'Setting','WallChar')
        
        self.AutoStatus = 0
        self.AutoSwich = False
        self.InitCheck = False
        self.RotateCheck = False
        self.MoveCheck = False
        self.FinishCheck = False
        
        self.Init = 1
        self.RotateSelect = 2
        self.MoveSelect = 3
        self.Finish = 4
        
        self.Wall = []


    