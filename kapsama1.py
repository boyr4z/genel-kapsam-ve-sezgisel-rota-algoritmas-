from PyQt5 import QtCore, QtGui, QtWidgets
import time



class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")

        Form.resize(853, 534)
        self.bittimi=0
        self.satir = 0
        self.sutun = 0
        self.btndizi = []
        self.genislik=0
        self.yukseklik = 0
        self.bosluk = 5
        self.korXmin = 58
        self.korXmax = 541
        self.korYmin = 124
        self.korYmax = 484
        self.siliniceksatirlar=[]
        self.Yfark = self.korYmax - self.korYmin
        self.Xfark = self.korXmax - self.korXmin
        self.genelkapsam = []

        self.alfabe = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']
        self.alfabelerid =[]
        self.sutunlarid = [1, 2]
        self.sutunlarid.clear()

        self.onerilensatirlarinbutonlari=[]

        self.onerilenstrkonum = 310
        self.onerilenstrgenislik = 60
        self.yazi = ""

        self.lblstroner=QtWidgets.QLabel(Form)
        self.lblstroner.setGeometry(QtCore.QRect(200, 10, 103, 20))
        self.lblstroner.setObjectName("lblstroner")
        self.lblstroner.setText("Önerilen Satırlar : ")
        self.lblstroner.setStyleSheet("color:purple;font-size:12px;")

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(15, 40, 41, 16))
        self.label_2.setObjectName("label_2")
        self.linesatir = QtWidgets.QLineEdit(Form)
        self.linesatir.setGeometry(QtCore.QRect(50, 10, 61, 20))
        self.linesatir.setObjectName("linesatir")
        self.linesatir.setAlignment(QtCore.Qt.AlignCenter)
        self.linesutun = QtWidgets.QLineEdit(Form)
        self.linesutun.setGeometry(QtCore.QRect(50, 40, 61, 20))
        self.linesutun.setObjectName("linesutun")
        self.linesutun.setAlignment(QtCore.Qt.AlignCenter)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 31, 16))
        self.label.setStyleSheet("")
        self.label.setObjectName("label")

        self.sutunlbltutanliste=[]
        self.satirlbltutanliste=[]


        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(10, 60, 171, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")


        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(180, 0, 3, 61))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(57, 123, 483, 360))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("background:#e9d3cd;")


        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(20, 123, 561, 1))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_3.setStyleSheet("border:1px solid; border-color:red;")

        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(57, 95, 1, 431))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_4.setStyleSheet("border:1px solid; border-color:red;")

        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(20, 482, 561, 1))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_5.setObjectName("line_5")
        self.line_5.setStyleSheet("border:1px solid; border-color:red;")

        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(539, 95, 1, 431))
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_6.setStyleSheet("border:1px solid; border-color:red;")





        # PROGRAMDAKİ BUTTON GRUPLAR
        self.btngrup = QtWidgets.QButtonGroup(Form)
        self.btngrup.setExclusive(True)
        self.btngrup.buttonClicked[int].connect(butontikla)

        self.onerilenstrgrup = QtWidgets.QButtonGroup(Form)
        self.onerilenstrgrup.setExclusive(True)
        self.onerilenstrgrup.buttonClicked[int].connect(onerilenstrdizisineekle)



        # TÜM BUTONLAR
        self.btnbasla = QtWidgets.QPushButton(Form)
        self.btnbasla.setGeometry(625, 10, 160, 30)
        self.btnbasla.setText("Başla")
        self.btnbasla.setStyleSheet("background:#494949;border-radius:5px;color:yellow;font-size:13px;")

        self.btntamam = QtWidgets.QPushButton(Form)
        self.btntamam.setGeometry(QtCore.QRect(120, 10, 51, 20))
        self.btntamam.setObjectName("btnolustur")
        self.btntamam.setText("Tamam")

        self.btnolustur = QtWidgets.QPushButton(Form)
        self.btnolustur.setGeometry(QtCore.QRect(120, 40, 51, 20))
        self.btnolustur.setObjectName("btnolustur")
        self.btnolustur.setText("Oluştur ")
        self.btnolustur.setEnabled(False)


        self.btnonerilensatirsil = QtWidgets.QPushButton(Form)
        self.btnonerilensatirsil.setGeometry(625, 50, 160, 30)
        self.btnonerilensatirsil.setText("Satir Sil")
        self.btnonerilensatirsil.setStyleSheet("background:#494949;border-radius:5px;color:yellow;font-size:13px;")

        self.kapsamara = QtWidgets.QPushButton(Form)
        self.kapsamara.setGeometry(625, 92, 160, 30)
        self.kapsamara.setText("Kapsam Ara")
        self.kapsamara.setStyleSheet("background:#494949;border-radius:5px;color:yellow;font-size:13px;")



        #PROGRAMDAKİ TIKLAMA OLAYLARI

        self.btntamam.clicked.connect(diziayarla)
        self.btnolustur.clicked.connect(butonlarolustur)
        self.btnbasla.clicked.connect(olaybasla)
        self.btnonerilensatirsil.clicked.connect(mutlaksatirsil)
        self.kapsamara.clicked.connect(kapsambul)

        self.yaziyaz = QtWidgets.QTextBrowser(Form)
        self.yaziyaz.setGeometry(590,145,230,300)
        self.yaziyaz.setText("ALOO")
        self.yaziyaz.setStyleSheet("color:Red;border:1px solid;border-color:blue;")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.kapsamara.setStyleSheet("background:#aeaeb5;")
        self.btnonerilensatirsil.setStyleSheet("background:#aeaeb5;")
        self.kapsamara.setEnabled(False)
        self.btnonerilensatirsil.setEnabled(False)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "KAPSAMA"))
        self.label_2.setText(_translate("Form", "Sütun :"))
        self.label.setText(_translate("Form", "Satır :"))


