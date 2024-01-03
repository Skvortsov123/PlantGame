
import sys

class Matrix:   #Matrix tick()
    def __init__(self, plantGame):
        self.plantGame = plantGame
        self.emptySlot = 0
        self.matrix = []
        self.zero_matrix()

    def printColorMatrix(self):
        self.move_cursor_start()
        self.refresh_matrix()
        reversedWorld = self.matrix[::-1]
        for row in reversedWorld:
            print("")
            for symb in row:
                if symb == self.emptySlot:
                    print('\033[30m' + f"{symb}" + '\033[0m', end="")
                elif symb == 1:
                    print('\033[31m' + f"{symb}" + '\033[0m', end="")
                elif symb == 2:
                    print('\033[32m' + f"{symb}" + '\033[0m', end="")
                elif symb == 3:
                    print('\033[33m' + f"{symb}" + '\033[0m', end="")
                elif symb == 4:
                    print('\033[34m' + f"{symb}" + '\033[0m', end="")
                elif symb == 5:
                    print('\033[35m' + f"{symb}" + '\033[0m', end="")
                else:
                    print('\033[92m' + f"{symb}" + '\033[0m', end="")
        print("")

    def set_matrix(self, x, y, group):
        self.matrix[y][x] = group

    def zero_matrix(self):
        self.matrix.clear()
        for y in range(self.plantGame.get_Ysize()):
            self.matrix.append([])
            for x in range(self.plantGame.get_Xsize()):
                self.matrix[y].append(self.emptySlot)

    def refresh_matrix(self):
        self.zero_matrix()
        for plant in self.plantGame.plantMng.get_plantSet():
            for cell in plant.get_cellSet():
                self.set_matrix(cell.get_x(), cell.get_y(), plant.get_group())

    def move_cursor_start(self):
        for _ in range(self.plantGame.get_Ysize()+2):
            print("\033[F", end='', flush=True)