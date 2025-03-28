from PlantMng.PlantMng import *
import time

class PlantTest:
    def __init__(self, Xsize=50, Ysize=50, amountTick=200):
        self.Xsize = Xsize
        self.Ysize = Ysize
        self.amountTick = amountTick
        self.tickTimer = 0
        self.plantMng = PlantMng(self)

    def run(self):
        for _ in range(self.amountTick):
            if not len(self.plantMng.get_plantSet()) <= 0:
                self.tick()
            else:
                break
        time.sleep(1)

    def tick(self):
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
