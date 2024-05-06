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

from ui_dashboard import Ui_Dashboard
from ui_addItemDialog import Ui_AddProductDialog
from ui_addEmployeeDialog import Ui_AddEmployeeDialog
from ui_serviceReportDialog import Ui_ServiceReportDialog
from ui_purchaseReportDialog import Ui_PurchaseReportDialog

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

# windows
class Dashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dashboard()
        self.ui.setupUi(self)

        self.showMaximized()

        self.ui.serviceReportButton.clicked.connect(self.openServiceReportDialog)
        self.ui.purchaseReportButton.clicked.connect(self.openPurchaseReportDialog)
        self.ui.logOutButton

        # pre-load all table data
        self.loadProductTable()
        self.loadEmployeeTable()

        # inventory tab
        self.ui.inventoryButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.addProductButton.clicked.connect(self.openAddProductDialog)
        self.ui.inventoryTabSearchBar.textChanged.connect(self.searchProduct)
        # self.ui.searchButton_2.clicked.connect(self.searchEmployee)
        
        # employee tab
        self.ui.employeeButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.addEmployeeButton.clicked.connect(self.openAddEmployeeDialog)
        self.ui.employeeTabSearchBar.textChanged.connect(self.searchEmployee)
        # self.ui.searchButton_2.clicked.connect(self.searchEmployee)

        # history tab
        self.ui.historyButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))

    # service report dialog
    def openServiceReportDialog(self):
        self.ServiceReportDialog = ServiceReportDialog()
        self.ServiceReportDialog.exec()

    # purchase dialog
    def openPurchaseReportDialog(self):
        self.PurchaseReportDialog = PurchaseReportDialog()
        self.PurchaseReportDialog.exec()

    # inventory functions
    def openAddProductDialog(self):
        self.AddProductDialog = AddProductDialog()
        self.AddProductDialog.exec()
        self.loadProductTable()

    def loadProductTable(self):
        self.connection = psycopg2.connect(     database    = "ptt_sample",
                                                user        = "postgres",
                                                host        = "localhost",
                                                password    = "p05tgr35ql",
                                                port        = 5432)

        self.cursor = self.connection.cursor()

        self.command =  """
                            SELECT * FROM INVENTORY;
                        """

        self.cursor.execute(self.command)

        self.result = self.cursor.fetchall()

        self.ui.productTable.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.ui.productTable.insertRow(row_number) # wako kasabot ari
            for column_number, column_data in enumerate(row_data):
                self.ui.productTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data))) # wako kassabot sa qtablewidgetitem

        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def searchProduct(self):
        self.search = self.ui.inventoryTabSearchBar.text()

        self.connection = psycopg2.connect(     database    = "ptt_sample",
                                                user        = "postgres",
                                                host        = "localhost",
                                                password    = "p05tgr35ql",
                                                port        = 5432)

        self.cursor = self.connection.cursor()

        self.command = f"""   
                            SELECT *
                            FROM INVENTORY
                            WHERE PROD_NAME LIKE '%{self.search}%';
                        """

        self.cursor.execute(self.command)

        self.result = self.cursor.fetchall()

        self.ui.productTable.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.ui.productTable.insertRow(row_number) # wako kasabot ari
            for column_number, column_data in enumerate(row_data):
                self.ui.productTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data))) # wako kassabot sa qtablewidgetitem

        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    # employee functions
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
        self.search = self.ui.employeeTabSearchBar.text()

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

# dialogs
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
        
class AddProductDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddProductDialog()
        self.ui.setupUi(self)

        self.ui.confirmButton.clicked.connect(self.addProductToDatabase)
        self.ui.cancelButton.clicked.connect(lambda: self.close())

    def addProductToDatabase(self):
        self.prodName = self.ui.productNameInput.text()
        self.prodQty = self.ui.quantityInput.text()
        self.prodPrice = self.ui.priceInput.text()
        self.prodCat = self.ui.categoryDropdown.currentText()
        
        # print(self.prodCat)
        
        self.connection = psycopg2.connect(     database    = "ptt_sample",
                                                user        = "postgres",
                                                host        = "localhost",
                                                password    = "p05tgr35ql",
                                                port        = 5432)

        self.cursor = self.connection.cursor()

        self.command = f"""   INSERT INTO INVENTORY (PROD_NAME, PROD_QTY, PROD_PRICE, PROD_CAT)
                           VALUES
                            ('{self.prodName}', '{self.prodQty}', '{self.prodPrice}', '{self.prodCat}');
                        """

        self.cursor.execute(self.command)

        self.connection.commit()
   
        self.cursor.close()
        self.connection.close()

        self.close()
        
class ServiceReportDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ServiceReportDialog()
        self.ui.setupUi(self)

        self.ui.cancelButton.clicked.connect(lambda: self.close())

class PurchaseReportDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_PurchaseReportDialog()
        self.ui.setupUi(self)

        self.ui.cancelButton.clicked.connect(lambda: self.close())

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # widget = Widget()
    # widget.show()

    # EmployeeWindow = EmployeeWindow()
    # EmployeeWindow.show()

    Dashboard = Dashboard()
    Dashboard.show()

    sys.exit(app.exec())