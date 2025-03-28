
import os
import shutil
import pickle
from PlantTest import *

class DNAsaver:
    def __init__(self, plantGame):
        self.plantGame = plantGame
        self.bestPlant = "BestPlants/BestPlant.pkl"

    def save_best_plant_DNA(self):
        lastBiggestPlant = self.plantGame.plantMng.get_biggest_plant()
        if lastBiggestPlant:
            biggestPlantDNA = lastBiggestPlant.DNA
            with open(self.bestPlant, 'rb') as file:
                if not pickle.load(file).get_uuid() == biggestPlantDNA.get_uuid():
                    #if self.if_plant_survivable(biggestPlantDNA):
                    self.save_plant_DNA_as_best(biggestPlantDNA)

    def if_plant_survivable(self, DNA):
        plantTest = PlantTest(self.plantGame.get_Xsize(), self.plantGame.get_Ysize(), self.plantGame.get_amountTick())
        plantTest.plantMng.create_plant(10,0,1).set_DNA(DNA)
        plantTest.run()
        return plantTest.get_tickTimer() == self.plantGame.get_amountTick()


    def create_best_DNA_plant(self, x, y, g):
        if not os.path.exists(self.bestPlant):  #If best plant was deletet, remove statistics
            shutil.copy("BestPlants/BestPlantCopy.pkl", self.bestPlant)
        with open(self.bestPlant, 'rb') as file:
            loadedBestDNA = pickle.load(file)
        plant = self.plantGame.plantMng.create_plant(x, y, g)
        plant.set_DNA(loadedBestDNA)
        return plant

    def save_plant_DNA_as_best(self, plant):
        with open(self.bestPlant, 'wb') as file:
            pickle.dump(plant, file)
