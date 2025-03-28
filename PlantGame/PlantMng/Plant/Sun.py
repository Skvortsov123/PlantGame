
class Sun:
    def __init__(self, plantMng):
        self.plantMng = plantMng

    def tick(self):
        plantList = self.plantMng.get_plantSet()
        cellUnderSun = self.plantMng.get_cell_under_sun()
        for cell in cellUnderSun:
            for plant in plantList:
                if plant.if_cell_exists(cell):
                    plant.energy.give_sunCost(cell.get_sunCoefficient())#*self.highCoefficient(cell))

    def highCoefficient(self, cell): #higher = more sun   #0.25 0.5 0.75 1
        coefficient = cell.get_x() * 0.25 + 0.25
        if coefficient > 1:
            coefficient = 1
        return coefficient