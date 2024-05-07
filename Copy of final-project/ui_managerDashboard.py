# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'managerDashboard.ui'
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
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_managerDashboard(object):
    def setupUi(self, managerDashboard):
        if not managerDashboard.objectName():
            managerDashboard.setObjectName(u"managerDashboard")
        managerDashboard.resize(1110, 657)
        self.horizontalLayout_2 = QHBoxLayout(managerDashboard)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.navigationPanel = QFrame(managerDashboard)
        self.navigationPanel.setObjectName(u"navigationPanel")
        self.navigationPanel.setFrameShape(QFrame.StyledPanel)
        self.navigationPanel.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.navigationPanel)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.inventoryButton = QPushButton(self.navigationPanel)
        self.inventoryButton.setObjectName(u"inventoryButton")

        self.verticalLayout_2.addWidget(self.inventoryButton)

        self.employeeButton = QPushButton(self.navigationPanel)
        self.employeeButton.setObjectName(u"employeeButton")

        self.verticalLayout_2.addWidget(self.employeeButton)

        self.historyButton = QPushButton(self.navigationPanel)
        self.historyButton.setObjectName(u"historyButton")

        self.verticalLayout_2.addWidget(self.historyButton)

        self.serviceReportButton = QPushButton(self.navigationPanel)
        self.serviceReportButton.setObjectName(u"serviceReportButton")

        self.verticalLayout_2.addWidget(self.serviceReportButton)

        self.purchaseButton = QPushButton(self.navigationPanel)
        self.purchaseButton.setObjectName(u"purchaseButton")

        self.verticalLayout_2.addWidget(self.purchaseButton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.logOutButton = QPushButton(self.navigationPanel)
        self.logOutButton.setObjectName(u"logOutButton")

        self.verticalLayout_2.addWidget(self.logOutButton)


        self.horizontalLayout_2.addWidget(self.navigationPanel)

        self.stackedWidget = QStackedWidget(managerDashboard)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.inventoryPage = QWidget()
        self.inventoryPage.setObjectName(u"inventoryPage")
        self.verticalLayout_3 = QVBoxLayout(self.inventoryPage)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.inventoryNavigation = QFrame(self.inventoryPage)
        self.inventoryNavigation.setObjectName(u"inventoryNavigation")
        self.inventoryNavigation.setFrameShape(QFrame.StyledPanel)
        self.inventoryNavigation.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.inventoryNavigation)
        self.gridLayout.setObjectName(u"gridLayout")
        self.searchButton = QPushButton(self.inventoryNavigation)
        self.searchButton.setObjectName(u"searchButton")

        self.gridLayout.addWidget(self.searchButton, 1, 3, 1, 1)

        self.searchBar = QLineEdit(self.inventoryNavigation)
        self.searchBar.setObjectName(u"searchBar")

        self.gridLayout.addWidget(self.searchBar, 1, 2, 1, 1)

        self.title = QLabel(self.inventoryNavigation)
        self.title.setObjectName(u"title")

        self.gridLayout.addWidget(self.title, 0, 0, 1, 4)

        self.addItemButton = QPushButton(self.inventoryNavigation)
        self.addItemButton.setObjectName(u"addItemButton")

        self.gridLayout.addWidget(self.addItemButton, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.inventoryNavigation)

        self.inventoryList = QFrame(self.inventoryPage)
        self.inventoryList.setObjectName(u"inventoryList")
        self.inventoryList.setFrameShape(QFrame.StyledPanel)
        self.inventoryList.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.inventoryList)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.products = QTableWidget(self.inventoryList)
        if (self.products.columnCount() < 6):
            self.products.setColumnCount(6)
        font = QFont()
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.products.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.products.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.products.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.products.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.products.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.products.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.products.setObjectName(u"products")
        self.products.horizontalHeader().setStretchLastSection(True)
        self.products.verticalHeader().setVisible(False)
        self.products.verticalHeader().setStretchLastSection(False)

        self.verticalLayout.addWidget(self.products)


        self.verticalLayout_3.addWidget(self.inventoryList)

        self.stackedWidget.addWidget(self.inventoryPage)
        self.employeePage = QWidget()
        self.employeePage.setObjectName(u"employeePage")
        self.verticalLayout_4 = QVBoxLayout(self.employeePage)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.employeeNavigation = QFrame(self.employeePage)
        self.employeeNavigation.setObjectName(u"employeeNavigation")
        self.employeeNavigation.setFrameShape(QFrame.StyledPanel)
        self.employeeNavigation.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.employeeNavigation)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)

        self.addEmployeeButton = QPushButton(self.employeeNavigation)
        self.addEmployeeButton.setObjectName(u"addEmployeeButton")

        self.gridLayout_2.addWidget(self.addEmployeeButton, 1, 0, 1, 1)

        self.searchBar_2 = QLineEdit(self.employeeNavigation)
        self.searchBar_2.setObjectName(u"searchBar_2")

        self.gridLayout_2.addWidget(self.searchBar_2, 1, 2, 1, 1)

        self.searchButton_2 = QPushButton(self.employeeNavigation)
        self.searchButton_2.setObjectName(u"searchButton_2")

        self.gridLayout_2.addWidget(self.searchButton_2, 1, 3, 1, 1)

        self.title_2 = QLabel(self.employeeNavigation)
        self.title_2.setObjectName(u"title_2")

        self.gridLayout_2.addWidget(self.title_2, 0, 0, 1, 4)


        self.verticalLayout_4.addWidget(self.employeeNavigation)

        self.employeeList = QFrame(self.employeePage)
        self.employeeList.setObjectName(u"employeeList")
        self.employeeList.setFrameShape(QFrame.StyledPanel)
        self.employeeList.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.employeeList)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.employees = QTableWidget(self.employeeList)
        if (self.employees.columnCount() < 8):
            self.employees.setColumnCount(8)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.employees.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.employees.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.employees.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.employees.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font);
        self.employees.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font);
        self.employees.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font);
        self.employees.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font);
        self.employees.setHorizontalHeaderItem(7, __qtablewidgetitem13)
        self.employees.setObjectName(u"employees")
        self.employees.horizontalHeader().setCascadingSectionResizes(False)
        self.employees.horizontalHeader().setProperty("showSortIndicator", False)
        self.employees.horizontalHeader().setStretchLastSection(True)
        self.employees.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_5.addWidget(self.employees)


        self.verticalLayout_4.addWidget(self.employeeList)

        self.stackedWidget.addWidget(self.employeePage)
        self.historyPage = QWidget()
        self.historyPage.setObjectName(u"historyPage")
        self.verticalLayout_7 = QVBoxLayout(self.historyPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.historyNavigation = QFrame(self.historyPage)
        self.historyNavigation.setObjectName(u"historyNavigation")
        self.historyNavigation.setFrameShape(QFrame.StyledPanel)
        self.historyNavigation.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.historyNavigation)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.title_3 = QLabel(self.historyNavigation)
        self.title_3.setObjectName(u"title_3")

        self.gridLayout_3.addWidget(self.title_3, 0, 0, 1, 1)


        self.verticalLayout_7.addWidget(self.historyNavigation)

        self.historyList = QFrame(self.historyPage)
        self.historyList.setObjectName(u"historyList")
        self.historyList.setFrameShape(QFrame.StyledPanel)
        self.historyList.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.historyList)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.history = QTableWidget(self.historyList)
        if (self.history.columnCount() < 6):
            self.history.setColumnCount(6)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font);
        self.history.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font);
        self.history.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font);
        self.history.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font);
        self.history.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font);
        self.history.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font);
        self.history.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        self.history.setObjectName(u"history")
        self.history.verticalHeader().setHighlightSections(False)

        self.verticalLayout_6.addWidget(self.history)


        self.verticalLayout_7.addWidget(self.historyList)

        self.stackedWidget.addWidget(self.historyPage)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.retranslateUi(managerDashboard)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(managerDashboard)
    # setupUi

    def retranslateUi(self, managerDashboard):
        managerDashboard.setWindowTitle(QCoreApplication.translate("managerDashboard", u"Manager Dashboard", None))
        self.inventoryButton.setText(QCoreApplication.translate("managerDashboard", u"Inventory", None))
        self.employeeButton.setText(QCoreApplication.translate("managerDashboard", u"Employee", None))
        self.historyButton.setText(QCoreApplication.translate("managerDashboard", u"History", None))
        self.serviceReportButton.setText(QCoreApplication.translate("managerDashboard", u"Service Report", None))
        self.purchaseButton.setText(QCoreApplication.translate("managerDashboard", u"Purchase", None))
        self.logOutButton.setText(QCoreApplication.translate("managerDashboard", u"Log Out", None))
        self.searchButton.setText(QCoreApplication.translate("managerDashboard", u"Search", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("managerDashboard", u"Product Name...", None))
        self.title.setText(QCoreApplication.translate("managerDashboard", u"INVENTORY", None))
        self.addItemButton.setText(QCoreApplication.translate("managerDashboard", u"Add Item", None))
        ___qtablewidgetitem = self.products.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("managerDashboard", u"Product ID", None));
        ___qtablewidgetitem1 = self.products.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("managerDashboard", u"Quantity", None));
        ___qtablewidgetitem2 = self.products.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("managerDashboard", u"Name", None));
        ___qtablewidgetitem3 = self.products.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("managerDashboard", u"Price", None));
        ___qtablewidgetitem4 = self.products.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("managerDashboard", u"Category", None));
        ___qtablewidgetitem5 = self.products.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("managerDashboard", u"Actions", None));
        self.addEmployeeButton.setText(QCoreApplication.translate("managerDashboard", u"Add Employee", None))
        self.searchBar_2.setPlaceholderText(QCoreApplication.translate("managerDashboard", u"Name...", None))
        self.searchButton_2.setText(QCoreApplication.translate("managerDashboard", u"Search", None))
        self.title_2.setText(QCoreApplication.translate("managerDashboard", u"EMPLOYEE", None))
        ___qtablewidgetitem6 = self.employees.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("managerDashboard", u"Employee ID", None));
        ___qtablewidgetitem7 = self.employees.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("managerDashboard", u"Name", None));
        ___qtablewidgetitem8 = self.employees.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("managerDashboard", u"Date Hired", None));
        ___qtablewidgetitem9 = self.employees.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("managerDashboard", u"Date Terminate", None));
        ___qtablewidgetitem10 = self.employees.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("managerDashboard", u"Address", None));
        ___qtablewidgetitem11 = self.employees.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("managerDashboard", u"Contact Number", None));
        ___qtablewidgetitem12 = self.employees.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("managerDashboard", u"Charge", None));
        ___qtablewidgetitem13 = self.employees.horizontalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("managerDashboard", u"Actions", None));
        self.title_3.setText(QCoreApplication.translate("managerDashboard", u"TRANSACTION HISTORY", None))
        ___qtablewidgetitem14 = self.history.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("managerDashboard", u"Date", None));
        ___qtablewidgetitem15 = self.history.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("managerDashboard", u"Customer Name", None));
        ___qtablewidgetitem16 = self.history.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("managerDashboard", u"Contact Number", None));
        ___qtablewidgetitem17 = self.history.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("managerDashboard", u"Technician", None));
        ___qtablewidgetitem18 = self.history.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("managerDashboard", u"Charge", None));
        ___qtablewidgetitem19 = self.history.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("managerDashboard", u"Status", None));
    # retranslateUi

