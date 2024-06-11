# This Python file uses the following encoding: utf-8

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

import sys
import psycopg2

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QTableWidgetItem, QDialog
from PySide6.QtCore import Signal
from ui_logInWindow import Ui_LogInWindow
from ui_managerDashboard import Ui_ManagerDashboard

from ui_addProductDialog import Ui_AddProductDialog
from ui_updateProductDialog import Ui_UpdateProductDialog
from ui_deleteProductDialog import Ui_DeleteProductDialog

from ui_addEmployeeDialog import Ui_AddEmployeeDialog
from ui_updateEmployeeDialog import Ui_UpdateEmployeeDialog
from ui_deleteEmployeeDialog import Ui_DeleteEmployeeDialog

'''
from ui_form import Ui_Widget

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
'''

# windows
class LogInWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_LogInWindow()
        self.ui.setupUi(self)

        self.ui.logInButton.clicked.connect(self.verifyUser)

    def verifyUser(self):
        if self.ui.usernameInput.text() == 'admin' and self.ui.passwordInput.text() == 'admin':
            self.ManagerDashboard = ManagerDashboard()
            self.ManagerDashboard.show()
            
            self.ui.usernameInput.setText('')
            self.ui.passwordInput.setText('')

            self.close()
        else:
            print('incorrect input')

class ManagerDashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ManagerDashboard()
        self.ui.setupUi(self)

        # load tables
        self.loadProductTable()
        self.loadEmployeeTable()

        # navigation panel buttons
        self.ui.inventoryButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.employeeButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.historyButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.logOutButton.clicked.connect(self.logOut)

        # inventory tab
        self.ui.searchBar.textChanged.connect(self.searchInventory)
        self.ui.addProductButton.clicked.connect(self.openAddProductDialog)
        self.ui.refreshButton.clicked.connect(self.loadProductTable)

        # employee tab
        self.ui.addEmployeeButton.clicked.connect(self.openAddEmployeeDialog)

    def searchInventory(self):
        self.searched = self.ui.searchBar.text()

        self.connection = psycopg2.connect(database="ptt_sample",
                                           user="postgres",
                                           host="localhost",
                                           password="p05tgr35ql",
                                           port=5432)

        self.cursor = self.connection.cursor()

        self.command =  f"""
                            SELECT * 
                            FROM 
                                INVENTORY
                            WHERE 
                                PROD_NAME ILIKE '%{self.searched}%' 
                                OR PROD_CAT ILIKE '%{self.searched}%'
                            ORDER 
                                BY PROD_ID;
                        """
        
        self.cursor.execute(self.command)
        
        self.result = self.cursor.fetchall()

        self.ui.productTable.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.ui.productTable.insertRow(row_number)
            update_deleteButton = buttonWidget(row_number, row_data, self)
            
            for column_number, column_data in enumerate(row_data):
                self.ui.productTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))
                self.ui.productTable.setCellWidget(row_number,5,update_deleteButton)
                self.ui.productTable.setRowHeight(row_number, 50)

        self.connection.close()
    
    def loadProductTable(self):
        self.connection = psycopg2.connect(database="ptt_sample",
                                           user="postgres",
                                           host="localhost",
                                           password="p05tgr35ql",
                                           port=5432)

        self.cursor = self.connection.cursor()
        self.command =  """
                            SELECT * 
                            FROM
                                INVENTORY
                            ORDER BY 
                                PROD_ID;
                        """
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchall()
        self.ui.productTable.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.ui.productTable.insertRow(row_number)
            update_deleteButton = buttonWidget(row_number, row_data, self)

            for column_number, column_data in enumerate(row_data):
                self.ui.productTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))    
                self.ui.productTable.setCellWidget(row_number,5,update_deleteButton)
                self.ui.productTable.setRowHeight(row_number, 50)

        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def openAddProductDialog(self):
        self.AddProductDialog = AddProductDialog()
        self.AddProductDialog.exec()
        self.loadProductTable()

    def loadEmployeeTable(self):
        self.connection = psycopg2.connect(database="ptt_sample",
                                           user="postgres",
                                           host="localhost",
                                           password="p05tgr35ql",
                                           port=5432)

        self.cursor = self.connection.cursor()
        self.command =  f"""
                            SELECT * 
                            FROM
                                EMPLOYEE
                            ORDER BY 
                                EMP_ID;
                        """
        
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchall()
        self.ui.employeeTable.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.ui.employeeTable.insertRow(row_number)
            updateButton = employeeTableButtons(row_number, row_data, self)
            
            for column_number, column_data in enumerate(row_data):
                self.ui.employeeTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))    
                self.ui.employeeTable.setCellWidget(row_number, 6, updateButton)
                self.ui.employeeTable.setRowHeight(row_number, 50)

        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def openAddEmployeeDialog(self):
        self.AddEmployeeDialog = AddEmployeeDialog()
        self.AddEmployeeDialog.exec()
        self.loadEmployeeTable()

    def logOut(self):
        self.LogInWindow = LogInWindow
        self.LogInWindow.show()
        
        self.close()

