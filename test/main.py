# This Python file uses the following encoding: utf-8
import sys
import psycopg2

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

'''
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
'''

# from ui_table import Ui_EmployeeWindow
from ui_employeeDashboard import Ui_EmployeeDashboard
from ui_addEmployeeDialog import Ui_AddEmployeeDialog

'''
class EmployeeWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_EmployeeWindow()
        self.ui.setupUi(self)

        # load database button
        self.ui.loadTable.clicked.connect(self.loadDatabase)
        self.ui.addRow.clicked.connect(self.addToDatabase)
        self.ui.removeRow.clicked.connect(self.removeFromDatabase)

    def loadDatabase(self):
        connection = psycopg2.connect(  database    = "ptt_sample",
                                        user        = "postgres",
                                        host        = "localhost",
                                        password    = "p05tgr35ql",
                                        port        = 5432)

        cursor = connection.cursor()

        command = """SELECT * FROM EMPLOYEE"""

        cursor.execute(command)

        result = cursor.fetchall()

        self.ui.employeeTable.setRowCount(0)

        for row_number, row_data in enumerate(result):
            self.ui.employeeTable.insertRow(row_number) # wako kasabot ari
            for column_number, column_data in enumerate(row_data):
                self.ui.employeeTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data))) # wako kassabot sa qtablewidgetitem

        connection.close()

    def addToDatabase(self):
        connection = psycopg2.connect(  database    = "ptt_sample",
                                        user        = "postgres",
                                        host        = "localhost",
                                        password    = "p05tgr35ql",
                                        port        = 5432)

        cursor = connection.cursor()

        command = f"""   INSERT INTO EMPLOYEE (EMP_ID, EMP_NAME, EMP_DATE_HIRED, EMP_ADDR, EMP_CONT, EMP_CHARGE)
                        VALUES
                        ({self.ui.rowToDelete.text()}, 'person 3', CURRENT_DATE, 'addr 3', 33333333333, 300.00);
                  """

        cursor.execute(command)

        connection.commit()
        
        cursor.close()
        connection.close()

    def removeFromDatabase(self):
        connection = psycopg2.connect(  database    = "ptt_sample",
                                        user        = "postgres",
                                        host        = "localhost",
                                        password    = "p05tgr35ql",
                                        port        = 5432)

        cursor = connection.cursor()

        command = f"""   DELETE FROM EMPLOYEE
                        WHERE EMP_ID = {self.ui.rowToDelete.text()};
                  """

        cursor.execute(command)

        connection.commit()
        
        cursor.close()
        connection.close()
'''

class EmployeeDashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_EmployeeDashboard()
        self.ui.setupUi(self)

        self.loadEmployeeTable()
        self.ui.addEmployeeButton.clicked.connect(self.openAddEmployeeDialog)
        # self.ui.searchButton_2.clicked.connect(self.searchEmployee)
        self.ui.inventoryButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.employeeButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.searchBar_2.textChanged.connect(self.searchEmployee)

        # self.ui.employeeTable. # wa gitiwas ni niez kaboang sad nimo oi

    def loadEmployeeTable(self):
        self.connection = psycopg2.connect(     database    = "ptt_sample",
                                                user        = "postgres",
                                                host        = "localhost",
                                                password    = "p05tgr35ql",
                                                port        = 5432)

        self.cursor = self.connection.cursor()

        self.command =  """
                            SELECT * FROM EMPLOYEE
                            ORDER BY EMP_ID;
                        """

        self.cursor.execute(self.command)

        self.result = self.cursor.fetchall()

        self.ui.employeeTable.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.ui.employeeTable.insertRow(row_number) # wako kasabot ari
            for column_number, column_data in enumerate(row_data):
                self.ui.employeeTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data))) # wako kassabot sa qtablewidgetitem

        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def openAddEmployeeDialog(self):
        self.AddEmployeeDialog = AddEmployeeDialog()
        self.AddEmployeeDialog.exec()
        self.loadEmployeeTable()

    def searchEmployee(self):
        self.search = self.ui.searchBar_2.text()

        self.connection = psycopg2.connect(     database    = "ptt_sample",
                                                user        = "postgres",
                                                host        = "localhost",
                                                password    = "p05tgr35ql",
                                                port        = 5432)

        self.cursor = self.connection.cursor()

        self.command = f"""   
                            SELECT *
                            FROM EMPLOYEE
                            WHERE EMP_NAME LIKE '%{self.search}%';
                        """

        self.cursor.execute(self.command)

        self.result = self.cursor.fetchall()

        self.ui.employeeTable.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.ui.employeeTable.insertRow(row_number) # wako kasabot ari
            for column_number, column_data in enumerate(row_data):
                self.ui.employeeTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data))) # wako kassabot sa qtablewidgetitem

        self.connection.commit()
        self.cursor.close()
        self.connection.close()

class AddEmployeeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddEmployeeDialog()
        self.ui.setupUi(self)

        self.ui.confirmButton.clicked.connect(self.addEmployeeToDatabase)
        self.ui.cancelButton.clicked.connect(lambda: self.close())

    def addEmployeeToDatabase(self):
        self.emp_name = self.ui.employeeNameInput.text()
        self.emp_date_hired = self.ui.dateHiredInput.text()
        self.emp_addr = self.ui.addressInput.text()
        self.emp_cont = self.ui.contactNumberInput.text()
        self.emp_charge = self.ui.chargeInput.text()

        self.connection = psycopg2.connect(     database    = "ptt_sample",
                                                user        = "postgres",
                                                host        = "localhost",
                                                password    = "p05tgr35ql",
                                                port        = 5432)

        self.cursor = self.connection.cursor()

        self.command = f"""   INSERT INTO EMPLOYEE (EMP_NAME, EMP_DATE_HIRED, EMP_ADDR, EMP_CONT, EMP_CHARGE)
                           VALUES
                            ('{self.emp_name}', '{self.emp_date_hired}', '{self.emp_addr}', {self.emp_cont}, {self.emp_charge});
                        """

        self.cursor.execute(self.command)

        self.connection.commit()
   
        self.cursor.close()
        self.connection.close()

        self.close()
        

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # widget = Widget()
    # widget.show()

    # EmployeeWindow = EmployeeWindow()
    # EmployeeWindow.show()

    EmployeeDashboard = EmployeeDashboard()
    EmployeeDashboard.show()

    sys.exit(app.exec())