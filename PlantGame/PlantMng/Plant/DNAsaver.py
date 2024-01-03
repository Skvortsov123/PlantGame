
import os
import shutil
import pickle

class DNAsaver:
    def __init__(self, plantMng):
        self.lastPlant = None
        self.plantMng = plantMng
        self.bestPlant = "BestPlants/BestPlant.pkl"

    def tick(self):
        if self.plantMng.get_biggest_plant():
            self.save_best_plant_DNA()

    def save_best_plant_DNA(self):
        if self.lastPlant != self.plantMng.get_biggest_plant():
            self.lastPlant = self.plantMng.get_biggest_plant()
            with open(self.bestPlant, 'wb') as file:
                pickle.dump(self.plantMng.get_biggest_plant().DNA.get_DNAList(), file)

    def create_best_DNA_plant(self, x, y, g):
        if not os.path.exists(self.bestPlant):
            shutil.copy("BestPlants/BestPlantCopy.pkl", self.bestPlant)
        with open(self.bestPlant, 'rb') as file:
            loadedBestDNA = pickle.load(file)
        plant = self.plantMng.create_plant(x, y, g)
        plant.DNA.set_DNA(loadedBestDNA)
        return plant