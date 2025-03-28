from PlantMng.PlantMng import *
from PlantMng.Matrix import *
from PlantMng.DNAsaver import *
from PlantMng.Statistics import *
from VideoMng.VideoMng import *
import time

class PlantGame:
    def __init__(self, Xsize=50, Ysize=50, amountTick=200):
        self.Xsize = Xsize
        self.Ysize = Ysize
        self.amountTick = amountTick
        self.tickTimer = 0
        self.plantMng = PlantMng(self)
        self.matrix = Matrix(self)
        self.DNAsaver = DNAsaver(self)
        self.statistics = Statistics(self)
        self.videoMng = VideoMng(self)

    def run(self):
        SaveTickTimer = 0
        if self.amountTick == 0:
            while len(self.plantMng.get_plantSet()) >= 1:
                self.tick()
                SaveTickTimer += 1
                if SaveTickTimer == 100:
                    self.DNAsaver.save_best_plant_DNA()
                    self.statistics.tick()
                    SaveTickTimer = 0
        else:
            for _ in range(self.amountTick):
                if len(self.plantMng.get_plantSet()) >= 1:
                    self.tick()
                else:
                    break
            self.DNAsaver.save_best_plant_DNA()
        #self.statistics.tick()
        #time.sleep(1)

    def tick(self):
            self.plantMng.tick()
            self.tick_tickTimer()
            self.videoMng.tick()
            #self.matrix.printColorMatrix()

    def tick_tickTimer(self):
        self.tickTimer += 1

    def get_Xsize(self):
        return self.Xsize

    def get_Ysize(self):
        return self.Ysize

    def get_tickTimer(self):
        return self.tickTimer

    def get_amountTick(self):
        return self.amountTick
