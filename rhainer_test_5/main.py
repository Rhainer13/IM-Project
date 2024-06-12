# This Python file uses the following encoding: utf-8
import sys, psycopg2

from PySide6.QtWidgets import QApplication, QWidget, QDialog, QTableWidgetItem, QPushButton, QHBoxLayout

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

        # load all tables
        self.loadInventoryTable()

        # navigation panel
        self.ui.logOut.clicked.connect(lambda: self.close())

        # inventory panel
        self.ui.addProduct.clicked.connect(self.openAddProductDialog)

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

    def openAddProductDialog(self):
        self.addProductDialog = AddProductDialog()
        self.addProductDialog.exec()
        self.loadInventoryTable()

    def openDetailsDialog(self, r):
        self.detailsDialog = DetailsDialog(r)
        self.detailsDialog.exec()

    def openEditProductDialog(self, r):
        self.editProductDialog = EditProductDialog(r)
        self.editProductDialog.exec()
        self.loadInventoryTable()

    def openDeleteProductDialog(self, r):
        self.deleteProductDialog = DeleteProductDialog(r)
        self.deleteProductDialog.exec()
        self.loadInventoryTable()

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
        self.name = self.ui.name.text()
        self.price = self.ui.price.value()

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # widget = Widget()
    # widget.show()
    
    adminPage = AdminPage()
    adminPage.show()
    
    sys.exit(app.exec())
