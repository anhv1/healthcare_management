from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

from PyQt5.QtWidgets import QMessageBox


class RegisterationForm( object ):
    # Function to Register users once the Register button is clicked
    def registerUsers(self):
        # Getting the data from lineEdits
        Name = self.NameEdit.text()
        email = self.EmailEdit.text()
        phone = self.PhoneNumEdit.text()
        password = self.PasswordEdit.text()
        confirmPass = self.ConfirmPassEdit.text()
        UserType = self.MultipleChoice2.currentText()

        db = sqlite3.connect( "project.db" )
        # IF the password matches the ConfirmPassowrd, create a table and insert the data
        if password == confirmPass:
                # Creating tables for receptionist and patient and inserting the data to tables
                if UserType == 'Receptionist':
                        db.execute("create table if not exists receptionistDB (Name text NOT NULL, email text NOT NULL, phone int NOT NULL, password text NOT NULL)")
                        db.execute( "insert into receptionistDB values(?,?,?,?)", (Name, email, phone, password) )
                        db.commit()
                        message1 = QMessageBox()
                        message1.setWindowTitle( "Successfull" )
                        message1.setInformativeText( "You have successfully registered by this Name as Receptionist:  " + Name )
                        message1.exec_()
                # If the user type is Patient then create a table for patient and insert the data
                elif UserType == 'Patient':
                        db.execute("create table if not exists registration (Name text NOT NULL, email text NOT NULL, phone int NOT NULL, password text NOT NULL)")
                        db.execute("insert into registration values(?,?,?,?)", (Name, email, phone, password))
                        db.commit()
                        message1 = QMessageBox()
                        message1.setWindowTitle( "Successfull" )
                        message1.setInformativeText( "You have successfully registered by this Name as a Patient:  " + Name )
                        message1.exec_()
                # Clearing all the fields when it is done or give an error
                db.close()
                self.NameEdit.clear()
                self.EmailEdit.clear()
                self.PhoneNumEdit.clear()
                self.PasswordEdit.clear()
                self.ConfirmPassEdit.clear()
        # If the password does not match, try again
        else:
                message1 = QMessageBox()
                message1.setWindowTitle( "Alert!" )
                message1.setInformativeText( "Your Password does not match. Please try again!  ")
                x = message1.exec_()
                self.PasswordEdit.clear()
                self.ConfirmPassEdit.clear()



    def setupUi(self, MainWindow):
                MainWindow.setObjectName( "MainWindowAdmin" )
                MainWindow.resize( 589, 559 )
                MainWindow.setStyleSheet( "@import \"compass/css3\";\n"
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
                                          "}" )
                self.centralwidget = QtWidgets.QWidget( MainWindow )
                self.centralwidget.setObjectName( "centralwidget" )
                self.label = QtWidgets.QLabel( self.centralwidget )
                self.label.setGeometry( QtCore.QRect( 1, 0, 591, 551 ) )
                self.label.setText( "" )
                self.label.setPixmap( QtGui.QPixmap( "bg.jpeg" ) )
                self.label.setScaledContents( True )
                self.label.setObjectName( "label" )
                self.lineEdit_2 = QtWidgets.QLineEdit( self.centralwidget )
                self.lineEdit_2.setGeometry( QtCore.QRect( 260, 190, 121, 31 ) )
                self.lineEdit_2.setObjectName( "lineEdit_2" )
                self.frame = QtWidgets.QFrame( self.centralwidget )
                self.frame.setGeometry( QtCore.QRect( 210, 40, 120, 80 ) )
                self.frame.setFrameShape( QtWidgets.QFrame.StyledPanel )
                self.frame.setFrameShadow( QtWidgets.QFrame.Raised )
                self.frame.setObjectName( "frame" )
                self.label_2 = QtWidgets.QLabel( self.centralwidget )
                self.label_2.setGeometry( QtCore.QRect( 170, 50, 271, 61 ) )
                self.label_2.setStyleSheet( "background-color: rgb(255, 255, 255);\n"
                                            "border-radius: 10%;" )
                self.label_2.setText( "" )
                self.label_2.setObjectName( "label_2" )
                self.label_3 = QtWidgets.QLabel( self.centralwidget )
                self.label_3.setGeometry( QtCore.QRect( 219, 50, 181, 51 ) )
                font = QtGui.QFont()
                font.setFamily( "Forte" )
                font.setPointSize( 26 )
                font.setBold( False )
                font.setItalic( False )
                font.setWeight( 50 )
                self.label_3.setFont( font )
                self.label_3.setObjectName( "label_3" )
                self.label_4 = QtWidgets.QLabel( self.centralwidget )
                self.label_4.setGeometry( QtCore.QRect( 170, 120, 271, 61 ) )
                self.label_4.setStyleSheet( "background-color: rgb(255, 255, 255);\n"
                                            "border-radius: 10%;" )
                self.label_4.setText( "" )
                self.label_4.setObjectName( "label_4" )
                self.label_8 = QtWidgets.QLabel( self.centralwidget )
                self.label_8.setGeometry( QtCore.QRect( 190, 119, 47, 21 ) )
                font = QtGui.QFont()
                font.setFamily( "Segoe Print" )
                font.setPointSize( 10 )
                font.setBold( True )
                font.setWeight( 75 )
                self.label_8.setFont( font )
                self.label_8.setObjectName( "label_1" )
                self.label_10 = QtWidgets.QLabel( self.centralwidget )
                self.label_10.setGeometry( QtCore.QRect( 170, 190, 271, 61 ) )
                self.label_10.setStyleSheet( "background-color: rgb(255, 255, 255);\n"
                                             "border-radius: 10%;" )
                self.label_10.setText( "" )
                self.label_10.setObjectName( "label_6" )
                self.label_9 = QtWidgets.QLabel( self.centralwidget )
                self.label_9.setGeometry( QtCore.QRect( 190, 185, 71, 31 ) )
                font = QtGui.QFont()
                font.setFamily( "Segoe Print" )
                font.setPointSize( 10 )
                font.setBold( True )
                font.setWeight( 75 )
                self.label_9.setFont( font )
                self.label_9.setObjectName( "label_2" )
                self.NameEdit = QtWidgets.QLineEdit( self.centralwidget )
                self.NameEdit.setGeometry( QtCore.QRect( 192, 140, 231, 31 ) )
                font = QtGui.QFont()
                font.setFamily( "Segoe UI Semilight" )
                font.setPointSize( 10 )
                self.NameEdit.setFont( font )
                self.NameEdit.setStyleSheet( "" )
                self.NameEdit.setObjectName( "Name" )
                self.EmailEdit = QtWidgets.QLineEdit( self.centralwidget )
                self.EmailEdit.setGeometry( QtCore.QRect( 190, 210, 231, 31 ) )
                font = QtGui.QFont()
                font.setFamily( "Segoe UI Semilight" )
                font.setPointSize( 10 )
                self.EmailEdit.setFont( font )
                self.EmailEdit.setObjectName( "Email" )
                self.label_11 = QtWidgets.QLabel( self.centralwidget )
                self.label_11.setGeometry( QtCore.QRect( 139, 405, 161, 61 ) )
                self.label_11.setStyleSheet( "background-color: rgb(255, 255, 255);\n"
                                             "border-radius: 10%;" )
                self.label_11.setText( "" )
                self.label_11.setObjectName( "label_7" )
                self.label_12 = QtWidgets.QLabel( self.centralwidget )
                self.label_12.setGeometry( QtCore.QRect( 170, 260, 271, 61 ) )
                self.label_12.setStyleSheet( "background-color: rgb(255, 255, 255);\n"
                                             "border-radius: 10%;" )
                self.label_12.setText( "" )
                self.label_12.setObjectName( "label_1" )
                self.label_14 = QtWidgets.QLabel( self.centralwidget )
                self.label_14.setGeometry( QtCore.QRect( 170, 475, 271, 61 ) )
                self.label_14.setStyleSheet( "background-color: rgb(255, 255, 255);\n"
                                             "border-radius: 10%;" )
                self.label_14.setText( "" )
                self.label_14.setObjectName( "label_14" )
                self.RegisterButton = QtWidgets.QPushButton( self.centralwidget )
                self.RegisterButton.setGeometry( QtCore.QRect( 270, 489, 71, 31 ) )
                font = QtGui.QFont()
                font.setFamily( "Segoe UI Semibold" )
                font.setPointSize( 10 )
                font.setBold( True )
                font.setWeight( 75 )
                self.RegisterButton.setFont( font )
                self.RegisterButton.setStyleSheet( "background-color: rgb(85, 170, 255);" )
                self.RegisterButton.setObjectName( "RegisterB" )
                self.RegisterButton.clicked.connect( self.registerUsers )
                self.PhoneNumEdit = QtWidgets.QLineEdit( self.centralwidget )
                self.PhoneNumEdit.setGeometry( QtCore.QRect( 190, 282, 231, 31 ) )
                font = QtGui.QFont()
                font.setFamily( "Segoe UI Semilight" )
                font.setPointSize( 10 )
                self.PhoneNumEdit.setFont( font )
                self.PhoneNumEdit.setObjectName( "Phone" )
                self.label_13 = QtWidgets.QLabel( self.centralwidget )
                self.label_13.setGeometry( QtCore.QRect( 190, 255, 101, 31 ) )
                font = QtGui.QFont()
                font.setFamily( "Segoe Print" )
                font.setPointSize( 10 )
                font.setBold( True )
                font.setWeight( 75 )
                self.label_13.setFont( font )
                self.label_13.setObjectName( "label_3" )
                self.PasswordEdit = QtWidgets.QLineEdit( self.centralwidget )
                self.PasswordEdit.setGeometry( QtCore.QRect( 159, 425, 121, 31 ) )
                font = QtGui.QFont()
                font.setFamily( "Segoe UI Semilight" )
                font.setPointSize( 10 )
                self.PasswordEdit.setFont( font )
                self.PasswordEdit.setEchoMode( QtWidgets.QLineEdit.Password )
                self.PasswordEdit.setObjectName( "Password" )
                self.label_16 = QtWidgets.QLabel( self.centralwidget )
                self.label_16.setGeometry( QtCore.QRect( 158, 400, 101, 31 ) )
                font = QtGui.QFont()
                font.setFamily( "Segoe Print" )
                font.setPointSize( 10 )
                font.setBold( True )
                font.setWeight( 75 )
                self.label_16.setFont( font )
                self.label_16.setObjectName( "label_6" )
                self.label_15 = QtWidgets.QLabel( self.centralwidget )
                self.label_15.setGeometry( QtCore.QRect( 310, 404, 161, 61 ) )
                self.label_15.setStyleSheet( "background-color: rgb(255, 255, 255);\n"
                                             "border-radius: 10%;" )
                self.label_15.setText( "" )
                self.label_15.setObjectName( "label_15" )
                self.label_17 = QtWidgets.QLabel( self.centralwidget )
                self.label_17.setGeometry( QtCore.QRect( 330, 399, 131, 31 ) )
                font = QtGui.QFont()
                font.setFamily( "Segoe Print" )
                font.setPointSize( 10 )
                font.setBold( True )
                font.setWeight( 75 )
                self.label_17.setFont( font )
                self.label_17.setObjectName( "label_17" )
                self.ConfirmPassEdit = QtWidgets.QLineEdit( self.centralwidget )
                self.ConfirmPassEdit.setGeometry( QtCore.QRect( 331, 425, 121, 31 ) )
                font = QtGui.QFont()
                font.setFamily( "Segoe UI Semilight" )
                font.setPointSize( 10 )
                self.ConfirmPassEdit.setFont( font )
                self.ConfirmPassEdit.setEchoMode( QtWidgets.QLineEdit.Password )
                self.ConfirmPassEdit.setObjectName( "ConfirmPassEdit" )
                self.label_18 = QtWidgets.QLabel( self.centralwidget )
                self.label_18.setGeometry( QtCore.QRect( 349, 560, 271, 61 ) )
                self.label_18.setStyleSheet( "background-color: rgb(255, 255, 255);\n"
                                             "border-radius: 10%;" )
                self.label_18.setText( "" )
                self.label_18.setObjectName( "label_18" )
                self.label_19 = QtWidgets.QLabel( self.centralwidget )
                self.label_19.setGeometry( QtCore.QRect( 170, 330, 271, 61 ) )
                self.label_19.setStyleSheet( "background-color: rgb(255, 255, 255);\n"
                                             "border-radius: 10%;" )
                self.label_19.setText( "" )
                self.label_19.setObjectName( "label_19" )
                self.label_20 = QtWidgets.QLabel( self.centralwidget )
                self.label_20.setGeometry( QtCore.QRect( 193, 343, 101, 31 ) )
                font = QtGui.QFont()
                font.setFamily( "Segoe Print" )
                font.setPointSize( 10 )
                font.setBold( True )
                font.setWeight( 75 )
                self.label_20.setFont( font )
                self.label_20.setObjectName( "label_1" )
                self.MultipleChoice2 = QtWidgets.QComboBox( self.centralwidget )
                self.MultipleChoice2.setGeometry( QtCore.QRect( 301, 345, 121, 31 ) )
                self.MultipleChoice2.setStyleSheet( "background-color: rgb(228, 230, 255);" )
                self.MultipleChoice2.setObjectName( "MultipleChoice2" )
                self.MultipleChoice2.addItem( "" )
                self.MultipleChoice2.setItemText( 0, "" )
                self.MultipleChoice2.addItem( "" )
                self.MultipleChoice2.addItem( "" )
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
                self.NameEdit.raise_()
                self.EmailEdit.raise_()
                self.label_11.raise_()
                self.label_14.raise_()
                self.RegisterButton.raise_()
                self.PhoneNumEdit.raise_()
                self.label_13.raise_()
                self.PasswordEdit.raise_()
                self.label_16.raise_()
                self.label_15.raise_()
                self.label_17.raise_()
                self.ConfirmPassEdit.raise_()
                self.label_18.raise_()
                self.label_19.raise_()
                self.label_20.raise_()
                self.MultipleChoice2.raise_()
                MainWindow.setCentralWidget( self.centralwidget )
                self.statusbar = QtWidgets.QStatusBar( MainWindow )
                self.statusbar.setObjectName( "statusbar" )
                MainWindow.setStatusBar( self.statusbar )

                self.retranslateUi( MainWindow )
                QtCore.QMetaObject.connectSlotsByName( MainWindow )

    def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle( _translate( "MainWindowAdmin", "MainWindowAdmin" ) )
                self.label_3.setText( _translate( "MainWindowAdmin", "Registration" ) )
                self.label_8.setText( _translate( "MainWindowAdmin", "Name" ) )
                self.label_9.setText( _translate( "MainWindowAdmin", "Email" ) )
                self.RegisterButton.setText( _translate( "MainWindowAdmin", "Register" ) )
                self.label_13.setText( _translate( "MainWindowAdmin", "Phone Number" ) )
                self.label_16.setText( _translate( "MainWindowAdmin", "Password" ) )
                self.label_17.setText( _translate( "MainWindowAdmin", "Confirm Password" ) )
                self.label_20.setText( _translate( "MainWindowAdmin", "User Type" ) )
                self.MultipleChoice2.setItemText( 1, _translate( "MainWindowAdmin", "Receptionist" ) )
                self.MultipleChoice2.setItemText( 2, _translate( "MainWindowAdmin", "Patient" ) )

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = RegisterationForm()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
