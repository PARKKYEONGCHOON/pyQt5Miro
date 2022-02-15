from ast import Return
import os
import numpy as np
from sympy import li
from MapCls import *


Map = MiroMap()

class MiroUnit:

    def __init__(self):
        self.Cx = 0
        self.Cy = 0
        self.tmpX = 0 
        self.tmpY = 0
        self.MoveCount = 0
        self.dir = 0 #위오아왼
        self.dirX = (-1, 0, 1, 0)
        self.dirY = (0, 1, 0, -1)
        self.Start_Pos = (-1,-1)
        self.Finish_Pos = (-1,-1)
        self.valiable = False
        self.tmpWall = []
    
    def UnitPosition_Init(self,start,finish):
        
        print("StartPosition :", start)
        print("FinishPosition :", finish)
        
        tmplist = list(start)
        
        #처음 유닛 시작위치
        self.tmpX = tmplist[0]
        self.tmpY = tmplist[1]
    
    
    def Rotate(self, directSelect):
        
        if directSelect == 1:
            self.dir += 1
            
            if self.dir > 3:
                self.dir = 0
                
        elif directSelect == 2:
            self.dir -= 1
            
            if self.dir < 0:
                self.dir = 3
            
        elif directSelect == 3:
            self.dir = self.dir
            
        elif directSelect == 4:
            self.dir += 2
            
            if self.dir > 3:
                self.dir = 0
        else:
            pass
            
    
    def Move(self, moveSelect, sizeX, SizeY):
        
        listdirX = list(self.dirX)
        listdirY = list(self.dirY)
        
        if moveSelect == 1:
            self.Cx += listdirX[self.dir]
            self.Cy += listdirY[self.dir]
            
        elif moveSelect == 2:
            self.Cx -= listdirX[self.dir]
            self.Cy -= listdirY[self.dir]
            
        else:
            pass
        
        if (self.Cx < sizeX and self.Cy < SizeY) and (self.Cx >= 0 and self.Cy >= 0):
            
            Clist = [self.Cy, self.Cx]
            
            
            
            if Clist not in glob.Wall:
               
               self.tmpX = self.Cx
               self.tmpY = self.Cy
            
               self.MoveCount += 1
               
               self.valiable = True
               
            
            else:
                self.valiable = False
                
            
        else:
            self.valiable = False
            
    
    def valiableFunc(self,bool):
        self.valiable = bool
        
        
class QtMiroUnit(MiroUnit):
    
    def __init__(self):
        super().__init__()
        self.tmpStartX = ''
        self.tmpStartY = ''
        self.tmpFinishX = ''
        self.tmpFinishY = ''
        
    def UnitPosition_Init(self,start,finish):
        
        tmpStartlist = list(start)
        tmpFinishlist = list(finish)
        
        #처음 유닛 시작위치
        self.tmpStartX = tmpStartlist[0]
        self.tmpStartY = tmpStartlist[1]
        
        #finish
        self.tmpFinishX = tmpFinishlist[0]
        self.tmpFinishY = tmpFinishlist[1]
        
        