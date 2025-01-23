import random
import math
from map import map

class Enemy():
    posY = 0
    posX = 0
    
    oldPosY = 0
    oldPosX = 0

    flowposX = 0
    flowposY = 0

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def step(self, flowposX, flowposY):

        if self.posX == 5 and self.posY == -1:
            self.posX = 5
            self.posY = 22

        if self.posX == 5 and self.posY == 23:
            self.posX = 5
            self.posY = 0

        if self.posX == 34 and self.posY==-1:
            self.posX = 34
            self.posY = 22

        if self.posX == 34 and self.posY == 23:
            self.posX = 34
            self.posY = 0

        self.flowposX = flowposX
        self.flowposY = flowposY

        moved: bool = False

        poss = []

        posX = self.posX
        posY = self.posY

        if map[posY + 1][posX] == 0 or map[posY + 1][posX] == 8:
            poss.append([posY + 1, posX])

        if map[posY - 1][posX] == 0 or map[posY - 1][posX] == 8:
            poss.append([posY - 1, posX])

        if map[posY][posX + 1] == 0 or map[posY][posX + 1] == 8:
            poss.append([posY, posX + 1])

        if map[posY][posX - 1] == 0 or map[posY][posX - 1] == 8:
            poss.append([posY, posX - 1])

        newPos = random.choice(poss)

        while newPos[0] == self.oldPosY and newPos[1] == self.oldPosX:
            newPos = random.choice(poss)

        self.oldPosX, self.oldPosY = self.posX, self.posY
        self.posX, self.posY = newPos[1], newPos[0]
        
        
        return

        if poss[0][1] != -1 and self.calcDist(poss[0]) <= self.calcDist(poss[1]) and self.calcDist(poss[0]) <= self.calcDist(poss[2]) and self.calcDist(poss[0]) <= self.calcDist(poss[3]):
            self.posX, self.posY = poss[0][1], poss[0][0]
            moved = True
        if poss[1][1] != -1 and self.calcDist(poss[1]) <= self.calcDist(poss[0]) and self.calcDist(poss[1]) <= self.calcDist(poss[2]) and self.calcDist(poss[1]) <= self.calcDist(poss[3]):
            self.posX, self.posY = poss[1][1], poss[1][0]
            moved = True
        if poss[2][1] != -1 and self.calcDist(poss[2]) <= self.calcDist(poss[0]) and self.calcDist(poss[2]) <= self.calcDist(poss[1]) and self.calcDist(poss[2]) <= self.calcDist(poss[3]):
            self.posX, self.posY = poss[2][1], poss[2][0]
            moved = True
        if poss[3][1] != -1 and self.calcDist(poss[3]) <= self.calcDist(poss[0]) and self.calcDist(poss[3]) <= self.calcDist(poss[2]) and self.calcDist(poss[3]) <= self.calcDist(poss[1]):
            self.posX, self.posY = poss[3][1], poss[3][0]
            moved = True

    def calcDist(self, selfPos) -> int:
        return math.sqrt(abs((self.flowposY - selfPos[1]))**2 + abs((self.flowposX - selfPos[0]))**2)




    