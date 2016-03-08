import datetime
import matplotlib
from GEdges import GEdges

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

__author__ = 'makar'


class GPoints(QGraphicsEllipseItem):
    def __init__(self, x, y, r1, r2, window):
        QGraphicsEllipseItem.__init__(self, x, y, r1, r2)
        self.in_edges = []
        self.out_edges = []
        self.window = window
        self.in_time = datetime.datetime.strptime("23:28", "%H:%M")

    def save_edges(self):
        for edge in self.in_edges:
            edge.set_point_to(self)
        for edge in self.out_edges:
            edge.set_point_from(self)

    def mousePressEvent(self, event):
        self.window.to_gpoint = 0
        if event.button() == Qt.RightButton:
            self.window.from_gpoint = self
            self.window.from_point.setX(event.scenePos().x())
            self.window.from_point.setY(event.scenePos().y())
            self.window.line.setLine(event.scenePos().x(), event.scenePos().y(), event.scenePos().x(), event.scenePos().y())
            self.window.view.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.RightButton:
            items = self.window.view.scene.items(event.scenePos().x(), event.scenePos().y(), event.scenePos().x(),
                                            event.scenePos().y(), Qt.IntersectsItemShape, Qt.DescendingOrder,
                                            self.window.view.transform())
            for i in items:
                if isinstance(i, GPoints):
                    self.window.to_gpoint = i
                if isinstance(i, GEdges):
                    self.window.redacted_line = i

            if isinstance(self.window.to_gpoint, GPoints):
                if self.window.to_gpoint != self.window.from_gpoint:
                    lin = GEdges(0, 0, 0, 0)
                    lin.setPen(self.window.view.p)
                    lin.setLine(self.window.line.line())
                    lin.point_to = self.window.to_gpoint
                    lin.point_from = self.window.from_gpoint
                    self.window.g_edges.append(lin)
                    self.window.view.scene.addItem(lin)
                    self.window.to_gpoint.in_edges.append(lin)
                    self.out_edges.append(lin)
                    #self.save_ages()
#                    self.window.ad_right()
#                    self.window.rightWidget.update()
#                    self.window.rightWidget.show()
            self.window.line.setLine(0, 0, 0, 0)
        self.window.save_path()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.setPos(event.scenePos().x() - self.window.r / 2, event.scenePos().y() - self.window.r / 2)
            for i in self.out_edges:
                i.setLine(event.scenePos().x(), event.scenePos().y(), i.line().x2(), i.line().y2())
            for i in self.in_edges:
                i.setLine(i.line().x1(), i.line().y1(), event.scenePos().x(), event.scenePos().y())

        if event.buttons() == QtCore.Qt.RightButton:
            self.window.path_mode = True
            self.window.line.setLine(self.window.from_point.x(), self.window.from_point.y(), event.scenePos().x(),
                                event.scenePos().y())
