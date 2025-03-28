from VideoMng.TerminalFramer import *
#from VideoMng.PyQTFramer import *

class VideoMng:
    def __init__(self, plantGame, videoType=[1,2]):
        self.plantGame = plantGame
        self.videoType = videoType #1-Terminal #2-PyQT
        self.cellMatrix = None
        self.ySize = None
        self.xSize = None
        self.tickTimer = None
        self.terminalFramer = TerminalFramer(self)
        #Testing
        #self.pyqtFramer = PyQTFramer(self)
        #self.pyqtFramer.startEventLoop()

    def tick(self):
        self.reload_variables()
        for type in self.videoType:
            if type == 1:
                self.show_terminal_frame()
            if type == 2:
                self.show_pyqt_frame()

    def reload_variables(self):
        self.cellMatrix = self.plantGame.plantMng.get_cellMatrix().copy()
        self.ySize = int(self.plantGame.get_Ysize())
        self.xSize = int(self.plantGame.get_Xsize())
        self.tickTimer = int(self.plantGame.get_tickTimer())

    def show_terminal_frame(self):
        self.terminalFramer.printColorMatrixMultipalSlices(3)

    def show_pyqt_frame(self):
        pass

    def get_cellMatrix(self):
        return self.cellMatrix

    def get_xSize(self):
        return self.xSize

    def get_ySize(self):
        return self.ySize

    def get_tickTimer(self):
        return self.tickTimer