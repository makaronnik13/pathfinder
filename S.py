import matplotlib
from MyWindow import MyWindow
matplotlib.use("Qt5Agg")
from PyQt5 import QtWidgets
import sys

if __name__ == '__main__':
    matplotlib.use("Qt5Agg")
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    window.setGeometry(100, 100, 900, 600)
    sys.exit(app.exec_())