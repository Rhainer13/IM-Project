# This Python file uses the following encoding: utf-8
import sys, psycopg2

from PySide6.QtWidgets import QApplication, QWidget, QDialog, QTableWidgetItem, QPushButton, QHBoxLayout, QHeaderView, QComboBox
from datetime import datetime

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py

from form import Ui_Widget
from admin import Ui_AdminPage
from addProductDialog import Ui_AddProductDialog
from detailsDialog import Ui_DetailsDialog
from editProductDialog import Ui_EditProductDialog
from deleteProductDialog import Ui_DeleteProductDialog
from orderDialog import Ui_OrderDialog
from purchaseReceiptDialog import Ui_PurchaseReceiptDialog

from addStaffDialog import Ui_AddStaffDialog
from deleteStaffDialog import Ui_DeleteStaffDialog

from serviceDialog import Ui_ServiceDialog

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

        # 
        self.showMaximized()

        # inventory columns
        self.allColumn = self.ui.inventoryTable.horizontalHeader()
        self.allColumn.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        # staff columns
        self.allColumn = self.ui.staffTable.horizontalHeader()
        self.allColumn.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # purchase history columns
        self.allColumn = self.ui.purchaseHistoryTable.horizontalHeader()
        self.allColumn.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # service history columns
        self.allColumn = self.ui.serviceHistory.horizontalHeader()
        self.allColumn.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        
        # load all tables
        self.loadInventoryTable()
        self.loadStaffTable()
        self.loadPurchaseHistory()
        self.loadServiceHistory()

        # navigation panel
        self.ui.inventory.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.staff.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.history.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.viewOrder.clicked.connect(self.openOrderDialog)
        self.ui.service.clicked.connect(self.openServiceDialog)
        self.ui.logOut.clicked.connect(lambda: self.close())

        # inventory panel
        self.ui.addProduct.clicked.connect(self.openAddProductDialog)

        # staff panel
        self.ui.addStaff.clicked.connect(self.openAddStaffDialog)

    def loadInventoryTable(self):
        self.conn = psycopg2.connect(database="test_5",
                                        user="postgres",
                                        host="localhost",
                                        password="p05tgr35ql",
                                        port=5432)

        self.cursor = self.conn.cursor()
        self.command =  """
                            select 
                                inv_id, prod_id, prod_cat, prod_brand, prod_name, prod_price, inv_qty
                            from
                            (
                                select inv_id, prod_id, prod_cat, prod_brand, prod_name, prod_price, inv_qty from inventory natural join product natural join cpu
                                union all
                                select inv_id, prod_id, prod_cat, prod_brand, prod_name, prod_price, inv_qty from inventory natural join product natural join ram
                                union all
                                select inv_id, prod_id, prod_cat, prod_brand, prod_name, prod_price, inv_qty from inventory natural join product natural join motherboard
                            )
                            order by 
                                prod_id
                        """
        
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchall()
        
        self.ui.inventoryTable.setRowCount(len(self.result))

        for row_number, row_data in enumerate(self.result):
            for column_number, column_data in enumerate(row_data[3:]):
                self.ui.inventoryTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))
            
            # Create a QWidget to hold order, edit, delete buttons
            button_widget = QWidget()
            button_layout = QHBoxLayout(button_widget)
            button_layout.setContentsMargins(0, 0, 0, 0)
            button_widget.setLayout(button_layout)

            # Add 'details' button
            details_button = QPushButton("Details")
            details_button.clicked.connect(lambda _, r=row_data: self.openDetailsDialog(r))
            button_layout.addWidget(details_button)

            # Add 'order' button
            order_button = QPushButton("Order")
            order_button.clicked.connect(lambda _, r=row_data: self.order(r))
            button_layout.addWidget(order_button)

            # Add Edit button
            edit_button = QPushButton("Edit")
            edit_button.clicked.connect(lambda _, r=row_data: self.openEditProductDialog(r))
            button_layout.addWidget(edit_button)

            # Add Delete button
            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda _, r=row_data: self.openDeleteProductDialog(r))
            button_layout.addWidget(delete_button)

            # Set the widget with buttons in the cell
            self.ui.inventoryTable.setCellWidget(row_number, len(row_data)-3, button_widget)

        self.cursor.close()
        self.conn.close()

    def loadStaffTable(self):
        self.conn = psycopg2.connect(database="test_5",
                                        user="postgres",
                                        host="localhost",
                                        password="p05tgr35ql",
                                        port=5432)

        self.cursor = self.conn.cursor()
        self.command =  """
                            select
                                staff_id, staff_fname, staff_lname, staff_mob_num, staff_addr, staff_hire_date
                            from
                                staff;
                        """
        
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchall()
        
        self.ui.staffTable.setRowCount(len(self.result))

        for row_number, row_data in enumerate(self.result):
            for column_number, column_data in enumerate(row_data[1:]):
                if column_number == 4:  # Assuming the first column is the date
                    # Convert the date string to a datetime object
                    date_object = datetime.strptime(str(column_data), '%Y-%m-%d')
                    # Format the datetime object to the desired string format
                    formatted_date = date_object.strftime('%B %d, %Y')
                    self.ui.staffTable.setItem(row_number, column_number, QTableWidgetItem(formatted_date))
                else:
                    self.ui.staffTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))
            
            # Create a QWidget to hold order, edit, delete buttons
            button_widget = QWidget()
            button_layout = QHBoxLayout(button_widget)
            button_layout.setContentsMargins(0, 0, 0, 0)
            button_widget.setLayout(button_layout)

            # Add Edit button
            edit_button = QPushButton("Edit")
            edit_button.clicked.connect(lambda _, r=row_data: self.openEditStaffDialog(r))
            button_layout.addWidget(edit_button)

            # Add Delete button
            delete_button = QPushButton("Delete")
            delete_button.clicked.connect(lambda _, r=row_data: self.openDeleteStaffDialog(r))
            button_layout.addWidget(delete_button)

            # Set the widget with buttons in the cell
            self.ui.staffTable.setCellWidget(row_number, len(row_data)-1, button_widget)

        self.cursor.close()
        self.conn.close()

    def loadPurchaseHistory(self):
        self.conn = psycopg2.connect(database="test_5",
                                        user="postgres",
                                        host="localhost",
                                        password="p05tgr35ql",
                                        port=5432)

        self.cursor = self.conn.cursor()
        
        self.command =  """
                            select
                                distinct comp_date, comp_cust_name
                            from
                                completed_orders
                            order by
                                comp_date desc;
                        """
        
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchall()
        
        self.ui.purchaseHistoryTable.setRowCount(len(self.result))

        for row_number, row_data in enumerate(self.result):
            for column_number, column_data in enumerate(row_data):
                if column_number == 0:  # Assuming the first column is the date
                    # Convert the date string to a datetime object
                    date_object = datetime.strptime(str(column_data), '%Y-%m-%d %H:%M:%S.%f')
                    # Format the datetime object to the desired string format
                    formatted_date = date_object.strftime('%B %d, %Y %H:%M')
                    self.ui.purchaseHistoryTable.setItem(row_number, column_number, QTableWidgetItem(formatted_date))
                else:
                    self.ui.purchaseHistoryTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))

            # Create a QWidget to hold order, edit, delete buttons
            button_widget = QWidget()
            button_layout = QHBoxLayout(button_widget)
            button_layout.setContentsMargins(0, 0, 0, 0)
            button_widget.setLayout(button_layout)

            # Add 'receipt' button
            receipt_button = QPushButton("View Receipt")
            receipt_button.clicked.connect(lambda _, r=row_data: self.openPurchaseReceiptDialog(r))
            button_layout.addWidget(receipt_button)

            # Set the widget with buttons in the cell
            self.ui.purchaseHistoryTable.setCellWidget(row_number, len(row_data), button_widget)

        self.cursor.close()
        self.conn.close()

    def loadServiceHistory(self):
        self.conn = psycopg2.connect(database="test_5",
                                        user="postgres",
                                        host="localhost",
                                        password="p05tgr35ql",
                                        port=5432)

        self.cursor = self.conn.cursor()
        
        self.command =  """
                            select
                                serv_det_date, serv_det_cust_name, staff_fname,  dev_type, serv_type, serv_det_total_fee
                            from
                                service_details natural join staff
                                natural join device 
                                natural join service
                            order by
                                serv_det_date desc;
                        """
        
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchall()
        
        self.ui.serviceHistory.setRowCount(len(self.result))

        for row_number, row_data in enumerate(self.result):
            for column_number, column_data in enumerate(row_data):
                self.ui.serviceHistory.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))

        self.cursor.close()
        self.conn.close()

    def openAddProductDialog(self):
        self.addProductDialog = AddProductDialog()
        self.addProductDialog.exec()
        self.loadInventoryTable()

    def openDetailsDialog(self, r):
        self.detailsDialog = DetailsDialog(r)
        self.detailsDialog.exec()

    def order(self, r):
        # for query purposes
        self.inv_id = r[0]

        self.conn = psycopg2.connect(database="test_5",
                                        user="postgres",
                                        host="localhost",
                                        password="p05tgr35ql",
                                        port=5432)

        self.cursor = self.conn.cursor()

        # Check if the item exists in the cart
        self.cursor.execute("SELECT 1 FROM cart WHERE inv_id = %s", (self.inv_id,))
        exists = self.cursor.fetchone()

        # If the item exists, update the quantity
        if exists:
            self.cursor.execute("SELECT inv_qty FROM inventory WHERE inv_id = %s", (self.inv_id,))
            inv_qty = self.cursor.fetchone()[0]
            
            self.cursor.execute("SELECT cart_qty FROM cart WHERE inv_id = %s", (self.inv_id,))
            cart_qty = self.cursor.fetchone()[0]
            
            if cart_qty < inv_qty:
                self.cursor.execute("UPDATE cart SET cart_qty = cart_qty + 1 WHERE inv_id = %s", (self.inv_id,))
            else:
                print('no')
        else:
            # If the item doesn't exist, insert it into the cart
            self.cursor.execute("INSERT INTO cart(inv_id) VALUES (%s)", (self.inv_id,))
        
        self.cursor.execute(self.command)
        self.conn.commit()

        self.cursor.close()
        self.conn.close()

    def openOrderDialog(self):
        self.orderDialog = OrderDialog()
        self.orderDialog.exec()
        self.loadInventoryTable()
        self.loadPurchaseHistory()

    def openEditProductDialog(self, r):
        self.editProductDialog = EditProductDialog(r)
        self.editProductDialog.exec()
        self.loadInventoryTable()

    def openDeleteProductDialog(self, r):
        self.deleteProductDialog = DeleteProductDialog(r)
        self.deleteProductDialog.exec()
        self.loadInventoryTable()

    # staff panel
    def openAddStaffDialog(self):
        self.addStaffDialog = AddStaffDialog()
        self.addStaffDialog.exec()
        self.loadStaffTable()

    def openDeleteStaffDialog(self, r):
        self.deleteStaffDialog = DeleteStaffDialog(r)
        self.deleteStaffDialog.exec()
        self.loadStaffTable()

    # history panel
    def openPurchaseReceiptDialog(self, r):
        self.purchaseReceiptDialog = PurchaseReceiptDialog(r)
        self.purchaseReceiptDialog.exec()

    # service button
    def openServiceDialog(self):
        self.serviceDialog = ServiceDialog()
        self.serviceDialog.exec()
        self.loadServiceHistory()

