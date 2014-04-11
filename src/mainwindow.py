from PyQt4 import QtGui, QtCore
from central_widget import *

class Main(QtGui.QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.initUI()

    def initUI(self):
        # Make actions
        self.makeActions()

        # Make bars
        self.makeStatusBar()
        self.makeMenuBar()
        self.makeToolbar()

        # Make the central widget
        cw = CentralWidget()
        self.setCentralWidget(cw)

        # Set window properties and display it
        self.showMaximized()
        self.setWindowTitle("Prototype for the BinPy GUI.")
        self.show()

        # Display a message in the status bar
        self.sb.showMessage("Prototype")

    def makeActions(self):
        # Actions for the File menu
        # New
        self.new_act = QtGui.QAction("New", self)
        self.new_act.setShortcut("Ctrl+N")
        self.new_act.setStatusTip("Create New Circuit")

        # Open
        self.open_act = QtGui.QAction("Open", self)
        self.open_act.setShortcut("Ctrl+O")
        self.open_act.setStatusTip("Open Circuit")

        # Save
        self.save_act = QtGui.QAction("Open", self)
        self.save_act.setShortcut("Ctrl+S")
        self.save_act.setStatusTip("Save Circuit")

        # Save As...
        self.save_as_act = QtGui.QAction("Open", self)
        self.save_as_act.setShortcut("Ctrl+Shift+S")
        self.save_as_act.setStatusTip("Save Circuit As...")

        # Close
        self.close_act = QtGui.QAction("Close Circuit", self)
        self.close_act.setShortcut("Ctrl+W")
        self.close_act.setStatusTip("Close Circuit")

        # Exit
        self.exit_act = QtGui.QAction("Exit", self)
        self.exit_act.setShortcut("Ctrl+Q")
        self.exit_act.setStatusTip("Exit Application")
        self.exit_act.triggered.connect(QtGui.qApp.quit)

        # Actions for the Edit menu
        # Undo
        self.undo_act = QtGui.QAction("Undo", self)
        self.undo_act.setShortcut("Ctrl+Z")
        self.undo_act.setStatusTip("Undo Changes")

        # Redo
        self.redo_act = QtGui.QAction("Redo", self)
        self.redo_act.setShortcut("Ctrl+Shift+Z")
        self.redo_act.setStatusTip("Redo Changes")

        # Copy
        self.copy_act = QtGui.QAction("Copy Selection", self)
        self.copy_act.setShortcut("Ctrl+C")
        self.copy_act.setStatusTip("Exit Application")

        # Cut
        self.cut_act = QtGui.QAction("Cut Selection", self)
        self.cut_act.setShortcut("Ctrl+X")
        self.cut_act.setStatusTip("Exit Application")

        # Paste
        self.paste_act = QtGui.QAction("Paste", self)
        self.paste_act.setShortcut("Ctrl+V")
        self.paste_act.setStatusTip("Exit Application")

        # Actions for the Simulation menu
        # Start
        self.start_act = QtGui.QAction("Start", self)
        self.start_act.setShortcut("Ctrl+R")
        self.start_act.setStatusTip("Start the Simulation")

        # Stop
        self.stop_act = QtGui.QAction("Stop", self)
        self.stop_act.setStatusTip("Stop the Simulation")

    def makeStatusBar(self):
        self.sb = self.statusBar()

    def makeMenuBar(self):
        menubar = self.menuBar()

        # File
        self.file_menu = menubar.addMenu("&File")
        self.file_menu.addAction(self.new_act)
        self.file_menu.addAction(self.open_act)
        self.file_menu.addAction(self.save_act)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.save_as_act)
        self.file_menu.addAction(self.exit_act)

        # Edit
        self.edit_menu = menubar.addMenu("&Edit")
        self.edit_menu.addAction(self.undo_act)
        self.edit_menu.addAction(self.redo_act)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.copy_act)
        self.edit_menu.addAction(self.cut_act)
        self.edit_menu.addAction(self.paste_act)

        # Simulation
        self.simulation_menu = menubar.addMenu("&Simulation")
        self.simulation_menu.addAction(self.start_act)
        self.simulation_menu.addAction(self.stop_act)

    def makeToolbar(self):
        self.toolbar = self.addToolBar("Exit")
        self.toolbar.addAction(self.exit_act)

        # File
        self.file_menu = self.addToolBar("File")
        self.file_menu.addAction(self.new_act)
        self.file_menu.addAction(self.open_act)
        self.file_menu.addAction(self.save_act)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.save_as_act)
        self.file_menu.addAction(self.exit_act)

        # Edit
        self.edit_menu = self.addToolBar("Edit")
        self.edit_menu.addAction(self.undo_act)
        self.edit_menu.addAction(self.redo_act)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.copy_act)
        self.edit_menu.addAction(self.cut_act)
        self.edit_menu.addAction(self.paste_act)

        # Simulation
        self.simulation_menu = self.addToolBar("Simulation")
        self.simulation_menu.addAction(self.start_act)
        self.simulation_menu.addAction(self.stop_act)

