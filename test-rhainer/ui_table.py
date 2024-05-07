# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'table.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHeaderView, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_EmployeeWindow(object):
    def setupUi(self, EmployeeWindow):
        if not EmployeeWindow.objectName():
            EmployeeWindow.setObjectName(u"EmployeeWindow")
        EmployeeWindow.resize(1027, 597)
        self.verticalLayout = QVBoxLayout(EmployeeWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.employeeTable = QTableWidget(EmployeeWindow)
        if (self.employeeTable.columnCount() < 6):
            self.employeeTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.employeeTable.setObjectName(u"employeeTable")
        self.employeeTable.setRowCount(0)
        self.employeeTable.horizontalHeader().setVisible(True)
        self.employeeTable.horizontalHeader().setCascadingSectionResizes(False)
        self.employeeTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.employeeTable.horizontalHeader().setStretchLastSection(False)
        self.employeeTable.verticalHeader().setVisible(False)
        self.employeeTable.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.employeeTable)

        self.rowToDelete = QLineEdit(EmployeeWindow)
        self.rowToDelete.setObjectName(u"rowToDelete")

        self.verticalLayout.addWidget(self.rowToDelete)

        self.addRow = QPushButton(EmployeeWindow)
        self.addRow.setObjectName(u"addRow")

        self.verticalLayout.addWidget(self.addRow)

        self.removeRow = QPushButton(EmployeeWindow)
        self.removeRow.setObjectName(u"removeRow")

        self.verticalLayout.addWidget(self.removeRow)

        self.loadTable = QPushButton(EmployeeWindow)
        self.loadTable.setObjectName(u"loadTable")

        self.verticalLayout.addWidget(self.loadTable)


        self.retranslateUi(EmployeeWindow)

        QMetaObject.connectSlotsByName(EmployeeWindow)
    # setupUi

    def retranslateUi(self, EmployeeWindow):
        EmployeeWindow.setWindowTitle(QCoreApplication.translate("EmployeeWindow", u"Form", None))
        ___qtablewidgetitem = self.employeeTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("EmployeeWindow", u"Employee Id", None));
        ___qtablewidgetitem1 = self.employeeTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("EmployeeWindow", u"Employee Name", None));
        ___qtablewidgetitem2 = self.employeeTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("EmployeeWindow", u"Date Hired", None));
        ___qtablewidgetitem3 = self.employeeTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("EmployeeWindow", u"Address", None));
        ___qtablewidgetitem4 = self.employeeTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("EmployeeWindow", u"Contact Number", None));
        ___qtablewidgetitem5 = self.employeeTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("EmployeeWindow", u"Charge", None));
        self.rowToDelete.setPlaceholderText(QCoreApplication.translate("EmployeeWindow", u"Employee Id to Delete", None))
        self.addRow.setText(QCoreApplication.translate("EmployeeWindow", u"Add Row", None))
        self.removeRow.setText(QCoreApplication.translate("EmployeeWindow", u"Remove Row", None))
        self.loadTable.setText(QCoreApplication.translate("EmployeeWindow", u"Load Database", None))
    # retranslateUi

