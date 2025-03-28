#!/usr/bin/python3

from PlantGame import *
import time
import sys

if not "-d" in sys.argv:    #Run Normal or create and save DNA
    while True:
        plantGame = PlantGame(1200, 30, 0)

        #plantGame.DNAsaver.create_best_DNA_plant(10, 0, 1)
        plantGame.DNAsaver.create_best_DNA_plant(190, 0, 2).DNA.mutate_DNA(0.3)

        plantGame.run()
else:
    plantGame = PlantGame(200, 30, 1000)
    pickle.dump(plantGame.plantMng.create_plant(10, 0, 1).DNA, open("BestPlants/BestPlantCopy.pkl", 'wb'))    #No copyFile, if no best, just generate it
