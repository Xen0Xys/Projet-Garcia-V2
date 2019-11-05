from PyQt5.QtWidgets import *
import sys

#pyinstaller -F -w "ui.py"

class MainUi(QWidget):
    def __init__(self):
        self.app = QApplication(sys.argv)
        super().__init__()
        self.fullscreen = True
        self.style_sheet = self.loadStyleSheet()
        self.setStyleSheet(self.style_sheet)
        self.setupWindow()
        self.mainVue()
        if self.fullscreen:
            self.showFullScreen()
        else:
            self.show()
        sys.exit(self.app.exec_())
    def loadStyleSheet(self):
        style_name = "white_style"
        file = open("styles/{}.css".format(style_name), "r")
        content = file.read()
        file.close()
        return content
    def setupWindow(self):
        self.setWindowTitle("Gestion tennis de table")
    def mainVue(self):
        test_button = QPushButton("Quitter")
        test_button.clicked.connect(lambda arg = self.app.exec: sys.exit(arg))
        layout = QGridLayout()
        layout.addWidget(test_button, 1, 1)
        self.setLayout(layout)

MainUi()