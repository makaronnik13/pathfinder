from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsScene
from GEdges import GEdges
from GPoints import GPoints

__author__ = 'makar'


class MyScene(QGraphicsScene):
    def __init__(self, window):
        super(QGraphicsScene, self).__init__()
        self.window = window

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            items = self.window.view.scene.items(event.scenePos().x(), event.scenePos().y(), event.scenePos().x(),
                                                 event.scenePos().y(), Qt.IntersectsItemShape, Qt.DescendingOrder,
                                                 self.window.view.transform())
            for i in items:
                if isinstance(i, GEdges):
                    self.window.redacted_line = i
            if self.window.redacted_line != 0:
                if self.window.red_mod:
                    self.window.rightWidget.hide()
                self.window.ad_right()
                self.window.rightWidget.update()
                self.window.rightWidget.show()
            else:
                gp = GPoints(event.pos().x(), event.pos().y(), self.window.r, self.window.r, self.window)
                gp.setPos(event.scenePos().x() - self.window.r / 2, event.scenePos().y() - self.window.r / 2)
                gp.setPen(self.window.view.p)
                gp.setBrush(self.window.view.b)
                self.window.g_points.append(gp)
                self.addItem(gp)