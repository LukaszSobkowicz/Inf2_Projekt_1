import sys
from gui_v1 import *
from funkcje import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QWidget, QMainWindow, QFileDialog, QColorDialog
from PyQt5.QtGui import *
import matplotlib.pyplot as plt
import numpy as np

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowTitle("przeciecie v1.0.0")    # tytuł okna
        self.col1 = 'r' # zmienne potrzebne do zmiany koloru linii
        self.col2 = 'g'
        self.col3 = 'b'
        self.ui.oblicz_btn.clicked.connect(self.oblicz) # przypisanie sygnałów do slotów
        self.ui.wyczysc_btn.clicked.connect(self.wyczysc)
        self.ui.wyczysc_wyniki_btn.clicked.connect(self.wyczysc_wyniki)
        self.ui.zapisz_btn.clicked.connect(self.zapisz)
        self.ui.rysuj_btn.clicked.connect(self.rysuj)
        self.ui.kolor1_btn.clicked.connect(self.zmien_kolor1)
        self.ui.kolor2_btn.clicked.connect(self.zmien_kolor2)
        self.ui.kolor3_btn.clicked.connect(self.zmien_kolor3)
        # Walidacja wprowadzanych danych
        validator = QtGui.QDoubleValidator()
        self.ui.edit_XA.setValidator(validator)
        self.ui.edit_YA.setValidator(validator)
        self.ui.edit_XB.setValidator(validator)
        self.ui.edit_YB.setValidator(validator)
        self.ui.edit_XC.setValidator(validator)
        self.ui.edit_YC.setValidator(validator)
        self.ui.edit_XD.setValidator(validator)
        self.ui.edit_YD.setValidator(validator)

        self.show()

    def oblicz(self): # Obliczenie współrzędnych punktu przecięcia P
        XA = float(self.ui.edit_XA.text()) # pobranie danych wpisowych z interfejsu
        YA = float(self.ui.edit_YA.text())
        XB = float(self.ui.edit_XB.text())
        YB = float(self.ui.edit_YB.text())
        XC = float(self.ui.edit_XC.text())
        YC = float(self.ui.edit_YC.text())
        XD = float(self.ui.edit_XD.text())
        YD = float(self.ui.edit_YD.text())
        # Funkcja obliczająca współrzędne punktu P
        komentarz, XP, YP = PktPrzec(XA, YA, XB, YB, XC, YC, XD, YD)

        self.ui.komentarz_lbl.setText(komentarz) # Wyświetlenie wyników
        self.ui.output_XP.setText(XP)
        self.ui.output_YP.setText(YP)
        # Funkcja obliczająca azymuty linii
        AzAB = Azymut(XA, YA, XB, YB)
        AzCD = Azymut(XC, YC, XD, YD)

        self.ui.output_AzAB.setText(AzAB) # Wyświetlenie wyników
        self.ui.output_AzCD.setText(AzCD)

    def wyczysc_wyniki(self): # Wyczyszczenie pól z wprowadzonymi danymi
        self.ui.output_XP.clear()
        self.ui.output_YP.clear()
        self.ui.output_AzAB.clear()
        self.ui.output_AzCD.clear()
        self.ui.komentarz_lbl.clear()

    def wyczysc(self): # Wyczyszczenie pól z wynikami obliczeń
        self.ui.edit_XA.clear()
        self.ui.edit_YA.clear()
        self.ui.edit_XB.clear()
        self.ui.edit_YB.clear()
        self.ui.edit_XC.clear()
        self.ui.edit_YC.clear()
        self.ui.edit_XD.clear()
        self.ui.edit_YD.clear()

    def zapisz(self): # Zapis wyników do pliku tekstowego
        options = QFileDialog.Options() # wywołanie okna dialogowego
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "",
                                                  "Text Files (*.txt)", options=options)
        if fileName:
            file = open(fileName + ".txt", "w") # Utworzenie pliku o wybranej nazwie
            XP = float(self.ui.output_XP.text())
            YP = float(self.ui.output_YP.text())
            AzAB = self.ui.output_AzAB.text()
            AzCD = self.ui.output_AzCD.text()
            # Format danych tekstowych
            form1 = "|{:20}|{:20}|{:20}|{:20}|".format("XP", "YP", "AzAB", "AzCD") + "\n"
            form2 = "|{:20.3f}|{:20.3f}|{:20}|{:20}|".format(XP, YP, AzAB, AzCD)
            file.write(form1)
            file.write(form2)
            file.close()

    def zmien_kolor1(self): # Zmiana koloru linii A-B
        color = QColorDialog.getColor() # wywołanie okna dialogowego

        if color.isValid():
            self.col1 = color.name() # Przypisanie nazwy koloru do zmiennej
            # Zmiana koloru przycisku (w celu wizualizacji wybranego przez użytkownika koloru)
            self.ui.kolor1_btn.setStyleSheet("background-color: " + color.name())

    def zmien_kolor2(self): # Zmiana koloru linii C-D
        color = QColorDialog.getColor()

        if color.isValid():
            self.col2 = color.name()
            self.ui.kolor2_btn.setStyleSheet("background-color: " + color.name())

    def zmien_kolor3(self): # Zmiana koloru punktu P
        color = QColorDialog.getColor()

        if color.isValid():
            self.col3 = color.name()
            self.ui.kolor3_btn.setStyleSheet("background-color: " + color.name())

    def rysuj(self): # Wyświetlenie wykresu
        XA = float(self.ui.edit_XA.text()) # pobranie danych wpisowych z interfejsu
        YA = float(self.ui.edit_YA.text())
        XB = float(self.ui.edit_XB.text())
        YB = float(self.ui.edit_YB.text())
        XC = float(self.ui.edit_XC.text())
        YC = float(self.ui.edit_YC.text())
        XD = float(self.ui.edit_XD.text())
        YD = float(self.ui.edit_YD.text())
        self.x1 = [XA, XB] # Zienne pomocnicze
        self.y1 = [YA, YB]
        self.x2 = [XC, XD]
        self.y2 = [YC, YD]


        if self.ui.output_XP.text() != ' brak ': # uwzględnienie przypadku równoległości prostych
            XP = float(self.ui.output_XP.text())
            YP = float(self.ui.output_YP.text())
            self.XP = XP
            self.YP = YP
            lista = [XA, YA, XB, YB, XC, YC, XD, YD, XP, YP]
            self.ui.MplWidget.canvas.ax.clear() # Usunięcie ewentualnych danych z poprzedniego wykresu
            # Wykresy prostych A-B, C-D oraz punktu P
            self.ui.MplWidget.canvas.ax.scatter(self.YP, self.XP, label="P", color = self.col3, marker = self.ui.comboBox.currentText(), zorder=3)
            self.ui.MplWidget.canvas.ax.plot(self.y1, self.x1, label = "linia AB",  marker='o', linewidth=2, color = self.col1, zorder=2)
            self.ui.MplWidget.canvas.ax.plot(self.y2, self.x2, label = "linia CD",  marker='o', linewidth=2, color = self.col2, zorder=1)
            # Przedłużenia prostych
            if self.ui.komentarz_lbl.text() == " na przecięciu odcinka i przedłużenia " or self.ui.komentarz_lbl.text() == " na przecięciu przedłużeń odcinków ":
                yrange = np.arange(min(lista), max(lista))
                if (YB - YA) == 0.0: # Uwzględnienie zera w mianowniku
                    self.ui.MplWidget.canvas.ax.plot(YB*np.ones(len(yrange)), yrange, linestyle='--', color=self.col1)
                else:
                    line_eqn1 = lambda y: ((XB - XA) / (YB - YA)) * (y - YA) + XA
                    self.ui.MplWidget.canvas.ax.plot(yrange, [line_eqn1(y) for y in yrange], linestyle='--', color=self.col1)
                if (YD - YC) == 0.0:
                    self.ui.MplWidget.canvas.ax.plot(YD*np.ones(len(yrange)), yrange, linestyle='--', color=self.col2)
                else:
                    line_eqn2 = lambda y: ((XD - XC) / (YD - YC)) * (y - YC) + XC
                    self.ui.MplWidget.canvas.ax.plot(yrange, [line_eqn2(y) for y in yrange], linestyle='--', color=self.col2)
            self.ui.MplWidget.canvas.ax.legend() # Legenda i wywołanie wykresu
            self.ui.MplWidget.canvas.draw()
        else: # Wykres bez punktu P (gdy proste są równoległe)
            self.ui.MplWidget.canvas.ax.clear()
            self.ui.MplWidget.canvas.ax.plot(self.y1, self.x1, label="linia AB", linewidth=2,  marker='o', color=self.col1)
            self.ui.MplWidget.canvas.ax.plot(self.y2, self.x2, label="linia CD", linewidth=2,  marker='o', color=self.col2)
            self.ui.MplWidget.canvas.ax.legend()
            self.ui.MplWidget.canvas.draw()



if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())