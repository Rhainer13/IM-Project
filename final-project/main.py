# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QDialog


# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py


from ui_logIn import Ui_logInWindow
from ui_managerDashboard import Ui_managerDashboard
from ui_employeeDashboard import Ui_employeeDashboard
from ui_deleteItemDialog import Ui_deleteItemDialog
from ui_addItemDialog import Ui_addItemDialog
from ui_updateItemDialog import Ui_updateItemDialog
from ui_addEmployeeDialog import Ui_addEmployeeDialog
from ui_updateEmployeeDialog import Ui_updateEmployeeDialog
from ui_serviceReportDialog import Ui_serviceReportDialog
from ui_purchaseDialog import Ui_purchaseDialog


# for widgets
class logInWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_logInWindow()
        self.ui.setupUi(self)
        self.ui.logInButton.clicked.connect(self.loginButton)

    def clearText(self):
        self.ui.usernameInput.clear()
        self.ui.passwordInput.clear()
        self.ui.notification.clear()

    def loginButton(self):
        self.usernameInput = self.ui.usernameInput.text()
        self.password = self.ui.passwordInput.text()
        if self.usernameInput == 'admin' and self.password == 'admin123':
            self.clearText()
            self.login = managerDashboard()
            self.login.show()
            self.close()
        elif self.usernameInput == 'employee' and self.password == '123456':
            self.clearText()
            self.employee()
        else:
            self.ui.notification.setText("Invalid")

    def employee(self):
        self.loginEmployee = employeeDashboard()
        self.loginEmployee.show()
        self.close()

class managerDashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_managerDashboard()
        self.ui.setupUi(self)
        self.ui.logOutButton.clicked.connect(self.loginWindow)
        self.ui.serviceReportButton.clicked.connect(self.serviceReport)
        self.ui.purchaseButton.clicked.connect(self.purchase)
        self.ui.addItemButton.clicked.connect(self.item)
        self.ui.addEmployeeButton.clicked.connect(self.employee)

    def loginWindow(self):
        self.login = logInWindow
        self.login.show()
        self.close()

    def purchase(self):
        self.purchased = purchaseDialog()
        self.purchased.exec()

    def serviceReport(self):
        self.service = serviceReportDialog()
        self.service.exec()

    def item(self):
        self.itemdialog = addItemDialog()
        self.itemdialog.exec()

    def employee(self):
        self.emp = addEmployeeDialog()
        self.emp.exec()

class employeeDashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_employeeDashboard()
        self.ui.setupUi(self)
        self.ui.serviceReportButton.clicked.connect(self.serviceReport)
        self.ui.logOutButton.clicked.connect(self.loginWindow)
        self.ui.purchaseButton.clicked.connect(self.purchase)

    def loginWindow(self):
        self.login = logInWindow
        self.login.show()
        self.close()

    def purchase(self):
        self.purchased = purchaseDialog()
        self.purchased.exec()

    def serviceReport(self):
        self.service = serviceReportDialog()
        self.service.exec()


# for dialogs
class addItemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_addItemDialog()
        self.ui.setupUi(self)
        self.ui.cancelButton.clicked.connect(self.closeDialog)

    def closeDialog(self):
        self.close()

class updateItemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_updateItemDialog()
        self.ui.setupUi(self)
        self.ui.cancelButton.clicked.connect(self.closeDialog)


    def closeDialog(self):
        self.close()

class deleteItemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_deleteItemDialog()
        self.ui.setupUi(self)

        self.ui.cancelButton.clicked.connect(self.closeDialog)

    def closeDialog(self):
        self.close()

class addEmployeeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_addEmployeeDialog()
        self.ui.setupUi(self)
        self.ui.cancelButton.clicked.connect(self.closeDialog)


    def closeDialog(self):
        self.close()

class updateEmployeeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_updateEmployeeDialog()
        self.ui.setupUi(self)
        self.ui.cancelButton.clicked.connect(self.closeDialog)


    def closeDialog(self):
        self.close()

class serviceReportDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_serviceReportDialog()
        self.ui.setupUi(self)
        self.ui.cancelButton.clicked.connect(self.closeDialog)


    def closeDialog(self):
        self.close()

class purchaseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_purchaseDialog()
        self.ui.setupUi(self)
        self.ui.cancelButton.clicked.connect(self.closeDialog)

    def closeDialog(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    logInWindow = logInWindow()
    logInWindow.show()

    sys.exit(app.exec())
