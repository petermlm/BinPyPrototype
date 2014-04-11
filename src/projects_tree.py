from PyQt4 import QtGui

class ProjectsTree(QtGui.QWidget):
    def __init__(self):
        super(ProjectsTree, self).__init__()
        self.initUI()

    def initUI(self):
        self.tree = QtGui.QTreeWidget()
        self.tree.setColumnCount(1)
        self.tree.header().close()

        circuit1 = QtGui.QTreeWidgetItem(self.tree)
        circuit2 = QtGui.QTreeWidgetItem(self.tree)

        circuit1.setText(0, "One Example Circuit")
        circuit2.setText(0, "Another Example")

        sub_circuit1 = QtGui.QTreeWidgetItem(circuit1)
        sub_circuit2 = QtGui.QTreeWidgetItem(circuit1)
        sub_circuit3 = QtGui.QTreeWidgetItem(circuit2)

        sub_circuit1.setText(0, "A Sub Circuit")
        sub_circuit2.setText(0, "Another Sub Circuit")
        sub_circuit3.setText(0, "Some Other Sub Circuit")

        box = QtGui.QVBoxLayout(self)
        box.addWidget(self.tree)
        self.setLayout(box)

