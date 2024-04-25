from PySide6.QtCore import Qt, QLineF, QRect, QPointF
from PySide6.QtGui import QFont, QPainter, QPen, QRadialGradient, QBrush, QPainterPath, QColor, QLinearGradient
from PySide6.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(600)
        self.setMinimumHeight(200)
        self.setWindowTitle("Рисование фигур")

    def paintEvent(self, arg__0):
        pen = QPen()
        pen.setStyle(Qt.SolidLine)
        pen.setWidth(3)
        pen.setBrush(Qt.black)
        painter = QPainter(self)
        #Треугольник
        painter.setPen(pen)
        painter.setBrush(QBrush(Qt.black))
        painter.drawLine(QLineF(275.0, 10.0, 200.0, 90.0))
        painter.drawLine(QLineF(275.0, 10.0, 350.0, 90.0))
        painter.drawLine(QLineF(200.0, 90.0, 350.0, 90.0))
        # Эллипс
        painter.setBrush(QBrush(Qt.red))
        painter.setPen(pen)
        painter.drawEllipse(10, 125, 150, 100)
        #Квадрат
        gradient = QLinearGradient(QPointF(150, 150), QPointF(200, 200))
        gradient.setColorAt(0.5, Qt.magenta)
        gradient.setColorAt(1, Qt.yellow)
        painter.setBrush(QBrush(gradient))
        painter.setPen(pen)
        painter.drawRect(200, 100, 150, 150)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()