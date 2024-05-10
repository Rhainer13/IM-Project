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
    QSizePolicy, QSpacerItem, QStackedWidget, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

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
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_3 = QFrame(self.page_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)

        self.addEmployeeButton = QPushButton(self.frame_3)
        self.addEmployeeButton.setObjectName(u"addEmployeeButton")

        self.gridLayout_2.addWidget(self.addEmployeeButton, 1, 0, 1, 1)

        self.searchBar_2 = QLineEdit(self.frame_3)
        self.searchBar_2.setObjectName(u"searchBar_2")

        self.gridLayout_2.addWidget(self.searchBar_2, 1, 3, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.refreshButton_2 = QPushButton(self.frame_3)
        self.refreshButton_2.setObjectName(u"refreshButton_2")

        self.gridLayout_2.addWidget(self.refreshButton_2, 1, 1, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_3)

        self.employeeTable = QTableWidget(self.page_2)
        if (self.employeeTable.columnCount() < 7):
            self.employeeTable.setColumnCount(7)
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
        __qtablewidgetitem12 = QTableWidgetItem()
        self.employeeTable.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        self.employeeTable.setObjectName(u"employeeTable")
        self.employeeTable.horizontalHeader().setStretchLastSection(True)
        self.employeeTable.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.employeeTable)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.page_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(ManagerDashboard)

        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ManagerDashboard)
    # setupUi

    def retranslateUi(self, ManagerDashboard):
        ManagerDashboard.setWindowTitle(QCoreApplication.translate("ManagerDashboard", u"Form", None))
        self.inventoryButton.setText(QCoreApplication.translate("ManagerDashboard", u"Inventory", None))
        self.employeeButton.setText(QCoreApplication.translate("ManagerDashboard", u"Employee", None))
        self.historyButton.setText(QCoreApplication.translate("ManagerDashboard", u"History", None))
        self.serviceReportButton.setText(QCoreApplication.translate("ManagerDashboard", u"Service Report", None))
        self.purchaseReportButton.setText(QCoreApplication.translate("ManagerDashboard", u"Purchase Report", None))
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
        self.addEmployeeButton.setText(QCoreApplication.translate("ManagerDashboard", u"Add Employe", None))
        self.searchBar_2.setPlaceholderText(QCoreApplication.translate("ManagerDashboard", u"Search", None))
        self.label_2.setText(QCoreApplication.translate("ManagerDashboard", u"EMPLOYEE", None))
        self.refreshButton_2.setText(QCoreApplication.translate("ManagerDashboard", u"Refresh", None))
        ___qtablewidgetitem6 = self.employeeTable.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ManagerDashboard", u"Employee Id", None));
        ___qtablewidgetitem7 = self.employeeTable.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ManagerDashboard", u"Employee Name", None));
        ___qtablewidgetitem8 = self.employeeTable.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ManagerDashboard", u"Date Hired", None));
        ___qtablewidgetitem9 = self.employeeTable.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ManagerDashboard", u"Address", None));
        ___qtablewidgetitem10 = self.employeeTable.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("ManagerDashboard", u"Contact", None));
        ___qtablewidgetitem11 = self.employeeTable.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("ManagerDashboard", u"Charge", None));
        ___qtablewidgetitem12 = self.employeeTable.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("ManagerDashboard", u"Action", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("ManagerDashboard", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("ManagerDashboard", u"Tab 2", None))
    # retranslateUi

