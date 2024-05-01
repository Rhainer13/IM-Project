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
from PySide6.QtWidgets import (QApplication, QColumnView, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_employeeDashboard(object):
    def setupUi(self, employeeDashboard):
        if not employeeDashboard.objectName():
            employeeDashboard.setObjectName(u"employeeDashboard")
        employeeDashboard.resize(1149, 666)
        self.logoutemployee = employeeDashboard
        self.horizontalLayout_2 = QHBoxLayout(employeeDashboard)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.navigationPanel = QFrame(employeeDashboard)
        self.navigationPanel.setObjectName(u"navigationPanel")
        self.navigationPanel.setFrameShape(QFrame.StyledPanel)
        self.navigationPanel.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.navigationPanel)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.inventoryButton = QPushButton(self.navigationPanel)
        self.inventoryButton.setObjectName(u"inventoryButton")

        self.verticalLayout.addWidget(self.inventoryButton)

        self.serviceReportButton = QPushButton(self.navigationPanel)
        self.serviceReportButton.setObjectName(u"serviceReportButton")

        self.verticalLayout.addWidget(self.serviceReportButton)

        self.purchaseButton = QPushButton(self.navigationPanel)
        self.purchaseButton.setObjectName(u"purchaseButton")

        self.verticalLayout.addWidget(self.purchaseButton)

        self.verticalSpacer = QSpacerItem(20, 473, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.logOutButton = QPushButton(self.navigationPanel)
        self.logOutButton.setObjectName(u"logOutButton")

        self.verticalLayout.addWidget(self.logOutButton)

        self.horizontalLayout_2.addWidget(self.navigationPanel)

        self.inventoryFrame = QFrame(employeeDashboard)
        self.inventoryFrame.setObjectName(u"inventoryFrame")
        self.inventoryFrame.setFrameShape(QFrame.StyledPanel)
        self.inventoryFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.inventoryFrame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.inventoryNavigation = QFrame(self.inventoryFrame)
        self.inventoryNavigation.setObjectName(u"inventoryNavigation")
        self.inventoryNavigation.setFrameShape(QFrame.StyledPanel)
        self.inventoryNavigation.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.inventoryNavigation)
        self.gridLayout.setObjectName(u"gridLayout")
        self.searchButton = QPushButton(self.inventoryNavigation)
        self.searchButton.setObjectName(u"searchButton")

        self.gridLayout.addWidget(self.searchButton, 1, 2, 1, 1)

        self.searchBar = QLineEdit(self.inventoryNavigation)
        self.searchBar.setObjectName(u"searchBar")

        self.gridLayout.addWidget(self.searchBar, 1, 1, 1, 1)

        self.inventoryTitle = QLabel(self.inventoryNavigation)
        self.inventoryTitle.setObjectName(u"inventoryTitle")

        self.gridLayout.addWidget(self.inventoryTitle, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.inventoryNavigation)

        self.inventoryList = QFrame(self.inventoryFrame)
        self.inventoryList.setObjectName(u"inventoryList")
        self.inventoryList.setFrameShape(QFrame.StyledPanel)
        self.inventoryList.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.inventoryList)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
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


        self.verticalLayout_2.addWidget(self.inventoryAttributes)

        self.products = QColumnView(self.inventoryList)
        self.products.setObjectName(u"products")

        self.verticalLayout_2.addWidget(self.products)


        self.verticalLayout_3.addWidget(self.inventoryList)


        self.horizontalLayout_2.addWidget(self.inventoryFrame)


        self.retranslateUi(employeeDashboard)

        QMetaObject.connectSlotsByName(employeeDashboard)
    # setupUi

    def retranslateUi(self, employeeDashboard):
        employeeDashboard.setWindowTitle(QCoreApplication.translate("employeeDashboard", u"Employee Dashboard", None))
        self.inventoryButton.setText(QCoreApplication.translate("employeeDashboard", u"Inventory", None))
        self.serviceReportButton.setText(QCoreApplication.translate("employeeDashboard", u"Service Report", None))
        self.purchaseButton.setText(QCoreApplication.translate("employeeDashboard", u"Purchase", None))
        self.logOutButton.setText(QCoreApplication.translate("employeeDashboard", u"Log Out", None))
        self.searchButton.setText(QCoreApplication.translate("employeeDashboard", u"Search", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("employeeDashboard", u"Product Name...", None))
        self.inventoryTitle.setText(QCoreApplication.translate("employeeDashboard", u"INVENTORY", None))
        self.productId.setText(QCoreApplication.translate("employeeDashboard", u"Product ID", None))
        self.productName.setText(QCoreApplication.translate("employeeDashboard", u"Product Name", None))
        self.quantity.setText(QCoreApplication.translate("employeeDashboard", u"Quantity", None))
        self.price.setText(QCoreApplication.translate("employeeDashboard", u"Price", None))
        self.category.setText(QCoreApplication.translate("employeeDashboard", u"Category", None))
    # retranslateUi

