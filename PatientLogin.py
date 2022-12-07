from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from PyQt5.QtWidgets import QMessageBox

class Patient_Login( object ):
    # Function to show appointments after appointment button is clickec
    def ShowAppointments(self):
        db = sqlite3.connect( "project.db" )
        # Getting the only email address that the patient entered when he/she logged in to check if there is data that matches with this email
        r = db.execute( "select Email from SaveEmails" )
        list = [] # Using for loop to go over SaveEmails table and append that email into a list
        # Going through the Emails by changing the data type, RowNum is the number of rows, RowData is the column data
        for RowNum, RowData in enumerate( r ):
            for columnNum, columnData in enumerate( RowData ):
                list.append( columnData )
        # Getting all the info of an appointment that matches with the email address in list[]
        result = db.execute( "select * from Appointments where Email= " + "'" + list[0] + "'" )
        # Set the row count to be zero in order to show all the info that matches with email
        self.tableWidgetAppointment.setRowCount( 0 )
        for RowNum, RowData in enumerate( result ):
            self.tableWidgetAppointment.insertRow( RowNum )
            for columnNum, columnData in enumerate( RowData ):
                self.tableWidgetAppointment.setItem( RowNum, columnNum, QtWidgets.QTableWidgetItem( str( columnData ) ) )


        db.close()
    # Function to delete an appointment based on FullName
    def DeleteAppointment(self):
        # Get the full name from lineEdit and delete data if it matches that fullname
        FullName = self.FullName.text()
        db = sqlite3.connect( "project.db" )
        db.execute(
            "delete from Appointments where FullName=" + "'" + FullName + "'")
        db.commit()
        message1 = QMessageBox()
        message1.setWindowTitle( "Successfull" )
        message1.setInformativeText( "You have successfully deleted your appointment" )
        x = message1.exec_()
        # Showing the Appointments of patient after deleting one
        result = db.execute( "select * from Appointments where FullName= " + "'" + FullName + "'" )
        self.tableWidgetAppointment.setRowCount( 0 )
        # Using two for loops to insert the data of Appointments if there is any into tableWidget
        for RowNum, RowDATA in enumerate( result ):
            self.tableWidgetAppointment.insertRow( RowNum )
            for ColumnNum, ColumnData in enumerate( RowDATA ):
                self.tableWidgetAppointment.setItem( RowNum, ColumnNum,
                                                     QtWidgets.QTableWidgetItem( str( ColumnData ) ) )
        # Clearing the fields after deleting
        db.close()
        self.FullName.clear()
        self.Age.clear()
        self.Phone.clear()
        self.Gender.setCurrentText("")
        self.MedicalCondition.clear()
        self.Email.clear()
        self.PreferDay.setCurrentText("")
    # Function to Update Appointment
    def UpdateAppointment(self):
        # Getting all the information for fields after user enters
        FullName = self.FullName.text()
        Age = self.Age.text()
        Phone = self.Phone.text()
        Gender = self.Gender.currentText()
        MedicalCondition = self.MedicalCondition.text()
        Email = self.Email.text()
        Day = self.PreferDay.currentText()
        Time = self.timeEdit.text()
        db = sqlite3.connect( "project.db" )
        # Updating the data accordingly
        db.execute( "update Appointments set FullName =?, Age =?, Phone =?, Gender =?, MedicalCondition =?, Day =?, Time =?, Email =? where FullName="+"'"+FullName+"'",
                    (FullName, Age, Phone, Gender, MedicalCondition, Day, Time, Email) )
        db.commit()
        message1 = QMessageBox()
        message1.setWindowTitle( "Successfull" )
        message1.setInformativeText( "You have successfully updated your appointment")
        x = message1.exec_()
    # Function to make an appointment
    def MakeAppointment(self):
        # creating a table and inserting the data from the user without AppStatus because it belongs to Receptionist not Patient
        AppStatus = ""
        FullName = self.FullName.text()
        Age = self.Age.text()
        Phone = self.Phone.text()
        Gender = self.Gender.currentText()
        MedicalCondition = self.MedicalCondition.text()
        Email = self.Email.text()
        Day = self.PreferDay.currentText()
        Time = self.timeEdit.text()
        db = sqlite3.connect("project.db")
        db.execute("create table if not exists Appointments (AppStatus text, FullName text, Age int, Phone int, Gender text, MedicalCondition text, Day text, Time text, Email text)")
        db.execute("insert into Appointments values(?,?,?,?,?,?,?,?,?)", (AppStatus, FullName, Age, Phone, Gender, MedicalCondition, Day, Time, Email))
        db.commit()
        message1 = QMessageBox()
        message1.setWindowTitle( "Successfull" )
        message1.setInformativeText( "You have successfully created an appointment for " + Day )
        x = message1.exec_()
    # Function for Viewing all the patient information
    def ViewPatientInfo(self):
        db = sqlite3.connect("project.db")
        # Selecting the email that was saved when the user entered for logging in
        r= db.execute("select Email from SaveEmails")
        list = [] # Appending that email to a list
        for RowNum, RowDATA in enumerate( r ):
            for ColumnNum, ColumnData in enumerate( RowDATA ):
                list.append(ColumnData)
        # Selecting all the patient info based on the email from list[] if it matches
        result = db.execute( "select * from PatientInformation where email="+"'"+list[0]+"'" )
        self.tableWidgetPatientInfo.setRowCount( 0 )
        # Using two for loops to insert the data into tableWidget
        for RowNum, RowDATA in enumerate( result ):
            self.tableWidgetPatientInfo.insertRow( RowNum )
            for ColumnNum, ColumnData in enumerate( RowDATA ):
                self.tableWidgetPatientInfo.setItem( RowNum, ColumnNum, QtWidgets.QTableWidgetItem( str( ColumnData ) ) )
        db.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName( "MainWindowAdmin" )
        MainWindow.resize( 702, 566 )
        self.centralwidget = QtWidgets.QWidget( MainWindow )
        self.centralwidget.setObjectName( "centralwidget" )
        self.AppointmentButton = QtWidgets.QPushButton( self.centralwidget )
        self.AppointmentButton.setGeometry( QtCore.QRect( 470, 420, 131, 31 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe UI Semibold" )
        font.setPointSize( 9 )
        font.setBold( True )
        font.setWeight( 75 )
        self.AppointmentButton.setFont( font )
        self.AppointmentButton.setStyleSheet( "background-color: rgb(85, 170, 255);" )
        self.AppointmentButton.setObjectName( "AppointmentButton" )
        self.AppointmentButton.clicked.connect( self.MakeAppointment )

        self.label_2 = QtWidgets.QLabel( self.centralwidget )
        self.label_2.setGeometry( QtCore.QRect( 250, 10, 211, 111 ) )
        self.label_2.setText( "" )
        self.label_2.setPixmap( QtGui.QPixmap( "Logo.png" ) )
        self.label_2.setObjectName( "label_2" )
        self.label_3 = QtWidgets.QLabel( self.centralwidget )
        self.label_3.setGeometry( QtCore.QRect( 10, 111, 131, 20 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        font.setPointSize( 10 )
        self.label_3.setFont( font )
        self.label_3.setObjectName( "label_3" )
        self.label_4 = QtWidgets.QLabel( self.centralwidget )
        self.label_4.setGeometry( QtCore.QRect( 8, 250, 141, 20 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        font.setPointSize( 10 )
        self.label_4.setFont( font )
        self.label_4.setObjectName( "label_4" )
        self.tableWidgetPatientInfo = QtWidgets.QTableWidget( self.centralwidget )
        self.tableWidgetPatientInfo.setGeometry( QtCore.QRect( 0, 140, 701, 91 ) )
        self.tableWidgetPatientInfo.setObjectName( "tableWidgetPatientInfo" )
        self.tableWidgetPatientInfo.setColumnCount( 8 )
        self.tableWidgetPatientInfo.setRowCount( 0 )
        item = QtWidgets.QTableWidgetItem()
        item.setBackground( QtGui.QColor( 85, 170, 255 ) )
        self.tableWidgetPatientInfo.setHorizontalHeaderItem( 0, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPatientInfo.setHorizontalHeaderItem( 1, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPatientInfo.setHorizontalHeaderItem( 2, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPatientInfo.setHorizontalHeaderItem( 3, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPatientInfo.setHorizontalHeaderItem( 4, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPatientInfo.setHorizontalHeaderItem( 5, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPatientInfo.setHorizontalHeaderItem( 6, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetPatientInfo.setHorizontalHeaderItem( 7, item )
        self.tableWidgetAppointment = QtWidgets.QTableWidget( self.centralwidget )
        self.tableWidgetAppointment.setGeometry( QtCore.QRect( 0, 280, 701, 91 ) )
        self.tableWidgetAppointment.setObjectName( "tableWidgetAppointment" )
        self.tableWidgetAppointment.setColumnCount( 9 )
        self.tableWidgetAppointment.setRowCount( 0 )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem( 0, item )
        item = QtWidgets.QTableWidgetItem()
        item.setBackground( QtGui.QColor( 85, 170, 255 ) )
        self.tableWidgetAppointment.setHorizontalHeaderItem( 1, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem( 2, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem( 3, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem( 4, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem( 5, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem( 6, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem( 7, item )
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem( 8, item )

        self.ShowApButton = QtWidgets.QPushButton( self.centralwidget )
        self.ShowApButton.setGeometry( QtCore.QRect( 568, 373, 131, 31 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe UI Semibold" )
        font.setPointSize( 9 )
        font.setBold( True )
        font.setWeight( 75 )
        self.ShowApButton.setFont( font )
        self.ShowApButton.setStyleSheet( "background-color: rgb(85, 170, 255);" )
        self.ShowApButton.setObjectName( "ShowApButton" )
        self.ShowApButton.clicked.connect(self.ShowAppointments)

        self.ShowInfoButton = QtWidgets.QPushButton( self.centralwidget )
        self.ShowInfoButton.setGeometry( QtCore.QRect( 567, 233, 131, 31 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe UI Semibold" )
        font.setPointSize( 9 )
        font.setBold( True )
        font.setWeight( 75 )
        self.ShowInfoButton.setFont( font )
        self.ShowInfoButton.setStyleSheet( "background-color: rgb(85, 170, 255);" )
        self.ShowInfoButton.setObjectName( "ShowInfoButton" )
        self.ShowInfoButton.clicked.connect( self.ViewPatientInfo )
        self.LogOutButton = QtWidgets.QPushButton( self.centralwidget )
        self.LogOutButton.setGeometry( QtCore.QRect( 4, 0, 81, 31 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe UI Semibold" )
        font.setPointSize( 9 )
        font.setBold( True )
        font.setWeight( 75 )
        self.LogOutButton.setFont( font )
        self.LogOutButton.setStyleSheet( "background-color: rgb(85, 170, 255);" )
        self.LogOutButton.setObjectName( "LogOutB" )
        self.LogOutButton.clicked.connect(QtWidgets.qApp.quit)
        self.label = QtWidgets.QLabel( self.centralwidget )
        self.label.setGeometry( QtCore.QRect( 17, 391, 61, 16 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        font.setPointSize( 8 )
        self.label.setFont( font )
        self.label.setObjectName( "label" )
        self.label_5 = QtWidgets.QLabel( self.centralwidget )
        self.label_5.setGeometry( QtCore.QRect( 51, 421, 31, 16 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        self.label_5.setFont( font )
        self.label_5.setObjectName( "label_5" )
        self.label_6 = QtWidgets.QLabel( self.centralwidget )
        self.label_6.setGeometry( QtCore.QRect( 25, 452, 61, 16 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        self.label_6.setFont( font )
        self.label_6.setObjectName( "label_6" )
        self.label_7 = QtWidgets.QLabel( self.centralwidget )
        self.label_7.setGeometry( QtCore.QRect( 32, 481, 47, 13 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        self.label_7.setFont( font )
        self.label_7.setObjectName( "label_7" )
        self.label_8 = QtWidgets.QLabel( self.centralwidget )
        self.label_8.setGeometry( QtCore.QRect( 215, 390, 101, 16 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        self.label_8.setFont( font )
        self.label_8.setObjectName( "label_1" )
        self.label_9 = QtWidgets.QLabel( self.centralwidget )
        self.label_9.setGeometry( QtCore.QRect( 238, 446, 81, 20 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        self.label_9.setFont( font )
        self.label_9.setObjectName( "label_2" )
        self.label_10 = QtWidgets.QLabel( self.centralwidget )
        self.label_10.setGeometry( QtCore.QRect( 233, 476, 91, 20 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        self.label_10.setFont( font )
        self.label_10.setObjectName( "label_6" )
        self.label_11 = QtWidgets.QLabel( self.centralwidget )
        self.label_11.setGeometry( QtCore.QRect( 281, 420, 47, 13 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe Print" )
        self.label_11.setFont( font )
        self.label_11.setObjectName( "label_7" )
        self.FullName = QtWidgets.QLineEdit( self.centralwidget )
        self.FullName.setGeometry( QtCore.QRect( 86, 390, 113, 20 ) )
        self.FullName.setObjectName( "FullName" )
        self.Age = QtWidgets.QLineEdit( self.centralwidget )
        self.Age.setGeometry( QtCore.QRect( 86, 420, 113, 20 ) )
        self.Age.setObjectName( "Age" )
        self.Phone = QtWidgets.QLineEdit( self.centralwidget )
        self.Phone.setGeometry( QtCore.QRect( 86, 449, 113, 20 ) )
        self.Phone.setObjectName( "Phone" )
        self.Email = QtWidgets.QLineEdit( self.centralwidget )
        self.Email.setGeometry( QtCore.QRect( 324, 417, 113, 20 ) )
        self.Email.setObjectName( "Email" )
        self.MedicalCondition = QtWidgets.QLineEdit( self.centralwidget )
        self.MedicalCondition.setGeometry( QtCore.QRect( 324, 390, 113, 20 ) )
        self.MedicalCondition.setObjectName( "MedicalCondition" )
        self.Gender = QtWidgets.QComboBox( self.centralwidget )
        self.Gender.setGeometry( QtCore.QRect( 86, 477, 81, 22 ) )
        self.Gender.setObjectName( "Get_Geneder" )
        self.Gender.addItem( "" )
        self.Gender.setItemText( 0, "" )
        self.Gender.addItem( "" )
        self.Gender.addItem( "" )
        self.Gender.addItem( "" )
        self.PreferDay = QtWidgets.QComboBox( self.centralwidget )
        self.PreferDay.setGeometry( QtCore.QRect( 324, 445, 111, 22 ) )
        self.PreferDay.setObjectName( "PreferDay" )
        self.PreferDay.addItem( "" )
        self.PreferDay.setItemText( 0, "" )
        self.PreferDay.addItem( "" )
        self.PreferDay.addItem( "" )
        self.PreferDay.addItem( "" )
        self.PreferDay.addItem( "" )
        self.PreferDay.addItem( "" )
        self.PreferDay.addItem( "" )
        self.PreferDay.addItem( "" )
        self.timeEdit = QtWidgets.QTimeEdit( self.centralwidget )
        self.timeEdit.setGeometry( QtCore.QRect( 324, 475, 71, 22 ) )
        self.timeEdit.setObjectName( "timeEdit" )
        self.UpdateButton = QtWidgets.QPushButton( self.centralwidget )
        self.UpdateButton.setGeometry( QtCore.QRect( 470, 460, 61, 31 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe UI Semibold" )
        font.setPointSize( 9 )
        font.setBold( True )
        font.setWeight( 75 )
        self.UpdateButton.setFont( font )
        self.UpdateButton.setStyleSheet( "background-color: rgb(85, 170, 255);" )
        self.UpdateButton.setObjectName( "UpdateRecordB" )
        self.UpdateButton.clicked.connect(self.UpdateAppointment)
        self.DeleteButton = QtWidgets.QPushButton( self.centralwidget )
        self.DeleteButton.setGeometry( QtCore.QRect( 541, 460, 61, 31 ) )
        font = QtGui.QFont()
        font.setFamily( "Segoe UI Semibold" )
        font.setPointSize( 9 )
        font.setBold( True )
        font.setWeight( 75 )
        self.DeleteButton.setFont( font )
        self.DeleteButton.setStyleSheet( "background-color: rgb(85, 170, 255);" )
        self.DeleteButton.setObjectName( "DeleteRecordB" )
        self.DeleteButton.clicked.connect(self.DeleteAppointment)
        MainWindow.setCentralWidget( self.centralwidget )
        self.menubar = QtWidgets.QMenuBar( MainWindow )
        self.menubar.setGeometry( QtCore.QRect( 0, 0, 702, 21 ) )
        self.menubar.setObjectName( "menubar" )
        MainWindow.setMenuBar( self.menubar )
        self.statusbar = QtWidgets.QStatusBar( MainWindow )
        self.statusbar.setObjectName( "statusbar" )
        MainWindow.setStatusBar( self.statusbar )

        self.retranslateUi( MainWindow )
        QtCore.QMetaObject.connectSlotsByName( MainWindow )

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle( _translate( "MainWindowAdmin", "MainWindowAdmin" ) )
        self.AppointmentButton.setText( _translate( "MainWindowAdmin", "Make an Appointment" ) )
        self.label_3.setText( _translate( "MainWindowAdmin", "Your Information:" ) )
        self.label_4.setText( _translate( "MainWindowAdmin", "Your Appointment:" ) )
        item = self.tableWidgetPatientInfo.horizontalHeaderItem( 0 )
        item.setText( _translate( "MainWindowAdmin", "Full Name" ) )
        item = self.tableWidgetPatientInfo.horizontalHeaderItem( 1 )
        item.setText( _translate( "MainWindowAdmin", "Birth Date" ) )
        item = self.tableWidgetPatientInfo.horizontalHeaderItem( 2 )
        item.setText( _translate( "MainWindowAdmin", "Full Address" ) )
        item = self.tableWidgetPatientInfo.horizontalHeaderItem( 3 )
        item.setText( _translate( "MainWindowAdmin", "Phone" ) )
        item = self.tableWidgetPatientInfo.horizontalHeaderItem( 4 )
        item.setText( _translate( "MainWindowAdmin", "Martial Status" ) )
        item = self.tableWidgetPatientInfo.horizontalHeaderItem( 5 )
        item.setText( _translate( "MainWindowAdmin", "Gender" ) )
        item = self.tableWidgetPatientInfo.horizontalHeaderItem( 6 )
        item.setText( _translate( "MainWindowAdmin", "Illness" ) )
        item = self.tableWidgetPatientInfo.horizontalHeaderItem( 7 )
        item.setText( _translate( "MainWindowAdmin", "Email" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 0 )
        item.setText( _translate( "MainWindowAdmin", "Ap. Status" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 1 )
        item.setText( _translate( "MainWindowAdmin", "Patient Full Name" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 2 )
        item.setText( _translate( "MainWindowAdmin", "Patient Age" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 3 )
        item.setText( _translate( "MainWindowAdmin", "Patient Phone" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 4 )
        item.setText( _translate( "MainWindowAdmin", "Patient Gender" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 5 )
        item.setText( _translate( "MainWindowAdmin", "Patient Medical Condition" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 6 )
        item.setText( _translate( "MainWindowAdmin", "Prefered Days of Appointment" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 7 )
        item.setText( _translate( "MainWindowAdmin", "Time of Appointment" ) )
        item = self.tableWidgetAppointment.horizontalHeaderItem( 8 )
        item.setText( _translate( "MainWindowAdmin", "Patient Email" ) )
        self.ShowApButton.setText( _translate( "MainWindowAdmin", "Show Appointment" ) )
        self.ShowInfoButton.setText( _translate( "MainWindowAdmin", "Show Information" ) )
        self.LogOutButton.setText( _translate( "MainWindowAdmin", "Log Out" ) )
        self.label.setText( _translate( "MainWindowAdmin", "Full Name:" ) )
        self.label_5.setText( _translate( "MainWindowAdmin", "Age:" ) )
        self.label_6.setText( _translate( "MainWindowAdmin", "Phone #:" ) )
        self.label_7.setText( _translate( "MainWindowAdmin", "Gender:" ) )
        self.label_8.setText( _translate( "MainWindowAdmin", "Medical Condition:" ) )
        self.label_9.setText( _translate( "MainWindowAdmin", "Prefered Day:" ) )
        self.label_10.setText( _translate( "MainWindowAdmin", "Prefered Time:" ) )
        self.label_11.setText( _translate( "MainWindowAdmin", "Email:" ) )
        self.Gender.setItemText( 1, _translate( "MainWindowAdmin", "Male" ) )
        self.Gender.setItemText( 2, _translate( "MainWindowAdmin", "Female" ) )
        self.Gender.setItemText( 3, _translate( "MainWindowAdmin", "Other" ) )
        self.PreferDay.setItemText( 1, _translate( "MainWindowAdmin", "Saturday" ) )
        self.PreferDay.setItemText( 2, _translate( "MainWindowAdmin", "Sunday" ) )
        self.PreferDay.setItemText( 3, _translate( "MainWindowAdmin", "Munday" ) )
        self.PreferDay.setItemText( 4, _translate( "MainWindowAdmin", "Tuesday" ) )
        self.PreferDay.setItemText( 5, _translate( "MainWindowAdmin", "Wednesday" ) )
        self.PreferDay.setItemText( 6, _translate( "MainWindowAdmin", "Thursday" ) )
        self.PreferDay.setItemText( 7, _translate( "MainWindowAdmin", "Friday" ) )
        self.UpdateButton.setText( _translate( "MainWindowAdmin", "Update" ) )
        self.DeleteButton.setText( _translate( "MainWindowAdmin", "Delete" ) )


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Patient_Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
