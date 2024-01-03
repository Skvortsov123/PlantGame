
class Sun:
    def __init__(self, plantMng):
        self.plantMng = plantMng

    def tick(self):
        plantList = self.plantMng.get_plantSet()
        cellUnderSun = self.get_cell_under_sun()
        for cell in cellUnderSun:
            for plant in plantList:
                if plant.if_cell_exists(cell):
                    plant.energy.give_sunCost()


    def get_cell_under_sun(self):
        matrix = self.plantMng.get_cellMatrix()
        firstElement = []
        for x in range(self.plantMng.plantGame.get_Xsize()):
            for y in range(self.plantMng.plantGame.get_Ysize() - 1, -1, -1):
                if matrix[y][x]:
                    firstElement.append(matrix[y][x])
                    break
        return firstElement