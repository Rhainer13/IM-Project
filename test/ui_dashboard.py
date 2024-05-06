# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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

class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        if not Dashboard.objectName():
            Dashboard.setObjectName(u"Dashboard")
        Dashboard.resize(1104, 686)
        self.horizontalLayout = QHBoxLayout(Dashboard)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(Dashboard)
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

        self.stackedWidget = QStackedWidget(Dashboard)
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

        self.addProductButton = QPushButton(self.frame_2)
        self.addProductButton.setObjectName(u"addProductButton")

        self.gridLayout.addWidget(self.addProductButton, 1, 0, 1, 1)

        self.inventoryTabSearchButton = QPushButton(self.frame_2)
        self.inventoryTabSearchButton.setObjectName(u"inventoryTabSearchButton")

        self.gridLayout.addWidget(self.inventoryTabSearchButton, 1, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.inventoryTabSearchBar = QLineEdit(self.frame_2)
        self.inventoryTabSearchBar.setObjectName(u"inventoryTabSearchBar")

        self.gridLayout.addWidget(self.inventoryTabSearchBar, 1, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.productTable = QTableWidget(self.page)
        if (self.productTable.columnCount() < 6):
            self.productTable.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.productTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.productTable.setObjectName(u"productTable")
        self.productTable.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.productTable)

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

        self.employeeTabSearchButton = QPushButton(self.frame_3)
        self.employeeTabSearchButton.setObjectName(u"employeeTabSearchButton")

        self.gridLayout_2.addWidget(self.employeeTabSearchButton, 1, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.employeeTabSearchBar = QLineEdit(self.frame_3)
        self.employeeTabSearchBar.setObjectName(u"employeeTabSearchBar")

        self.gridLayout_2.addWidget(self.employeeTabSearchBar, 1, 2, 1, 1)


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
        self.verticalLayout_5 = QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.serviceHistoryTable = QTableWidget(self.tab)
        if (self.serviceHistoryTable.columnCount() < 7):
            self.serviceHistoryTable.setColumnCount(7)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.serviceHistoryTable.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.serviceHistoryTable.setHorizontalHeaderItem(1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.serviceHistoryTable.setHorizontalHeaderItem(2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.serviceHistoryTable.setHorizontalHeaderItem(3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.serviceHistoryTable.setHorizontalHeaderItem(4, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.serviceHistoryTable.setHorizontalHeaderItem(5, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.serviceHistoryTable.setHorizontalHeaderItem(6, __qtablewidgetitem18)
        self.serviceHistoryTable.setObjectName(u"serviceHistoryTable")
        self.serviceHistoryTable.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_5.addWidget(self.serviceHistoryTable)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.purchaseHistoryTable = QTableWidget(self.tab_2)
        if (self.purchaseHistoryTable.columnCount() < 4):
            self.purchaseHistoryTable.setColumnCount(4)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.purchaseHistoryTable.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.purchaseHistoryTable.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.purchaseHistoryTable.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.purchaseHistoryTable.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        self.purchaseHistoryTable.setObjectName(u"purchaseHistoryTable")
        self.purchaseHistoryTable.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_6.addWidget(self.purchaseHistoryTable)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(Dashboard)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dashboard)
    # setupUi

    def retranslateUi(self, Dashboard):
        Dashboard.setWindowTitle(QCoreApplication.translate("Dashboard", u"Form", None))
        self.inventoryButton.setText(QCoreApplication.translate("Dashboard", u"Inventory", None))
        self.employeeButton.setText(QCoreApplication.translate("Dashboard", u"Employee", None))
        self.historyButton.setText(QCoreApplication.translate("Dashboard", u"History", None))
        self.serviceReportButton.setText(QCoreApplication.translate("Dashboard", u"Service Report", None))
        self.purchaseReportButton.setText(QCoreApplication.translate("Dashboard", u"Purchase Report", None))
        self.logOutButton.setText(QCoreApplication.translate("Dashboard", u"Log Out", None))
        self.inventory.setText(QCoreApplication.translate("Dashboard", u"INVENTORY", None))
        self.addProductButton.setText(QCoreApplication.translate("Dashboard", u"Add Product", None))
        self.inventoryTabSearchButton.setText(QCoreApplication.translate("Dashboard", u"Search", None))
        self.inventoryTabSearchBar.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Search", None))
        ___qtablewidgetitem = self.productTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Dashboard", u"Product ID", None));
        ___qtablewidgetitem1 = self.productTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Dashboard", u"Product Name", None));
        ___qtablewidgetitem2 = self.productTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Dashboard", u"Quantity", None));
        ___qtablewidgetitem3 = self.productTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Dashboard", u"Price", None));
        ___qtablewidgetitem4 = self.productTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Dashboard", u"Category", None));
        ___qtablewidgetitem5 = self.productTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Dashboard", u"Actions", None));
        self.employee.setText(QCoreApplication.translate("Dashboard", u"EMPLOYEE", None))
        self.addEmployeeButton.setText(QCoreApplication.translate("Dashboard", u"Add Employee", None))
        self.employeeTabSearchButton.setText(QCoreApplication.translate("Dashboard", u"Search", None))
        self.employeeTabSearchBar.setPlaceholderText(QCoreApplication.translate("Dashboard", u"Search", None))
        ___qtablewidgetitem6 = self.employeeTable.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Dashboard", u"Employee Id", None));
        ___qtablewidgetitem7 = self.employeeTable.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Dashboard", u"Employee Name", None));
        ___qtablewidgetitem8 = self.employeeTable.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Dashboard", u"Date Hired", None));
        ___qtablewidgetitem9 = self.employeeTable.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Dashboard", u"Address", None));
        ___qtablewidgetitem10 = self.employeeTable.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Dashboard", u"Contact", None));
        ___qtablewidgetitem11 = self.employeeTable.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Dashboard", u"Charge", None));
        ___qtablewidgetitem12 = self.serviceHistoryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Dashboard", u"Date", None));
        ___qtablewidgetitem13 = self.serviceHistoryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Dashboard", u"Customer Name", None));
        ___qtablewidgetitem14 = self.serviceHistoryTable.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Dashboard", u"Service Type", None));
        ___qtablewidgetitem15 = self.serviceHistoryTable.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Dashboard", u"Payment", None));
        ___qtablewidgetitem16 = self.serviceHistoryTable.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Dashboard", u"Customer Contact", None));
        ___qtablewidgetitem17 = self.serviceHistoryTable.horizontalHeaderItem(5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Dashboard", u"Status", None));
        ___qtablewidgetitem18 = self.serviceHistoryTable.horizontalHeaderItem(6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Dashboard", u"Actions", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Dashboard", u"Service History", None))
        ___qtablewidgetitem19 = self.purchaseHistoryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Dashboard", u"Date", None));
        ___qtablewidgetitem20 = self.purchaseHistoryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Dashboard", u"Customer Name", None));
        ___qtablewidgetitem21 = self.purchaseHistoryTable.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Dashboard", u"Customer Contact", None));
        ___qtablewidgetitem22 = self.purchaseHistoryTable.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Dashboard", u"Payment", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Dashboard", u"Purchase History", None))
    # retranslateUi

