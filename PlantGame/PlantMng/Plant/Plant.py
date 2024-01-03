

from PlantMng.Plant.Cell.Cell import *
from PlantMng.Plant.Cell.Energy import *
from PlantMng.Plant.Cell.DNA import *

class Plant:
    def __init__(self, x, y, group, plantMng):
        self.x = x
        self.y = y
        self.group = group
        self.plantMng = plantMng
        self.cellSet = set()
        self.energy = Energy()
        self.DNA = DNA(self, 100)
        self.createCell(self.x, self.y)
        self.tickTimer = 0

    def tick(self):
        if self.energy.get_energy() <= 0:
            self.deleteSelf()
        else:
            self.tick_tickTimer()
            self.DNA.tick(self.get_cellSet())
            cellList = list(self.cellSet)
            for cell in cellList:
                cell.tick()
                self.energy.give_hungerCost()

    def createCell(self, x, y, relative_x=0, relative_y=0):
        if x >= self.plantMng.plantGame.get_Xsize():         #To cycle X to loop
            x = x - (self.plantMng.plantGame.get_Xsize())
        if x < 0:
            x = x + self.plantMng.plantGame.get_Xsize()
        if not self.plantMng.if_cell_exists(x, y):
            if x < self.plantMng.plantGame.get_Xsize() and x >= 0 and y < self.plantMng.plantGame.get_Ysize() and y >= 0:
                self._forceCreateCell(x, y, relative_x, relative_y)
                self.energy.give_growCost()

    def _forceCreateCell(self, x, y, relative_x, relative_y):
        cell = Cell(x, y, relative_x, relative_y, self)
        self.cellSet.add(cell)
        self.plantMng.add_cell_matrix(cell)

    def deleteSelf(self):   #Raises flag in PlantMng to del self
        self.plantMng.add_to_deletePlantSet(self)

    def tick_tickTimer(self):
        self.tickTimer += 1


    def if_cell_exists(self, checkCell):
        existsFlag = 0
        if checkCell in self.get_cellSet():
            return 1
        else:
            return 0

    def get_tickTimer(self):
        return self.tickTimer

    def get_cellSet(self):
        return self.cellSet

    def get_group(self):
        return self.group

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return f"Plant: x{self.x} y{self.y} g{self.group}"