# dialogs
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
        self.prodCat = self.ui.categoryChoice.currentText()
        
        self.connection = psycopg2.connect(     database    = "ptt_sample",
                                                user        = "postgres",
                                                host        = "localhost",
                                                password    = "p05tgr35ql",
                                                port        = 5432)

        self.cursor = self.connection.cursor()

        self.command = f"""
                           INSERT INTO INVENTORY (PROD_NAME, PROD_QTY, PROD_PRICE, PROD_CAT)
                           VALUES
                            ('{self.prodName}', '{self.prodQty}', '{self.prodPrice}', '{self.prodCat}');
                        """

        self.cursor.execute(self.command)

        self.connection.commit()
   
        self.cursor.close()
        self.connection.close()
        self.close()

class UpdateProductDialog(QDialog):
    data_update = Signal()
    def __init__(self, product_id, parent=None):
        super().__init__(parent)
        self.ui = Ui_UpdateProductDialog()
        self.ui.setupUi(self)

        self.prod_id = product_id

        self.ui.confirmButton.clicked.connect(self.updateProductInDatabase)
        self.ui.cancelButton.clicked.connect(lambda: self.close())

    def updateProductInDatabase(self):
        self.prodName = self.ui.productNameInput.text()
        self.prodQty = self.ui.quantityInput.text()
        self.prodPrice = self.ui.priceInput.text()
        self.prodCat = self.ui.categoryChoice.currentText()
        
        self.connection = psycopg2.connect(     database    = "ptt_sample",
                                                user        = "postgres",
                                                host        = "localhost",
                                                password    = "p05tgr35ql",
                                                port        = 5432)

        self.cursor = self.connection.cursor()

        self.command = f"""
                            UPDATE INVENTORY
                            SET 
                                PROD_NAME = '{self.prodName}',
                                PROD_QTY = '{self.prodQty}',
                                PROD_PRICE = '{self.prodPrice}',
                                PROD_CAT = '{self.prodCat}'
                            WHERE
                                PROD_ID = {self.prod_id};
                        """

        self.cursor.execute(self.command)

        self.connection.commit()

        self.cursor.close()
        self.connection.close()
        self.close()

        self.data_update.emit()

class DeleteProductDialog(QDialog):
    data_update = Signal()
    def __init__(self, product_id, product_name, parent=None):
        super().__init__(parent)
        self.ui = Ui_DeleteProductDialog()
        self.ui.setupUi(self)

        self.product_id = product_id
        self.product_name = product_name

        self.ui.label.setText(f"Are you sure you want to delete {self.product_name}?")

        self.ui.confirmButton.clicked.connect(self.deleteProductInDatabase)
        self.ui.cancelButton.clicked.connect(lambda: self.close())

    def deleteProductInDatabase(self):
        self.connection = psycopg2.connect(     database    = "ptt_sample",
                                                user        = "postgres",
                                                host        = "localhost",
                                                password    = "p05tgr35ql",
                                                port        = 5432)

        self.cursor = self.connection.cursor()

        self.command = f"""
                            DELETE FROM INVENTORY
                            WHERE
                                PROD_ID = {self.product_id};
                        """

        self.cursor.execute(self.command)

        self.connection.commit()
   
        self.cursor.close()
        self.connection.close()
        self.close()

        self.data_update.emit()

class AddEmployeeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddEmployeeDialog()
        self.ui.setupUi(self)

        self.ui.confirmButton.clicked.connect(self.addEmployeeToDatabase)
        self.ui.cancelButton.clicked.connect(lambda: self.close())
    
    def addEmployeeToDatabase(self):
        self.empName = self.ui.employeeNameInput.text()
        self.dateHired = self.ui.dateHiredInput.text()
        self.address = self.ui.addressInput.text()
        self.contact = self.ui.contactInput.text()
        self.charge = self.ui.chargeInput.text()

        self.connection = psycopg2.connect(     database    = "ptt_sample",
                                                user        = "postgres",
                                                host        = "localhost",
                                                password    = "p05tgr35ql",
                                                port        = 5432)

        self.cursor = self.connection.cursor()

        self.command = f"""
                           INSERT INTO EMPLOYEE (EMP_NAME, EMP_DATE_HIRED, EMP_ADDR, EMP_CONT, EMP_CHARGE)
                           VALUES
                            ('{self.empName}', '{self.dateHired}', '{self.address}', '{self.contact}', '{self.charge}');
                        """

        self.cursor.execute(self.command)

        self.connection.commit()
   
        self.cursor.close()
        self.connection.close()
        self.close()

