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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_AdminPage(object):
    def setupUi(self, AdminPage):
        if not AdminPage.objectName():
            AdminPage.setObjectName(u"AdminPage")
        AdminPage.resize(1007, 600)
        self.horizontalLayout = QHBoxLayout(AdminPage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(AdminPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logOut = QPushButton(self.frame)
        self.logOut.setObjectName(u"logOut")

        self.verticalLayout.addWidget(self.logOut)


        self.horizontalLayout.addWidget(self.frame)

        self.stackedWidget = QStackedWidget(AdminPage)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.addProduct = QPushButton(self.page)
        self.addProduct.setObjectName(u"addProduct")

        self.verticalLayout_2.addWidget(self.addProduct)

        self.inventoryTable = QTableWidget(self.page)
        if (self.inventoryTable.columnCount() < 5):
            self.inventoryTable.setColumnCount(5)
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
        self.inventoryTable.setObjectName(u"inventoryTable")
        self.inventoryTable.horizontalHeader().setProperty("showSortIndicator", False)
        self.inventoryTable.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout_2.addWidget(self.inventoryTable)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout.addWidget(self.stackedWidget)


        self.retranslateUi(AdminPage)

        QMetaObject.connectSlotsByName(AdminPage)
    # setupUi

    def retranslateUi(self, AdminPage):
        AdminPage.setWindowTitle(QCoreApplication.translate("AdminPage", u"Form", None))
        self.logOut.setText(QCoreApplication.translate("AdminPage", u"Log Out", None))
        self.addProduct.setText(QCoreApplication.translate("AdminPage", u"Add Product", None))
        ___qtablewidgetitem = self.inventoryTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("AdminPage", u"Brand", None));
        ___qtablewidgetitem1 = self.inventoryTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("AdminPage", u"Name", None));
        ___qtablewidgetitem2 = self.inventoryTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("AdminPage", u"Price", None));
        ___qtablewidgetitem3 = self.inventoryTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("AdminPage", u"Quantity", None));
        ___qtablewidgetitem4 = self.inventoryTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("AdminPage", u"Actions", None));
    # retranslateUi

