import datetime
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGraphicsLineItem, QGraphicsEllipseItem, QTableWidget, QTableWidgetItem

__author__ = 'makar'


class GEdges(QGraphicsLineItem):
    def __init__(self, x1, y1, x2, y2):
        QGraphicsEllipseItem.__init__(self, x1, y1, x2, y2)
        self.point_to = 0
        self.point_from = 0
        self.path_point = 0
        self.path_point_to = 0
        self.tbl = QTableWidget(1, 2)
        item = QTableWidgetItem("0:00")
        self.tbl.setItem(0, 0, item)
        item = QTableWidgetItem("0:00")
        self.tbl.setItem(0, 1, item)
        self.tbl.setFixedWidth(219)
        item = QTableWidgetItem("time of origin")
        self.tbl.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem("path time")
        self.tbl.setHorizontalHeaderItem(1, item)

    def save_points(self):
        self.point_from.out_edges.append(self)
        self.point_to.in_edges.append(self)

    def mouseDoubleClickEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("RDACT!")

    def set_point_to(self, point):
        self.point_to = point

    def set_point_from(self, point):
        self.point_from = point

    def weight(self, time):
        for i in range(0, self.tbl.rowCount()):
            if datetime.datetime.strptime(self.tbl.item(i, 0).text(), "%H:%M") > time:
                return datetime.datetime.strptime(self.tbl.item(i, 1).text(), "%H:%M")+datetime.timedelta(hours=datetime.datetime.strptime(self.tbl.item(i, 0).text(), "%H:%M").hour, minutes=datetime.datetime.strptime(self.tbl.item(i, 0).text(), "%H:%M").minute)-datetime.timedelta(hours=time.hour, minutes=time.minute)
        return datetime.datetime.strptime("14:28", "%H:%M")

    def save_info(self, tbl):
        self.tbl = tbl