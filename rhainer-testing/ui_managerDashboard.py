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

class Ui_ManagerDashboard(object):
    def setupUi(self, ManagerDashboard):
        if not ManagerDashboard.objectName():
            ManagerDashboard.setObjectName(u"ManagerDashboard")
        ManagerDashboard.resize(1072, 632)
        self.horizontalLayout = QHBoxLayout(ManagerDashboard)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(ManagerDashboard)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.inventoryButton = QPushButton(self.frame)
        self.inventoryButton.setObjectName(u"inventoryButton")

        self.verticalLayout.addWidget(self.inventoryButton)

        self.logOutButton = QPushButton(self.frame)
        self.logOutButton.setObjectName(u"logOutButton")

        self.verticalLayout.addWidget(self.logOutButton)


        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(ManagerDashboard)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.addProductButton = QPushButton(self.frame_2)
        self.addProductButton.setObjectName(u"addProductButton")

        self.gridLayout.addWidget(self.addProductButton, 1, 0, 1, 1)

        self.searchBar = QLineEdit(self.frame_2)
        self.searchBar.setObjectName(u"searchBar")

        self.gridLayout.addWidget(self.searchBar, 1, 3, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.refreshButton = QPushButton(self.frame_2)
        self.refreshButton.setObjectName(u"refreshButton")

        self.gridLayout.addWidget(self.refreshButton, 1, 1, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)

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
        self.productTable.horizontalHeader().setStretchLastSection(True)
        self.productTable.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.productTable)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(ManagerDashboard)

        QMetaObject.connectSlotsByName(ManagerDashboard)
    # setupUi

    def retranslateUi(self, ManagerDashboard):
        ManagerDashboard.setWindowTitle(QCoreApplication.translate("ManagerDashboard", u"Form", None))
        self.inventoryButton.setText(QCoreApplication.translate("ManagerDashboard", u"Inventory", None))
        self.logOutButton.setText(QCoreApplication.translate("ManagerDashboard", u"Log Out", None))
        self.addProductButton.setText(QCoreApplication.translate("ManagerDashboard", u"Add Product", None))
        self.searchBar.setPlaceholderText(QCoreApplication.translate("ManagerDashboard", u"Search", None))
        self.label.setText(QCoreApplication.translate("ManagerDashboard", u"INVENTORY", None))
        self.refreshButton.setText(QCoreApplication.translate("ManagerDashboard", u"Refresh", None))
        ___qtablewidgetitem = self.productTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ManagerDashboard", u"Product Id", None));
        ___qtablewidgetitem1 = self.productTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ManagerDashboard", u"Product Name", None));
        ___qtablewidgetitem2 = self.productTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ManagerDashboard", u"Product Quantity", None));
        ___qtablewidgetitem3 = self.productTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ManagerDashboard", u"Product Price", None));
        ___qtablewidgetitem4 = self.productTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ManagerDashboard", u"Category", None));
        ___qtablewidgetitem5 = self.productTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ManagerDashboard", u"Actions", None));
    # retranslateUi

