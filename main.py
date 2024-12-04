import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt6.QtGui import QPainter, QPen, QBrush, QColor
from PyQt6.QtCore import Qt, QRect
import random


class Ui_MainWindow(object):
    def __init__(self):
        self.centralwidget = None
        self.button = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setLayout(QVBoxLayout())
        self.button = QPushButton("Добавить круг", parent=self.centralwidget)
        self.button.setObjectName("button")


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.circles = []
        self.setupUi(self)
        self.button.clicked.connect(self.addCircle)
        self.show()

    def addCircle(self):
        x = random.randint(0, 700)
        y = random.randint(0, 500)
        diameter = random.randint(10, 100)
        color_ = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.circles.append((x, y, diameter, color_))
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        for x, y, diameter, color_ in self.circles:
            qp.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
            qp.setBrush(QBrush(QColor(color_[0], color_[1], color_[2])))
            qp.drawEllipse(QRect(x, y, diameter, diameter))
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())


