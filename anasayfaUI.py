# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'anasayfa.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1227, 797)
        MainWindow.setStyleSheet("/*\n"
"Neon Style Sheet for QT Applications (QpushButton)\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 24/10/2020, 15:42.\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/NeonButtons.qss\n"
"*/\n"
"QPushButton{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"    background-color: #100E19;\n"
"}\n"
"QPushButton::default{\n"
"    border-style: solid;\n"
"    border-color: #050a0e;\n"
"    border-width: 1px;\n"
"    border-radius: 5px;\n"
"    color: #FFFFFF;\n"
"    padding: 2px;\n"
"    background-color: #151a1e;\n"
"}\n"
"QPushButton:hover{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #C0DB50, stop:0.4 #C0DB50, stop:0.5 #100E19, stop:1 #100E19);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #C0DB50, stop:1 #C0DB50);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #C0DB50, stop:0.3 #C0DB50, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-width: 2px;\n"
"    border-radius: 1px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"}\n"
"QPushButton:pressed{\n"
"    border-style: solid;\n"
"    border-top-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #d33af1, stop:0.4 #d33af1, stop:0.5 #100E19, stop:1 #100E19);\n"
"    border-bottom-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:1, stop:0 #100E19, stop:0.5 #100E19, stop:0.6 #d33af1, stop:1 #d33af1);\n"
"    border-left-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-right-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #d33af1, stop:0.3 #d33af1, stop:0.7 #100E19, stop:1 #100E19);\n"
"    border-width: 2px;\n"
"    border-radius: 1px;\n"
"    color: #d3dae3;\n"
"    padding: 2px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 741, 321))
        self.groupBox.setObjectName("groupBox")
        self.saat = QtWidgets.QLabel(self.groupBox)
        self.saat.setGeometry(QtCore.QRect(360, 260, 26, 16))
        self.saat.setObjectName("saat")
        self.odemetipbox = QtWidgets.QComboBox(self.groupBox)
        self.odemetipbox.setGeometry(QtCore.QRect(110, 230, 131, 20))
        self.odemetipbox.setObjectName("odemetipbox")
        self.odemetipbox.addItem("")
        self.odemetipbox.addItem("")
        self.saatbox = QtWidgets.QTimeEdit(self.groupBox)
        self.saatbox.setGeometry(QtCore.QRect(410, 260, 81, 22))
        self.saatbox.setObjectName("saatbox")
        self.yikamatipbox = QtWidgets.QComboBox(self.groupBox)
        self.yikamatipbox.setGeometry(QtCore.QRect(110, 170, 131, 20))
        self.yikamatipbox.setObjectName("yikamatipbox")
        self.yikamatipbox.addItem("")
        self.yikamatipbox.addItem("")
        self.yikamatipbox.addItem("")
        self.tarih = QtWidgets.QLabel(self.groupBox)
        self.tarih.setGeometry(QtCore.QRect(361, 41, 31, 16))
        self.tarih.setObjectName("tarih")
        self.adbox = QtWidgets.QLineEdit(self.groupBox)
        self.adbox.setGeometry(QtCore.QRect(110, 30, 133, 20))
        self.adbox.setObjectName("adbox")
        self.aractipbox = QtWidgets.QComboBox(self.groupBox)
        self.aractipbox.setGeometry(QtCore.QRect(110, 120, 131, 20))
        self.aractipbox.setObjectName("aractipbox")
        self.aractipbox.addItem("")
        self.aractipbox.addItem("")
        self.aractipbox.addItem("")
        self.plakabox = QtWidgets.QLineEdit(self.groupBox)
        self.plakabox.setGeometry(QtCore.QRect(110, 80, 133, 20))
        self.plakabox.setObjectName("plakabox")
        self.takvim = QtWidgets.QCalendarWidget(self.groupBox)
        self.takvim.setGeometry(QtCore.QRect(410, 40, 312, 183))
        self.takvim.setObjectName("takvim")
        self.yikamatipi = QtWidgets.QLabel(self.groupBox)
        self.yikamatipi.setGeometry(QtCore.QRect(31, 172, 61, 16))
        self.yikamatipi.setObjectName("yikamatipi")
        self.aractipi = QtWidgets.QLabel(self.groupBox)
        self.aractipi.setGeometry(QtCore.QRect(31, 125, 51, 16))
        self.aractipi.setObjectName("aractipi")
        self.plaka = QtWidgets.QLabel(self.groupBox)
        self.plaka.setGeometry(QtCore.QRect(31, 78, 31, 16))
        self.plaka.setObjectName("plaka")
        self.adsoyad = QtWidgets.QLabel(self.groupBox)
        self.adsoyad.setGeometry(QtCore.QRect(31, 31, 51, 16))
        self.adsoyad.setObjectName("adsoyad")
        self.odemetipi = QtWidgets.QLabel(self.groupBox)
        self.odemetipi.setGeometry(QtCore.QRect(31, 219, 58, 16))
        self.odemetipi.setObjectName("odemetipi")
        self.bilgilerliste = QtWidgets.QTableWidget(self.centralwidget)
        self.bilgilerliste.setGeometry(QtCore.QRect(40, 360, 751, 321))
        self.bilgilerliste.setRowCount(100)
        self.bilgilerliste.setColumnCount(7)
        self.bilgilerliste.setObjectName("bilgilerliste")
        item = QtWidgets.QTableWidgetItem()
        self.bilgilerliste.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bilgilerliste.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.bilgilerliste.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.bilgilerliste.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.bilgilerliste.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.bilgilerliste.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.bilgilerliste.setHorizontalHeaderItem(6, item)
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(900, 70, 191, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.kayitekle = QtWidgets.QPushButton(self.layoutWidget)
        self.kayitekle.setObjectName("kayitekle")
        self.verticalLayout.addWidget(self.kayitekle)
        self.kayitsil = QtWidgets.QPushButton(self.layoutWidget)
        self.kayitsil.setObjectName("kayitsil")
        self.verticalLayout.addWidget(self.kayitsil)
        self.kayitara = QtWidgets.QPushButton(self.layoutWidget)
        self.kayitara.setObjectName("kayitara")
        self.verticalLayout.addWidget(self.kayitara)
        self.kayitlarilistele = QtWidgets.QPushButton(self.layoutWidget)
        self.kayitlarilistele.setObjectName("kayitlarilistele")
        self.verticalLayout.addWidget(self.kayitlarilistele)
        self.cikis = QtWidgets.QPushButton(self.layoutWidget)
        self.cikis.setObjectName("cikis")
        self.verticalLayout.addWidget(self.cikis)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1227, 21))
        self.menubar.setObjectName("menubar")
        self.menuYard_m = QtWidgets.QMenu(self.menubar)
        self.menuYard_m.setObjectName("menuYard_m")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.hakkinda = QtWidgets.QAction(MainWindow)
        self.hakkinda.setObjectName("hakkinda")
        self.iletisim = QtWidgets.QAction(MainWindow)
        self.iletisim.setObjectName("iletisim")
        self.menuYard_m.addAction(self.hakkinda)
        self.menuYard_m.addAction(self.iletisim)
        self.menubar.addAction(self.menuYard_m.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Bilgiler"))
        self.saat.setText(_translate("MainWindow", "SAAT"))
        self.odemetipbox.setItemText(0, _translate("MainWindow", "Nakit"))
        self.odemetipbox.setItemText(1, _translate("MainWindow", "Kart"))
        self.yikamatipbox.setItemText(0, _translate("MainWindow", "İç-Dış Yıkama"))
        self.yikamatipbox.setItemText(1, _translate("MainWindow", "İç-Dış Yıkama + Cila"))
        self.yikamatipbox.setItemText(2, _translate("MainWindow", "İç-Dış Yıkama + Cila + Pasta Polish"))
        self.tarih.setText(_translate("MainWindow", "TARİH"))
        self.aractipbox.setItemText(0, _translate("MainWindow", "Binek"))
        self.aractipbox.setItemText(1, _translate("MainWindow", "Ticari"))
        self.aractipbox.setItemText(2, _translate("MainWindow", "Kamyonet"))
        self.yikamatipi.setText(_translate("MainWindow", "YIKAMA TİPİ"))
        self.aractipi.setText(_translate("MainWindow", "ARAÇ TİPİ"))
        self.plaka.setText(_translate("MainWindow", "PLAKA"))
        self.adsoyad.setText(_translate("MainWindow", "AD SOYAD"))
        self.odemetipi.setText(_translate("MainWindow", "ÖDEME TİPİ"))
        item = self.bilgilerliste.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "AD SOYAD"))
        item = self.bilgilerliste.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "PLAKA"))
        item = self.bilgilerliste.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "ARAÇ TİPİ"))
        item = self.bilgilerliste.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "YIKAMA TİPİ"))
        item = self.bilgilerliste.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "ÖDEME TİPİ"))
        item = self.bilgilerliste.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "TARİH"))
        item = self.bilgilerliste.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "SAAT"))
        self.kayitekle.setText(_translate("MainWindow", "KAYIT EKLE"))
        self.kayitsil.setText(_translate("MainWindow", "KAYIT SİL"))
        self.kayitara.setText(_translate("MainWindow", "KAYIT ARA"))
        self.kayitlarilistele.setText(_translate("MainWindow", "KAYITLARI LİSTELE"))
        self.cikis.setText(_translate("MainWindow", "ÇIKIŞ"))
        self.menuYard_m.setTitle(_translate("MainWindow", "Yardım"))
        self.hakkinda.setText(_translate("MainWindow", "Hakkında"))
        self.iletisim.setText(_translate("MainWindow", "İletişim"))

