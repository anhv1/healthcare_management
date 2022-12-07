from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

from PyQt5.QtWidgets import QMessageBox
class EmployeeRegistration( object ):
    # Function to Register Employees if the Register button is clicked
    def RegisterEMP(self):
        # Get all the data from the admin about employees
        EmpID = self.EmpID.text()
        EmpName = self.EmpName.text()
        EmpAddress = self.EmpAddress.text()
        EmpEmail = self.EmpEmail.text()
        EmpPhone = self.EmpPhone.text()
        EmpAge = self.EmpAge.text()
        EmpStatus = self.EmpStatus.currentText()
        EmpGender = self.EmpGender.currentText()
        EmpJob = self.EmpJob.currentText()
        EmpSalary = self.EmpSalary.currentText()
        db = sqlite3.connect("project.db")
        # Creating table of Employees and inserting data
        db.execute("create table if not exists EmployeeInfo (ID int, Name text, Address text, Email text, Phone int, Age int, Status text, Gender text, Job text, Salary text)")
        db.execute("insert into EmployeeInfo values (?,?,?,?,?,?,?,?,?,?)", (EmpID, EmpName, EmpAddress, EmpEmail, EmpPhone, EmpAge, EmpStatus, EmpGender, EmpJob, EmpSalary))
        db.commit()
        message1 = QMessageBox()
        message1.setWindowTitle( "Successfull" )
        message1.setInformativeText( "You have successfully registered:  " + EmpName )
        message1.exec_()
        # Clearing all the fields once it is done
        self.EmpID.clear()
        self.EmpName.clear()
        self.EmpAddress.clear()
        self.EmpEmail.clear()
        self.EmpPhone.clear()
        self.EmpAge.clear()
        self.EmpStatus.setCurrentText("")
        self.EmpGender.setCurrentText("")
        self.EmpJob.setCurrentText("")
        self.EmpSalary.setCurrentText("")
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
        self.label_3.setGeometry(QtCore.QRect(190, 54, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 190, 271, 61))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(50, 189, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_1")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 330, 271, 61))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(50, 325, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_2")
        self.EmpName = QtWidgets.QLineEdit(self.centralwidget)
        self.EmpName.setGeometry(QtCore.QRect(52, 210, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.EmpName.setFont(font)
        self.EmpName.setStyleSheet("")
        self.EmpName.setObjectName("EmpName")
        self.EmpEmail = QtWidgets.QLineEdit(self.centralwidget)
        self.EmpEmail.setGeometry(QtCore.QRect(50, 350, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.EmpEmail.setFont(font)
        self.EmpEmail.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.EmpEmail.setObjectName("EmpEmail")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 400, 271, 61))
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_1")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(170, 466, 271, 61))
        self.label_14.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.RegisterButton = QtWidgets.QPushButton(self.centralwidget)
        self.RegisterButton.setGeometry(QtCore.QRect(270, 480, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.RegisterButton.setFont(font)
        self.RegisterButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        ##################################################
        self.RegisterButton.setObjectName("RegisterB")
        self.RegisterButton.clicked.connect(self.RegisterEMP)
        self.EmpPhone = QtWidgets.QLineEdit(self.centralwidget)
        self.EmpPhone.setGeometry(QtCore.QRect(50, 422, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.EmpPhone.setFont(font)
        self.EmpPhone.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.EmpPhone.setObjectName("EmpPhone")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(50, 395, 171, 31))
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
        self.label_18.setGeometry(QtCore.QRect(333, 140, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.EmpAddress = QtWidgets.QLineEdit(self.centralwidget)
        self.EmpAddress.setGeometry(QtCore.QRect(52, 280, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.EmpAddress.setFont(font)
        self.EmpAddress.setStyleSheet("")
        self.EmpAddress.setObjectName("EmpAddress")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 260, 271, 61))
        self.label_6.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(50, 259, 141, 21))
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
        self.label_22.setGeometry(QtCore.QRect(331, 212, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.EmpStatus = QtWidgets.QComboBox(self.centralwidget)
        self.EmpStatus.setGeometry(QtCore.QRect(460, 209, 101, 31))
        self.EmpStatus.setObjectName("EmpStatus")
        self.EmpStatus.addItem("")
        self.EmpStatus.setItemText(0, "")
        self.EmpStatus.addItem("")
        self.EmpStatus.addItem("")
        self.EmpStatus.addItem("")
        self.EmpStatus.addItem("")
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
        self.EmpGender = QtWidgets.QComboBox(self.centralwidget)
        self.EmpGender.setGeometry(QtCore.QRect(459, 275, 101, 31))
        self.EmpGender.setObjectName("EmpGender")
        self.EmpGender.addItem("")
        self.EmpGender.setItemText(0, "")
        self.EmpGender.addItem("")
        self.EmpGender.addItem("")
        self.EmpGender.addItem("")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(309, 330, 271, 61))
        self.label_23.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
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
        self.EmpAge = QtWidgets.QLineEdit(self.centralwidget)
        self.EmpAge.setGeometry(QtCore.QRect(459, 137, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.EmpAge.setFont(font)
        self.EmpAge.setStyleSheet("")
        self.EmpAge.setObjectName("EmpAge")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 120, 271, 61))
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_7")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(50, 119, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.EmpID = QtWidgets.QLineEdit(self.centralwidget)
        self.EmpID.setGeometry(QtCore.QRect(51, 141, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.EmpID.setFont(font)
        self.EmpID.setObjectName("EmpID")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(310, 400, 271, 61))
        self.label_16.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_16.setText("")
        self.label_16.setObjectName("label_6")
        self.EmpJob = QtWidgets.QComboBox(self.centralwidget)
        self.EmpJob.setGeometry(QtCore.QRect(330, 351, 231, 31))
        self.EmpJob.setObjectName("EmpJob")
        self.EmpJob.addItem("")
        self.EmpJob.setItemText(0, "")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.EmpJob.addItem("")
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(329, 394, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.EmpSalary = QtWidgets.QComboBox(self.centralwidget)
        self.EmpSalary.setGeometry(QtCore.QRect(460, 421, 101, 31))
        self.EmpSalary.setObjectName("EmpSalary")
        self.EmpSalary.addItem("")
        self.EmpSalary.setItemText(0, "")
        self.EmpSalary.addItem("")
        self.EmpSalary.addItem("")
        self.EmpSalary.addItem("")
        self.EmpSalary.addItem("")
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
        self.EmpName.raise_()
        self.EmpEmail.raise_()
        self.label_14.raise_()
        self.RegisterButton.raise_()
        self.EmpPhone.raise_()
        self.label_13.raise_()
        self.label_18.raise_()
        self.EmpAddress.raise_()
        self.label_21.raise_()
        self.label_7.raise_()
        self.label_22.raise_()
        self.EmpStatus.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.EmpGender.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.EmpAge.raise_()
        self.label_11.raise_()
        self.label_15.raise_()
        self.EmpID.raise_()
        self.label_16.raise_()
        self.EmpJob.raise_()
        self.label_25.raise_()
        self.EmpSalary.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindowAdmin", "MainWindowAdmin"))
        self.label_3.setText(_translate("MainWindowAdmin", "Employee Registration"))
        self.label_8.setText(_translate("MainWindowAdmin", "Employee Name"))
        self.label_9.setText(_translate("MainWindowAdmin", "Employee Email"))
        self.RegisterButton.setText(_translate("MainWindowAdmin", "Register"))
        self.label_13.setText(_translate("MainWindowAdmin", "Employee Phone Number"))
        self.label_18.setText(_translate("MainWindowAdmin", "Employee Age"))
        self.label_21.setText(_translate("MainWindowAdmin", "Employee Address"))
        self.label_22.setText(_translate("MainWindowAdmin", "Martial Status"))
        self.EmpStatus.setItemText(1, _translate("MainWindowAdmin", "Single"))
        self.EmpStatus.setItemText(2, _translate("MainWindowAdmin", "Married"))
        self.EmpStatus.setItemText(3, _translate("MainWindowAdmin", "Divorced"))
        self.EmpStatus.setItemText(4, _translate("MainWindowAdmin", "Widowed"))
        self.label_20.setText(_translate("MainWindowAdmin", "Gender"))
        self.EmpGender.setItemText(1, _translate("MainWindowAdmin", "Male"))
        self.EmpGender.setItemText(2, _translate("MainWindowAdmin", "Female"))
        self.EmpGender.setItemText(3, _translate("MainWindowAdmin", "Other"))
        self.label_24.setText(_translate("MainWindowAdmin", "Employee Job"))
        self.label_15.setText(_translate("MainWindowAdmin", "Employee ID"))
        self.EmpJob.setItemText(1, _translate("MainWindowAdmin", "Medical Technologist"))
        self.EmpJob.setItemText(2, _translate("MainWindowAdmin", "Radiologic Technician"))
        self.EmpJob.setItemText(3, _translate("MainWindowAdmin", "Dietician"))
        self.EmpJob.setItemText(4, _translate("MainWindowAdmin", "Respiratory Therapist"))
        self.EmpJob.setItemText(5, _translate("MainWindowAdmin", "Registered Nurse"))
        self.EmpJob.setItemText(6, _translate("MainWindowAdmin", "Occupational Therapist"))
        self.EmpJob.setItemText(7, _translate("MainWindowAdmin", "Pharmacist"))
        self.EmpJob.setItemText(8, _translate("MainWindowAdmin", "Physician Assistant"))
        self.EmpJob.setItemText(9, _translate("MainWindowAdmin", "Surgeon"))
        self.EmpJob.setItemText(10, _translate("MainWindowAdmin", "Anesthesiologist"))
        self.EmpJob.setItemText(11, _translate("MainWindowAdmin", "Medical Admissions Clerk"))
        self.EmpJob.setItemText(12, _translate("MainWindowAdmin", "Medical Records Clerk"))
        self.EmpJob.setItemText(13, _translate("MainWindowAdmin", "Coding Specialist"))
        self.EmpJob.setItemText(14, _translate("MainWindowAdmin", "Medical Social Worker"))
        self.EmpJob.setItemText(15, _translate("MainWindowAdmin", "Information Technology Specialist"))
        self.EmpJob.setItemText(16, _translate("MainWindowAdmin", "Human Resources Manager"))
        self.EmpJob.setItemText(17, _translate("MainWindowAdmin", "Chief Executive Officer"))
        self.EmpJob.setItemText(18, _translate("MainWindowAdmin", "Receptionist"))
        self.EmpJob.setItemText(19, _translate("MainWindowAdmin", "Other"))
        self.label_25.setText(_translate("MainWindowAdmin", "Employee Salary"))
        self.EmpSalary.setItemText(1, _translate("MainWindowAdmin", "Below $1000"))
        self.EmpSalary.setItemText(2, _translate("MainWindowAdmin", "$1000-$5000"))
        self.EmpSalary.setItemText(3, _translate("MainWindowAdmin", "$5000-$10000"))
        self.EmpSalary.setItemText(4, _translate("MainWindowAdmin", "Above $10000"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = EmployeeRegistration()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
