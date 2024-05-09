# This Python file uses the following encoding: utf-8

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

import sys
import psycopg2

from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QTableWidgetItem, QDialog
from ui_logInWindow import Ui_LogInWindow
from ui_managerDashboard import Ui_ManagerDashboard

from ui_addProductDialog import Ui_AddProductDialog
from ui_updateProductDialog import Ui_UdpateProductDialog

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

        # load product table
        self.loadProductTable()

        # navigation panel buttons
        self.ui.logOutButton.clicked.connect(self.logOut)

        # inventory tab
        self.ui.addProductButton.clicked.connect(self.openAddProductDialog)
        self.ui.refreshButton.clicked.connect(self.loadProductTable)
    
    def loadProductTable(self):
        self.connection = psycopg2.connect(database="ptt_sample",
                                           user="postgres",
                                           host="localhost",
                                           password="p05tgr35ql",
                                           port=5432)

        self.cursor = self.connection.cursor()
        self.command =  """
                            SELECT * FROM INVENTORY
                            ORDER BY PROD_ID;
                        """
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchall()
        self.ui.productTable.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.ui.productTable.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.ui.productTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))
                
                update_deleteButton = buttonWidget(row_number, row_data)
                self.ui.productTable.setCellWidget(row_number,5,update_deleteButton)
                self.ui.productTable.setRowHeight(row_number, 50)

        self.connection.close()

    def openAddProductDialog(self):
        self.AddProductDialog = AddProductDialog()
        self.AddProductDialog.exec()
        self.loadProductTable()

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
    def __init__(self, product_id, parent=None):
        super().__init__(parent)
        self.ui = Ui_UdpateProductDialog()
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

# for action buttons
class buttonWidget(QWidget):
    def __init__(self, row_number, row_data):
        super().__init__()
        self.row_number = row_number
        self.row_data = row_data

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
        # self.delete_button.clicked.connect(self.delete)

        layout.addWidget(self.update_button)
        layout.addWidget(self.delete_button)

    def openUpdateProductDialog(self):
        self.UpdateProductDialog = UpdateProductDialog(self.product_id)
        self.UpdateProductDialog.exec()

        # print(self.product_id)
        # print(self.product_name)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)

    '''
    widget = Widget()
    widget.show()
    '''

    LogInWindow = LogInWindow()
    LogInWindow.show()

    sys.exit(app.exec())
