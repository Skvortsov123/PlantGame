
from PlantMng.Plant.Plant import *
from PlantMng.Plant.Sun import *
from array import array
import copy

class PlantMng:
    def __init__(self, plantGame):
        self.plantGame = plantGame
        self.sun = Sun(self)
        self.plantSet = set()
        self.cellMatrix = [[None] * plantGame.get_Xsize() for _ in range(plantGame.get_Ysize())]
        self.cellAmount = 0
        self.deletePlantSet = set()

    def tick(self):
        for plant in self.plantSet:
            plant.tick()
        self.sun.tick()
        self.delete_deletePlantSet()

    def create_plant(self, x, y, group):
        if x >= 0 and y >= 0 and x < self.plantGame.get_Xsize() and y < self.plantGame.get_Ysize():
            if not self.if_cell_exists(x, y):
                return self.force_create_plant(x, y, group)

    def force_create_plant(self, x, y, group):
        plant = Plant(x, y, group, self)
        self.plantSet.add(plant)
        return plant

    def if_plant_exists(self, plant):
        if plant in self.get_plantSet():
            return 1
        else:
            return 0

    def if_cell_exists(self, x, y):     #Many tick's
        if x > self.plantGame.get_Xsize()-1:
            x = 0
        if x < 0:
            x = self.plantGame.get_Xsize()-1
        if y > self.plantGame.get_Ysize()-1:
            return 0
        if self.get_cellMatrix()[y][x]:
            return 1
        return 0

    def add_cell_matrix(self, cell):
        self.cellMatrix[cell.get_y()][cell.get_x()] = cell
        self.cellAmount += 1

    def add_to_deletePlantSet(self, plant):
        self.deletePlantSet.add(plant)

    def delete_deletePlantSet(self):
        for plant in self.deletePlantSet:
            self.plantSet.remove(plant)
            self.deletePlantSet = set()
            matrix = self.get_cellMatrix()
            for y in range(len(matrix)):
                for x in range(len(matrix[y])):
                    if matrix[y][x] in plant.get_cellSet():
                        matrix[y][x] = None
                        self.cellAmount -= 1
            self.plant_seeds(plant)

    def plant_seeds(self, plant):
        if plant.get_cellSeedSet():
            pass
            #self.plantGame.DNAsaver.save_plant_DNA_as_best(plant.get_DNA())    #It makes too many saves per time, will kill ssd
        for cellSeed in plant.get_cellSeedSet():
            if cellSeed.get_tickTimer() > 10:   #10
                newPlant = self.create_plant(cellSeed.get_x(), 0, int(random.random()*256))
                if not newPlant == None:
                    newPlant.set_DNA(copy.deepcopy(plant.get_DNA()))
                    newPlant.DNA.mutate_DNA(0.01)    #0.01

    def get_biggest_plant(self):
        max_length = 0
        biggest_plant = None
        for plant in self.get_plantSet():
            current_length = plant.get_cellAmount()
            if current_length > max_length:
                max_length = current_length       #Many Tick's
                biggest_plant = plant
        return biggest_plant

    def get_plantSet(self):
        return self.plantSet

    def get_cellMatrix(self): #Get cells from all Plants
        return self.cellMatrix

    def get_cell_under_sun(self):   #Move into PlantMng
        matrix = self.get_cellMatrix()
        firstElement = []
        for x in range(self.plantGame.get_Xsize()):
            for y in range(self.plantGame.get_Ysize() - 1, -1, -1):
                if matrix[y][x]:
                    firstElement.append(matrix[y][x])
                    break
        return firstElement

    def get_cellAmount(self):
        return self.cellAmount