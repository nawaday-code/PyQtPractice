import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.resize(400, 300)
        self.move(400, 300)
        self.setWindowTitle('first PyQt5')

        btn = QPushButton('Hello World!', self)

        btn.resize(btn.sizeHint())
        btn.move(100, 59)

app = QApplication(sys.argv)
mainWindow = MainWindow()
mainWindow.show()
sys.exit(app.exec_())