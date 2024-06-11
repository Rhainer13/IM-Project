# This Python file uses the following encoding: utf-8
import sys, psycopg2

from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QHBoxLayout, QPushButton, QDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
from ui_admin import Ui_AdminPage
from ui_cartDialog import Ui_CartDialog
from ui_addProductDialog import Ui_AddProductDialog
from ui_detailsDialog import Ui_DetailsDialog
from ui_deleteProductDialog import Ui_DeleteProductDialog

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

class AdminPage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AdminPage()
        self.ui.setupUi(self)

        # load inventory table
        self.loadInventoryTable()
        self.loadPurchaseHistoryTable()

        # navigation buttons
        self.ui.inventoryButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.historyButton.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.viewOrderButton.clicked.connect(self.openCartDialog)

        # inventory pane buttons
        self.ui.addProductButton.clicked.connect(self.openAddProductDialog)

    def loadInventoryTable(self):
        self.connection = psycopg2.connect(database="test_3",
                                           user="postgres",
                                           host="localhost",
                                           password="p05tgr35ql",
                                           port=5432)

        self.cursor = self.connection.cursor()
        self.command =  """
                            select inv_id, prod_id, name, inv_pc_part, price, inv_qty
                            from(
                                select inv_id, cpu_id as prod_id, name, inv_pc_part, price, inv_qty from inventory natural join cpu
                                union
                                select inv_id, ram_id as prod_id, name, inv_pc_part, price, inv_qty from inventory natural join ram
                                union
                                select inv_id, mb_id as prod_id, name, inv_pc_part, price, inv_qty from inventory natural join motherboard
                            )
                            order by inv_id asc
                        """
        
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchall()
        
        self.ui.inventoryTable.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.ui.inventoryTable.insertRow(row_number)
            for column_number, column_data in enumerate(row_data[2:]):
                self.ui.inventoryTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))

            # Create a QWidget to hold buttons
            button_widget = QWidget()
            button_layout = QHBoxLayout(button_widget)
            button_layout.setContentsMargins(0, 0, 0, 0)
            button_widget.setLayout(button_layout)

            # Add 'details' button
            edit_button = QPushButton("Details")
            edit_button.clicked.connect(lambda _, r=row_data: self.details(r))
            button_layout.addWidget(edit_button)            

            # Set the widget with buttons in the cell
            self.ui.inventoryTable.setCellWidget(row_number, len(row_data)-2, button_widget)

            # Create a QWidget to hold buttons
            button_widget = QWidget()
            button_layout = QHBoxLayout(button_widget)
            button_layout.setContentsMargins(0, 0, 0, 0)
            button_widget.setLayout(button_layout)

            # Add 'order' button
            edit_button = QPushButton("Order")
            edit_button.clicked.connect(lambda _, r=row_data: self.order(r))
            button_layout.addWidget(edit_button)

            # Add Edit button
            edit_button = QPushButton("Edit")
            edit_button.clicked.connect(lambda _, r=row_data: self.open_edit_product_dialog(r))
            button_layout.addWidget(edit_button)

            # Add Delete button
            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda _, r=row_data: self.openDeleteProductDialog(r))
            button_layout.addWidget(delete_button)

            # Set the widget with buttons in the cell
            self.ui.inventoryTable.setCellWidget(row_number, len(row_data)-1, button_widget)

        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def loadPurchaseHistoryTable(self):
        self.connection = psycopg2.connect(database="test_3",
                                           user="postgres",
                                           host="localhost",
                                           password="p05tgr35ql",
                                           port=5432)

        self.cursor = self.connection.cursor()
        self.command =  """
                            select 
                                ord_date, cust_name, prod_name, pc_part, prod_price, quantity, total
                            from 
                                ordered_items
                            order by 
                                ord_date
                        """
        
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchall()
        
        self.ui.purchaseHistoryTable.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.ui.purchaseHistoryTable.insertRow(row_number)
            for column_number, column_data in enumerate(row_data):
                self.ui.purchaseHistoryTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))

        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def openCartDialog(self):
        self.cartDialog = CartDialog()
        self.cartDialog.exec()
        self.loadPurchaseHistoryTable()

    def openAddProductDialog(self):
        self.addProductDialog = AddProductDialog()
        self.addProductDialog.exec()
        self.loadInventoryTable()

    def details(self, r):
        self.detailsDialog = DetailsDialog(r)
        self.detailsDialog.exec()

    def order(self, r):
        # print(r)

        # for query purposes
        self.inv_id = r[0]

        self.connection = psycopg2.connect(database="test_3",
                                            user="postgres",
                                            host="localhost",
                                            password="p05tgr35ql",
                                            port=5432)

        self.cursor = self.connection.cursor()
        self.command =  f"""
                            insert into cart(inv_id)
                            values
                            ({self.inv_id});
                        """
        
        self.cursor.execute(self.command)

        self.connection.commit()
        self.cursor.close()
        self.connection.close()

    def openDeleteProductDialog(self, r):
        self.deleteProductDialog = DeleteProductDialog(r)
        self.deleteProductDialog.exec()
        self.loadInventoryTable()

