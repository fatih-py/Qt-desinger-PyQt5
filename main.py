#kütüphane

import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from anasayfaUI import *

#uygulama

Uygulama = QApplication(sys.argv)
ana_pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(ana_pencere)
ana_pencere.show()


#veri tabanı oluşturma

import sqlite3
global curs
global conn
conn = sqlite3.connect('veritabani.db')
curs = conn.cursor()
sorguarac = ("CREATE TABLE IF NOT EXISTS bilgiler(              \
             ADSOYAD TEXT NOT NULL ,                            \
             PLAKA TEXT NOT NULL ,                              \
             ARACTİPİ TEXT NOT NULL,                            \
             YIKAMATİPİ TEXT NOT NULL,                          \
             ODEMETİPİ TEXT NOT NULL,                           \
             TARIH TEXT NOT NULL)")
             
curs.execute(sorguarac)
conn.commit()

#kaydet

def EKLE():
    lneadsoyad = ui.adbox.text()
    lneplaka = ui.plakabox.text()
    cbmarac = ui.aractipbox.currentText()
    lneyıkama = ui.yikamatipbox.currentText()
    lneodeme = ui.odemetipbox.currentText()
    cwtakvim = ui.takvim.selectedDate().toString(QtCore.Qt.ISODate)

        
    curs.execute("INSERT INTO bilgiler   \
                       (ADSOYAD,PLAKA,ARACTİPİ,YIKAMATİPİ,ODEMETİPİ,TARIH)  \
                        VALUES (?,?,?,?,?,?)",  \
                        (lneadsoyad,lneplaka,cbmarac,lneyıkama,lneodeme,cwtakvim))
    conn.commit()
    LISTELE()
#LİSTELE       (ıd sayısını geri alamıyor)
def LISTELE():
    ui.bilgilerliste.clear()
    ui.bilgilerliste.setHorizontalHeaderLabels(('Id','Ad Soyad','Plaka','Araç Tipi','Yıkama Tipi','Ödeme Tipi','Tarih'))
    ui.bilgilerliste.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    curs.execute("SELECT* FROM bilgiler")
    
    for satirIndex,satirVeri in enumerate(curs):
        for sutunIndex,sutunVeri in enumerate(satirVeri):
            ui.bilgilerliste.setItem(satirIndex, sutunIndex, QTableWidgetItem(str(sutunVeri)))

    ui.adbox.clear()            
    ui.plakabox.clear()
    ui.odemetipbox.setCurrentIndex(-1)
    ui.yikamatipbox.setCurrentIndex(-1)
    ui.aractipbox.setCurrentIndex(-1)
    
LISTELE()

#çıkış(Kapatma sorunu var)

def CIKIS():
    cevap = QMessageBox.question(ana_pencere,"ÇIKIŞ","Programdan çıkmak istediğinize emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
        
    if cevap == QMessageBox.Yes:
       conn.close()
       sys.exit(Uygulama.exec_())
        
    else:
       ana_pencere.show()
        
            
#sil

def SIL():
    cevap=QMessageBox.question(ana_pencere,"KAYIT SİL","Kaydı silmek istediğinize emin misiniz?",\
                         QMessageBox.Yes | QMessageBox.No)
    if cevap==QMessageBox.Yes:
        secili=ui.bilgilerliste.selectedItems()
        silinecek=secili[2].text()
        try:
            curs.execute("DELETE FROM bilgiler WHERE PLAKA='%s'" %(silinecek))
            conn.commit()
            LISTELE()
            ui.statusbar.showMessage("KAYIT SİLME İŞLEMİ BAŞARIYLA GERÇEKLEŞTİ...",10000)
        except Exception as Hata:
            ui.statusbar.showMessage("Şöyle bir hata ile karşılaşıldı:"+str(Hata))
    else:
        ui.statusbar.showMessage("Silme işlemi iptal edildi...",10000)

#arama

def ARA():
    aranan1=ui.plakabox.text()
    aranan2=ui.takvim.selectedDate().toString(QtCore.Qt.ISODate)
    curs.execute("SELECT * FROM bilgiler WHERE PLAKA=? OR TARIH=? ", (aranan1,aranan2,))
    conn.commit()
    ui.bilgilerliste.clear()
    for satirIndeks, satirVeri in enumerate(curs):
        for sutunIndeks, sutunVeri in enumerate (satirVeri):
            ui.bilgilerliste.setItem(satirIndeks,sutunIndeks,QTableWidgetItem(str(sutunVeri)))

#İNFO

def HAKKINDA():
    penHakkinda.show()

#sinyal gönder
ui.kayitekle.clicked.connect(EKLE)
ui.kayitlarilistele.clicked.connect(LISTELE)
ui.cikis.clicked.connect(CIKIS)
ui.kayitsil.clicked.connect(SIL)
ui.kayitara.clicked.connect(ARA)


sys.exit(Uygulama.exec_())


















