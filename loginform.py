from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox
import AdminForm
import ReceptionistForm
import RegisterForm
import PatientLogin

class LoginForm( object ):
    # Function for checking the Email, Passowrd and user type and open a new NewWindow accordingly
    def loginUsers(self):
        # Getting the data from lineEdits
        Email = self.EmailEdit.text()
        Password = self.PasswordEdit.text()
        UserType = self.MultipleChoice.currentText()
        # Connecting to project.db database

        db = sqlite3.connect("project.db")
        # IF the user type is 'Admin', create a table with only one admin user.
        if UserType == 'Admin':
                db.execute( "create table if not exists adminOnly (email text, password text)" )
                db.execute( "insert into adminOnly values('admin@gmail.com', 'admin')" )
                db.commit()
                CheckAdmin = db.execute("select email, password from adminOnly where email=? and password =?", (Email, Password))
                # if the email and password is correct, show a messagebox and open 'Admin' NewWindow
                if CheckAdmin.fetchall():
                        message2 = QMessageBox()
                        message2.setWindowTitle( "Successfull" )
                        message2.setInformativeText( "Welcome to the Care & Cure Hospital! "+ Email)
                        message2.exec_()
                        self.openWindow = QtWidgets.QMainWindow()
                        self.AdminForm = AdminForm.Admin_Form()
                        self.AdminForm.setupUi(self.openWindow)
                        self.openWindow.show()

                #If not show a messagebox and try again
                else:
                        message2 = QMessageBox()
                        message2.setWindowTitle( "Unsuccessfull" )
                        message2.setInformativeText( "Please Enter correct email address /password! " )
                        message2.exec_()
        # IF the usertype is 'Patient' then open another NewWindow for 'Patient' only
        elif UserType == 'Patient':
                # Save the Email to another table, the purpose of it is to show the patient and appointment info of only one person
                ID = "0" # Just to save the emails
                db.execute("drop table SaveEmails")
                db.execute("create table if not exists SaveEmails (ID, Email text)")
                db.execute("insert into SaveEmails values(?,?)", (ID, Email))
                db.commit()
                check = db.execute( "select email, password from registration where email =? and password = ?",
                                    (Email, Password) )
                # If the email and password and usertype belongs to a patient, log In otherwise it gives a message
                if check.fetchall():
                        message1 = QMessageBox()
                        message1.setWindowTitle( "Successfull" )
                        message1.setInformativeText( "Welcome to the Care & Cure Hospital! "+ Email)
                        message1.exec_()

                        self.window = QtWidgets.QMainWindow()
                        self.classPatient = PatientLogin.Patient_Login()
                        self.classPatient.setupUi( self.window )
                        self.window.show()
                else:
                        message1 = QMessageBox()
                        message1.setWindowTitle( "Unsuccessfull" )
                        message1.setInformativeText( "Please Enter correct email address /password! " )
                        message1.exec_()
        # Check if the usertype is 'Receptionist' go to receptionsit table and check the email and password
        elif UserType == 'Receptionist':
                checkReceptionist = db.execute("select email, password from receptionistDB where email =? and password = ?", (Email, Password))
                if checkReceptionist.fetchall():
                        message1 = QMessageBox()
                        message1.setWindowTitle( "Successfull" )
                        message1.setInformativeText( "Welcome to the Care & Cure Hospital! "+Email)
                        message1.exec_()
                        # OpenWindow Receptionist NewWindow
                        self.window = QtWidgets.QMainWindow()
                        self.classPatient = ReceptionistForm.ReceptionistLogIn()
                        self.classPatient.setupUi( self.window )
                        self.window.show()
                else:
                        message1 = QMessageBox()
                        message1.setWindowTitle( "Unsuccessfull" )
                        message1.setInformativeText( "Please Enter correct email address /password! " )
                        message1.exec_()

        db.close()
        self.EmailEdit.clear()
        self.PasswordEdit.clear()

    #Funtion for displaying Registration form is the Sign Up button is clicked
    def SignUpAction(self):
        self.window = QtWidgets.QMainWindow()
        self.OpenSignUp = RegisterForm.RegisterationForm()
        self.OpenSignUp.setupUi(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindowAdmin")
        MainWindow.resize(589, 538)
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 3, 591, 481))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("bg.jpeg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 190, 121, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
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
        self.label_3.setGeometry(QtCore.QRect(270, 50, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 120, 271, 61))
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(190, 119, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_1")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(170, 190, 271, 61))
        self.label_10.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_10.setText("")
        self.label_10.setObjectName("label_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(190, 185, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_2")
        self.EmailEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.EmailEdit.setGeometry(QtCore.QRect(192, 140, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.EmailEdit.setFont(font)
        self.EmailEdit.setStyleSheet("")
        self.EmailEdit.setObjectName("Get_Email")
        self.PasswordEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.PasswordEdit.setGeometry(QtCore.QRect(190, 210, 231, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semilight")
        font.setPointSize(10)
        self.PasswordEdit.setFont(font)
        self.PasswordEdit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.PasswordEdit.setObjectName("Get_Password")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(170, 330, 271, 61))
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_11.setText("")
        self.label_11.setObjectName("label_7")
        self.SignInButton = QtWidgets.QPushButton(self.centralwidget)
        self.SignInButton.setGeometry(QtCore.QRect(270, 344, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SignInButton.setFont(font)
        self.SignInButton.setStyleSheet("background-color: rgb(36, 160, 237);")
        self.SignInButton.setObjectName("SignINB")
        self.SignInButton.clicked.connect(self.loginUsers)
        self.MultipleChoice = QtWidgets.QComboBox(self.centralwidget)
        self.MultipleChoice.setGeometry(QtCore.QRect(300, 277, 121, 31))
        self.MultipleChoice.setStyleSheet("background-color: rgb(228, 230, 255);")
        self.MultipleChoice.setObjectName("MultipleChoice")
        self.MultipleChoice.addItem("")
        self.MultipleChoice.setItemText(0, "")
        self.MultipleChoice.addItem("")
        self.MultipleChoice.addItem("")
        self.MultipleChoice.addItem("")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(170, 260, 271, 61))
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_12.setText("")
        self.label_12.setObjectName("label_1")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(192, 274, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_3")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(170, 400, 271, 61))
        self.label_14.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10%;")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(190, 413, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.SignUpButton = QtWidgets.QPushButton(self.centralwidget)
        self.SignUpButton.setGeometry(QtCore.QRect(350, 414, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SignUpButton.setFont(font)
        self.SignUpButton.setStyleSheet("background-color: rgb(219, 216, 255);")
        self.SignUpButton.setObjectName("SignUPB")
        self.SignUpButton.clicked.connect(self.SignUpAction)
        self.label.raise_()
        self.label_12.raise_()
        self.lineEdit_2.raise_()
        self.frame.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.label_9.raise_()
        self.EmailEdit.raise_()
        self.PasswordEdit.raise_()
        self.label_11.raise_()
        self.SignInButton.raise_()
        self.MultipleChoice.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.SignUpButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 589, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindowAdmin", "MainWindowAdmin"))
        self.label_3.setText(_translate("MainWindowAdmin", "Login"))
        self.label_8.setText(_translate("MainWindowAdmin", "Email"))
        self.label_9.setText(_translate("MainWindowAdmin", "Password"))
        self.SignInButton.setText(_translate("MainWindowAdmin", "Sign In"))
        self.MultipleChoice.setItemText(1, _translate("MainWindowAdmin", "Admin"))
        self.MultipleChoice.setItemText(2, _translate("MainWindowAdmin", "Receptionist"))
        self.MultipleChoice.setItemText(3, _translate("MainWindowAdmin", "Patient"))
        self.label_13.setText(_translate("MainWindowAdmin", "User Type"))
        self.label_15.setText(_translate("MainWindowAdmin", "Create an account!"))
        self.SignUpButton.setText(_translate("MainWindowAdmin", "Sign Up"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LoginForm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