# dialogs
class AddProductDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddProductDialog()
        self.ui.setupUi(self)

        # change form
        self.ui.category.currentIndexChanged.connect(self.changeForm)

        # confirm and cancel buttons
        self.ui.confirm.clicked.connect(self.addProduct)
        self.ui.cancel.clicked.connect(lambda: self.close())

    def changeForm(self):
        self.category = self.ui.category.currentText()

        match self.category:
            case 'CPU':
                self.ui.stackedWidget.setCurrentIndex(0)
            case 'RAM':
                self.ui.stackedWidget.setCurrentIndex(1)
            case 'Motherboard':
                self.ui.stackedWidget.setCurrentIndex(2)

    def addProduct(self):
        self.category = self.ui.category.currentText()

        self.name = self.ui.name.text()
        self.price = self.ui.price.value()
        self.quantity = self.ui.quantity.value()

        match self.category:
            case 'CPU':
                self.brand = self.ui.cpuBrand.currentText()
                self.coreCount = self.ui.coreCount.value()

                self.conn = psycopg2.connect(database="test_5",
                                        user="postgres",
                                        host="localhost",
                                        password="p05tgr35ql",
                                        port=5432)

                self.cursor = self.conn.cursor()

                self.command =  f"""
                                    insert into 
                                        product(prod_brand, prod_name, prod_price, prod_cat)
                                    values
                                        ('{self.brand}', '{self.name}', {self.price}, '{self.category}');

                                    update 
                                        cpu
                                    set 
                                        cpu_core_count = {self.coreCount}
                                    where
                                        prod_id = (select max(prod_id) from product);
                                """
                
                self.cursor.execute(self.command)

                self.command =  f"""
                                    update
                                        inventory
                                    set
                                        inv_qty = {self.quantity}
                                    where
                                        inv_id = (select max(inv_id) from inventory);
                                """
                
                self.cursor.execute(self.command)

                self.conn.commit()

                self.cursor.close()
                self.conn.close()

                self.close()
                
            case 'RAM':
                self.brand = self.ui.ramBrand.currentText()
                self.ramSize = int(self.ui.ramSize.currentText())

                self.conn = psycopg2.connect(database="test_5",
                                        user="postgres",
                                        host="localhost",
                                        password="p05tgr35ql",
                                        port=5432)

                self.cursor = self.conn.cursor()
                self.command =  f"""
                                    insert into 
                                        product(prod_brand, prod_name, prod_price, prod_cat)
                                    values
                                        ('{self.brand}', '{self.name}', {self.price}, '{self.category}');

                                    update 
                                        ram
                                    set 
                                        ram_size = {self.ramSize}
                                    where
                                        prod_id = (select max(prod_id) from product);
                                """
                
                self.cursor.execute(self.command)

                self.command =  f"""
                                    update
                                        inventory
                                    set
                                        inv_qty = {self.quantity}
                                    where
                                        inv_id = (select max(inv_id) from inventory);
                                """
                
                self.cursor.execute(self.command)

                self.conn.commit()

                self.cursor.close()
                self.conn.close()

                self.close()

            case 'Motherboard':
                self.brand = self.ui.mbBrand.currentText()
                self.mbSize = self.ui.mbSize.currentText()

                self.conn = psycopg2.connect(database="test_5",
                                        user="postgres",
                                        host="localhost",
                                        password="p05tgr35ql",
                                        port=5432)

                self.cursor = self.conn.cursor()

                self.command =  f"""
                                    insert into 
                                        product(prod_brand, prod_name, prod_price, prod_cat)
                                    values
                                        ('{self.brand}', '{self.name}', {self.price}, '{self.category}');

                                    update 
                                        motherboard
                                    set 
                                        mb_size = '{self.mbSize}'
                                    where
                                        prod_id = (select max(prod_id) from product);
                                """
                
                self.cursor.execute(self.command)

                self.command =  f"""
                                    update
                                        inventory
                                    set
                                        inv_qty = {self.quantity}
                                    where
                                        inv_id = (select max(inv_id) from inventory);
                                """
                
                self.cursor.execute(self.command)

                self.conn.commit()

                self.cursor.close()
                self.conn.close()

                self.close()

