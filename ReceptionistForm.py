from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
class ReceptionistLogIn( object ):
    # Function for approval of appointments after the Approve button is clicked
    def ApproveApp(self):
        # Getting the info from field of PatientName for updating the appointments AppStatus
        Name = self.PatientName.text()
        db = sqlite3.connect("project.db")
        # Update Appointment if it matches with the Name
        db.execute("update Appointments set AppStatus='Approved' where FullName = "+"'"+Name+"'")
        db.commit() # save
        # Selecting everything from appointments and view it in tableWidgets
        result = db.execute("select * from Appointments")
        self.tableWidgetAppointment.setRowCount( 0 )
        # Using two for loops to insert the data into tableWidgets
        for RowNum, RowDATA in enumerate( result ):
            self.tableWidgetAppointment.insertRow( RowNum ) # adding row number
            for ColumnNum, ColumnData in enumerate( RowDATA ):
                self.tableWidgetAppointment.setItem( RowNum, ColumnNum,
                                                     QtWidgets.QTableWidgetItem( str( ColumnData ) ) ) # col Data is Appointment
        db.close()
        self.PatientName.clear() # Clearing Patient Name when it is done
    # Function for Denying Appoinments
    def DenyApp(self):
        # Getting the Name from the user
        Name = self.PatientName.text()
        db = sqlite3.connect( "project.db" )
        # Updating the AppStatus to Denied if it matches with the name
        db.execute("update Appointments set AppStatus='Denied' where FullName = "+"'"+Name+"'")
        db.commit()
        # Selecting everything after updating Appointment to show it in tableWidget
        result = db.execute( "select * from Appointments" )
        self.tableWidgetAppointment.setRowCount( 0 )
        # Using two for loops to insert the data into Rows and columns
        for RowNum, RowDATA in enumerate( result ):
            self.tableWidgetAppointment.insertRow( RowNum ) # Inserting Row Get_Number
            for ColumnNum, ColumnData in enumerate( RowDATA ):
                self.tableWidgetAppointment.setItem( RowNum, ColumnNum,
                                                     QtWidgets.QTableWidgetItem( str( ColumnData ) ) )
        db.close()
        self.PatientName.clear() # Clearing Patient Name after it is donw
    # Function to view all the appointments
    def ShowAppointments(self):
        db = sqlite3.connect("project.db")
        # selecting everything from appointment table and using for loop to go over them and insert them into tableWidget
        result = db.execute("select * from Appointments")
        self.tableWidgetAppointment.setRowCount( 0 )
        # Using two for loops to insert the data into Rows and columns
        for RowNum, RowDATA in enumerate( result ):
            self.tableWidgetAppointment.insertRow( RowNum )
            for ColumnNum, ColumnData in enumerate( RowDATA ):
                self.tableWidgetAppointment.setItem( RowNum, ColumnNum,
                                                     QtWidgets.QTableWidgetItem( str( ColumnData ) ) )
        db.close()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindowAdmin")
        MainWindow.resize(702, 363)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ApproveButton = QtWidgets.QPushButton(self.centralwidget)
        self.ApproveButton.setGeometry(QtCore.QRect(260, 280, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ApproveButton.setFont(font)
        self.ApproveButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.ApproveButton.setObjectName("ApproveButton")
        self.ApproveButton.clicked.connect(self.ApproveApp)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 10, 211, 111))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Logo.png"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 111, 211, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tableWidgetAppointment = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidgetAppointment.setGeometry(QtCore.QRect(0, 140, 701, 121))
        self.tableWidgetAppointment.setObjectName("tableWidgetAppointment")
        self.tableWidgetAppointment.setColumnCount(9)
        self.tableWidgetAppointment.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setBackground(QtGui.QColor(85, 170, 255))
        self.tableWidgetAppointment.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidgetAppointment.setHorizontalHeaderItem(8, item)
        self.ShowAppButton = QtWidgets.QPushButton(self.centralwidget)
        self.ShowAppButton.setGeometry(QtCore.QRect(570, 262, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.ShowAppButton.setFont(font)
        self.ShowAppButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.ShowAppButton.setObjectName("ShowAppButton")
        self.ShowAppButton.clicked.connect(self.ShowAppointments)
        self.LogOutButton = QtWidgets.QPushButton(self.centralwidget)
        self.LogOutButton.setGeometry(QtCore.QRect(3, 1, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.LogOutButton.setFont(font)
        self.LogOutButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.LogOutButton.setObjectName("LogOutB")
        self.LogOutButton.clicked.connect(QtWidgets.qApp.quit)
        self.DenyButton = QtWidgets.QPushButton(self.centralwidget)
        self.DenyButton.setGeometry(QtCore.QRect(400, 280, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.DenyButton.setFont(font)
        self.DenyButton.setStyleSheet("background-color: rgb(85, 170, 255);")
        self.DenyButton.setObjectName("DenyButton")
        self.DenyButton.clicked.connect(self.DenyApp)
        self.PatientName = QtWidgets.QLineEdit(self.centralwidget)
        self.PatientName.setGeometry(QtCore.QRect(100, 280, 131, 31))
        self.PatientName.setObjectName("PatientName")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 278, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 702, 21))
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
        self.ApproveButton.setText(_translate("MainWindowAdmin", "Approve"))
        self.label_3.setText(_translate("MainWindowAdmin", "Appointments"))
        item = self.tableWidgetAppointment.horizontalHeaderItem(0)
        item.setText(_translate("MainWindowAdmin", "Ap. Status"))
        item = self.tableWidgetAppointment.horizontalHeaderItem(1)
        item.setText(_translate("MainWindowAdmin", "Patient Full Name"))
        item = self.tableWidgetAppointment.horizontalHeaderItem(2)
        item.setText(_translate("MainWindowAdmin", "Patient Age"))
        item = self.tableWidgetAppointment.horizontalHeaderItem(3)
        item.setText(_translate("MainWindowAdmin", "Patient Phone"))
        item = self.tableWidgetAppointment.horizontalHeaderItem(4)
        item.setText(_translate("MainWindowAdmin", "Patient Gender"))
        item = self.tableWidgetAppointment.horizontalHeaderItem(5)
        item.setText(_translate("MainWindowAdmin", "Pateint Medical Condition"))
        item = self.tableWidgetAppointment.horizontalHeaderItem(6)
        item.setText(_translate("MainWindowAdmin", "Prefered Days of Appointment"))
        item = self.tableWidgetAppointment.horizontalHeaderItem(7)
        item.setText(_translate("MainWindowAdmin", "Time of Appointment"))
        item = self.tableWidgetAppointment.horizontalHeaderItem(8)
        item.setText(_translate("MainWindowAdmin", "Email"))
        self.ShowAppButton.setText(_translate("MainWindowAdmin", "Show Appointments"))
        self.LogOutButton.setText(_translate("MainWindowAdmin", "Log Out"))
        self.DenyButton.setText(_translate("MainWindowAdmin", "Deny"))
        self.label.setText(_translate("MainWindowAdmin", "Patient Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ReceptionistLogIn()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
