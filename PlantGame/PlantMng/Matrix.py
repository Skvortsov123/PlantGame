
import sys

class Matrix:   #Matrix tick()
    def __init__(self, plantGame):
        self.plantGame = plantGame
        self.emptySlot = [0, 0]
        self.matrix = []
        self.zero_matrix()

    def printColorMatrix(self):
        self.move_cursor_start()
        self.refresh_matrix()
        reversedWorld = self.matrix[::-1]
        print(f"Tick: {self.plantGame.get_tickTimer()}" + "\033[30m" + "000" + '\033[0m')
        print(f"Amount Cell: {self.plantGame.plantMng.get_cellAmount()}" + "\033[30m" + "0000" + '\033[0m')
        for rowList in reversedWorld:
            print("")   #Next row
            for symbList in rowList:
                if symbList == self.emptySlot:
                    print('\033[30m' + f"{symbList[1]}" + '\033[0m', end="")
                else:
                    print(f"\033[38;5;{symbList[0] % 256}m{symbList[1]}\033[0m", end="")
        print("")

    def set_pixel_matrix(self, x, y, group):
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
                self.set_pixel_matrix(cell.get_x(), cell.get_y(), [plant.get_group(), cell.get_printName()])

    def move_cursor_start(self):
        for _ in range(self.plantGame.get_Ysize()+4):
            print("\033[F", end='', flush=True)