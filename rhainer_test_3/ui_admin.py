# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
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
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QStackedWidget, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_AdminPage(object):
    def setupUi(self, AdminPage):
        if not AdminPage.objectName():
            AdminPage.setObjectName(u"AdminPage")
        AdminPage.resize(1097, 730)
        self.horizontalLayout = QHBoxLayout(AdminPage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(AdminPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.inventoryButton = QPushButton(self.frame)
        self.inventoryButton.setObjectName(u"inventoryButton")

        self.verticalLayout.addWidget(self.inventoryButton)

        self.historyButton = QPushButton(self.frame)
        self.historyButton.setObjectName(u"historyButton")

        self.verticalLayout.addWidget(self.historyButton)

        self.viewOrderButton = QPushButton(self.frame)
        self.viewOrderButton.setObjectName(u"viewOrderButton")

        self.verticalLayout.addWidget(self.viewOrderButton)


        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(AdminPage)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.addProductButton = QPushButton(self.page)
        self.addProductButton.setObjectName(u"addProductButton")

        self.verticalLayout_2.addWidget(self.addProductButton)

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
        self.inventoryTable.horizontalHeader().setDefaultSectionSize(150)
        self.inventoryTable.horizontalHeader().setStretchLastSection(True)
        self.inventoryTable.verticalHeader().setVisible(False)

        self.verticalLayout_2.addWidget(self.inventoryTable)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout = QGridLayout(self.page_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.page_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)

        self.purchaseHistoryTable = QTableWidget(self.tab)
        if (self.purchaseHistoryTable.columnCount() < 7):
            self.purchaseHistoryTable.setColumnCount(7)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.purchaseHistoryTable.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.purchaseHistoryTable.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.purchaseHistoryTable.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.purchaseHistoryTable.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.purchaseHistoryTable.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.purchaseHistoryTable.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.purchaseHistoryTable.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        self.purchaseHistoryTable.setObjectName(u"purchaseHistoryTable")

        self.verticalLayout_3.addWidget(self.purchaseHistoryTable)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(AdminPage)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AdminPage)
    # setupUi

    def retranslateUi(self, AdminPage):
        AdminPage.setWindowTitle(QCoreApplication.translate("AdminPage", u"Admin Page", None))
        self.inventoryButton.setText(QCoreApplication.translate("AdminPage", u"Inventory", None))
        self.historyButton.setText(QCoreApplication.translate("AdminPage", u"History", None))
        self.viewOrderButton.setText(QCoreApplication.translate("AdminPage", u"View Order", None))
        self.addProductButton.setText(QCoreApplication.translate("AdminPage", u"Add Product", None))
        ___qtablewidgetitem = self.inventoryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AdminPage", u"Product Name", None));
        ___qtablewidgetitem1 = self.inventoryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AdminPage", u"PC Part", None));
        ___qtablewidgetitem2 = self.inventoryTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AdminPage", u"Price", None));
        ___qtablewidgetitem3 = self.inventoryTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AdminPage", u"Quantity", None));
        ___qtablewidgetitem4 = self.inventoryTable.horizontalHeaderItem(5)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AdminPage", u"Actions", None));
        self.label.setText(QCoreApplication.translate("AdminPage", u"Purchase History", None))
        ___qtablewidgetitem5 = self.purchaseHistoryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("AdminPage", u"Date", None));
        ___qtablewidgetitem6 = self.purchaseHistoryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("AdminPage", u"Customer Name", None));
        ___qtablewidgetitem7 = self.purchaseHistoryTable.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("AdminPage", u"Product Name", None));
        ___qtablewidgetitem8 = self.purchaseHistoryTable.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("AdminPage", u"PC Part", None));
        ___qtablewidgetitem9 = self.purchaseHistoryTable.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("AdminPage", u"Price", None));
        ___qtablewidgetitem10 = self.purchaseHistoryTable.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("AdminPage", u"Quantity", None));
        ___qtablewidgetitem11 = self.purchaseHistoryTable.horizontalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("AdminPage", u"Total", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("AdminPage", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("AdminPage", u"Tab 2", None))
    # retranslateUi

