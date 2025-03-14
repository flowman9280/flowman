import random
import math
import pygame
import config
from map import map


def revenir_a_cage():
    print("ok")

class Enemy:
    eposY = 0
    eposX = 0
    
    oldPosY = 0
    oldePosX = 0

    floweposX = 0
    flowposY = 0

    def __init__(self, eposX, eposY):
        self.eposX = eposX
        self.eposY = eposY

    def step(self, floweposX, flowposY, rag):

        if self.eposX == 5 and self.eposY == -1:
            self.eposX = 5
            self.eposY = 22

        if self.eposX == 5 and self.eposY == 23:
            self.eposX = 5
            self.eposY = 0

        if self.eposX == 34 and self.eposY==-1:
            self.eposX = 34
            self.eposY = 22

        if self.eposX == 34 and self.eposY == 23:
            self.eposX = 34
            self.eposY = 0

        self.floweposX = floweposX
        self.flowposY = flowposY

        moved: bool = False

        poss = []

        eposX = self.eposX
        eposY = self.eposY
        if map[eposY + 1][eposX] != 3 or map[eposY + 1][eposX] == 8:
            poss.append([eposY + 1, eposX])

        if map[eposY - 1][eposX] != 3 or map[eposY - 1][eposX] == 8:
            poss.append([eposY - 1, eposX])

        if map[eposY][eposX + 1] != 3 or map[eposY][eposX + 1] == 8:
            poss.append([eposY, eposX + 1])

        if map[eposY][eposX - 1] != 3 or map[eposY][eposX - 1] == 8:
            poss.append([eposY, eposX - 1])

        newPos = random.choice(poss)

        while newPos[0] == self.oldPosY and newPos[1] == self.oldePosX:
            newPos = random.choice(poss)

        self.oldePosX, self.oldPosY = self.eposX, self.eposY
        self.eposX, self.eposY = newPos[1], newPos[0]
        if floweposX == self.eposX and flowposY == self.eposY and rag:
            revenir_a_cage()
    
        return

        if poss[0][1] != -1 and self.calcDist(poss[0]) <= self.calcDist(poss[1]) and self.calcDist(poss[0]) <= self.calcDist(poss[2]) and self.calcDist(poss[0]) <= self.calcDist(poss[3]):
            self.eposX, self.eposY = poss[0][1], poss[0][0]
            moved = True
        if poss[1][1] != -1 and self.calcDist(poss[1]) <= self.calcDist(poss[0]) and self.calcDist(poss[1]) <= self.calcDist(poss[2]) and self.calcDist(poss[1]) <= self.calcDist(poss[3]):
            self.eposX, self.eposY = poss[1][1], poss[1][0]
            moved = True
        if poss[2][1] != -1 and self.calcDist(poss[2]) <= self.calcDist(poss[0]) and self.calcDist(poss[2]) <= self.calcDist(poss[1]) and self.calcDist(poss[2]) <= self.calcDist(poss[3]):
            self.eposX, self.eposY = poss[2][1], poss[2][0]
            moved = True
        if poss[3][1] != -1 and self.calcDist(poss[3]) <= self.calcDist(poss[0]) and self.calcDist(poss[3]) <= self.calcDist(poss[2]) and self.calcDist(poss[3]) <= self.calcDist(poss[1]):
            self.eposX, self.eposY = poss[3][1], poss[3][0]
            moved = True

    def calcDist(self, selfPos) -> int:
        return math.sqrt(abs((self.flowposY - selfPos[1]))**2 + abs((self.floweposX - selfPos[0]))**2)




    