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

class managerDashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_managerDashboard()
        self.ui.setupUi(self)

class employeeDashboard(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_employeeDashboard()
        self.ui.setupUi(self)


# for dialogs
class addItemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_addItemDialog()
        self.ui.setupUi(self)

class updateItemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_updateItemDialog()
        self.ui.setupUi(self)

class deleteItemDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_deleteItemDialog()
        self.ui.setupUi(self)

class addEmployeeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_addEmployeeDialog()
        self.ui.setupUi(self)

class updateEmployeeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_updateEmployeeDialog()
        self.ui.setupUi(self)

class serviceReportDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_serviceReportDialog()
        self.ui.setupUi(self)

class purchaseDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_purchaseDialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # logInWindow = logInWindow()
    # logInWindow.show()

    # managerDashboard = managerDashboard()
    # managerDashboard.show()

    # employeeDashboard = employeeDashboard()
    # employeeDashboard.show()

    # addItemDialog = addItemDialog()
    # addItemDialog.show()

    # updateItemDialog = updateItemDialog()
    # updateItemDialog.show()

    # deleteItemDialog = deleteItemDialog()
    # deleteItemDialog.show()

    # addEmployeeDialog = addEmployeeDialog()
    # addEmployeeDialog.show()

    # updateEmployeeDialog = updateEmployeeDialog()
    # updateEmployeeDialog.show()

    # serviceReportDialog = serviceReportDialog()
    # serviceReportDialog.show()

    # purchaseDialog = purchaseDialog()
    # purchaseDialog.show()

    sys.exit(app.exec())