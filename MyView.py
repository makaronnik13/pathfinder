from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPen, QPainter, QBrush, QColor
from PyQt5.QtWidgets import QGraphicsView
from MyScene import MyScene

__author__ = 'makar'


class MyView(QGraphicsView):
    def __init__(self, window):
        self.window = window
        self.scene = MyScene(window)
        super(QGraphicsView, self).__init__(self.scene)
        self.setScene(self.scene)
        self.setRenderHint(QPainter.HighQualityAntialiasing)
        self.p = QPen(QColor(121, 48, 34), 3, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin)
        self.b2 = QBrush(QColor(218, 126, 7))
        self.b = QBrush(QColor(157, 106, 107))
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setSceneRect(0, 0, 100, 100)
