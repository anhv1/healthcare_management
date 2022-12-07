from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

from PyQt5.QtWidgets import QMessageBox
class Generate_Bill( object ):
    # Function to Save Bills when the Save button is clicked
    def SaveBill(self):
        # Getting all the info from user when the user enters info into fields
        Name = self.Name.text()
        BillNum = self.BillNum.text()
        RoomRent = self.RoomRent.text()
        ICU = self.ICUCharges.text()
        Medicine = self.Medicine.text()
        Invest = self.InvestCharg.text()
        MisCharges = self.MisCharges.text()
        Package = self.PackageCharg.text()
        Recieved = self.ReceivedBy.text()
        Date = self.Date.text()
        DateAd = self.DateAd.text()
        DateDis = self.DateDis.text()
        RMO = self.RMOService.text()
        Consultant = self.ConsVisit.text()
        Surgery = self.SurgeryC.text()
        Imp = self.Imp.text()
        Other = self.AnyOther.text()
        # changing the data type to float and sum all of them
        sumTotal = float(RoomRent) + float(ICU)+float(Medicine)+float(Invest)+float(MisCharges)+float(Package)+float(RMO)+float(Consultant)+float(Surgery)+float(Imp)+float(Other)
        self.BilledAmount.setText(str(sumTotal)) # Changing sumTotal to string
        Total = self.BilledAmount.text() # Setting Total to BilledAmount in order to save it in table without calculating every one of them
        db = sqlite3.connect("project.db")
        db.execute("create table if not exists Bills (BillNum int NOT NULL, Name text NOT NULL, DateAd text NOT NULL,"
                   "DateDis text NOT NULL,RoomRent real, ICU real, Medicine real, Invest real, MisCharges real, Package real, "
                   "RMOServices real, ConsVisits real, Surgery real, Imp real, Other real, Total real, Received text NOT NULL, Date text NOT NULL)")
        db.execute("insert into Bills values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                   (BillNum, Name, DateAd, DateDis,RoomRent, ICU, Medicine, Invest, MisCharges, Package, RMO, Consultant, Surgery, Imp, Other, Total, Recieved, Date) )
        db.commit()
        message1 = QMessageBox() # View a message if it is saved
        message1.setWindowTitle( "Successfull" )
        message1.setInformativeText( "You have successfully Generated a bill by the name of :  "+Name+" with Total amount of "+ self.BilledAmount.text())
        message1.exec_()
        # Clearing all the fields
        self.Name.clear()
        self.BillNum.clear()
        self.RoomRent.clear()
        self.ICUCharges.clear()
        self.Medicine.clear()
        self.InvestCharg.clear()
        self.MisCharges.clear()
        self.PackageCharg.clear()
        self.ReceivedBy.clear()
        self.RMOService.clear()
        self.ConsVisit.clear()
        self.SurgeryC.clear()
        self.Imp.clear()
        self.AnyOther.clear()
        self.BilledAmount.clear()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindowAdmin")
        MainWindow.resize(617, 565)
        MainWindow.setStyleSheet("@import \"compass/css3\";\n"
"\n"
"$body-bg: #c1bdba;\n"
"$form-bg: #13232f;\n"
"$white: #ffffff;\n"
"\n"
"$main: #1ab188;\n"
"$main-light: lighten($main,5%);\n"
"$main-dark: darken($main,5%);\n"
"\n"
"$gray-light: #a0b3b0;\n"
"$gray: #ddd;\n"
"\n"
"$thin: 300;\n"
"$normal: 400;\n"
"$bold: 600;\n"
"$br: 4px;\n"
"\n"
"*, *:before, *:after {\n"
"  box-sizing: border-box;\n"
"}\n"
"\n"
"html {\n"
"    overflow-y: scroll; \n"
"}\n"
"\n"
"body {\n"
"  background:$body-bg;\n"
"  font-family: \'Titillium Web\', sans-serif;\n"
"}\n"
"\n"
"a {\n"
"  text-decoration:none;\n"
"  color:$main;\n"
"  transition:.5s ease;\n"
"  &:hover {\n"
"    color:$main-dark;\n"
"  }\n"
"}\n"
"\n"
".form {\n"
"  background:rgba($form-bg,.9);\n"
"  padding: 40px;\n"
"  max-width:600px;\n"
"  margin:40px auto;\n"
"  border-radius:$br;\n"
"  box-shadow:0 4px 10px 4px rgba($form-bg,.3);\n"
"}\n"
"\n"
".tab-group {\n"
"  list-style:none;\n"
"  padding:0;\n"
"  margin:0 0 40px 0;\n"
"  &:after {\n"
"    content: \"\";\n"
"    display: table;\n"
"    clear: both;\n"
"  }\n"
"  li a {\n"
"    display:block;\n"
"    text-decoration:none;\n"
"    padding:15px;\n"
"    background:rgba($gray-light,.25);\n"
"    color:$gray-light;\n"
"    font-size:20px;\n"
"    float:left;\n"
"    width:50%;\n"
"    text-align:center;\n"
"    cursor:pointer;\n"
"    transition:.5s ease;\n"
"    &:hover {\n"
"      background:$main-dark;\n"
"      color:$white;\n"
"    }\n"
"  }\n"
"  .active a {\n"
"    background:$main;\n"
"    color:$white;\n"
"  }\n"
"}\n"
"\n"
".tab-content > div:last-child {\n"
"  display:none;\n"
"}\n"
"\n"
"\n"
"h1 {\n"
"  text-align:center;\n"
"  color:$white;\n"
"  font-weight:$thin;\n"
"  margin:0 0 40px;\n"
"}\n"
"\n"
"label {\n"
"  position:absolute;\n"
"  transform:translateY(6px);\n"
"  left:13px;\n"
"  color:rgba($white,.5);\n"
"  transition:all 0.25s ease;\n"
"  -webkit-backface-visibility: hidden;\n"
"  pointer-events: none;\n"
"  font-size:22px;\n"
"  .req {\n"
"    margin:2px;\n"
"    color:$main;\n"
"  }\n"
"}\n"
"\n"
"label.active {\n"
"  transform:translateY(50px);\n"
"  left:2px;\n"
"  font-size:14px;\n"
"  .req {\n"
"    opacity:0;\n"
"  }\n"
"}\n"
"\n"
"label.highlight {\n"
"    color:$white;\n"
"}\n"
"\n"
"input, textarea {\n"
"  font-size:22px;\n"
"  display:block;\n"
"  width:100%;\n"
"  height:100%;\n"
"  padding:5px 10px;\n"
"  background:none;\n"
"  background-image:none;\n"
"  border:1px solid $gray-light;\n"
"  color:$white;\n"
"  border-radius:0;\n"
"  transition:border-color .25s ease, box-shadow .25s ease;\n"
"  &:focus {\n"
"        outline:0;\n"
"        border-color:$main;\n"
"  }\n"
"}\n"
"\n"
"textarea {\n"
"  border:2px solid $gray-light;\n"
"  resize: vertical;\n"
"}\n"
"\n"
".field-wrap {\n"
"  position:relative;\n"
"  margin-bottom:40px;\n"
"}\n"
"\n"
".top-row {\n"
"  &:after {\n"
"    content: \"\";\n"
"    display: table;\n"
"    clear: both;\n"
"  }\n"
"\n"
"  > div {\n"
"    float:left;\n"
"    width:48%;\n"
"    margin-right:4%;\n"
"    &:last-child { \n"
"      margin:0;\n"
"    }\n"
"  }\n"
"}\n"
"\n"
".button {\n"
"  border:0;\n"
"  outline:none;\n"
"  border-radius:0;\n"
"  padding:15px 0;\n"
"  font-size:2rem;\n"
"  font-weight:$bold;\n"
"  text-transform:uppercase;\n"
"  letter-spacing:.1em;\n"
"  background:$main;\n"
"  color:$white;\n"
"  transition:all.5s ease;\n"
"  -webkit-appearance: none;\n"
"  &:hover, &:focus {\n"
"    background:$main-dark;\n"
"  }\n"
"}\n"
"\n"
".button-block {\n"
"  display:block;\n"
"  width:100%;\n"
"}\n"
"\n"
".forgot {\n"
"  margin-top:-20px;\n"
"  text-align:right;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 271, 61))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(207, 21, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 92, 271, 61))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(53, 97, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_1")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 231, 271, 61))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_6")
        self.Name = QtWidgets.QLineEdit(self.centralwidget)
        self.Name.setGeometry(QtCore.QRect(142, 98, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.Name.setFont(font)
        self.Name.setStyleSheet("")
        self.Name.setObjectName("Name")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 300, 271, 61))
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_1")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(310, 369, 271, 61))
        self.label_14.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.SaveButton = QtWidgets.QPushButton(self.centralwidget)
        self.SaveButton.setGeometry(QtCore.QRect(410, 383, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SaveButton.setFont(font)
        self.SaveButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.SaveButton.setObjectName("SaveButton")

        self.SaveButton.clicked.connect(self.SaveBill)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 91, 271, 61))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(332, 99, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.DateAd = QtWidgets.QDateEdit(self.centralwidget)
        self.DateAd.setGeometry(QtCore.QRect(449, 101, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DateAd.setFont(font)
        self.DateAd.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.DateAd.setObjectName("DateAd")
        self.RoomRent = QtWidgets.QLineEdit(self.centralwidget)
        self.RoomRent.setGeometry(QtCore.QRect(144, 167, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.RoomRent.setFont(font)
        self.RoomRent.setStyleSheet("")
        self.RoomRent.setObjectName("RoomRent")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(32, 160, 271, 61))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(40, 166, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_7")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(310, 160, 271, 61))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(308, 230, 271, 61))
        self.label_19.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(309, 300, 271, 61))
        self.label_23.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 621, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../PycharmProjects/b/bg.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(333, 124, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.DateDis = QtWidgets.QDateEdit(self.centralwidget)
        self.DateDis.setGeometry(QtCore.QRect(449, 125, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.DateDis.setFont(font)
        self.DateDis.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.DateDis.setObjectName("DateDis")
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(62, 121, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.BillNum = QtWidgets.QLineEdit(self.centralwidget)
        self.BillNum.setGeometry(QtCore.QRect(142, 123, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.BillNum.setFont(font)
        self.BillNum.setStyleSheet("")
        self.BillNum.setObjectName("BillNum")
        self.ICUCharges = QtWidgets.QLineEdit(self.centralwidget)
        self.ICUCharges.setGeometry(QtCore.QRect(144, 193, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.ICUCharges.setFont(font)
        self.ICUCharges.setStyleSheet("")
        self.ICUCharges.setObjectName("ICUCharges")
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(63, 190, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(336, 167, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(320, 190, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_28.setFont(font)
        self.label_28.setObjectName("label_28")
        self.ConsVisit = QtWidgets.QLineEdit(self.centralwidget)
        self.ConsVisit.setGeometry(QtCore.QRect(423, 192, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.ConsVisit.setFont(font)
        self.ConsVisit.setStyleSheet("")
        self.ConsVisit.setObjectName("ConsVisit")
        self.RMOService = QtWidgets.QLineEdit(self.centralwidget)
        self.RMOService.setGeometry(QtCore.QRect(423, 166, 141, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.RMOService.setFont(font)
        self.RMOService.setStyleSheet("")
        self.RMOService.setObjectName("RMOService")
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(90, 239, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(39, 263, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_30.setFont(font)
        self.label_30.setObjectName("label_30")
        self.InvestCharg = QtWidgets.QLineEdit(self.centralwidget)
        self.InvestCharg.setGeometry(QtCore.QRect(154, 266, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.InvestCharg.setFont(font)
        self.InvestCharg.setStyleSheet("")
        self.InvestCharg.setObjectName("InvestCharg")
        self.Medicine = QtWidgets.QLineEdit(self.centralwidget)
        self.Medicine.setGeometry(QtCore.QRect(154, 240, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.Medicine.setFont(font)
        self.Medicine.setStyleSheet("")
        self.Medicine.setObjectName("Medicine")
        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(332, 235, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.SurgeryC = QtWidgets.QLineEdit(self.centralwidget)
        self.SurgeryC.setGeometry(QtCore.QRect(440, 236, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.SurgeryC.setFont(font)
        self.SurgeryC.setStyleSheet("")
        self.SurgeryC.setObjectName("SurgeryC")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(317, 258, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.Imp = QtWidgets.QLineEdit(self.centralwidget)
        self.Imp.setGeometry(QtCore.QRect(440, 261, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.Imp.setFont(font)
        self.Imp.setStyleSheet("")
        self.Imp.setObjectName("Imp")
        self.PackageCharg = QtWidgets.QLineEdit(self.centralwidget)
        self.PackageCharg.setGeometry(QtCore.QRect(153, 336, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.PackageCharg.setFont(font)
        self.PackageCharg.setStyleSheet("")
        self.PackageCharg.setObjectName("PackageCharg")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(50, 333, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(36, 309, 171, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.MisCharges = QtWidgets.QLineEdit(self.centralwidget)
        self.MisCharges.setGeometry(QtCore.QRect(153, 310, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.MisCharges.setFont(font)
        self.MisCharges.setStyleSheet("")
        self.MisCharges.setObjectName("MisCharges")
        self.AnyOther = QtWidgets.QLineEdit(self.centralwidget)
        self.AnyOther.setGeometry(QtCore.QRect(433, 307, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.AnyOther.setFont(font)
        self.AnyOther.setStyleSheet("")
        self.AnyOther.setObjectName("AnyOther")
        self.BilledAmount = QtWidgets.QLineEdit(self.centralwidget)
        self.BilledAmount.setGeometry(QtCore.QRect(433, 333, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(9)
        self.BilledAmount.setFont(font)
        self.BilledAmount.setStyleSheet("")
        self.BilledAmount.setText("Click Save to Calculate")
        self.BilledAmount.setObjectName("BilledAmount")
        self.label_35 = QtWidgets.QLabel(self.centralwidget)
        self.label_35.setGeometry(QtCore.QRect(350, 306, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_35.setFont(font)
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(self.centralwidget)
        self.label_36.setGeometry(QtCore.QRect(320, 331, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_36.setFont(font)
        self.label_36.setObjectName("label_36")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(30, 370, 271, 61))
        self.label_15.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.label_37 = QtWidgets.QLabel(self.centralwidget)
        self.label_37.setGeometry(QtCore.QRect(90, 403, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_37.setFont(font)
        self.label_37.setObjectName("label_37")
        self.label_38 = QtWidgets.QLabel(self.centralwidget)
        self.label_38.setGeometry(QtCore.QRect(70, 379, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.ReceivedBy = QtWidgets.QLineEdit(self.centralwidget)
        self.ReceivedBy.setGeometry(QtCore.QRect(150, 380, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.ReceivedBy.setFont(font)
        self.ReceivedBy.setStyleSheet("")
        self.ReceivedBy.setObjectName("ReceivedBy")
        self.Date = QtWidgets.QDateEdit(self.centralwidget)
        self.Date.setGeometry(QtCore.QRect(150, 406, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Date.setFont(font)
        self.Date.setDateTime(QtCore.QDateTime(QtCore.QDate(2020, 1, 1), QtCore.QTime(0, 0, 0)))
        self.Date.setObjectName("Date")
        self.label.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.label_12.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.Name.raise_()
        self.label_14.raise_()
        self.SaveButton.raise_()
        self.label_18.raise_()
        self.DateAd.raise_()
        self.RoomRent.raise_()
        self.label_21.raise_()
        self.label_7.raise_()
        self.label_19.raise_()
        self.label_23.raise_()
        self.label_25.raise_()
        self.DateDis.raise_()
        self.label_26.raise_()
        self.BillNum.raise_()
        self.ICUCharges.raise_()
        self.label_27.raise_()
        self.label_22.raise_()
        self.label_28.raise_()
        self.ConsVisit.raise_()
        self.RMOService.raise_()
        self.label_29.raise_()
        self.label_30.raise_()
        self.InvestCharg.raise_()
        self.Medicine.raise_()
        self.label_31.raise_()
        self.SurgeryC.raise_()
        self.label_32.raise_()
        self.Imp.raise_()
        self.PackageCharg.raise_()
        self.label_33.raise_()
        self.label_34.raise_()
        self.MisCharges.raise_()
        self.AnyOther.raise_()
        self.BilledAmount.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.label_15.raise_()
        self.label_37.raise_()
        self.label_38.raise_()
        self.ReceivedBy.raise_()
        self.Date.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindowAdmin", "MainWindowAdmin"))
        self.label_3.setText(_translate("MainWindowAdmin", "Generate Bill"))
        self.label_8.setText(_translate("MainWindowAdmin", "Patient Name"))
        self.SaveButton.setText(_translate("MainWindowAdmin", "Save"))
        self.label_18.setText(_translate("MainWindowAdmin", "Date: Admission"))
        self.label_21.setText(_translate("MainWindowAdmin", "Room Rent Serv($)"))
        self.label_25.setText(_translate("MainWindowAdmin", "Date: Discharge"))
        self.label_26.setText(_translate("MainWindowAdmin", "Bill Number"))
        self.label_27.setText(_translate("MainWindowAdmin", "ICU Charges($)"))
        self.label_22.setText(_translate("MainWindowAdmin", "RMO Services($)"))
        self.label_28.setText(_translate("MainWindowAdmin", "ConsultantVisits($)"))
        self.label_29.setText(_translate("MainWindowAdmin", "Medicine($)"))
        self.label_30.setText(_translate("MainWindowAdmin", "   Investig. Charg($)"))
        self.label_31.setText(_translate("MainWindowAdmin", "Surgery Charges($)"))
        self.label_32.setText(_translate("MainWindowAdmin", "Imp.& Equipments($)"))
        self.label_33.setText(_translate("MainWindowAdmin", "Package Charges($)"))
        self.label_34.setText(_translate("MainWindowAdmin", "MiscellaneousCharg($)"))
        self.label_35.setText(_translate("MainWindowAdmin", "Any Other($)"))
        self.label_36.setText(_translate("MainWindowAdmin", "    Total Amount($)"))
        self.label_37.setText(_translate("MainWindowAdmin", "Date"))
        self.label_38.setText(_translate("MainWindowAdmin", "Received By"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Generate_Bill()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