class DetailsDialog(QDialog):
    def __init__(self, r, parent=None):
        super().__init__(parent)
        self.ui = Ui_DetailsDialog()
        self.ui.setupUi(self)

        # for query purposes
        self.prod_id = r[1]
        self.prod_cat = r[2]

        # set appropriate page and values
        match self.prod_cat:
            case 'CPU':
                self.ui.stackedWidget.setCurrentIndex(0)

                self.conn = psycopg2.connect(database="test_5",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

                self.cursor = self.conn.cursor()
                
                self.command =  f"""
                                    select 
                                        prod_cat, prod_brand, prod_name, prod_price, cpu_core_count 
                                    from 
                                        inventory 
                                        natural join product 
                                        natural join cpu
                                    where
                                        prod_id = {self.prod_id};
                                """
                
                self.cursor.execute(self.command)
                self.result = self.cursor.fetchone()

                self.cursor.close()
                self.conn.close()

                self.ui.category.setText(self.result[0])
                self.ui.cpuBrand.setText(self.result[1])
                self.ui.name.setText(self.result[2])
                self.ui.price.setText(str(self.result[3]))
                self.ui.coreCount.setText(str(self.result[4]))
            
            case 'RAM':
                self.ui.stackedWidget.setCurrentIndex(1)

                self.conn = psycopg2.connect(database="test_5",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

                self.cursor = self.conn.cursor()
                
                self.command =  f"""
                                    select 
                                        prod_cat, prod_brand, prod_name, prod_price, ram_size 
                                    from 
                                        inventory 
                                        natural join product 
                                        natural join ram
                                    where
                                        prod_id = {self.prod_id};
                                """
                
                self.cursor.execute(self.command)
                self.result = self.cursor.fetchone()

                self.cursor.close()
                self.conn.close()

                self.ui.category.setText(self.result[0])
                self.ui.ramBrand.setText(self.result[1])
                self.ui.name.setText(self.result[2])
                self.ui.price.setText(str(self.result[3]))
                self.ui.ramSize.setText(str(self.result[4]))

            case 'Motherboard':
                self.ui.stackedWidget.setCurrentIndex(2)

                self.conn = psycopg2.connect(database="test_5",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

                self.cursor = self.conn.cursor()
                
                self.command =  f"""
                                    select 
                                        prod_cat, prod_brand, prod_name, prod_price, mb_size 
                                    from 
                                        inventory 
                                        natural join product 
                                        natural join motherboard
                                    where
                                        prod_id = {self.prod_id};
                                """
                
                self.cursor.execute(self.command)
                self.result = self.cursor.fetchone()

                self.cursor.close()
                self.conn.close()

                self.ui.category.setText(self.result[0])
                self.ui.mbBrand.setText(self.result[1])
                self.ui.name.setText(self.result[2])
                self.ui.price.setText(str(self.result[3]))
                self.ui.mbSize.setText(str(self.result[4]))
        
        self.ui.close.clicked.connect(lambda: self.close())

class OrderDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_OrderDialog()
        self.ui.setupUi(self)

        # resize for all columns
        self.allColumns = self.ui.cartTable.horizontalHeader()
        self.allColumns.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)

        # load table
        self.loadCartTable()

        # confirm and cancel orders
        self.ui.confirmOrder.clicked.connect(self.confirmOrder)
        self.ui.cancelOrder.clicked.connect(self.cancelOrder)

    def loadCartTable(self):
        self.conn = psycopg2.connect(database="test_5",
                                        user="postgres",
                                        host="localhost",
                                        password="p05tgr35ql",
                                        port=5432)

        self.cursor = self.conn.cursor()

        self.command =  """
                            select 
                                inv_id, cart_id, prod_brand, prod_name, prod_cat, prod_price, cart_qty, (prod_price * cart_qty)
                            from(
                                select inv_id, cart_id, prod_brand, prod_name, prod_cat, prod_price, cart_qty from cart natural join inventory natural join product natural join cpu
                                union all
                                select inv_id, cart_id, prod_brand, prod_name, prod_cat, prod_price, cart_qty from cart natural join inventory natural join product natural join ram
                                union all
                                select inv_id, cart_id, prod_brand, prod_name, prod_cat, prod_price, cart_qty from cart natural join inventory natural join product natural join motherboard
                            )
                            order by
                                cart_id asc;
                        """
        
        self.cursor.execute(self.command)

        self.result = self.cursor.fetchall()
        
        self.ui.cartTable.setRowCount(len(self.result))

        for row_number, row_data in enumerate(self.result):
            for column_number, column_data in enumerate(row_data[2:]):
                self.ui.cartTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))
            
            # Create a QWidget to hold order, edit, delete buttons
            button_widget = QWidget()
            button_layout = QHBoxLayout(button_widget)
            button_layout.setContentsMargins(0, 0, 0, 0)
            button_widget.setLayout(button_layout)

            # Add '-' button
            decrease_button = QPushButton("-")
            decrease_button.clicked.connect(lambda _, r=row_data: self.decreaseQty(r))
            button_layout.addWidget(decrease_button)

            # Add '+' button
            increase_button = QPushButton("+")
            increase_button.clicked.connect(lambda _, r=row_data: self.increaseQty(r))
            button_layout.addWidget(increase_button)

            # Add Delete button
            remove_button = QPushButton("Remove Item")
            remove_button.clicked.connect(lambda _, r=row_data: self.removeFromCart(r))
            button_layout.addWidget(remove_button)

            # Set the widget with buttons in the cell
            self.ui.cartTable.setCellWidget(row_number, len(row_data)-2, button_widget)

        # for total
        self.command =  """
                            select
                                sum(prod_price * cart_qty)
                            from(
                                select prod_price, cart_qty from cart natural join inventory natural join product natural join cpu
                                union all
                                select prod_price, cart_qty from cart natural join inventory natural join product natural join ram
                                union all
                                select prod_price, cart_qty from cart natural join inventory natural join product natural join motherboard
                            );
                        """
        
        self.cursor.execute(self.command)
        
        self.result = self.cursor.fetchone()[0]

        if self.result:
            self.ui.total.setValue(self.result)
        else:
            self.ui.total.setValue(0)

        self.cursor.close()
        self.conn.close()

    def increaseQty(self, r):
        # for query purposes
        self.inv_id = r[0]

        self.conn = psycopg2.connect(database="test_5",
                                        user="postgres",
                                        host="localhost",
                                        password="p05tgr35ql",
                                        port=5432)

        self.cursor = self.conn.cursor()

        self.cursor.execute("SELECT inv_qty FROM inventory WHERE inv_id = %s", (self.inv_id,))
        inv_qty = self.cursor.fetchone()[0]
        
        self.cursor.execute("SELECT cart_qty FROM cart WHERE inv_id = %s", (self.inv_id,))
        cart_qty = self.cursor.fetchone()[0]
        
        if cart_qty < inv_qty:
            self.cursor.execute("UPDATE cart SET cart_qty = cart_qty + 1 WHERE inv_id = %s", (self.inv_id,))
        else:
            print('no')
        
        self.conn.commit()

        self.cursor.close()
        self.conn.close()

        self.loadCartTable()

    def decreaseQty(self, r):
        # for query purposes
        self.inv_id = r[0]

        self.conn = psycopg2.connect(database="test_5",
                                        user="postgres",
                                        host="localhost",
                                        password="p05tgr35ql",
                                        port=5432)

        self.cursor = self.conn.cursor()

        self.cursor.execute("SELECT cart_qty FROM cart WHERE inv_id = %s", (self.inv_id,))
        cart_qty = self.cursor.fetchone()[0]
        
        if cart_qty > 1:
            self.cursor.execute("UPDATE cart SET cart_qty = cart_qty - 1 WHERE inv_id = %s", (self.inv_id,))
        else:
            print('no')
        
        self.conn.commit()

        self.cursor.close()
        self.conn.close()

        self.loadCartTable()

    def removeFromCart(self, r):
        # for query purposes
        self.inv_id = r[0]

        self.conn = psycopg2.connect(database="test_5",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

        self.cursor = self.conn.cursor()
        
        self.command =  f"""
                            delete from
                                cart
                            where
                                inv_id = {self.inv_id};
                        """
        
        self.cursor.execute(self.command)

        self.conn.commit()

        self.cursor.close()
        self.conn.close()

        self.loadCartTable()

    def confirmOrder(self):
        self.custName = self.ui.customerName.text()
        
        self.connection = psycopg2.connect(database="test_5",
                                           user="postgres",
                                           host="localhost",
                                           password="p05tgr35ql",
                                           port=5432)

        self.cursor = self.connection.cursor()

        self.command =  f"""
                            insert into
                                completed_orders(comp_date, comp_cust_name, comp_prod_brand, comp_prod_name, comp_prod_cat, comp_prod_price, comp_qty, comp_total, inv_id)
                            select
                                now(), '{self.custName}', prod_brand, prod_name, prod_cat, prod_price, cart_qty, (prod_price * cart_qty), inv_id
                            from(
                                select prod_brand, prod_name, prod_cat, prod_price, cart_qty, inv_id from cart natural join inventory natural join product natural join cpu
                                union all
                                select prod_brand, prod_name, prod_cat, prod_price, cart_qty, inv_id from cart natural join inventory natural join product natural join ram
                                union all
                                select prod_brand, prod_name, prod_cat, prod_price, cart_qty, inv_id from cart natural join inventory natural join product natural join motherboard
                            )
                        """
        
        self.cursor.execute(self.command)

        self.connection.commit()
        
        self.cursor.close()
        self.connection.close()

        self.ui.customerName.clear()
        self.cancelOrder()
        self.loadCartTable()

    def cancelOrder(self):
        self.conn = psycopg2.connect(database="test_5",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

        self.cursor = self.conn.cursor()
        
        self.command =  f"""
                            delete from
                                cart;
                        """
        
        self.cursor.execute(self.command)

        self.conn.commit()

        self.cursor.close()
        self.conn.close()

        self.loadCartTable()

class EditProductDialog(QDialog):
    def __init__(self, r, parent=None):
        super().__init__(parent)
        self.ui = Ui_EditProductDialog()
        self.ui.setupUi(self)

        # for query purposes
        self.prod_id = r[1]
        self.prod_cat = r[2]

        # set values
        self.conn = psycopg2.connect(database="test_5",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

        self.cursor = self.conn.cursor()
        
        self.command =  f"""
                            select 
                                * 
                            from(
                                select prod_id, prod_cat, prod_brand, prod_name, prod_price, inv_qty  from inventory natural join product natural join cpu
                                union all
                                select prod_id, prod_cat, prod_brand, prod_name, prod_price, inv_qty from inventory natural join product natural join ram
                                union all
                                select prod_id, prod_cat, prod_brand, prod_name, prod_price, inv_qty from inventory natural join product natural join motherboard
                            )
                            where prod_id = {self.prod_id};
                        """
        
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchone()

        self.cursor.close()
        self.conn.close()

        self.ui.category.setText(self.result[1])
        self.ui.name.setText(self.result[3])
        self.ui.price.setValue(self.result[4])
        self.ui.quantity.setValue(self.result[5])

        # confirm and close buttons
        self.ui.confirm.clicked.connect(self.updateProduct)
        self.ui.cancel.clicked.connect(lambda: self.close())
    
    def updateProduct(self):
        self.name = self.ui.name.text()
        self.price = self.ui.price.value()
        self.quantity = self.ui.quantity.value()

        self.conn = psycopg2.connect(database="test_5",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

        self.cursor = self.conn.cursor()
        
        self.command =  f"""
                            update 
                                product
                            set 
                                prod_name = '{self.name}', prod_price = {self.price}
                            where
                                prod_id = {self.prod_id};

                            update
                                inventory
                            set
                                inv_qty = {self.quantity}
                            where
                                prod_id = {self.prod_id};
                        """
        
        self.cursor.execute(self.command)

        self.conn.commit()

        self.cursor.close()
        self.conn.close()

        self.close()

class DeleteProductDialog(QDialog):
    def __init__(self, r, parent=None):
        super().__init__(parent)
        self.ui = Ui_DeleteProductDialog()
        self.ui.setupUi(self)

        # for query purposes
        self.prod_id = r[1]
        self.prod_cat = r[2]

        # change to appropriate deletion form
        self.changeForm()
        
        # confirm and cancel buttons
        self.ui.confirm.clicked.connect(self.deleteProduct)
        self.ui.cancel.clicked.connect(lambda: self.close())
    
    def changeForm(self):
        match self.prod_cat:
            case 'CPU':
                self.ui.stackedWidget.setCurrentIndex(0)

                self.conn = psycopg2.connect(database="test_5",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

                self.cursor = self.conn.cursor()
                
                self.command =  f"""
                                    select 
                                        prod_cat, prod_brand, prod_name, prod_price, cpu_core_count 
                                    from 
                                        inventory 
                                        natural join product 
                                        natural join cpu
                                    where
                                        prod_id = {self.prod_id};
                                """
                
                self.cursor.execute(self.command)
                self.result = self.cursor.fetchone()

                self.cursor.close()
                self.conn.close()

                self.ui.category.setText(self.result[0])
                self.ui.cpuBrand.setText(self.result[1])
                self.ui.name.setText(self.result[2])
                self.ui.price.setText(str(self.result[3]))
                self.ui.coreCount.setText(str(self.result[4]))

            case 'RAM':
                self.ui.stackedWidget.setCurrentIndex(1)

                self.conn = psycopg2.connect(database="test_5",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

                self.cursor = self.conn.cursor()
                
                self.command =  f"""
                                    select 
                                        prod_cat, prod_brand, prod_name, prod_price, ram_size 
                                    from 
                                        inventory 
                                        natural join product 
                                        natural join ram
                                    where
                                        prod_id = {self.prod_id};
                                """
                
                self.cursor.execute(self.command)
                self.result = self.cursor.fetchone()

                self.cursor.close()
                self.conn.close()

                self.ui.category.setText(self.result[0])
                self.ui.ramBrand.setText(self.result[1])
                self.ui.name.setText(self.result[2])
                self.ui.price.setText(str(self.result[3]))
                self.ui.ramSize.setText(str(self.result[4]))

            case 'Motherboard':
                self.ui.stackedWidget.setCurrentIndex(2)

                self.conn = psycopg2.connect(database="test_5",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

                self.cursor = self.conn.cursor()
                
                self.command =  f"""
                                    select 
                                        prod_cat, prod_brand, prod_name, prod_price, mb_size 
                                    from 
                                        inventory 
                                        natural join product 
                                        natural join motherboard
                                    where
                                        prod_id = {self.prod_id};
                                """
                
                self.cursor.execute(self.command)
                self.result = self.cursor.fetchone()

                self.cursor.close()
                self.conn.close()

                self.ui.category.setText(self.result[0])
                self.ui.mbBrand.setText(self.result[1])
                self.ui.name.setText(self.result[2])
                self.ui.price.setText(str(self.result[3]))
                self.ui.mbSize.setText(str(self.result[4]))

    def deleteProduct(self):
        self.conn = psycopg2.connect(database="test_5",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

        self.cursor = self.conn.cursor()
        
        self.command =  f"""
                            delete from
                                product
                            where
                                prod_id = {self.prod_id};
                        """
        
        self.cursor.execute(self.command)

        self.conn.commit()

        self.cursor.close()
        self.conn.close()

        self.close()

class PurchaseReceiptDialog(QDialog):
    def __init__(self, r, parent=None):
        super().__init__(parent)
        self.ui = Ui_PurchaseReceiptDialog()
        self.ui.setupUi(self)

        # purchase receipt
        self.allColumn = self.ui.purchaseReceiptTable.horizontalHeader()
        self.allColumn.setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        # for query purposes
        self.comp_date = r[0]

        # close
        self.ui.close.clicked.connect(lambda: self.close())

        self.conn = psycopg2.connect(database="test_5",
                                                    user="postgres",
                                                    host="localhost",
                                                    password="p05tgr35ql",
                                                    port=5432)

        self.cursor = self.conn.cursor()
        
        # for table
        self.command =  f"""
                            select
                                comp_cust_name, comp_prod_brand, comp_prod_name, comp_prod_cat, comp_prod_price, comp_qty, comp_total
                            from
                                completed_orders
                            where
                                comp_date = '{self.comp_date}';
                        """
        
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchall()

        self.ui.purchaseReceiptTable.setRowCount(len(self.result))

        for row_number, row_data in enumerate(self.result):
            for column_number, column_data in enumerate(row_data[1:]):
                self.ui.purchaseReceiptTable.setItem(row_number, column_number, QTableWidgetItem(str(column_data)))

        # for total
        self.command =  f"""
                            select
                                sum(comp_total)
                            from
                                completed_orders
                            where
                                comp_date = '{self.comp_date}';
                        """
        
        self.cursor.execute(self.command)
        self.result = self.cursor.fetchone()[0]

        self.ui.total.setValue(self.result)

        self.cursor.close()
        self.conn.close()

class AddStaffDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AddStaffDialog()
        self.ui.setupUi(self)

        # confirm and cancel buttons
        self.ui.confirm.clicked.connect(self.addStaff)
        self.ui.cancel.clicked.connect(lambda: self.close())

    def addStaff(self):
        self.fname = self.ui.fname.text().upper()
        self.lname = self.ui.lname.text().upper()
        self.mobileNum = self.ui.mobileNum.text()
        self.address = self.ui.address.text().upper()
        self.dateHired = self.ui.dateHired.text()

        self.conn = psycopg2.connect(database="test_5",
                                        user="postgres",
                                        host="localhost",
                                        password="p05tgr35ql",
                                        port=5432)

        self.cursor = self.conn.cursor()

        self.command =  f"""
                            insert into
                                staff(staff_fname, staff_lname, staff_mob_num, staff_addr, staff_hire_date)
                            values
                                ('{self.fname}', '{self.lname}', '{self.mobileNum}', '{self.address}', '{self.dateHired}');
                        """
        
        self.cursor.execute(self.command)

        self.conn.commit()

        self.cursor.close()
        self.conn.close()

        self.close()

class DeleteStaffDialog(QDialog):
    def __init__(self, r, parent=None):
        super().__init__(parent)
        self.ui = Ui_DeleteStaffDialog()
        self.ui.setupUi(self)

        # for query purposes
        self.staffId = r[0]

        # set name to delete
        self.conn = psycopg2.connect(database="test_5",
                                    user="postgres",
                                    host="localhost",
                                    password="p05tgr35ql",
                                    port=5432)

        self.cursor = self.conn.cursor()
        
        self.command =  f"""
                            select
                                staff_fname, staff_lname
                            from
                                staff
                            where
                                staff_id = {self.staffId};
                        """
        
        self.cursor.execute(self.command)

        self.result = self.cursor.fetchone()

        self.ui.notification.setText(f'Are you sure you want to delete {self.result[0]} {self.result[1]}?')

        self.cursor.close()
        self.conn.close()

        # confirm and cancel buttons
        self.ui.confirm.clicked.connect(self.deleteStaff)
        self.ui.cancel.clicked.connect(lambda: self.close())

    def deleteStaff(self):
        self.conn = psycopg2.connect(database="test_5",
                                    user="postgres",
                                    host="localhost",
                                    password="p05tgr35ql",
                                    port=5432)

        self.cursor = self.conn.cursor()
        
        self.command =  f"""
                            delete from
                                staff
                            where
                                staff_id = {self.staffId};
                        """
        
        self.cursor.execute(self.command)

        self.conn.commit()

        self.cursor.close()
        self.conn.close()

        self.close()

class ServiceDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ServiceDialog()
        self.ui.setupUi(self)

        # load dropdown boxes
        self.loadDropdown()

        # confirm and cancel buttons
        self.ui.confirm.clicked.connect(self.confirmService)
        self.ui.cancel.clicked.connect(lambda: self.close())

    def loadDropdown(self):
        self.conn = psycopg2.connect(database="test_5",
                                    user="postgres",
                                    host="localhost",
                                    password="p05tgr35ql",
                                    port=5432)

        self.cursor = self.conn.cursor()

        # for device type
        self.command =  f"""
                            select
                                dev_id, dev_type
                            from
                                device;
                        """
        
        self.cursor.execute(self.command)

        self.result = self.cursor.fetchall()

        for data in self.result:
            self.devId = data[0]
            self.device = data[1]
            self.ui.device.addItem(self.device, self.devId)
        
        # for technician
        self.command =  f"""
                            select
                                staff_id, staff_fname, staff_lname
                            from
                                staff;
                        """
        
        self.cursor.execute(self.command)

        self.result = self.cursor.fetchall()

        for data in self.result:
            self.staffId = data[0]
            self.fullName = f'{data[1]} {data[2]}'
            self.ui.technician.addItem(self.fullName, self.staffId)

        # for service type
        self.command =  f"""
                            select
                                serv_id, serv_type
                            from
                                service;
                        """
        
        self.cursor.execute(self.command)

        self.result = self.cursor.fetchall()

        for data in self.result:
            self.servId = data[0]
            self.servType = data[1]
            self.ui.serviceType.addItem(self.servType, self.servId)

        self.cursor.close()
        self.conn.close()

    def confirmService(self):
        self.custName = self.ui.customer.text().strip().upper()
        self.device = self.ui.device.currentData()
        self.technician = self.ui.technician.currentData()
        self.servType = self.ui.serviceType.currentData()
        self.fee = self.ui.additionalFee.value() + 250

        self.conn = psycopg2.connect(database="test_5",
                                    user="postgres",
                                    host="localhost",
                                    password="p05tgr35ql",
                                    port=5432)

        self.cursor = self.conn.cursor()
        
        self.command =  f"""
                            insert into
                                service_details(serv_det_date, serv_det_cust_name, serv_det_total_fee, staff_id, dev_id, serv_id)
                            values
                                (now(), '{self.custName}', {self.fee}, {self.technician}, {self.device}, {self.servType});
                        """
        
        self.cursor.execute(self.command)

        self.conn.commit()

        self.cursor.close()
        self.conn.close()

        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # widget = Widget()
    # widget.show()
    
    adminPage = AdminPage()
    adminPage.show()
    
    sys.exit(app.exec())