

from PlantMng.PlantMng import *
from PlantMng.Matrix import *


class PlantGame:
    def __init__(self, Xsize=100, Ysize=100):
        self.Xsize = Xsize
        self.Ysize = Ysize
        self.tickTimer = 0
        self.plantMng = PlantMng(self)
        self.matrix = Matrix(self)

    def tick(self):
        self.matrix.printColorMatrix()
        self.plantMng.tick()
        self.tick_tickTimer()

    def tick_tickTimer(self):
        self.tickTimer += 1

    def get_Xsize(self):
        return self.Xsize

    def get_Ysize(self):
        return self.Ysize

    def get_tickTimer(self):
        return self.tickTimer