def diziayarla():
    ui.satir = int(ui.linesatir.text())
    ui.sutun = int(ui.linesutun.text())

    ui.alfabe = ui.alfabe[0:ui.satir]

    for i in range(0, ui.sutun):
        ui.sutunlarid.append(i)

    for i in range(0,ui.satir):
        ui.alfabelerid.append(i)

    ui.btntamam.setEnabled(False)
    ui.btnolustur.setEnabled(True)
       # --DİZİ AYARLA SON--#




def butonlarolustur():
    ui.btnolustur.setEnabled(False)
    genislik = (int(ui.Xfark) - int(((ui.sutun + 1) * 5))) / int(ui.sutun)
    yukseklik = int((ui.Yfark - ((ui.satir + 1) * 5)) / ui.satir)
    solkosex = int(ui.korXmin + 5)
    solkosey = int(ui.korYmin + 5)


    butonid=0
    butonsatir = []



    for i in range(0, ui.satir):
        for j in range(0, ui.sutun):
            buton = QtWidgets.QPushButton(Form)
            buton.setGeometry(int(solkosex), int(solkosey), int(genislik), int(yukseklik))
            buton.setStyleSheet("border:1px solid;border-color:blue;border-radius:3px;")
            buton.show()
            ui.btngrup.addButton(buton,butonid)
            butonsatir.append(buton)
            butonid+=1
            solkosex+=ui.bosluk+genislik

        solkosex = int(ui.korXmin + 5)
        solkosey+=yukseklik+ui.bosluk

        ui.btndizi.append(butonsatir[i*ui.sutun:i*ui.sutun+ui.sutun])

    harfvesayiyaz()



def butonlariyinele():
    ui.btnolustur.setEnabled(False)
    genislik = (int(ui.Xfark) - int(((ui.sutun + 1) * 5))) / int(ui.sutun)
    yukseklik = int((ui.Yfark - ((ui.satir + 1) * 5)) / ui.satir)
    solkosex = int(ui.korXmin + 5)
    solkosey = int(ui.korYmin + 5)

    for i in range(0, ui.satir):
            for j in range(0, ui.sutun):
                    ui.btndizi[i][j].setGeometry(int(solkosex), int(solkosey), int(genislik), int(yukseklik))
                    ui.btndizi[i][j].show()
                    solkosex += ui.bosluk + genislik
            solkosex = int(ui.korXmin + 5)
            solkosey += yukseklik + ui.bosluk





