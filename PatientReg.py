from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

from PyQt5.QtWidgets import QMessageBox
class RegistrationPatientsAdmin( object ):
    # Function for Registration of Patients
    def PatientRegister(self):
        # Getting all the info from the user
        Name = self.NameEdit.text()
        BirthDate = self.dateEdit.text()
        Address = self.AddressEdit.text()
        Phone = self.PhoneNumEdit.text()
        Status = self.MartialStatus.currentText()
        Gender = self.Gender.currentText()
        Illness = self.IllnessEdit.text()
        Email = self.EmailEdit.text()
        # Creating table for Patients with the information of user admin
        db = sqlite3.connect("project.db")
        db.execute("create table if not exists PatientInformation(name text NOT NULL, birthday text NOT NULL, address text NOT NULL,"
                   " phone int NOT NULL, status text NOT NULL,gender text NOT NULL, illness text NOT NULL, email text NOT NULL)")
        db.execute("insert into PatientInformation values(?,?,?,?,?,?,?,?)", (Name, BirthDate, Address, Phone, Status, Gender, Illness, Email))
        db.commit()
        message1 = QMessageBox()
        message1.setWindowTitle( "Successfull" )
        message1.setInformativeText( "You have successfully registered your patient:  " + Name )
        x = message1.exec_()
        self.NameEdit.clear()
        self.dateEdit.clear()
        self.AddressEdit.clear()
        self.PhoneNumEdit.clear()
        self.MartialStatus.setCurrentText("")
        self.Gender.setCurrentText("")
        self.IllnessEdit.clear()
        self.EmailEdit.clear()

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
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(210, 40, 120, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 50, 271, 61))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(195, 51, 231, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 120, 271, 61))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 119, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_1")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 260, 271, 61))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 255, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_2")
        self.NameEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.NameEdit.setGeometry(QtCore.QRect(52, 140, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.NameEdit.setFont(font)
        self.NameEdit.setStyleSheet("")
        self.NameEdit.setObjectName("Get_Name")
        self.EmailEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.EmailEdit.setGeometry(QtCore.QRect(50, 280, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.EmailEdit.setFont(font)
        self.EmailEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.EmailEdit.setObjectName("Get_Email")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 330, 271, 61))
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_1")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(170, 410, 271, 61))
        self.label_14.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.RegisterButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegisterButton.setGeometry(QtCore.QRect(270, 424, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.RegisterButton.setFont(font)
        self.RegisterButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.RegisterButton.setObjectName("RegisterB")
        self.RegisterButton.clicked.connect(self.PatientRegister)
        self.PhoneNumEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PhoneNumEdit.setGeometry(QtCore.QRect(50, 352, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.PhoneNumEdit.setFont(font)
        self.PhoneNumEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.PhoneNumEdit.setObjectName("Get_Phone")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(50, 325, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(310, 121, 271, 61))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(333, 140, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")

        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(463, 138, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dateEdit.setFont(font)
        self.dateEdit.setObjectName("dateEdit")
        self.AddressEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.AddressEdit.setGeometry(QtCore.QRect(52, 210, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.AddressEdit.setFont(font)
        self.AddressEdit.setStyleSheet("")
        self.AddressEdit.setObjectName("Get_Address")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 190, 271, 61))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(50, 189, 71, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_7")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(308, 190, 271, 61))
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(331, 210, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.MartialStatus = QtWidgets.QComboBox(self.centralwidget)
        self.MartialStatus.setGeometry(QtCore.QRect(460, 209, 101, 31))
        self.MartialStatus.setObjectName("MartialStatus")
        self.MartialStatus.addItem("")
        self.MartialStatus.setItemText(0, "")
        self.MartialStatus.addItem("")
        self.MartialStatus.addItem("")
        self.MartialStatus.addItem("")
        self.MartialStatus.addItem("")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(308, 260, 271, 61))
        self.label_19.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_19.setText("")
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(329, 274, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_1")
        self.Gender = QtWidgets.QComboBox(self.centralwidget)
        self.Gender.setGeometry(QtCore.QRect(459, 275, 101, 31))
        self.Gender.setObjectName("Get_Geneder")
        self.Gender.addItem("")
        self.Gender.setItemText(0, "")
        self.Gender.addItem("")
        self.Gender.addItem("")
        self.Gender.addItem("")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(309, 330, 271, 61))
        self.label_23.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.IllnessEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.IllnessEdit.setGeometry(QtCore.QRect(329, 352, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.IllnessEdit.setFont(font)
        self.IllnessEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.IllnessEdit.setObjectName("IllnessEdit")
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(329, 325, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, -6, 621, 561))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../PycharmProjects/b/bg.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.label_6.raise_()
        self.label_5.raise_()
        self.label_12.raise_()
        self.frame.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.NameEdit.raise_()
        self.EmailEdit.raise_()
        self.label_14.raise_()
        self.RegisterButton.raise_()
        self.PhoneNumEdit.raise_()
        self.label_13.raise_()
        self.label_18.raise_()
        self.dateEdit.raise_()
        self.AddressEdit.raise_()
        self.label_21.raise_()
        self.label_7.raise_()
        self.label_22.raise_()
        self.MartialStatus.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.Gender.raise_()
        self.label_23.raise_()
        self.IllnessEdit.raise_()
        self.label_24.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindowAdmin", "MainWindowAdmin"))
        self.label_3.setText(_translate("MainWindowAdmin", "Patient Registration"))
        self.label_8.setText(_translate("MainWindowAdmin", "Full Name"))
        self.label_9.setText(_translate("MainWindowAdmin", "Email"))
        self.RegisterButton.setText(_translate("MainWindowAdmin", "Register"))
        self.label_13.setText(_translate("MainWindowAdmin", "Phone Number"))
        self.label_18.setText(_translate("MainWindowAdmin", "Birth Date"))
        self.label_21.setText(_translate("MainWindowAdmin", "Address"))
        self.label_22.setText(_translate("MainWindowAdmin", "Martial Status"))
        self.MartialStatus.setItemText(1, _translate("MainWindowAdmin", "Single"))
        self.MartialStatus.setItemText(2, _translate("MainWindowAdmin", "Married"))
        self.MartialStatus.setItemText(3, _translate("MainWindowAdmin", "Divorced"))
        self.MartialStatus.setItemText(4, _translate("MainWindowAdmin", "Widowed"))
        self.label_20.setText(_translate("MainWindowAdmin", "Gender"))
        self.Gender.setItemText(1, _translate("MainWindowAdmin", "Male"))
        self.Gender.setItemText(2, _translate("MainWindowAdmin", "Female"))
        self.Gender.setItemText(3, _translate("MainWindowAdmin", "Other"))
        self.label_24.setText(_translate("MainWindowAdmin", "Illness"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RegistrationPatientsAdmin()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
