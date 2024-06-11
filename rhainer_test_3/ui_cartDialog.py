# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cartDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_CartDialog(object):
    def setupUi(self, CartDialog):
        if not CartDialog.objectName():
            CartDialog.setObjectName(u"CartDialog")
        CartDialog.resize(541, 590)
        self.verticalLayout = QVBoxLayout(CartDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(CartDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.customerName = QLineEdit(CartDialog)
        self.customerName.setObjectName(u"customerName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.customerName)


        self.verticalLayout.addLayout(self.formLayout)

        self.cartTable = QTableWidget(CartDialog)
        if (self.cartTable.columnCount() < 4):
            self.cartTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.cartTable.setObjectName(u"cartTable")
        self.cartTable.horizontalHeader().setStretchLastSection(True)
        self.cartTable.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.cartTable)

        self.frame = QFrame(CartDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.confirmButton = QPushButton(self.frame)
        self.confirmButton.setObjectName(u"confirmButton")

        self.horizontalLayout.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(self.frame)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout.addWidget(self.cancelButton)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(CartDialog)

        QMetaObject.connectSlotsByName(CartDialog)
    # setupUi

    def retranslateUi(self, CartDialog):
        CartDialog.setWindowTitle(QCoreApplication.translate("CartDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("CartDialog", u"Customer Name", None))
        ___qtablewidgetitem = self.cartTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("CartDialog", u"Product Name", None));
        ___qtablewidgetitem1 = self.cartTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("CartDialog", u"Price", None));
        ___qtablewidgetitem2 = self.cartTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("CartDialog", u"Quantity", None));
        ___qtablewidgetitem3 = self.cartTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("CartDialog", u"Actions", None));
        self.confirmButton.setText(QCoreApplication.translate("CartDialog", u"Confirm Order", None))
        self.cancelButton.setText(QCoreApplication.translate("CartDialog", u"Cancel Order", None))
    # retranslateUi

