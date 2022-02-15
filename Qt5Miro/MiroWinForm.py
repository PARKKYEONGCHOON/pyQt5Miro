from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import *
import sys
import os
from MapCls import *
from GlobalVariable import *
from UnitCls import *
from threading import Thread
from multiprocessing import Process, Queue


diretory = os.path.dirname(os.path.abspath(__file__))
os.chdir(diretory)

glo = GlobalVariable()
Unit = MiroUnit()
#Unit2 = QtMiroUnit()
Map = MiroMap()

         

class MainForm(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        self.startList = []
        self.FinishList = []
        self.LoadList = []
        self.WallList = []
        #self.AutoRun = AutoThread(self)
        
        
        
    def initUI(self):

        main_layout = QVBoxLayout()
        main_laySub1 = QHBoxLayout()
        main_laySub1_1 = QVBoxLayout()
        main_laySub1_2 = QVBoxLayout()
        main_laySub2 = QHBoxLayout()
        main_laySub2_1 = QHBoxLayout()
        main_laySub2_2 = QHBoxLayout()       
        self.btn_layout1 = QGridLayout()
        self.btn_layout2 = QGridLayout()
        self.btnMap_layout = QGridLayout()
        txtStatuas_layout = QGridLayout()
                
        groupbox_1 = QGroupBox("MAP")
        groupbox_2 = QGroupBox("DIRECTION")
        groupbox_3 = QGroupBox("MOVE")
        groupbox_4 = QGroupBox("STATUS")
        
        self.txtEdit_Status = QTextEdit()
        self.txtEdit_Status.setEnabled(False)
        
        self.setLayout(main_layout)
        main_layout.addLayout(main_laySub1)
        main_layout.addLayout(main_laySub2)
        
        main_laySub1.addLayout(main_laySub1_1)
        main_laySub1.addLayout(main_laySub1_2)
       
        main_laySub2.addLayout(main_laySub2_1)
        main_laySub2.addLayout(main_laySub2_2)
        
        main_laySub1_1.addWidget(groupbox_1)
        main_laySub1_1.addWidget(groupbox_4)
        main_laySub2_1.addWidget(groupbox_2)
        main_laySub2_2.addWidget(groupbox_3)
        
        groupbox_1.setLayout(self.btnMap_layout)
        groupbox_2.setLayout(self.btn_layout1)
        groupbox_3.setLayout(self.btn_layout2)
        groupbox_4.setLayout(txtStatuas_layout)
        
        self.startList,self.FinishList,self.LoadList,self.WallList = Map.BtnMapPositionInit(glo.MapStartChar,glo.MapFinishChar,glo.MapLoadChar,glo.MapWallChar)
        self.MapbtnInit(self.startList,self.FinishList,self.LoadList,self.WallList)
        
        txtStatuas_layout.addWidget(self.txtEdit_Status)
        
        self.DirMovebtnInit()
        
        self.setWindowTitle("Miro")
        self.resize(500,1000)
        self.Center()
        self.show()
        
    def Center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    
    def dirbutton_clicked(self, id):
        
        self.RotateFunc(id)
                
    def Movebutton_clicked(self, id):
        
        self.MoveFunc(id)
    
    def SetText(self,txt):
        
            self.txtEdit_Status.append(txt)
            
    def clearText(self):
            
            self.txtEdit_Status.clear()
            
    def DirMovebtnInit(self):
        self.dirbtnGroup = QButtonGroup()
        self.dirbtnGroup.setExclusive(False)
        self.dirbtnGroup.buttonClicked[int].connect(self.dirbutton_clicked)
        
        buttonUp = QPushButton("↑")
        self.dirbtnGroup.addButton(buttonUp, 3)
        self.btn_layout1.addWidget(buttonUp,0,1)
 
        buttonRight = QPushButton("→")
        self.dirbtnGroup.addButton(buttonRight, 1)
        self.btn_layout1.addWidget(buttonRight,1,2)
        
        buttonDown = QPushButton("↓")
        self.dirbtnGroup.addButton(buttonDown, 4)
        self.btn_layout1.addWidget(buttonDown,2,1)
        
        buttonLeft = QPushButton("←")
        self.dirbtnGroup.addButton(buttonLeft, 2)
        self.btn_layout1.addWidget(buttonLeft,1,0)
        
        self.movebtnGroup = QButtonGroup()
        self.movebtnGroup.setExclusive(False)
        self.movebtnGroup.buttonClicked[int].connect(self.Movebutton_clicked)
 
        buttonStraight = QPushButton("↑")
        self.movebtnGroup.addButton(buttonStraight, 1)
        self.btn_layout2.addWidget(buttonStraight)
        
        buttonBack = QPushButton("↓")
        self.movebtnGroup.addButton(buttonBack, 2)
        self.btn_layout2.addWidget(buttonBack)
            
    def MapbtnInit(self,s,f,l,w):
        
        id = 0
        
        self.MapbtnGroup = QButtonGroup()
        self.MapbtnGroup.setExclusive(False)
        
        
        for x in range(int(glo.MapXsize)):
            for y in range(int(glo.MapYsize)):
                
                if [x,y] in l:
                
                    self.btnMap = QPushButton(glo.MapLoadChar)
                    self.btnMap.setEnabled(False)
                    self.MapbtnGroup.addButton(self.btnMap, id)
                    self.btnMap_layout.addWidget(self.btnMap,x,y)
                    
                    
                elif [x,y] in w:
                    self.btnMap = QPushButton(glo.MapWallChar)
                    self.btnMap.setEnabled(False)
                    self.MapbtnGroup.addButton(self.btnMap, id)
                    self.btnMap_layout.addWidget(self.btnMap,x,y)
                     
                elif [x,y] == s:
                    self.btnMap = QPushButton(glo.MapStartChar)
                    self.btnMap.setEnabled(False)
                    self.MapbtnGroup.addButton(self.btnMap, id)
                    self.btnMap_layout.addWidget(self.btnMap,x,y) 
                    
                elif [x,y] == f:
                    self.btnMap = QPushButton(glo.MapFinishChar)
                    self.btnMap.setEnabled(False)
                    self.MapbtnGroup.addButton(self.btnMap, id)
                    self.btnMap_layout.addWidget(self.btnMap,x,y)   
                
                id += 1
                
    def CurrentBtn(self,pos,Cx,Cy):
        
        if pos == 1: #start
            str = glo.MapStartChar
        elif pos == 2: #load
            str = glo.MapLoadChar
        elif pos == 3: #finish
            str = glo.MapFinishChar
            
        self.CurBtn = QPushButton(str)
        self.CurBtn.setEnabled(False)
        self.CurBtn.setStyleSheet("background-Color : yellow")
        self.btnMap_layout.addWidget(self.CurBtn,Cx,Cy)

    def Initialize(self):
        
        Unit.UnitPosition_Init(Map.Start_Pos,Map.Finish_Pos)
        Unit.Cx = Unit.tmpX
        Unit.Cy = Unit.tmpY
        self.CurrentBtn(1,Unit.Cx,Unit.Cy)
    
    def printPos(self):
        
        Unit.Cx = Unit.tmpX
        Unit.Cy = Unit.tmpY
        
        self.SetText("Start Position : " + str(Map.Start_Pos))
        self.SetText("Finish Position : " + str(Map.Finish_Pos))
        self.SetText("MoveCount : " + str(Unit.MoveCount))
        self.SetText("Current Position : " + str([Unit.Cx,Unit.Cy]))
        self.SetText("Current Direction : " + str(Unit.dir))
    
    
    def RotateFunc(self,select):
        
        Unit.Rotate(select)
        self.SetText("Current Direction : " + str(Unit.dir))
        self.printPos()
        
    def MoveFunc(self,select):
        
        
        Unit.Move(select,int(glo.MapXsize),int(glo.MapYsize))
        self.SetText("MoveCount : " + str(Unit.MoveCount))
        
        if Unit.valiable:
            self.CurrentBtn(2,Unit.Cx,Unit.Cy)
            self.printPos()
            
        if self.Finishcheck():
            self.SetText("End")
        
    def Finishcheck(self):
        
        if [Unit.Cx,Unit.Cy] == Map.Finish_Pos:
            return True
       
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    main = MainForm()
    #main.show()
    main.Initialize()
    main.printPos()
    app.exec_()
    
    