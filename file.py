# Boudouaia Oumayma

import librosa
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import qApp,QMessageBox
from dtaidistance import dtw
from dtw1 import dtw as dtwtest
import numpy as np


class Ui_MainWindow(object):
    path1 = ""
    path2 = ""
    def setupUi(self, MainWindow):
        self.path1 = ""
        self.path2 = ""

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(742, 517)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(67, 0, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 85, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 0, 203))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.LinkVisited, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Link, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.LinkVisited, brush)
        MainWindow.setPalette(palette)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_W = QtWidgets.QLabel(self.centralwidget)
        self.label_W.setGeometry(QtCore.QRect(170, 70, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Palatino Linotype")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_W.setFont(font)
        self.label_W.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_W.setTextFormat(QtCore.Qt.AutoText)
        self.label_W.setScaledContents(False)
        self.label_W.setObjectName("label_W")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 30, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.btnR = QtWidgets.QPushButton(self.centralwidget)
        self.btnR.setGeometry(QtCore.QRect(310, 420, 101, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.btnR.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btnR.setFont(font)
        self.btnR.setObjectName("btnR")
        self.label_R = QtWidgets.QLabel(self.centralwidget)
        self.label_R.setGeometry(QtCore.QRect(50, 180, 631, 221))
        self.label_R.setText("")
        self.label_R.setPixmap(QtGui.QPixmap("../Users/dell/Pictures/qc_stateofplay_onq_header.png"))
        self.label_R.setObjectName("label_R")

        self.dialog = QtWidgets.QFileDialog(self.centralwidget)
        self.dialog.setWindowTitle('Open wav File')
        self.dialog.setNameFilter('wav files (*.wav)')

        self.btnA1 = QtWidgets.QPushButton(self.centralwidget)
        self.btnA1.setGeometry(QtCore.QRect(220, 130, 81, 31))
        self.btnA1.setObjectName("btnA1")
        self.btnA2 = QtWidgets.QPushButton(self.centralwidget)
        self.btnA2.setGeometry(QtCore.QRect(370, 130, 81, 31))
        self.btnA2.setObjectName("btnA2")
        self.label_f1 = QtWidgets.QLabel(self.centralwidget)
        self.label_f1.setGeometry(QtCore.QRect(0, 110, 231, 51))
        self.label_f1.setObjectName("label_f1")
        self.label_f2 = QtWidgets.QLabel(self.centralwidget)
        self.label_f2.setGeometry(QtCore.QRect(490, 120, 221, 41))
        self.label_f2.setObjectName("label_f2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 742, 21))
        self.menubar.setObjectName("menubar")
        self.menuhey = QtWidgets.QMenu(self.menubar)
        self.menuhey.setObjectName("menuhey")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionf = QtWidgets.QAction(MainWindow)
        self.actionf.setObjectName("actionf")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuhey.addAction(self.actionExit)
        self.menubar.addAction(self.menuhey.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_W.setText(_translate("MainWindow", "           Import your two audios File"))
        self.label_2.setText(_translate("MainWindow", "        Welcome to Our GUI"))
        self.btnR.setText(_translate("MainWindow", "Results"))
        self.btnA1.setText(_translate("MainWindow", "AUDIO 1"))
        self.btnA2.setText(_translate("MainWindow", "AUDIO 2"))
        self.label_f1.setText(_translate("MainWindow", ""))
        self.label_f2.setText(_translate("MainWindow", ""))
        self.menuhey.setTitle(_translate("MainWindow", "File"))
        self.actionf.setText(_translate("MainWindow", "Open File"))
        self.actionf.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Esc"))

        # pour contrôler les actions des boutons et menuBar
        self.actionExit.triggered.connect(self.quit_trigger)
        self.btnA1.clicked.connect(self.openFile1)
        self.btnA2.clicked.connect(self.openFile2)
        self.btnR.clicked.connect(self.Compare)



    def quit_trigger(self):
            qApp.quit()


    # pour ouvrir le 1er fichier
    def openFile1(self):
        self.dialog.setDirectory(QtCore.QDir.currentPath())
        self.dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        # test sur le chemin de fichier
        if self.dialog.exec_() == QtWidgets.QDialog.Accepted:
            file_full_path = str(self.dialog.selectedFiles()[0])
            print(("select file"))
        else:
            return None

        self.label_f1.setText(file_full_path)
        self.path1 = file_full_path

        self.label_W.setText("            Import the second audio")

    # pour ouvrir le 2eme fichier
    def openFile2(self):
        self.dialog.setDirectory(QtCore.QDir.currentPath())
        self.dialog.setFileMode(QtWidgets.QFileDialog.ExistingFile)
        if self.dialog.exec_() == QtWidgets.QDialog.Accepted:
            file_full_path = str(self.dialog.selectedFiles()[0])
            print("select file", self.path1)
        else:
            return None
        self.label_f2.setText(file_full_path)
        self.path2 = file_full_path

        self.label_W.setText("                    Click on results")

    # la fonction pour comparer les deux audios
    def Compare(self):
        # test sur les fichier si ils sont bien importer ou non
        if self.path1=="" or self.path2=="":
            self.label_W.setText("Importer les audio SVP !!")
        # pour lire le 1er fichier
        y1, sr1 = librosa.load(self.path1)
        #pour lire le 2eme fichier
        y2, sr2 = librosa.load(self.path2)
        # pour calculer la durée de chaque audio
        n = librosa.get_duration(y1, sr1)
        m = librosa.get_duration(y2, sr2)

        # la durée de chaque audio ne doit pas depasser 5s
        if n > 5 and m > 5:
            mbx= QMessageBox()
            mbx.setWindowTitle("The duration of audios")
            mbx.setText("the duration of your audios is longer than 5s")
            x=mbx.exec_()

        # si la duree est moins que 5s alors on traite les audios
        else:

            print("dirct show of the duration", librosa.get_duration(filename="hello1.wav"))

            # on applique MFCC sur chaque audio pour obtenir la représentation vectorielle
            mfcc1 = librosa.feature.mfcc(y1,sr1)
            mfcc2 = librosa.feature.mfcc(y2, sr2)

            # pour transformer chaque audio en vecteur sans modifier ses données.
            x = np.array(mfcc1).reshape(-1, 1)
            y = np.array(mfcc2).reshape(-1, 1)

            # ici j'ai utiliser dtw de Python pour le test et aussi cette fonction est plus rapide que DTW qui j'ai développée
            d1 = dtw.distance(x, y)

            # la fonction DTW développée

            #d1 = dtwtest(x,y)

            print("dtw.distance (x,y)=", d1)

            # le test de similarité
            if d1 == 0 : #les audios sont similaires
                mbx = QMessageBox()
                mbx.setWindowTitle("Results")
                mbx.setText("distance ="+str(d1)+"\n""Your two audios are  similar")
                x = mbx.exec_()
            elif d1 > 0 and d1 < 1000: # les audios sont presque similaires
                mbx = QMessageBox()
                mbx.setWindowTitle("Results")
                mbx.setText("distance =" + str(d1) + "\n""Your two audios are nearly similar")
                x = mbx.exec_()
            elif d1>=1000: # les audios ne sont pas similaires
                mbx = QMessageBox()
                mbx.setWindowTitle("Results")
                mbx.setText("distance ="+str(d1)+"\n""Your two audios are not similar")
                x = mbx.exec_()

            self.label_W.setText("                       Import your two audios File")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
