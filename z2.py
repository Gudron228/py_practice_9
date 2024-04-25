from PySide6.QtCore import QPropertyAnimation, QPoint, QEasingCurve, QPointF, QParallelAnimationGroup
from PySide6.QtWidgets import QApplication, QWidget, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(1000)
        self.setMinimumHeight(500)
        self.setWindowTitle("Анимация виджетов")

        self.widget = QWidget(self)
        self.widget.setGeometry(50, 150, 100, 100)
        self.widget.setStyleSheet("background-color: green;")

        self.secondWidget = QWidget(self)
        self.secondWidget.setGeometry(50, 200, 150, 100)
        self.secondWidget.setStyleSheet("background-color: red;")


        anim = QPropertyAnimation(self.widget, b"pos", self)
        anim.setDuration(3000)
        anim.setStartValue(QPoint(50, 150))
        anim.setEndValue(QPoint(300,400))
        anim.setEasingCurve(QEasingCurve.OutInBounce)

        secondAnim = QPropertyAnimation(self.secondWidget, b"pos", self)
        secondAnim.setDuration(3000)
        secondAnim.setStartValue(QPoint(0, 0))
        secondAnim.setEndValue(QPoint(600, 400))
        secondAnim.setEasingCurve(QEasingCurve.InOutBounce)

        sequenceAnim = QParallelAnimationGroup(self)
        sequenceAnim.addAnimation(anim)
        sequenceAnim.addAnimation(secondAnim)
        sequenceAnim.start()

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    app.exec()
