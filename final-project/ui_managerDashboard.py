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
from PySide6.QtWidgets import (QApplication, QColumnView, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QVBoxLayout,
    QWidget)

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
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 1, 1, 1)

        self.addItemButton = QPushButton(self.inventoryNavigation)
        self.addItemButton.setObjectName(u"addItemButton")

        self.gridLayout.addWidget(self.addItemButton, 1, 0, 1, 1)

        self.searchBar = QLineEdit(self.inventoryNavigation)
        self.searchBar.setObjectName(u"searchBar")

        self.gridLayout.addWidget(self.searchBar, 1, 2, 1, 1)

        self.searchButton = QPushButton(self.inventoryNavigation)
        self.searchButton.setObjectName(u"searchButton")

        self.gridLayout.addWidget(self.searchButton, 1, 3, 1, 1)

        self.title = QLabel(self.inventoryNavigation)
        self.title.setObjectName(u"title")

        self.gridLayout.addWidget(self.title, 0, 0, 1, 4)


        self.verticalLayout_3.addWidget(self.inventoryNavigation)

        self.inventoryList = QFrame(self.inventoryPage)
        self.inventoryList.setObjectName(u"inventoryList")
        self.inventoryList.setFrameShape(QFrame.StyledPanel)
        self.inventoryList.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.inventoryList)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.inventoryAttributes = QFrame(self.inventoryList)
        self.inventoryAttributes.setObjectName(u"inventoryAttributes")
        self.inventoryAttributes.setFrameShape(QFrame.StyledPanel)
        self.inventoryAttributes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.inventoryAttributes)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.productId = QLabel(self.inventoryAttributes)
        self.productId.setObjectName(u"productId")

        self.horizontalLayout.addWidget(self.productId)

        self.productName = QLabel(self.inventoryAttributes)
        self.productName.setObjectName(u"productName")

        self.horizontalLayout.addWidget(self.productName)

        self.quantity = QLabel(self.inventoryAttributes)
        self.quantity.setObjectName(u"quantity")

        self.horizontalLayout.addWidget(self.quantity)

        self.price = QLabel(self.inventoryAttributes)
        self.price.setObjectName(u"price")

        self.horizontalLayout.addWidget(self.price)

        self.category = QLabel(self.inventoryAttributes)
        self.category.setObjectName(u"category")

        self.horizontalLayout.addWidget(self.category)


        self.verticalLayout.addWidget(self.inventoryAttributes)

        self.products = QColumnView(self.inventoryList)
        self.products.setObjectName(u"products")

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
        self.employeeAttributes = QFrame(self.employeeList)
        self.employeeAttributes.setObjectName(u"employeeAttributes")
        self.employeeAttributes.setFrameShape(QFrame.StyledPanel)
        self.employeeAttributes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.employeeAttributes)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.employeeId = QLabel(self.employeeAttributes)
        self.employeeId.setObjectName(u"employeeId")

        self.horizontalLayout_3.addWidget(self.employeeId)

        self.employeeName = QLabel(self.employeeAttributes)
        self.employeeName.setObjectName(u"employeeName")

        self.horizontalLayout_3.addWidget(self.employeeName)

        self.employeeDateHired = QLabel(self.employeeAttributes)
        self.employeeDateHired.setObjectName(u"employeeDateHired")

        self.horizontalLayout_3.addWidget(self.employeeDateHired)

        self.employeeAddress = QLabel(self.employeeAttributes)
        self.employeeAddress.setObjectName(u"employeeAddress")

        self.horizontalLayout_3.addWidget(self.employeeAddress)

        self.employeeContact = QLabel(self.employeeAttributes)
        self.employeeContact.setObjectName(u"employeeContact")

        self.horizontalLayout_3.addWidget(self.employeeContact)

        self.employeeCharge = QLabel(self.employeeAttributes)
        self.employeeCharge.setObjectName(u"employeeCharge")

        self.horizontalLayout_3.addWidget(self.employeeCharge)


        self.verticalLayout_5.addWidget(self.employeeAttributes)

        self.employees = QColumnView(self.employeeList)
        self.employees.setObjectName(u"employees")

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
        self.historyAttributes = QFrame(self.historyList)
        self.historyAttributes.setObjectName(u"historyAttributes")
        self.historyAttributes.setFrameShape(QFrame.StyledPanel)
        self.historyAttributes.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.historyAttributes)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.date = QLabel(self.historyAttributes)
        self.date.setObjectName(u"date")

        self.horizontalLayout_4.addWidget(self.date)

        self.customerName = QLabel(self.historyAttributes)
        self.customerName.setObjectName(u"customerName")

        self.horizontalLayout_4.addWidget(self.customerName)

        self.contactNumber = QLabel(self.historyAttributes)
        self.contactNumber.setObjectName(u"contactNumber")

        self.horizontalLayout_4.addWidget(self.contactNumber)

        self.technician = QLabel(self.historyAttributes)
        self.technician.setObjectName(u"technician")

        self.horizontalLayout_4.addWidget(self.technician)

        self.labchargeel_6 = QLabel(self.historyAttributes)
        self.labchargeel_6.setObjectName(u"labchargeel_6")

        self.horizontalLayout_4.addWidget(self.labchargeel_6)

        self.serviceType = QLabel(self.historyAttributes)
        self.serviceType.setObjectName(u"serviceType")

        self.horizontalLayout_4.addWidget(self.serviceType)

        self.status = QLabel(self.historyAttributes)
        self.status.setObjectName(u"status")

        self.horizontalLayout_4.addWidget(self.status)


        self.verticalLayout_6.addWidget(self.historyAttributes)

        self.history = QColumnView(self.historyList)
        self.history.setObjectName(u"history")

        self.verticalLayout_6.addWidget(self.history)


        self.verticalLayout_7.addWidget(self.historyList)

        self.stackedWidget.addWidget(self.historyPage)

        self.horizontalLayout_2.addWidget(self.stackedWidget)


        self.retranslateUi(managerDashboard)

        self.stackedWidget.setCurrentIndex(2)


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
        self.addItemButton.setText(QCoreApplication.translate("managerDashboard", u"Add Item", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("managerDashboard", u"Product Name...", None))
        self.searchButton.setText(QCoreApplication.translate("managerDashboard", u"Search", None))
        self.title.setText(QCoreApplication.translate("managerDashboard", u"INVENTORY", None))
        self.productId.setText(QCoreApplication.translate("managerDashboard", u"Product ID", None))
        self.productName.setText(QCoreApplication.translate("managerDashboard", u"Product Name", None))
        self.quantity.setText(QCoreApplication.translate("managerDashboard", u"Quantity", None))
        self.price.setText(QCoreApplication.translate("managerDashboard", u"Price", None))
        self.category.setText(QCoreApplication.translate("managerDashboard", u"Category", None))
        self.addEmployeeButton.setText(QCoreApplication.translate("managerDashboard", u"Add Employee", None))
        self.searchBar_2.setPlaceholderText(QCoreApplication.translate("managerDashboard", u"Name...", None))
        self.searchButton_2.setText(QCoreApplication.translate("managerDashboard", u"Search", None))
        self.title_2.setText(QCoreApplication.translate("managerDashboard", u"EMPLOYEE", None))
        self.employeeId.setText(QCoreApplication.translate("managerDashboard", u"Employee ID", None))
        self.employeeName.setText(QCoreApplication.translate("managerDashboard", u"Name", None))
        self.employeeDateHired.setText(QCoreApplication.translate("managerDashboard", u"Date Hired", None))
        self.employeeAddress.setText(QCoreApplication.translate("managerDashboard", u"Address", None))
        self.employeeContact.setText(QCoreApplication.translate("managerDashboard", u"Contact Number", None))
        self.employeeCharge.setText(QCoreApplication.translate("managerDashboard", u"Charge", None))
        self.title_3.setText(QCoreApplication.translate("managerDashboard", u"TRANSACTION HISTORY", None))
        self.date.setText(QCoreApplication.translate("managerDashboard", u"Date", None))
        self.customerName.setText(QCoreApplication.translate("managerDashboard", u"Customer Name", None))
        self.contactNumber.setText(QCoreApplication.translate("managerDashboard", u"Contact Number", None))
        self.technician.setText(QCoreApplication.translate("managerDashboard", u"Technician", None))
        self.labchargeel_6.setText(QCoreApplication.translate("managerDashboard", u"Charge", None))
        self.serviceType.setText(QCoreApplication.translate("managerDashboard", u"Service Type", None))
        self.status.setText(QCoreApplication.translate("managerDashboard", u"Status", None))
    # retranslateUi