def harfvesayiyaz():

    for i in ui.satirlbltutanliste:
        i.close()

    for j in ui.sutunlbltutanliste:
        j.close()

    ui.sutunlbltutanliste.clear()
    ui.satirlbltutanliste.clear()

    genislik = (int(ui.Xfark) - int((ui.sutun + 1) * 5)) / int(ui.sutun)
    yukseklik = int((ui.Yfark - ((ui.satir + 1) * 5)) / ui.satir)

    solkosex = int(ui.korXmin + 5)
    solkosey=int(ui.korYmin+5)

    for i in range(0,ui.sutun):
        lblsutun = QtWidgets.QLabel(Form)
        lblsutun.setText(str(ui.sutunlarid[i]))
        lblsutun.setAlignment(QtCore.Qt.AlignCenter)
        lblsutun.setGeometry(int(solkosex),108,int(genislik),15)
        lblsutun.show()
        ui.sutunlbltutanliste.append(lblsutun)
        solkosex+=genislik+ui.bosluk

    for i in range(0, ui.satir):
        lblsatir = QtWidgets.QLabel(Form)
        lblsatir.setText(str(ui.alfabe[i]))
        lblsatir.setAlignment(QtCore.Qt.AlignVCenter)
        lblsatir.setGeometry(48, int(solkosey), 20,int( yukseklik))
        lblsatir.show()
        ui.satirlbltutanliste.append(lblsatir)
        solkosey += yukseklik + ui.bosluk



def butontikla(id):  # YANLIŞ YAZMIŞ OLABİLİRİM
     for button in ui.btngrup.buttons():
        if button == ui.btngrup.button(id):
            if button.text() == "1":
                button.setText("")
            else:
                button.setText("1")



def dene():
    # BU FONKSİYON BTNSATİR satir ve sutunlarında ki 1 olan şeylerin koordinatını verir
    for i in range(0, ui.satir):
        for j in range(0, ui.sutun):
            if ui.btndizi[ui.alfabelerid[i]][ui.sutunlarid[j]].text() == "1":
                print(i, j, "\n")



def stnagirlikbul():

    stnagirlik = []


    for i in range(0, ui.sutun):
        stnagirlik.append(int(0))

    for i in range(0, ui.satir):
        for j in range(0, ui.sutun):
            if ui.btndizi[i][j].text() == "1":
                stnagirlik[j] += 1

    return stnagirlik
    # --STNAGİRLİKBUL BİTTİ-- #




def mutlakbul():
    agirliklar = stnagirlikbul()

    mutlaksutunlarindistut = []
    mutlaksatirlarindistut = []


    for i in range(len(agirliklar)):
        if agirliklar[i] == 1:
            mutlaksutunlarindistut.append(int(i))

    for i in range(0, ui.satir):
        for j in range(0, ui.sutun):
            if j in mutlaksutunlarindistut and ui.btndizi[i][j].text() == "1" and i not in mutlaksatirlarindistut:
                mutlaksatirlarindistut.append(int(i))

    return mutlaksatirlarindistut


def olaybasla():

    b=stnagirlikbul()
    for i in range(0,len(b)):
        if b[i]==0:
            ui.yaziyaz.append(str("Kapsam Yoktur ..."))


    butonlariyinele()
    harfvesayiyaz()

    ui.btnbasla.setText("Bi sonraki Adım")
    # PROGRAM BİTİRME

    a = stnagirlikbul()
    for i in range(0,ui.satir):
        for j in range(0,ui.sutun):
            ui.btndizi[i][j].setEnabled(False)

    a=mutlakbul()
    if ui.satir==0 and ui.sutun==0:
        ui.yaziyaz.append(str("Genel Kapsam Bulunmuştur.."))
        ui.yaziyaz.append(str("Genel Kapsam \n--------------\n"))
        ui.yaziyaz.append(str(ui.genelkapsam))

    if len(a)!=0:
        onerilensatirdiz(a)


    else:
        ui.yaziyaz.append("Sezgisel deneniyor ...")
        b=sezgisel()
        onerilensatirdiz(b)