# Dialogs
class AddProductDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddProductDialog()
        self.ui.setupUi(self)

        # changes the form when the dropdown is changed
        self.ui.pcPartDropdown.currentIndexChanged.connect(self.changeForm)

        # confirm and cancel buttons
        self.ui.confirmButton.clicked.connect(self.addProduct)
        self.ui.cancelButton.clicked.connect(lambda: self.close())

    def changeForm(self):
        self.pc_part = self.ui.pcPartDropdown.currentText()

        match self.pc_part:
            case 'CPU':
                self.ui.stackedWidget.setCurrentIndex(0)
            case 'RAM':
                self.ui.stackedWidget.setCurrentIndex(1)
            case 'MOTHERBOARD':
                self.ui.stackedWidget.setCurrentIndex(2)

    def addProduct(self):
        self.pc_part = self.ui.pcPartDropdown.currentText()
        self.name = self.ui.name.text()
        self.price = self.ui.price.value()
        self.qty = self.ui.quantity.value()

        match self.pc_part:
            case 'CPU':
                self.core_count = self.ui.coreCount.value()

                self.connection = psycopg2.connect(database="test_3",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

                self.cursor = self.connection.cursor()
                self.command =  f"""
                                    insert into cpu(name, price, core_count)
                                    values
                                    ('{self.name}', {self.price}, {self.core_count});

                                    update inventory
                                    set inv_qty = {self.qty}
                                    where cpu_id = (select MAX(cpu_id) from cpu);
                                """
                
                self.cursor.execute(self.command)

                self.connection.commit()
                self.cursor.close()
                self.connection.close()

                self.close()
            case 'RAM':
                self.size = int(self.ui.size.currentText())

                self.connection = psycopg2.connect(database="test_3",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

                self.cursor = self.connection.cursor()
                
                self.command =  f"""
                                    insert into ram(name, price, size)
                                    values
                                    ('{self.name}', {self.price}, {self.size});

                                    update inventory
                                    set inv_qty = {self.qty}
                                    where ram_id = (select MAX(ram_id) from ram);
                                """
                
                self.cursor.execute(self.command)

                self.connection.commit()
                self.cursor.close()
                self.connection.close()

                self.close()
            case 'MOTHERBOARD':
                self.form_factor = self.ui.formFactor.currentText()

                self.connection = psycopg2.connect(database="test_3",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

                self.cursor = self.connection.cursor()
                
                self.command =  f"""
                                    insert into motherboard(name, price, form_factor)
                                    values
                                    ('{self.name}', {self.price}, '{self.form_factor}');

                                    update inventory
                                    set inv_qty = {self.qty}
                                    where mb_id = (select MAX(mb_id) from motherboard);
                                """
                
                self.cursor.execute(self.command)

                self.connection.commit()
                self.cursor.close()
                self.connection.close()

                self.close()

class DetailsDialog(QDialog):
    def __init__(self, r, parent=None):
        super().__init__(parent)
        self.ui = Ui_DetailsDialog()
        self.ui.setupUi(self)

        # for transaction purposes
        self.prod_id = r[1]
        self.pc_part = r[3]

        # close button
        self.ui.closeButton.clicked.connect(lambda: self.close())

        match self.pc_part:
            case 'CPU':
                self.ui.stackedWidget.setCurrentIndex(0)
                self.result = self.query(table=self.pc_part, tableId='cpu_id', idValue=self.prod_id)

                self.ui.name.setText(self.result[1])                
                self.ui.price.setText(str(self.result[2]))                
                self.ui.coreCount.setText(str(self.result[3]))                
            case 'RAM':
                self.ui.stackedWidget.setCurrentIndex(1)
                self.result = self.query(table=self.pc_part, tableId='ram_id', idValue=self.prod_id)

                self.ui.name.setText(self.result[1])                
                self.ui.price.setText(str(self.result[2]))                
                self.ui.size.setText(str(self.result[3]))      
            case 'MOTHERBOARD':
                self.ui.stackedWidget.setCurrentIndex(2)
                self.result = self.query(table=self.pc_part, tableId='mb_id', idValue=self.prod_id)

                self.ui.name.setText(self.result[1])                
                self.ui.price.setText(str(self.result[2]))                
                self.ui.formFactor.setText(self.result[3])      

    def query(self, table, tableId, idValue):
        self.connection = psycopg2.connect(database="test_3",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

        self.cursor = self.connection.cursor()
        
        self.command =  f"""
                            select * from {table} where {tableId} = {idValue}; 
                        """
        
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchone()

        self.connection.commit()
        self.cursor.close()
        self.connection.close()

        return self.result

class DeleteProductDialog(QDialog):
    def __init__(self, r, parent=None):
        super().__init__(parent)
        self.ui = Ui_DeleteProductDialog()
        self.ui.setupUi(self)
        
        # for transaction purposes
        self.prod_id = r[1]
        self.pc_part = r[3]

        # change to appropriate form
        self.changeForm()

        # confirm and cancel buttons
        self.ui.confirmButton.clicked.connect(self.deleteProduct)
        self.ui.cancelButton.clicked.connect(lambda: self.close())

    def changeForm(self,):
        match self.pc_part:
            case 'CPU':
                self.ui.stackedWidget.setCurrentIndex(0)

                self.result = self.query(table=self.pc_part, tableId='cpu_id', idValue=self.prod_id)

                self.ui.name.setText(self.result[1])
                self.ui.price.setText(str(self.result[2]))
                self.ui.coreCount.setText(str(self.result[3]))
            case 'RAM':
                self.ui.stackedWidget.setCurrentIndex(1)

                self.result = self.query(table=self.pc_part, tableId='ram_id', idValue=self.prod_id)

                self.ui.name.setText(self.result[1])
                self.ui.price.setText(str(self.result[2]))
                self.ui.size.setText(str(self.result[3]))
            case 'MOTHERBOARD':
                self.ui.stackedWidget.setCurrentIndex(2)

                self.result = self.query(table=self.pc_part, tableId='mb_id', idValue=self.prod_id)

                self.ui.name.setText(self.result[1])
                self.ui.price.setText(str(self.result[2]))
                self.ui.formFactor.setText(str(self.result[3]))
    
    def query(self, table, tableId, idValue):
        self.connection = psycopg2.connect(database="test_3",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

        self.cursor = self.connection.cursor()
        
        self.command =  f"""
                            select * from {table} where {tableId} = {idValue}; 
                        """
        
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchone()

        self.connection.commit()
        self.cursor.close()
        self.connection.close()

        return self.result
    
    def deleteProduct(self):
        match self.pc_part:
            case 'CPU':
                tableId = 'cpu_id'
            case 'RAM':
                tableId = 'ram_id'
            case 'MOTHERBOARD':
                tableId = 'mb_id'

        self.connection = psycopg2.connect(database="test_3",
                                        user="postgres",
                                        host="localhost",
                                        password="p05tgr35ql",
                                        port=5432)

        self.cursor = self.connection.cursor()
        self.command =  f"""
                            delete from {self.pc_part} where {tableId} = {self.prod_id};  
                        """
        
        self.cursor.execute(self.command)

        self.connection.commit()
        self.cursor.close()
        self.connection.close()

        self.close()

class CartDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_CartDialog()
        self.ui.setupUi(self)

        # load cart table
        self.loadCartTable()

        # confirm and cancel buttons
        self.ui.confirmButton.clicked.connect(self.confirmOrder)
        self.ui.cancelButton.clicked.connect(self.clearCart)

    def loadCartTable(self):
        self.connection = psycopg2.connect(database="test_3",
                                           user="postgres",
                                           host="localhost",
                                           password="p05tgr35ql",
                                           port=5432)

        self.cursor = self.connection.cursor()
        self.command =  """
                            select cart_id, name, price, cart_qty
                            from(
                                select cart_id, name, price, cart_qty from cart natural join inventory natural join cpu
                                union all
                                select cart_id, name, price, cart_qty from cart natural join inventory natural join ram
                                union all
                                select cart_id, name, price, cart_qty from cart natural join inventory natural join motherboard
                            )
                            order by cart_id
                        """
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchall()
        
        self.ui.cartTable.setRowCount(0)

        for row_number, row_data in enumerate(self.result):
            self.ui.cartTable.insertRow(row_number)
            for column_number, column_data in enumerate(row_data[1:]):
                self.ui.cartTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))

            # Create a QWidget to hold buttons
            button_widget = QWidget()
            button_layout = QHBoxLayout(button_widget)
            button_layout.setContentsMargins(0, 0, 0, 0)
            button_widget.setLayout(button_layout)

            # Add '+' button
            edit_button = QPushButton("+")
            edit_button.clicked.connect(lambda _, r=row_data: self.increase(r))
            button_layout.addWidget(edit_button)

            # Add '-' button
            edit_button = QPushButton("-")
            edit_button.clicked.connect(lambda _, r=row_data: self.decrease(r))
            button_layout.addWidget(edit_button)

            # Add Delete button
            delete_button = QPushButton("Remove Item")
            delete_button.clicked.connect(lambda _, r=row_data: self.remove(r))
            button_layout.addWidget(delete_button)

            # Set the widget with buttons in the cell
            self.ui.cartTable.setCellWidget(row_number, len(row_data)-1, button_widget)

        self.connection.commit()
        self.cursor.close()
        self.connection.close()
    
    def increase(self, r):
        # print(r)

        # for query purposes
        self.cart_id = r[0]

        self.connection = psycopg2.connect(database="test_3",
                                           user="postgres",
                                           host="localhost",
                                           password="p05tgr35ql",
                                           port=5432)

        self.cursor = self.connection.cursor()

        self.command =  f"""
                            UPDATE 
                                CART
                            SET
                                CART_QTY = CART_QTY + 1
                            WHERE
                                CART_ID = {self.cart_id};
                        """
        self.cursor.execute(self.command)

        self.connection.commit()
        
        self.cursor.close()
        self.connection.close()

        self.loadCartTable()

    def decrease(self, r):
        # print(r)
        
        # for query purposes
        self.cart_id = r[0]

        self.connection = psycopg2.connect(database="test_3",
                                           user="postgres",
                                           host="localhost",
                                           password="p05tgr35ql",
                                           port=5432)

        self.cursor = self.connection.cursor()

        self.command =  f"""
                            UPDATE 
                                CART
                            SET
                                CART_QTY = CART_QTY - 1
                            WHERE
                                CART_ID = {self.cart_id};
                        """
        self.cursor.execute(self.command)

        self.connection.commit()
        
        self.cursor.close()
        self.connection.close()

        self.loadCartTable()

    def remove(self, r):
        # for query purposes
        self.cart_id = r[0]

        self.connection = psycopg2.connect(database="test_3",
                                           user="postgres",
                                           host="localhost",
                                           password="p05tgr35ql",
                                           port=5432)

        self.cursor = self.connection.cursor()

        self.command =  f"""
                            DELETE FROM
                                CART
                            WHERE
                                CART_ID = {self.cart_id};
                        """
        self.cursor.execute(self.command)

        self.connection.commit()
        
        self.cursor.close()
        self.connection.close()

        self.loadCartTable()

    def confirmOrder(self):
        self.custName = self.ui.customerName.text()
        self.connection = psycopg2.connect(database="test_3",
                                           user="postgres",
                                           host="localhost",
                                           password="p05tgr35ql",
                                           port=5432)

        self.cursor = self.connection.cursor()

        self.command =  f"""
                            INSERT INTO ORDERED_ITEMS(CART_ID, ORD_DATE, CUST_NAME, PROD_NAME, PC_PART, PROD_PRICE, QUANTITY, TOTAL)
                            SELECT CART_ID, NOW(), '{self.custName}', NAME, INV_PC_PART, PRICE, CART_QTY, TOTAL
                            FROM(
                                SELECT CART_ID, NAME, INV_PC_PART, PRICE, CART_QTY, (PRICE * CART_QTY) AS TOTAL FROM CART NATURAL JOIN INVENTORY NATURAL JOIN CPU
                                UNION ALL
                                SELECT CART_ID, NAME, INV_PC_PART, PRICE, CART_QTY, (PRICE * CART_QTY) FROM CART NATURAL JOIN INVENTORY NATURAL JOIN RAM
                                UNION ALL
                                SELECT CART_ID, NAME, INV_PC_PART, PRICE, CART_QTY, (PRICE * CART_QTY) FROM CART NATURAL JOIN INVENTORY NATURAL JOIN MOTHERBOARD
                            )
                        """
        self.cursor.execute(self.command)

        self.connection.commit()
        
        self.cursor.close()
        self.connection.close()

        self.ui.customerName.clear()
        self.clearCart()
        self.loadCartTable()

    def clearCart(self):
        self.connection = psycopg2.connect(database="test_3",
                                           user="postgres",
                                           host="localhost",
                                           password="p05tgr35ql",
                                           port=5432)

        self.cursor = self.connection.cursor()

        self.command =  f"""
                            DELETE FROM CART;
                        """
        self.cursor.execute(self.command)

        self.connection.commit()
        
        self.cursor.close()
        self.connection.close()

        self.loadCartTable()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # widget = Widget()
    # widget.show()

    adminPage = AdminPage()
    adminPage.show()
    
    sys.exit(app.exec())