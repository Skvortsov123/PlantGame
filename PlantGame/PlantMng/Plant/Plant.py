

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
        self.cellSeedSet = set()
        self.energy = Energy()
        self.DNA = DNA(self)
        self.createCell(self.x, self.y)
        self.tickTimer = 0
        self.lifeTime = self.DNA.get_lifeTime()

    def tick(self):
        if self.energy.get_energy() <= 0:
            self.deleteSelf()
        elif self.get_tickTimer() >= self.lifeTime:   #Make suicide DNA
            self.deleteSelf()
        else:
            self.tick_tickTimer()
            self.DNA.tick(self.get_cellSet())
            cellList = list(self.cellSet)
            for cell in cellList:
                cell.tick()
                self.energy.give_hungerCost(cell.get_hungerCoefficient())

    def createCell(self, x, y, relative_x=0, relative_y=0, cellType="Normal"):     #Make different types
        if x >= self.plantMng.plantGame.get_Xsize():         #To cycle X to loop
            x = x - (self.plantMng.plantGame.get_Xsize())
        if x < 0:
            x = x + self.plantMng.plantGame.get_Xsize()
        if not self.plantMng.if_cell_exists(x, y):
            if x < self.plantMng.plantGame.get_Xsize() and x >= 0 and y < self.plantMng.plantGame.get_Ysize() and y >= 0:
                cell = None
                if cellType == "Normal":
                    cell = self._forceCreateCellNormal(x, y, relative_x, relative_y)
                if cellType == "Sun":
                    cell = self._forceCreateCellSun(x, y, relative_x, relative_y)
                if cellType == "Seed":
                    cell = self._forceCreateCellSeed(x, y, relative_x, relative_y)
                self.energy.give_growCost(cell.get_growCoefficient())

    def _forceCreateCellNormal(self, x, y, relative_x, relative_y):
        cell = Cell(x, y, relative_x, relative_y, self)
        self.cellSet.add(cell)
        self.plantMng.add_cell_matrix(cell)
        return cell

    def _forceCreateCellSun(self, x, y, relative_x, relative_y):
        cell = CellSun(x, y, relative_x, relative_y, self)
        self.cellSet.add(cell)
        self.plantMng.add_cell_matrix(cell)
        return cell

    def _forceCreateCellSeed(self, x, y, relative_x, relative_y):
        cell = CellSeed(x, y, relative_x, relative_y, self)
        self.cellSet.add(cell)
        self.cellSeedSet.add(cell)
        self.plantMng.add_cell_matrix(cell)
        return cell

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

    def set_DNA(self, DNA):
        self.DNA = DNA

    def get_DNA(self):
        return self.DNA

    def get_tickTimer(self):
        return self.tickTimer

    def get_cellSet(self):
        return self.cellSet

    def get_cellSeedSet(self):
        return self.cellSeedSet

    def get_cellAmount(self):
        return len(self.get_cellSet())

    def get_group(self):
        return self.group

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        return f"Plant: x{self.x} y{self.y} g{self.group}"