def sezgisel():

    a=stnagirlikbul()                                   # TÜM SÜTUNLARIN AĞIRLIKLARI BULUNDU
    b=min(a)                                            # MİNİMUM AĞIRLIK DEĞERİ BULUNDU

    minagirliklisatirindis=[]
    hesaplanacaksatirlar=[]
    satiragirliklar=[]
    minsutunlarid=[]

    for i in range(0,len(a)):                           # MİNİMUM AĞIRLIĞA SAHİP OLAN SÜTUNLARIN İD Sİ BULUNDU
        if a[i]==b:
            minsutunlarid.append(i)


    for i in range(0,ui.satir):                                                 # ağırlığı hesaplanması gereken satırların indisleri tutuldu
        for j in range(0,ui.sutun):
            if j in minsutunlarid and ui.btndizi[i][j].text()=="1" and i not in hesaplanacaksatirlar:
                hesaplanacaksatirlar.append(i)



    toplam=0
    for i in range(0,ui.satir):
        if i in hesaplanacaksatirlar:
            for j in range(0,ui.sutun):
                toplam +=1/a[j]

            satiragirliklar.append(toplam)
        toplam=0

    minagirlik = min(satiragirliklar)

    for i in range(0,len(hesaplanacaksatirlar)):
        if satiragirliklar[i]==minagirlik:
            minagirliklisatirindis.append(i)


    return minagirliklisatirindis


def onerilenstrdizisineekle(x):
    ui.btnonerilensatirsil.setEnabled(True)
    ui.btnonerilensatirsil.setStyleSheet("background:#494949;border-radius:5px;color:yellow;font-size:13px;")

    if x not in ui.siliniceksatirlar:
        ui.siliniceksatirlar.append(x)



def onerilensatirdiz(dizi):

    baslax=310
    genislik=60

    for i in range(0,len(dizi)):
        buton = QtWidgets.QPushButton(Form)
        buton.setGeometry(int(baslax),11,int(genislik),20)
        buton.setText(str(ui.alfabe[dizi[i]]))
        buton.setStyleSheet("background:#494949;border-radius:5px;color:yellow;font-size:13px;")
        ui.onerilenstrgrup.addButton(buton,dizi[i])
        buton.show()
        baslax+=70





def butonlarisil():
    for i in range(0,ui.satir):
        for j in range(0,ui.sutun):
            ui.btndizi[i][j].close()





def bossatirvarmi():

    bossatirlar=[]
    t=0
    for i in range(ui.satir-1,-1,-1):
        for j in range(0,ui.sutun):
            if ui.btndizi[i][j].text()=="1":
                t+=1

        if t==0:
            bossatirlar.append(i)
        t=0
    return bossatirlar



def kapsambul():

    ui.kapsamara.setEnabled(False)
    ui.kapsamara.setStyleSheet("background:#494949;border-radius:5px;color:yellow;font-size:13px;")

    butonlariyinele()
    harfvesayiyaz()
    satirjleri=[]
    kapsananlar=[]
    kapsayanlar=[]

    for i in range(0,ui.satir):
        satirjleri.append("")



    for i in range(0,ui.satir):
        for j in range(0,ui.sutun):
            if ui.btndizi[i][j].text()=="1":
                satirjleri[i]+=str(j)

    t=0
    birak=0
    for denedigimizsatir in range(0,ui.satir):                                     # şu an ele aldığımız satir
        birak=0
        for karsilastirdigimizsatir in range(0,ui.satir):                                                # ele aldığımız satırla karşılaştırılacak satir

            if denedigimizsatir != karsilastirdigimizsatir:                                              # iki satır birbirinden farklı olsun
                for suankiindis in range(0,len(satirjleri[denedigimizsatir])):               # ele aldığımız satırın elemanları
                     if satirjleri[denedigimizsatir][suankiindis] in satirjleri[karsilastirdigimizsatir]:          # eğer ele aldığımız satırın elemanı diğer satır da varsa
                         t+=1
                if t==len(satirjleri[denedigimizsatir]) :

                    kapsananlar.append(denedigimizsatir)
                    kapsayanlar.append(karsilastirdigimizsatir)
                    birak+=1
            t=0
            if birak==1:
                break

    if len(kapsananlar)==0:
        ui.yaziyaz.append("Maalesef kapsam bulunamadı ...")
    else:
        onerilensatirdiz(kapsananlar)










