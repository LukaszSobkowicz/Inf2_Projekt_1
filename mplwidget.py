# -------------------- mplwidget.py --------------------
# Importy
from PyQt5 import QtWidgets
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib

# Wymuszenie PyQt5
matplotlib.use('QT5Agg')

# Matplotlib canvas do stworzenia wykresu
class MplCanvas(FigureCanvas):
    def __init__(self):
        self.fig = Figure()
        self.ax = self.fig.add_subplot(111)
        FigureCanvas.__init__(self, self.fig)
        #zmiana rozmiaru przy rozciaganiu okna
        FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Expanding, QtWidgets.
            QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

 # Matplotlib widget
class MplWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent) # dziedziczenie z QWidget
        self.canvas = MplCanvas() # utworzenie canvas
        self.vbl = QtWidgets.QVBoxLayout() # ustawienie elementtu
        self.vbl.addWidget(self.canvas)
        self.setLayout(self.vbl)