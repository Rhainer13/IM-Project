# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'orderDialog.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QDoubleSpinBox,
    QFormLayout, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_OrderDialog(object):
    def setupUi(self, OrderDialog):
        if not OrderDialog.objectName():
            OrderDialog.setObjectName(u"OrderDialog")
        OrderDialog.resize(942, 577)
        self.verticalLayout = QVBoxLayout(OrderDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(OrderDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.customerName = QLineEdit(OrderDialog)
        self.customerName.setObjectName(u"customerName")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.customerName)


        self.verticalLayout.addLayout(self.formLayout)

        self.cartTable = QTableWidget(OrderDialog)
        if (self.cartTable.columnCount() < 7):
            self.cartTable.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.cartTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.cartTable.setObjectName(u"cartTable")
        self.cartTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cartTable.horizontalHeader().setDefaultSectionSize(100)
        self.cartTable.horizontalHeader().setStretchLastSection(True)
        self.cartTable.verticalHeader().setVisible(False)

        self.verticalLayout.addWidget(self.cartTable)

        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(OrderDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.total = QDoubleSpinBox(OrderDialog)
        self.total.setObjectName(u"total")
        self.total.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.total)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.frame = QFrame(OrderDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.confirmOrder = QPushButton(self.frame)
        self.confirmOrder.setObjectName(u"confirmOrder")

        self.horizontalLayout.addWidget(self.confirmOrder)

        self.cancelOrder = QPushButton(self.frame)
        self.cancelOrder.setObjectName(u"cancelOrder")

        self.horizontalLayout.addWidget(self.cancelOrder)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(OrderDialog)

        QMetaObject.connectSlotsByName(OrderDialog)
    # setupUi

    def retranslateUi(self, OrderDialog):
        OrderDialog.setWindowTitle(QCoreApplication.translate("OrderDialog", u"Ongoing Orders", None))
        self.label.setText(QCoreApplication.translate("OrderDialog", u"Customer Name", None))
        ___qtablewidgetitem = self.cartTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("OrderDialog", u"Brand", None));
        ___qtablewidgetitem1 = self.cartTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("OrderDialog", u"Name", None));
        ___qtablewidgetitem2 = self.cartTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("OrderDialog", u"Category", None));
        ___qtablewidgetitem3 = self.cartTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("OrderDialog", u"Price", None));
        ___qtablewidgetitem4 = self.cartTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("OrderDialog", u"Quantity", None));
        ___qtablewidgetitem5 = self.cartTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("OrderDialog", u"Subtotal", None));
        ___qtablewidgetitem6 = self.cartTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("OrderDialog", u"Actions", None));
        self.label_2.setText(QCoreApplication.translate("OrderDialog", u"Total", None))
        self.confirmOrder.setText(QCoreApplication.translate("OrderDialog", u"Confirm Order", None))
        self.cancelOrder.setText(QCoreApplication.translate("OrderDialog", u"Cancel Order", None))
    # retranslateUi

