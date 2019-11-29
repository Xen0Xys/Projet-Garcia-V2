from PyQt5 import QtCore
from PyQt5.QtWidgets import *
import sys

#pyinstaller -F -w "ui.py"

class SearchSettingsCanvas(QGroupBox):
    def __init__(self):
        super().__init__()

class MainUi(QWidget):
    resized = QtCore.pyqtSignal()
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.fullscreen = False
        self.style_sheet = self.loadStyleSheet()
        self.setStyleSheet(self.style_sheet)
        self.setupWindow()
        self.mainVue()
        self.resized.connect(self.sayWindowSize)
        if self.fullscreen:
            self.showFullScreen()
        else:
            self.show()
        sys.exit(self.app.exec_())
    def resizeEvent(self, event):
        self.resized.emit()
        return None
    def sayWindowSize(self):
        #print("Window Resize :", self.geometry().width(), self.geometry().height())
        pass
    def loadStyleSheet(self):
        style_name = "white_style"
        file = open("styles/{}.css".format(style_name), "r")
        content = file.read()
        file.close()
        return content
    def setupWindow(self):
        self.setWindowTitle("Gestion tennis de table")
        self.setGeometry(300, 300, 250, 150)
    def mainVue(self):
        test_button = QPushButton("Quitter", self)
        test_button.clicked.connect(lambda arg = self.app.exec: sys.exit(arg))
        test_button.move(10, 10)
        
        layout = QGridLayout()
        layout.addWidget(test_button, 1, 1)
        self.setLayout(layout)
        

MainUi()