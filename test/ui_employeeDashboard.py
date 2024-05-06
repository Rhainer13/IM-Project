# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'employeeDashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_EmployeeDashboard(object):
    def setupUi(self, EmployeeDashboard):
        if not EmployeeDashboard.objectName():
            EmployeeDashboard.setObjectName(u"EmployeeDashboard")
        EmployeeDashboard.resize(1104, 686)
        self.horizontalLayout = QHBoxLayout(EmployeeDashboard)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(EmployeeDashboard)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.inventoryButton = QPushButton(self.frame)
        self.inventoryButton.setObjectName(u"inventoryButton")

        self.verticalLayout.addWidget(self.inventoryButton)

        self.employeeButton = QPushButton(self.frame)
        self.employeeButton.setObjectName(u"employeeButton")

        self.verticalLayout.addWidget(self.employeeButton)

        self.historyButton = QPushButton(self.frame)
        self.historyButton.setObjectName(u"historyButton")

        self.verticalLayout.addWidget(self.historyButton)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.serviceReportButton = QPushButton(self.frame)
        self.serviceReportButton.setObjectName(u"serviceReportButton")

        self.verticalLayout.addWidget(self.serviceReportButton)

        self.purchaseReportButton = QPushButton(self.frame)
        self.purchaseReportButton.setObjectName(u"purchaseReportButton")

        self.verticalLayout.addWidget(self.purchaseReportButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.logOutButton = QPushButton(self.frame)
        self.logOutButton.setObjectName(u"logOutButton")

        self.verticalLayout.addWidget(self.logOutButton)


        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(EmployeeDashboard)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_3 = QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.inventory = QLabel(self.frame_2)
        self.inventory.setObjectName(u"inventory")

        self.gridLayout.addWidget(self.inventory, 0, 0, 1, 1)

        self.addItemButton = QPushButton(self.frame_2)
        self.addItemButton.setObjectName(u"addItemButton")

        self.gridLayout.addWidget(self.addItemButton, 1, 0, 1, 1)

        self.searchButton = QPushButton(self.frame_2)
        self.searchButton.setObjectName(u"searchButton")

        self.gridLayout.addWidget(self.searchButton, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.searchBar = QLineEdit(self.frame_2)
        self.searchBar.setObjectName(u"searchBar")

        self.gridLayout.addWidget(self.searchBar, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.inventoryTable = QTableWidget(self.page)
        if (self.inventoryTable.columnCount() < 6):
            self.inventoryTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.inventoryTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.inventoryTable.setObjectName(u"inventoryTable")

        self.verticalLayout_3.addWidget(self.inventoryTable)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_2 = QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.employee = QLabel(self.frame_3)
        self.employee.setObjectName(u"employee")

        self.gridLayout_2.addWidget(self.employee, 0, 0, 1, 1)

        self.addEmployeeButton = QPushButton(self.frame_3)
        self.addEmployeeButton.setObjectName(u"addEmployeeButton")

        self.gridLayout_2.addWidget(self.addEmployeeButton, 1, 0, 1, 1)

        self.searchButton_2 = QPushButton(self.frame_3)
        self.searchButton_2.setObjectName(u"searchButton_2")

        self.gridLayout_2.addWidget(self.searchButton_2, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.searchBar_2 = QLineEdit(self.frame_3)
        self.searchBar_2.setObjectName(u"searchBar_2")

        self.gridLayout_2.addWidget(self.searchBar_2, 1, 2, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.employeeTable = QTableWidget(self.page_2)
        if (self.employeeTable.columnCount() < 6):
            self.employeeTable.setColumnCount(6)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        self.employeeTable.setObjectName(u"employeeTable")
        self.employeeTable.horizontalHeader().setProperty("showSortIndicator", True)
        self.employeeTable.horizontalHeader().setStretchLastSection(True)
        self.employeeTable.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.employeeTable)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.page_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_4 = QGridLayout(self.tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableWidget = QTableWidget(self.tab)
        self.tableWidget.setObjectName(u"tableWidget")

        self.gridLayout_4.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(EmployeeDashboard)

        self.stackedWidget.setCurrentIndex(2)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(EmployeeDashboard)
    # setupUi

    def retranslateUi(self, EmployeeDashboard):
        EmployeeDashboard.setWindowTitle(QCoreApplication.translate("EmployeeDashboard", u"Form", None))
        self.inventoryButton.setText(QCoreApplication.translate("EmployeeDashboard", u"Inventory", None))
        self.employeeButton.setText(QCoreApplication.translate("EmployeeDashboard", u"Employee", None))
        self.historyButton.setText(QCoreApplication.translate("EmployeeDashboard", u"History", None))
        self.serviceReportButton.setText(QCoreApplication.translate("EmployeeDashboard", u"Service Report", None))
        self.purchaseReportButton.setText(QCoreApplication.translate("EmployeeDashboard", u"Purchase Report", None))
        self.logOutButton.setText(QCoreApplication.translate("EmployeeDashboard", u"Log Out", None))
        self.inventory.setText(QCoreApplication.translate("EmployeeDashboard", u"INVENTORY", None))
        self.addItemButton.setText(QCoreApplication.translate("EmployeeDashboard", u"Add Item", None))
        self.searchButton.setText(QCoreApplication.translate("EmployeeDashboard", u"Search", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("EmployeeDashboard", u"Search", None))
        ___qtablewidgetitem = self.inventoryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("EmployeeDashboard", u"Product ID", None));
        ___qtablewidgetitem1 = self.inventoryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("EmployeeDashboard", u"Product Name", None));
        ___qtablewidgetitem2 = self.inventoryTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("EmployeeDashboard", u"Quantity", None));
        ___qtablewidgetitem3 = self.inventoryTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("EmployeeDashboard", u"Price", None));
        ___qtablewidgetitem4 = self.inventoryTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("EmployeeDashboard", u"Category", None));
        ___qtablewidgetitem5 = self.inventoryTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("EmployeeDashboard", u"Actions", None));
        self.employee.setText(QCoreApplication.translate("EmployeeDashboard", u"EMPLOYEE", None))
        self.addEmployeeButton.setText(QCoreApplication.translate("EmployeeDashboard", u"Add Employee", None))
        self.searchButton_2.setText(QCoreApplication.translate("EmployeeDashboard", u"Search", None))
        ___qtablewidgetitem6 = self.employeeTable.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("EmployeeDashboard", u"Employee Id", None));
        ___qtablewidgetitem7 = self.employeeTable.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("EmployeeDashboard", u"Employee Name", None));
        ___qtablewidgetitem8 = self.employeeTable.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("EmployeeDashboard", u"Date Hired", None));
        ___qtablewidgetitem9 = self.employeeTable.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("EmployeeDashboard", u"Address", None));
        ___qtablewidgetitem10 = self.employeeTable.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("EmployeeDashboard", u"Contact", None));
        ___qtablewidgetitem11 = self.employeeTable.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("EmployeeDashboard", u"Charge", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("EmployeeDashboard", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("EmployeeDashboard", u"Tab 2", None))
    # retranslateUi

