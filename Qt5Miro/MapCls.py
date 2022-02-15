from copy import deepcopy
import os
from tkinter import W
import numpy as np
from sympy import li

from GlobalVariable import GlobalVariable

glob = GlobalVariable()

class MiroMap:
    
    def __init__(self):
        self.mapSizeX = 9
        self.mapSizeY = 9
        self.Start_Pos = (-1,-1)
        self.Finish_Pos = (-1,-1)
        self.map = []
        self.mapReverse = False
        self.Wall = []
        
        
    def LoadMap(self):
        
        f = open("map.txt",'r',encoding='utf-8')
        
        while True:
            
            line = f.readline()
            
            if len(line) <= 0: 
               break 
           
            line = line.replace('\n', '')
            splitline = line.split(' ')
            
            if self.mapReverse == False:
                
                self.map.append(splitline)
                
            else:
                
                self.map.insert(0,splitline)             
            
        f.close()
        
        print("맵 로딩 성공")
        
        
    def PrintMap(self):     
        
        row = 0
        col = 0
        self.map[row][col]
        stdmap = self.map[:]
        
        if self.mapReverse == True:
            stdmap.reverse()
               
        for mapRow in stdmap:
            for maptile in mapRow:
                print(maptile, end = '')
                
            print()
            
    
    def PositionInit(self):
        
        row = 0
        col = 0
        
        self.map[row][col]
        stdmap = self.map[:]
        
        
        if self.mapReverse == True:
            stdmap.reverse()
               
        for mapRow in stdmap:
            for maptile in mapRow:
                if maptile == 'S':
                    self.Start_Pos = (row,col)
                    
                if maptile == 'F':
                    self.Finish_Pos = (row,col)
                
                if maptile == 'x':
                    self.Wall += [row, col]
                
                col += 1
    
            row +=1
            col = 0
        
        
        self.Wall = listchunk(self.Wall,2)

        
        
        return self.Start_Pos, self.Finish_Pos

def listchunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]


def dequote(s):
    """
    If a string has single or double quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found, return the string unchanged.
    """
    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s

class MiroMap(MiroMap):
    def __init__(self):
        super().__init__()
        self.LoadMap()
        
        self.tmpmap = []
        self.Load = []
        self.StartChar = ''
        self.FinishChar = ''
        self.AllPos = []
        self.Wall = []
        
    def LoadMap(self):
        
        f = open("map.txt",'r',encoding='utf-8')
        
        while True:
            
            line = f.readline()
            
            if len(line) <= 0: 
               break 
           
            line = line.replace('\n', '')
            splitline = line.split(' ')
            
            if self.mapReverse == False:
                
                self.map.append(splitline)
                
            else:
                
                self.map.insert(0,splitline)             
            
        f.close()
        
        print("맵 로딩 성공")
        
        
    def MapModify(self):
        
        for i in self.map:
            self.tmpmap +=i
        
        return self.tmpmap
    
    def BtnMapPositionInit(self,StartChar,FinishChar,LoadChar,WallChar):
        
        row = 0
        col = 0
        
        self.map[row][col]
        stdmap = self.map[:]
        
               
        for mapRow in stdmap:
            for maptile in mapRow:
                
                if maptile == dequote(StartChar):
                    self.Start_Pos = [row,col]
                    
                if maptile == dequote(FinishChar):
                    self.Finish_Pos = [row,col]
                
                if maptile == dequote(LoadChar):
                    self.Load += [row, col]
                
                if maptile == dequote(WallChar):
                    self.Wall += [row, col]
                    glob.Wall += [row, col]
                
                self.AllPos += [row,col]
                
                col += 1
    
            row +=1
            col = 0
        
        self.Load = listchunk(self.Load,2)
        self.Wall = listchunk(self.Wall,2)
        self.AllPos = listchunk(self.AllPos,2)
        glob.Wall = listchunk(glob.Wall,2)
        
        print(self.Start_Pos)
        print(self.Finish_Pos)
        print(self.Load)
        print(self.Wall)
    
        
        
        return self.Start_Pos, self.Finish_Pos, self.Load, self.Wall
   