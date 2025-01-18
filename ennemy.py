import random

class Enemy():
    posY = 0
    posX = 0
    path = [[]]

    def __init__(self, posX, posY, map):
        self.posX = posX
        self.posY = posY
        self.path = map

    def step(self):
        poss = []

        for y in range(self.posY - 1 , self.posY + 1):
            for x in range(self.posX - 1, self.posX + 1):
                if self.path[y][x] == 0:
                    poss.append([y, x])

        self.posX, self.posY = random.choice(poss)

    

    