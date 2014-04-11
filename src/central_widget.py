from PyQt4 import QtGui, QtCore
from placeholder import *
from projects_tree import *

class CentralWidget(QtGui.QWidget):
    def __init__(self):
        super(CentralWidget, self).__init__()
        self.initUI()

    def initUI(self):
        # Make the widgets
        self.makeWidgets()

        # Main layout
        box = QtGui.QHBoxLayout()
        box.addWidget(self.main_split)
        self.setLayout(box)

    def makeWidgets(self):
        # Make widgets
        self.elements_catalog = PH("Costume Widget for Digital Elements Catalog Will Go Here.")
        self.circuit_display = PH("Costume Widget for Circuit Display and Manipulation Will Go Here.")
        self.projects_tree = ProjectsTree()
        self.properties_display = PH("Properties will go here.")

        # Make splits and add widgets
        self.right_split = QtGui.QSplitter(QtCore.Qt.Vertical)
        self.right_split.addWidget(self.projects_tree)
        self.right_split.addWidget(self.properties_display)

        self.main_split = QtGui.QSplitter(QtCore.Qt.Horizontal)
        self.main_split.addWidget(self.elements_catalog)
        self.main_split.addWidget(self.circuit_display)
        self.main_split.addWidget(self.right_split)

        # Set relative sizes of splits
        height = self.right_split.size().height()
        self.right_split.setSizes([height * (1.0 / 4.0), height * (3.0 / 4.0)])

        width = self.main_split.size().width()
        self.main_split.setSizes([width * (2.0 / 10.0), width * (8.0 / 10.0), width * (2.0 / 10.0)])