def mutlaksatirsil():
    ui.btnonerilensatirsil.setEnabled(False)
    ui.btnonerilensatirsil.setStyleSheet("background:#aeaeb5;border-radius:5px;color:yellow;font-size:13px;")

    for i in ui.onerilenstrgrup.buttons():
        i.close()

    for buton in ui.btngrup.buttons():
        buton.close()


    a = mutlakbul()

    if len(a)!=0:

        ui.kapsamara.setEnabled(True)
        ui.kapsamara.setStyleSheet("background:#494949;border-radius:5px;color:yellow;font-size:13px;")

        strtut="| "
        for i in range(0,len(a)):
            strtut+=str(ui.alfabe[a[i]])
            strtut+=","

        strtut+=" | "
        ui.yaziyaz.append(strtut + "Mutlak Satırları Silindi.")


        a = satirsutunkesisme(ui.siliniceksatirlar)
        sutunsil(a)




        for i in range(len(ui.siliniceksatirlar)-1, -1, -1):
            del ui.btndizi[int(ui.siliniceksatirlar[i])]

        for i in range(len(ui.siliniceksatirlar) - 1, -1, -1):
            ui.genelkapsam += str(ui.alfabe[ui.siliniceksatirlar[i]])
            del ui.alfabe[ui.siliniceksatirlar[i]]
            del ui.alfabelerid[ui.siliniceksatirlar[i]]

        ui.satir -= len(ui.siliniceksatirlar)



    else:
        satirsil(ui.siliniceksatirlar)

    for i in range(0,len(ui.siliniceksatirlar)):
        for buton in ui.onerilenstrgrup.buttons():
            if buton == ui.onerilenstrgrup.button(ui.siliniceksatirlar[i]):
                buton.close()
                ui.onerilenstrgrup.removeButton(buton)

    ui.siliniceksatirlar.clear()

    a=bossatirvarmi()
    if len(a)!=0:
        for i in range(0,len(a)):
            print(ui.alfabe[a[i]])

        ui.yaziyaz.append("Boş Satır Bulundu ve siliniyor..")
        satirsil(a)

    if ui.satir ==0:
        ui.yaziyaz.append("Genel Kapsam Bulunmuştur")
        strtut="[ "

        for i in range(0,len(ui.genelkapsam)):
            strtut+=str(ui.genelkapsam[i])
            strtut+=" "
        strtut+=" ]"
        ui.yaziyaz.append(strtut )
        ui.btnbasla.setEnabled(False)
        ui.btnonerilensatirsil.setEnabled(False)
        ui.kapsamara.setEnabled(False)
        ui.btnbasla.setStyleSheet("background:#aeaeb5;")
        ui.btnonerilensatirsil.setStyleSheet("background:#aeaeb5;")
        ui.kapsamara.setStyleSheet("background:#aeaeb5;")


    if ui.satir!=0:
        sonkezbutondiz()

def sonkezbutondiz():
    harfvesayiyaz()
    butonlariyinele()
def satirsutunkesisme(dizi):
    kesisensutunindis=[]

    for i in range(0,ui.satir):
        if i in dizi:
            for j in range(0,ui.sutun):
                if ui.btndizi[i][j].text()=="1" and j not in kesisensutunindis:
                    kesisensutunindis.append(j)

    kesisensutunindis.sort()
    return kesisensutunindis


def sutunsil(dizi):
    strtut="| "
    for i in range(0,len(dizi)):
        strtut+=str(ui.sutunlarid[dizi[i]])
        strtut+=","

    strtut+=" | "

    ui.yaziyaz.append(strtut + " Sütunları Silindi")
    for i in range(0,ui.satir):
        for j in range(ui.sutun-1,-1,-1):
            if j in dizi:
                del ui.btndizi[i][j]


    for i in range(len(dizi)-1,-1,-1):
        del ui.sutunlarid[dizi[i]]

    ui.sutun-=len(dizi)


def satirsil(dizi):
    strtut="| "
    for i in range(0,len(dizi)):
        strtut+=ui.alfabe[dizi[i]]
        strtut+=","

    strtut+=" |"


    ui.yaziyaz.append(strtut + " satırları silindi ...")

    for i in range(len(dizi)-1,-1,-1):
        del ui.btndizi[dizi[i]]
        del ui.alfabe[dizi[i]]
        del ui.alfabelerid[dizi[i]]

    ui.satir-=len(dizi)
    butonlariyinele()
    harfvesayiyaz()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
