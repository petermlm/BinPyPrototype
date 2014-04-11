import sys
from PyQt4 import QtGui
from mainwindow import Main

def main():
    app = QtGui.QApplication(sys.argv)
    m = Main()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

