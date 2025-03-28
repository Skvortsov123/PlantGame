from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import threading

class PyQTFramer():
    def __init__(self, videoMng=None):
        self.videoMng = videoMng
        self.app = QApplication(sys.argv)
        framer = PlantWidget()
        framer.show()

    def run(self):
        self.app.exec_()

    def startEventLoop(self):
        """Run the event loop in a separate thread."""
        event_thread = threading.Thread(target=self.run)
        event_thread.daemon = True  # Allow the thread to exit when the program exits
        event_thread.start()

class PlantWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PlantGame")

    def tick(self):
        #first add more rect
        self.update()

    def paintEvent(self, event):
        """Draw rectangles."""
        painter = QPainter(self)
        painter.setBrush(QColor(0, 150, 255))  # Blue color
        painter.drawRect(1, 1, 10, 10)


