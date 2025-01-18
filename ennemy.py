import random
import math
from map import map

class Enemy():
    posY = 0
    posX = 0

    def __init__(self, posX, posY):
        self.posX = posX
        self.posY = posY

    def step(self, flowposX, flowposY):
        poss = []
        dists = []

        if map[self.posY - 1][self.posX - 1] == 0:
            poss.append([self.posY - 1, self.posX - 1])
        if map[self.posY - 1][self.posX] == 0:
            poss.append([self.posY - 1, self.posX])
        if map[self.posY - 1][self.posX + 1] == 0:
            poss.append([self.posY - 1, self.posX + 1])

        if map[self.posY][self.posX - 1] == 0:
            poss.append([self.posY, self.posX - 1])
        if map[self.posY][self.posX + 1] == 0:
            poss.append([self.posY, self.posX + 1])

        if map[self.posY + 1][self.posX - 1] == 0:
            poss.append([self.posY + 1, self.posX - 1])
        if map[self.posY + 1][self.posX] == 0:
            poss.append([self.posY + 1, self.posX])
        if map[self.posY + 1][self.posX + 1] == 0:
            poss.append([self.posY + 1, self.posX + 1])

        for pos in poss:
            dists.append(self.calcDist(flowposX, flowposY))

        nearest = 9999999999999
        index = 0
        for i in range(0, len(dists)):
            if dists[i] <= nearest:
                nearest = dists[i]
                index = i

        self.posX, self.posY = poss[i]

    def calcDist(self, flowposX, flowposY) -> int:
        return math.sqrt(abs((flowposY - self.posY))**2 + abs((flowposX - self.posX))**2)




    