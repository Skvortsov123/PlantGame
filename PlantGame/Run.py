
from PlantGame import *

plantGame = PlantGame(300,50)
plantGame.plantMng.DNAsaver.create_best_DNA_plant(60-30,0,1)
plantGame.plantMng.DNAsaver.create_best_DNA_plant(120-30,0,2).DNA.mutate_DNA(0.1)
plantGame.plantMng.DNAsaver.create_best_DNA_plant(180-30,0,3).DNA.mutate_DNA(0.1)
plantGame.plantMng.DNAsaver.create_best_DNA_plant(240-30,0,4).DNA.mutate_DNA(0.1)
plantGame.plantMng.DNAsaver.create_best_DNA_plant(300-30,0,5).DNA.mutate_DNA(0.1)


for _ in range(300):
    if not len(plantGame.plantMng.get_plantSet()) <= 1:
        plantGame.tick()
        print(f"Tick: {plantGame.get_tickTimer()}")

    #max tick 1000 "conditions"