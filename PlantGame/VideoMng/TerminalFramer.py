
class TerminalFramer():
    def __init__(self, videoMng):
        self.videoMng = videoMng
        self.emptySlot = None
        self.lineCache = None
        self.clear_lineCache()
        self.frameCache = None

    def printColorMatrix(self):
        reversedWorld = self.videoMng.get_cellMatrix()[::-1]
        #print(f"Tick: {self.videoMng.get_tickTimer()}" + "\033[30m" + "000" + '\033[0m')
        #print(f"Amount Cell: {self.videoMng.plantMng.get_cellAmount()}" + "\033[30m" + "0000" + '\033[0m')
        for rowList in reversedWorld:
            print("")  # Next row
            for cell in rowList:
                if cell == self.emptySlot:
                    print('\033[30m' + "0" + '\033[0m', end="")
                else:
                    print(f"\033[38;5;{cell.get_group()}m{cell.get_printName()}\033[0m", end="")
        print("")
        self.move_cursor_start()

    def printColorMatrixMultipalSlices(self, amountSlices):
        self.clear_lineCache()
        self.clear_frameCache()
        print(f"\033[KTick: {self.videoMng.get_tickTimer()}")   #\033[K to clear line before writing
        reversedWorld = self.videoMng.get_cellMatrix()[::-1]
        for i in range(amountSlices):
            for rowList in reversedWorld:
                for cellNumber in range(len(rowList)//amountSlices):
                    cell = rowList[cellNumber+len(rowList)//amountSlices*i]
                    if cell == self.emptySlot:
                        self.lineCache += '\033[30m' + "0" + '\033[0m' #print('\033[30m' + "0" + '\033[0m', end="")
                    else:
                        self.lineCache += f"\033[38;5;{cell.get_group()}m{cell.get_printName()}\033[0m" #print(f"\033[38;5;{cell.get_group()}m{cell.get_printName()}\033[0m", end="")
                self.frameCache += self.lineCache  + '\n'
                self.clear_lineCache()
            print(self.frameCache)
            self.clear_frameCache()
        for _ in range(amountSlices):
            self.move_cursor_start()
        self.move_cursor_back(1) #Compensate Tick output

    def clear_lineCache(self):
        self.lineCache = str()

    def clear_frameCache(self):
        self.frameCache = str()

    def move_cursor_start(self):
        self.move_cursor_back(self.videoMng.get_ySize() + 1)

    def move_cursor_back(self, backLines):
        for _ in range(backLines):
            print("\033[F", end='', flush=True)