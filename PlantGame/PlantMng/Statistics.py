import os

class Statistics:
    def __init__(self, plantGame):
        self.plantGame = plantGame


    def tick(self): #Tick at end
        pass
        #self.save_amount_plant()
        #self.save_biggest_plant_amount_cell()
        #self.save_biggest_plant_amount_cell_end_of_round()

    def save_biggest_plant_amount_cell(self):
        filePath = "Statistics/BiggestPlantAmountCell"
        if self.plantGame.plantMng.get_biggest_plant():
            with open(filePath, "a") as file:
                file.write(str(self.plantGame.plantMng.get_biggest_plant().get_cellAmount())+"\n")

    def save_biggest_plant_amount_cell_end_of_round(self):
        filePath = "Statistics/BiggestPlantAmountCellEndOfRound"
        if self.plantGame.plantMng.get_biggest_plant():
            if self.plantGame.get_amountTick() == self.plantGame.get_tickTimer():
                with open(filePath, "a") as file:
                    file.write(str(self.plantGame.plantMng.get_biggest_plant().get_cellAmount())+"\n")

    def save_amount_plant(self):
        filePath = "Statistics/AmountPlantOpenWorld"
        with open(filePath, "a") as file:
            file.write(str(len(self.plantGame.plantMng.get_plantSet())) + "\n")