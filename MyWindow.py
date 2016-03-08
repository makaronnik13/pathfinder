from PyQt5.QtGui import QKeySequence
from PyQt5.uic.properties import QtGui
import matplotlib
from matplotlib.dates import DateFormatter
import sip
import time

from GEdges import GEdges
from GPoints import GPoints
from MyView import MyView

matplotlib.use("Qt5Agg")
from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from pylab import *
import random

__author__ = 'makar'


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.figure = plt.figure()  # PLOT GRAPH
        self.view = MyView(self)
        self.g_points = []
        self.g_edges = []
        self.createUI()
        self.t = 0
        self.nums = 5
        self.chance =0.5
        self.red_mod = False
        self.last_time = 0
        self.mainWidget = QWidget(self)
        self.setCentralWidget(self.mainWidget)
        self.redacted_line = 0
        self.leftLayout = QHBoxLayout()
        self.mainLayout = QHBoxLayout(self.mainWidget)
        self.mainLayout.addLayout(self.leftLayout)
        self.leftLayout.addWidget(self.view)
        self.base_tree_edges = []
        # self.base_tree_points = []
        self.tree_edges = []
        self.tree_points = []
        self.tree_points_g = []
        self.tree_edges_g = set()
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
        self.r = math.sqrt(self.width() * self.width() + self.height() * self.height()) / 32

        self.line = GEdges(0, 0, 0, 0)
        self.line.setPen(self.view.p)
        self.from_point = QtCore.QPoint(0, 0)
        self.from_gpoint = GPoints(0, 0, 0, 0, self)
        self.to_gpoint = GPoints(0, 0, 0, 0, self)
        self.view.scene.addItem(self.line)

    def stat(self):

        f = open('stat.txt', 'a')
        f.write('++++++++'+'\n')
        self.nums = 5 #10
        f.write('++++'+str(self.nums)+'++++'+'\n')
        print("++++", self.nums, "++++")
        f.close()
        self.chance = 0.2
        self.statistic()
        self.chance = 0.5
        self.statistic()
        self.chance = 0.7
        self.statistic()
        self.chance = 1
        self.statistic()
        print("++++++++++++++++")

        f = open('stat.txt', 'a')
        f.write('+++++++++++++++ '+'\n')
        print("++++++++++++++++")
        self.nums = 10
        f.write('++++'+str(self.nums)+'++++'+'\n')
        print("++++", self.nums, "++++")
        f.close()
        self.chance = 0.2
        self.statistic()
        self.chance = 0.5
        self.statistic()
        self.chance = 0.7
        self.statistic()
        self.chance = 1
        self.statistic()

        f = open('stat.txt', 'a')
        f.write('+++++++++++++++ '+'\n')
        print("++++++++++++++++")
        self.nums = 15
        f.write('++++'+str(self.nums)+'++++'+'\n')
        print("++++", self.nums, "++++")
        f.close()
        self.chance = 0.2
        self.statistic()
        self.chance = 0.5
        self.statistic()
        self.chance = 0.7
        self.statistic()
        self.chance = 1
        self.statistic()
        """f = open('stat.txt', 'a')
        self.nums = 20
        f.write('++++'+str(self.nums)+'++++'+'\n')
        print("++++", str(self.nums), "++++")
        f.close()
        self.chance = 0.2
        self.statistic()
        self.chance = 0.5
        self.statistic()
        self.chance = 0.7
        self.statistic()
        self.chance = 1
        self.statistic()
        """
        f = open('stat.txt', 'a')
        f.write('++++++++'+'\n')
        f.close()

    def statistic(self):
        fi = open('stat.txt', 'a')
        fi.write('-----'+str(self.chance)+'-----'+'\n')
        print("-----", self.chance, "-----")
        all_bad = 0
        all_algo = 0
        all_algo2 = 0
        all_algo3 = 0
        all_check = 0
        all_algo_t = 0
        all_check_t = 0
        fi.close()
        times = 1
        for i in range(0, times):
            self.create_random()
            t1 = time.time()
            self.find_spaning_tree()
        #    print("bad: ", (self.get_global_weight().day-1)*24*60+self.get_global_weight().hour*60+self.get_global_weight().minute)
            all_bad += (self.get_global_weight().day-1)*24*60+self.get_global_weight().hour*60+self.get_global_weight().minute
            if self.base_tree_edges.__len__() != self.g_edges.__len__():
                self.balance_graph(1)
        #    print("algo: ", (self.get_global_weight().day-1)*24*60+self.get_global_weight().hour*60+self.get_global_weight().minute)
            all_algo += (self.get_global_weight().day-1)*24*60+self.get_global_weight().hour*60+self.get_global_weight().minute
            all_algo_t += time.time() - t1
            #2-й тип
            #self.g_edges = self.base_tree_edges
            #for p in self.g_points:
            #    p.save_edges()
            #self.find_spaning_tree()

            if self.base_tree_edges.__len__() != self.g_edges.__len__():
                self.balance_graph(2)
        #    print("algo2: ", (self.getы_global_weight().day-1)*24*60+self.get_global_weight().hour*60+self.get_global_weight().minute)
            all_algo2 += (self.get_global_weight().day-1)*24*60+self.get_global_weight().hour*60+self.get_global_weight().minute

            #3-й
            if self.base_tree_edges.__len__() != self.g_edges.__len__():
                self.balance_graph(3)
        #    print("algo3: ", (self.get_global_weight().day-1)*24*60+self.get_global_weight().hour*60+self.get_global_weight().minute)
            all_algo3 += (self.get_global_weight().day-1)*24*60+self.get_global_weight().hour*60+self.get_global_weight().minute

            #полный перебор
            t1 = time.time()
        #    print("check all: ", self.full_check())
            all_check += self.full_check()
            all_check_t += time.time() - t1
            #self.print_global_weight()
            #print(time.time() - t1)
        #    print("_____")
        fi = open('stat.txt', 'a')
        fi.write(str(all_bad/times)+' | 1:'+str(all_algo/times)+' | 2:'+str(all_algo2/times)+' | 3:'+str(all_algo3/times)+' | '+str(all_check/times)+'\n')
        fi.write(str(all_algo_t/times)+' | '+str(all_check_t/times)+'\n')
        fi.write('______'+'\n')
        print(all_bad/10, " | 1:", all_algo/10, " | 2:", all_algo2/10, " | 3:", all_algo3/10, " | ", all_check/10)
        print(all_algo_t/10, " | ", all_check_t/10)
        print("_____")
        fi.close()

    def full_check(self):
        #self.find_spaning_tree()
        s = 0
        for i in range(0, self.base_tree_edges.__len__()):
            s += math.pow(2, i)
        #print(s)
        min_time = 99999999
        for ch_e in range(self.g_edges.__len__()-1, int(s)+1):
            z = ch_e
            self.g_edges = []

            for en in range(0, self.base_tree_edges.__len__()):
                if z >= math.pow(2, self.base_tree_edges.__len__())/math.pow(2, en)/2:
                    #print("z=", z, "-", math.pow(2, self.base_tree_edges.__len__())/math.pow(2, en)/2, "   ", self.base_tree_edges[en])
                    self.g_edges.append(self.base_tree_edges[en])
                    z -= math.pow(2, self.base_tree_edges.__len__())/math.pow(2, en)/2

            for p in self.g_points:
                p.in_edges = []
                p.out_edges = []

            for e in self.g_edges:
                e.save_points()
                #print(e, " ", e.point_from, " ", e.point_to)
            #print(self.check_connection())
            if self.check_connection():
                if min_time > (self.get_global_weight().day-1)*24*60+self.get_global_weight().hour*60+self.get_global_weight().minute:
                    min_time = (self.get_global_weight().day-1)*24*60+self.get_global_weight().hour*60+self.get_global_weight().minute
                #print((self.get_global_weight().day-1)*24*60+self.get_global_weight().hour*60+self.get_global_weight().minute)
                #self.print_global_weight()
                #print("min time ", min_time)
                #print("________")
                #print(self.get_global_weight())
            if self.check_connection():
                #self.print_global_weight()
                for e in self.g_edges:
                    self.view.scene.addItem(e)
            #print("+++")
        #print("!!!!!!")
        return (min_time)

    def randomDate(self, start, end):
        return str(random.randint(start, end)) + ":" + str(random.randint(1, 59))

    def save_path(self):
        self.g_points = []
        self.g_edges = []
        for e in self.view.scene.items():
            if isinstance(e, GPoints):
                self.g_points.append(e)
            if isinstance(e, GEdges):
                if e != self.line:
                    self.g_edges.append(e)

        for p in self.g_points:
            p.in_edges = []
            p.out_edges = []
        for e in self.g_edges:
            e.point_to.in_edges.append(e)
            e.point_from.out_edges.append(e)
        for j in self.g_points:
            for i in j.out_edges:
                i.setLine(j.scenePos().x() + self.r / 2, j.scenePos().y() + self.r / 2, i.line().x2(),
                          i.line().y2())
            for i in j.in_edges:
                i.setLine(i.line().x1(), i.line().y1(), j.scenePos().x() + self.r / 2,
                          j.scenePos().y() + self.r / 2)

    def check_connection(self):
        checked_points = [self.g_points[0]]
        for p in checked_points:
            # print("-", checked_points.__len__(), "-")
            for e in p.in_edges:
                if e.point_to not in checked_points:
                    checked_points.append(e.point_to)
                if e.point_from not in checked_points:
                    checked_points.append(e.point_from)
            for e in p.out_edges:
                if e.point_to not in checked_points:
                    checked_points.append(e.point_to)
                if e.point_from not in checked_points:
                    checked_points.append(e.point_from)
        if checked_points.__len__() == self.g_points.__len__():
            return True
        else:
            return False

    def balance_graph(self, type):
        if type == 1:
            self.t = self.g_edges.__len__() * 2 * self.g_points.__len__()
        elif type == 2:
            tn = self.g_edges.__len__() * 2 * self.g_points.__len__()
            x = 1
            self.t = tn
        elif type ==3:
            tn = self.g_edges.__len__() * 2 * self.g_points.__len__()
            x = tn
            self.t = tn

        while self.t > 0:
    #        print("---", self.t, "---")
            self.add_random_edge()
            if type == 1:
                self.t -= 1
            elif type == 2:
                x += 1
                self.t = math.sqrt(math.pow(tn, 2)-math.pow(x, 2))
            elif type ==3:
                x -= 1
                self.t = tn-math.sqrt(math.pow(tn, 2)-math.pow(x, 2))

    def create_random(self):
        self.create_new()
        point_num = 20
        point_num = self.nums
        edge_chance = 1
        edge_chance = self.chance
        for i in range(point_num):
            k1 = random.random() - 0.5
            k2 = random.random() - 0.5
            gp = GPoints(0, 0, self.r, self.r, self)
            gp.setPos(self.view.width() * k1 * 0.9 + self.r, self.view.height() * k2 * 0.9 + self.r)
            gp.setPen(self.view.p)
            gp.setBrush(self.view.b)
            self.g_points.append(gp)
            self.view.scene.addItem(gp)
        # for p in self.g_points:
        for p in range(self.g_points.__len__()):
            for p2 in range(0, p):
                if random.random() < edge_chance:
                    lin = GEdges(self.g_points[p].x(), self.g_points[p].y(), self.g_points[p2].x(),
                                 self.g_points[p2].y())
                    lin.setLine(self.g_points[p].x(), self.g_points[p].y(), self.g_points[p2].x(),
                                self.g_points[p2].y())
                    lin.setPen(self.view.p)
                    lin.point_to = self.g_points[p]
                    lin.point_from = self.g_points[p2]
                    self.g_edges.append(lin)
                    self.view.scene.addItem(lin)
        self.save_path()
        if not self.check_connection():
            self.create_random()
        for e in self.g_edges:
            self.redacted_line = e
            self.tbl = self.redacted_line.tbl
            self.create_random_table(True)
            self.redacted_line.save_info(self.tbl)
            self.redacted_line = 0

    def add_random_edge(self):
        miss_edges = []
        for e in self.base_tree_edges:
            if e not in self.g_edges:
                miss_edges.append(e)
        r1 = random.randint(0, miss_edges.__len__() - 1)
        r2 = random.randint(0, self.g_edges.__len__() - 1)
        adding_edge = miss_edges[r1]
        del_edge = self.g_edges[r2]
        '''print(self.base_tree_edges)
        print(miss_edges)
        print(self.g_edges)
        print(miss_edges[r1], " & ", self.g_edges[r2])'''
        self.view.scene.addItem(adding_edge)
        self.g_edges.append(adding_edge)
        self.view.scene.removeItem(del_edge)
        self.g_edges.remove(del_edge)
        self.view.scene.update()
        self.save_path()
        if not self.check_connection():
            self.view.scene.addItem(del_edge)
            self.g_edges.append(del_edge)
            self.view.scene.removeItem(adding_edge)
            self.g_edges.remove(adding_edge)
            self.view.scene.update()
            self.add_random_edge()
        else:
            '''if de_num > 0:
                self.view.scene.addItem(del_edge)
                self.g_edges.append(del_edge)
                self.view.scene.removeItem(adding_edge)
                self.g_edges.remove(adding_edge)
                self.view.scene.update()
            else:
                print("\/")
                print(-de_num)
                print("||")'''
    #        print("-------------")
    #        print(self.last_time)
    #        print("\/")
            dif = -self.last_time
            noch = self.last_time
            self.last_time = (self.get_global_weight().day-1)*24*60+self.get_global_weight().hour*60+self.get_global_weight().minute
            dif += self.last_time
    #        print(dif)
            ra_a = random.uniform(0, math.e)
            ra_b = math.pow(math.e, -dif/self.t)
    #        print(math.pow(math.e, -dif/self.t))
    #        print("\/")
    #        print(self.last_time)
            if (dif > 0) or (ra_a > ra_b):
                self.last_time = noch
                self.view.scene.addItem(del_edge)
                self.g_edges.append(del_edge)
                self.view.scene.removeItem(adding_edge)
                self.g_edges.remove(adding_edge)
                self.view.scene.update()
    #        else:
    #           print("changed!")

    def create_random_table(self, flag=False):
        if not flag:
            self.tbl = self.rightWidget.findChild(QTableWidget)
        self.tbl.setRowCount(0)
        self.tbl.setColumnCount(2)
        self.tbl.clear()
        for i in range(0, 6):
            self.tbl.setRowCount(self.tbl.rowCount() + 1)
            item = QTableWidgetItem(self.randomDate(0, 3))
            self.tbl.setItem(self.tbl.rowCount() - 1, 1, item)
            item = QTableWidgetItem(self.randomDate(i * 3, (i + 1) * 3))
            self.tbl.setItem(self.tbl.rowCount() - 1, 0, item)

    def print_global_weight(self):
        global_time = self.get_global_weight()
        print(
            str(global_time.day - 1) + " days/" + str(global_time.hour) + " hours/" + str(
                global_time.minute) + " minutes")

    def get_global_weight(self):
        # print("++++++")
        #for g in self.g_points:
        #        print(g, "|", g.in_edges, "|", g.out_edges)
        #print("++++++")

        check_points = []
        check_edges = []
        start_point = self.g_points[0]
        start_time = datetime.datetime.strptime('01 00:00', '%d %H:%M')
        start_point.in_time = start_time
        check_points.append(start_point)
        for p in check_points:
            if check_points.__len__() == self.g_points.__len__():
                break
            for e in p.in_edges:
                if e not in check_edges:
                    e.path_point = p
                    if e.point_to == p:
                        e.path_point_to = e.point_from
                    else:
                        e.path_point_to = e.point_to
                    e.path_point_to.in_time = e.path_point.in_time + datetime.timedelta(
                        minutes=e.weight(e.path_point.in_time).minute, hours=e.weight(e.path_point.in_time).hour)
                    check_points.append(e.path_point_to)
                    check_edges.append(e)
                    #print("+ ", e.weight(e.path_point.in_time))
                    start_time += datetime.timedelta(minutes=e.weight(e.path_point.in_time).minute,
                                                     hours=e.weight(e.path_point.in_time).hour)
                    #print(start_time)
            for e in p.out_edges:
                if e not in check_edges:
                    e.path_point = p
                    if e.point_to == p:
                        e.path_point_to = e.point_from
                    else:
                        e.path_point_to = e.point_to
                    e.path_point_to.in_time = e.path_point.in_time + datetime.timedelta(
                        minutes=e.weight(e.path_point.in_time).minute, hours=e.weight(e.path_point.in_time).hour)
                    check_edges.append(e)
                    check_points.append(e.path_point_to)
                    #print("+ ", e.weight(e.path_point.in_time))
                    start_time += datetime.timedelta(minutes=e.weight(e.path_point.in_time).minute,
                                                     hours=e.weight(e.path_point.in_time).hour)
                    #print(start_time)
        return start_time

    def find_spaning_tree(self):
        self.base_tree_edges = self.g_edges.copy()
        # self.base_tree_points = self.g_points
        for g in self.g_points:
            g.save_edges()

        """for g in self.g_points:
                print(g, "|", g.in_edges, "|", g.out_edges)
        print("++++++++++++++++++++")"""
        ## global_time = self.get_global_weight()
        ##print(str(global_time.day)+" days/"+str(global_time.hour)+" hours/"+str(global_time.minute)+" minutes")

        if self.g_points.__len__() != 0:
            start_time = datetime.datetime.strptime("00:00", "%H:%M")  # start time
            start_point_num = 0  # start_point
            span_edges = []

            self.tree_points.append(self.g_points[start_point_num])
            self.tree_points[0].in_time = start_time

            while True:
                for point in self.tree_points:
                    for edge in point.in_edges:
                        edge.path_point = point
                        if edge not in self.tree_edges:
                            if not ((edge.point_to in self.tree_points) and (edge.point_from in self.tree_points)):
                                span_edges.append(edge)
                    for edge in point.out_edges:
                        edge.path_point = point
                        if edge not in self.tree_edges:
                            if not ((edge.point_to in self.tree_points) and (edge.point_from in self.tree_points)):
                                span_edges.append(edge)
                if len(span_edges) == 0:
                    break
                check_edge = span_edges[0]
                for edge in span_edges:
                    if edge.weight(edge.path_point.in_time) < check_edge.weight(check_edge.path_point.in_time):
                        check_edge = edge
                # print(datetime.timedelta(minutes=check_edge.weight(check_edge.path_point.in_time).minute, hours=check_edge.weight(check_edge.path_point.in_time).hour))
                start_time += datetime.timedelta(minutes=check_edge.weight(check_edge.path_point.in_time).minute,
                                                 hours=check_edge.weight(check_edge.path_point.in_time).hour)
                self.tree_edges.append(check_edge)
                if check_edge.point_to not in self.tree_points:
                    check_edge.point_to.in_time = check_edge.weight(start_time)
                    self.tree_points.append(check_edge.point_to)
                else:
                    check_edge.point_from.in_time = check_edge.weight(start_time)
                    self.tree_points.append(check_edge.point_from)
                span_edges.clear()
                #print(str(start_time.day)+" days/"+str(start_time.hour)+" hours/"+str(start_time.minute)+" minutes")
            self.create_new(True)

            #self.print_global_weight()
            self.last_time = (self.get_global_weight().day-1)*24*60+self.get_global_weight().hour*60+self.get_global_weight().minute

        for p in self.g_points:
            p.setBrush(self.view.b)
        self.g_points[0].setBrush(self.view.b2)

    def ad_right(self):
        start = []
        finish = []
        self.tbl = self.redacted_line.tbl
        all_rows = self.tbl.rowCount()
        struct_time_x = datetime.datetime.strptime("00:00", "%H:%M")
        start.append(struct_time_x)
        struct_time_y = datetime.datetime.strptime(self.tbl.item(0, 1).text(), "%H:%M") + datetime.timedelta(
            hours=datetime.datetime.strptime(self.tbl.item(0, 0).text(), "%H:%M").hour,
            minutes=datetime.datetime.strptime(self.tbl.item(0, 0).text(), "%H:%M").minute)
        finish.append(struct_time_y)

        for i in range(0, all_rows):
            struct_time_x = datetime.datetime.strptime(self.tbl.item(i, 0).text(), "%H:%M")
            start.append(struct_time_x)
            start.append(struct_time_x)
            struct_time_y = datetime.datetime.strptime(self.tbl.item(i, 1).text(), "%H:%M")
            finish.append(struct_time_y)
            if i < all_rows - 1:
                struct_time_x2 = datetime.datetime.strptime(self.tbl.item(i + 1, 0).text(), "%H:%M")
                struct_time_y = datetime.datetime.strptime(self.tbl.item(i, 1).text(), "%H:%M") + datetime.timedelta(
                    minutes=struct_time_x2.minute, hours=struct_time_x2.hour) - datetime.timedelta(
                    minutes=struct_time_x.minute, hours=struct_time_x.hour)
            else:
                struct_time_y = finish[0] + datetime.timedelta(minutes=59, hours=23) - datetime.timedelta(
                    minutes=struct_time_x.minute, hours=struct_time_x.hour)
            finish.append(struct_time_y)

        struct_time_x = datetime.datetime.strptime("23:59", "%H:%M")
        start.append(struct_time_x)
        struct_time_y = finish[0]
        finish.append(struct_time_y)

        start = matplotlib.dates.date2num(start)
        finish = matplotlib.dates.date2num(finish)
        hours = MinuteLocator(byminute=range(720), interval=15, tz=None)
        hoursFmt = DateFormatter("%H:%M")
        fig, ax = plt.subplots()
        pd = plot_date(start, finish, '-')
        plt.setp(pd, color='brown', linestyle='-', linewidth=1, marker='o', markersize=4, markeredgecolor='brown',
                 markerfacecolor='peru', markeredgewidth=2)
        # ax.yaxis.set_major_locator(hours)
        ax.yaxis.set_major_formatter(hoursFmt)
        # ax.autoscale_view()
        ax.grid(True)
        axes = plt.gca()
        axes.set_xlim([datetime.datetime.strptime("00:00", "%H:%M"), datetime.datetime.strptime("23:59", "%H:%M")])
        axes.set_ylim([datetime.datetime.strptime("00:00", "%H:%M"), datetime.datetime.strptime("23:59", "%H:%M")])

        fig.autofmt_xdate()
        self.canvas = FigureCanvas(fig)
        self.canvas.update()
        self.rightWidget = QWidget()
        self.rightWidget.setFixedWidth(400)
        self.rightLayout = QVBoxLayout(self.rightWidget)
        self.mainLayout.addWidget(self.rightWidget)
        self.tbl.setParent(self.rightWidget)
        self.rightLayout.addWidget(self.tbl, Qt.AlignTop)
        self.rightLayout.addWidget(self.canvas, Qt.AlignTop)
        ai = QPushButton("add item")
        ai.clicked.connect(self.ad_item)
        self.rightLayout.addWidget(ai, Qt.AlignTop)
        ab = QPushButton("acsept")
        ab.clicked.connect(self.abM)
        self.rightLayout.addWidget(ab, Qt.AlignTop)
        ra = QPushButton("randomize")
        ra.clicked.connect(self.create_random_table)
        self.rightLayout.addWidget(ra, Qt.AlignTop)
        self.red_mod = True

    def ad_item(self):
        self.tbl = self.rightWidget.findChild(QTableWidget)
        self.tbl.setRowCount(self.tbl.rowCount() + 1)
        item = QTableWidgetItem("0:00")
        self.tbl.setItem(self.tbl.rowCount() - 1, 1, item)
        item = QTableWidgetItem(self.tbl.item(self.tbl.rowCount() - 2, 0).text())
        self.tbl.setItem(self.tbl.rowCount() - 1, 0, item)

    def abM(self):
        self.redacted_line.save_info(self.tbl)
        self.rightWidget.hide()
        self.redacted_line = 0
        self.red_mod = False
        self.save_path()

    def create_new(self, finding=False):
        if finding:
            # self.view.scene.update()

            boof = []
            for go in self.g_edges:
                if go not in self.tree_edges:
                    boof.append(go)
            for go in boof:
                self.g_edges.remove(go)
                self.view.scene.removeItem(go)
            boof = []
            for g in self.g_points:
                if g not in self.tree_points:
                    boof.append(g)
            for go in boof:
                self.g_points.remove(go)
                self.view.scene.removeItem(go)
            self.view.scene.update()

            self.tree_points.clear()
            self.tree_edges.clear()
            for g in self.g_points:
                g.in_edges = []
                g.out_edges = []
            for g in self.g_edges:
                g.save_points()
        else:
            self.g_points = []
            self.g_edges = []
            self.redacted_line = 0
            widget_name = self.view
            self.leftLayout.removeWidget(widget_name)
            sip.delete(widget_name)
            self.view = MyView(self)
            self.leftLayout.addWidget(self.view)
            self.view.scene.addItem(self.line)

    def about(self):
        QMessageBox.information(self, "Information", "Tishkin Nikita\nMIEM HSE\n2015")

    def help(self):
        QMessageBox.information(self, "Help",
                                "Double click: create point\nDouble click on point and drag: create edge\nClick and drag: move pont")

    def createUI(self):
        self.setWindowTitle('Pathfinder')
        menu = self.menuBar().addMenu('File')
        about = self.menuBar().addMenu('About')
        find = self.menuBar().addMenu('Find')
        create = self.menuBar().addMenu('Create')
        span_tree = find.addAction('Spaning tree')
        get_weigh = find.addAction('Weigh')
        ch_edge = find.addAction('Change')
        full_check = find.addAction('Full check')
        balance = find.addAction('Balance')
        create_r = create.addAction('Random graph')
        stat = create.addAction('Statistic')
        help = about.addAction('Help')
        info = about.addAction('Info')
        new = menu.addAction('New')
        # save = menu.addAction('Save')
        # load = menu.addAction('Load')
        new.triggered.connect(self.create_new)
        stat.triggered.connect(self.stat)
        full_check.triggered.connect(self.full_check)
        # save.triggered.connect(self.save_json)
        # load.triggered.connect(self.load_json)
        info.triggered.connect(self.about)
        help.triggered.connect(self.help)
        balance.triggered.connect(self.balance_graph)
        get_weigh.triggered.connect(self.print_global_weight)
        span_tree.triggered.connect(self.find_spaning_tree)
        ch_edge.triggered.connect(self.add_random_edge)  #!!!
        create_r.triggered.connect(self.create_random)
        balance.setShortcuts(QKeySequence("Ctrl+B"))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter:
            self.add_random_edge()
        if event.key() == Qt.Key_Delete:
            self.tbl = self.rightWidget.findChild(QTableWidget)
            self.tbl.removeRow(self.tbl.currentRow())
        if self.tbl.rowCount() == 0:
            self.view.scene.removeItem(self.redacted_line)
            self.abM()