class UpdateEmployeeDialog(QDialog):
    data_update = Signal()
    def __init__(self, emp_id, parent=None):
        super().__init__(parent)
        self.ui = Ui_UpdateEmployeeDialog()
        self.ui.setupUi(self)

        self.emp_id = emp_id

        self.ui.confirmButton.clicked.connect(self.updateEmployeeInDatabase)
        self.ui.cancelButton.clicked.connect(lambda: self.close())

    def updateEmployeeInDatabase(self):
        self.empName = self.ui.employeeNameInput.text()
        self.dateHired = self.ui.dateHiredInput.text()
        self.address = self.ui.addressInput.text()
        self.contact = self.ui.contactInput.text()
        self.charge = self.ui.chargeInput.text()

        self.connection = psycopg2.connect(     database    = "ptt_sample",
                                                user        = "postgres",
                                                host        = "localhost",
                                                password    = "p05tgr35ql",
                                                port        = 5432)

        self.cursor = self.connection.cursor()

        self.command = f"""
                            UPDATE EMPLOYEE
                            SET
                                EMP_NAME = '{self.empName}',    
                                EMP_DATE_HIRED = '{self.dateHired}',
                                EMP_ADDR = '{self.address}',    
                                EMP_CONT = '{self.contact}',    
                                EMP_CHARGE = '{self.charge}'
                            WHERE
                                EMP_ID = '{self.emp_id}';   
                        """

        self.cursor.execute(self.command)

        self.connection.commit()
   
        self.cursor.close()
        self.connection.close()
        self.close()

        self.data_update.emit()

class DeleteEmployeeDialog(QDialog):
    data_update = Signal()
    def __init__(self, emp_id, emp_name, parent=None):
        super().__init__(parent)
        self.ui = Ui_DeleteEmployeeDialog()
        self.ui.setupUi(self)

        self.emp_id = emp_id
        self.emp_name = emp_name

        self.ui.label.setText(f"Are you sure you want to delete {self.emp_name}?")

        self.ui.confirmButton.clicked.connect(self.deleteEmployeeInDatabase)
        self.ui.cancelButton.clicked.connect(lambda: self.close())

    def deleteEmployeeInDatabase(self):
        self.connection = psycopg2.connect(     database    = "ptt_sample",
                                                user        = "postgres",
                                                host        = "localhost",
                                                password    = "p05tgr35ql",
                                                port        = 5432)

        self.cursor = self.connection.cursor()

        self.command = f"""
                            DELETE FROM EMPLOYEE
                            WHERE
                                EMP_ID = {self.emp_id};
                        """

        self.cursor.execute(self.command)

        self.connection.commit()
   
        self.cursor.close()
        self.connection.close()
        self.close()

        self.data_update.emit()

# for action buttons
class buttonWidget(QWidget):
    def __init__(self, row_number, row_data, manager):
        super().__init__()
        self.row_number = row_number
        self.row_data = row_data
        self.manager = manager

        self.product_id = self.row_data[0]
        self.product_name = self.row_data[1]

        layout = QHBoxLayout(self)
        
        self.update_button = QPushButton("Update", self)
        self.update_button.setStyleSheet("background-color: blue;")
        self.update_button.setFixedSize(61,31)
        self.update_button.clicked.connect(self.openUpdateProductDialog)

        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setStyleSheet("background-color: red;")
        self.delete_button.setFixedSize(61, 31)
        self.delete_button.clicked.connect(self.openDeleteProductDialog)

        layout.addWidget(self.update_button)
        layout.addWidget(self.delete_button)

    def openUpdateProductDialog(self):
        self.UpdateProductDialog = UpdateProductDialog(self.product_id)
        self.UpdateProductDialog.data_update.connect(self.manager.loadProductTable)
        self.UpdateProductDialog.exec()

    def openDeleteProductDialog(self):
        self.DeleteProductDialog = DeleteProductDialog(self.product_id, self.product_name)
        self.DeleteProductDialog.data_update.connect(self.manager.loadProductTable)
        self.DeleteProductDialog.exec()

class employeeTableButtons(QWidget):
    def __init__(self, row_number, row_data, manager):
        super().__init__()
        self.row_number = row_number
        self.row_data = row_data
        self.manager = manager

        self.emp_id = self.row_data[0]
        self.emp_name = self.row_data[1]

        layout = QHBoxLayout(self)
        
        self.update_button = QPushButton("Update", self)
        self.update_button.setStyleSheet("background-color: blue;")
        self.update_button.setFixedSize(61,31)
        self.update_button.clicked.connect(self.openUpdateEmployeeDialog)

        self.delete_button = QPushButton("Delete", self)
        self.delete_button.setStyleSheet("background-color: red;")
        self.delete_button.setFixedSize(61, 31)
        self.delete_button.clicked.connect(self.openDeleteEmployeeDialog)

        layout.addWidget(self.update_button)
        layout.addWidget(self.delete_button)

    def openUpdateEmployeeDialog(self):
        self.UpdateEmployeeDialog = UpdateEmployeeDialog(self.emp_id)
        self.UpdateEmployeeDialog.data_update.connect(self.manager.loadEmployeeTable)
        self.UpdateEmployeeDialog.exec()

    def openDeleteEmployeeDialog(self):
        self.DeleteEmployeeDialog = DeleteEmployeeDialog(self.emp_id, self.emp_name)
        self.DeleteEmployeeDialog.data_update.connect(self.manager.loadEmployeeTable)
        self.DeleteEmployeeDialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    '''
    widget = Widget()
    widget.show()
    '''

    LogInWindow = LogInWindow()
    LogInWindow.show()

    sys.exit(app.exec())