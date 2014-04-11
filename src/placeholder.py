from PyQt4 import QtGui, QtCore

class PH(QtGui.QWidget):
    def __init__(self, text):
        super(PH, self).__init__()
        self.text = text
        self.initUI()

    def initUI(self):
        label_text = "<span style='font-size: 14pt; font-face: bold;'>" + self.text + "</span>"

        label = QtGui.QLabel(label_text, self)
        label.setAlignment(QtCore.Qt.AlignCenter)
        label.setWordWrap(True)

        box = QtGui.QVBoxLayout(self)
        box.addWidget(label)
        self.setLayout(box)

    def paintEvent(self, e):
        # Set sizes of the frame corner
        corner_s = 5
        corner_b = 20

        # Set pen and brush and begin rawing
        qp = QtGui.QPainter()
        qp.begin(self)

        color = QtGui.QColor(0, 0, 0)
        qp.setPen(color)
        qp.setBrush(QtGui.QColor(0, 0, 0))

        # Get width and height
        size = self.size()
        width = size.width()
        height = size.height()

        # Top left corner
        qp.drawRect(0, 0, corner_s, corner_b)
        qp.drawRect(0, 0, corner_b, corner_s)

        # Top right corner
        qp.drawRect(width, 0, -corner_s, corner_b)
        qp.drawRect(width, 0, -corner_b, corner_s)

        # bottom left corner
        qp.drawRect(0, height, corner_s, -corner_b)
        qp.drawRect(0, height, corner_b, -corner_s)

        # bottom right corner
        qp.drawRect(width, height, -corner_s, -corner_b)
        qp.drawRect(width, height, -corner_b, -corner_s)

        qp.end()

    def makeStuff(self, qp):
        qp.setPen(QtCore.Qt.red)
        qp.drawRect(10, 10, 40, 40)
        qp.drawRect(60, 10, 40, 40)
        qp.drawRect(10, 60, 90, 40)

