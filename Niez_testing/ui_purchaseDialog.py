# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'purchaseDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_ViewOrderDialog(object):
    def setupUi(self, purchaseDialog):
        if not purchaseDialog.objectName():
            purchaseDialog.setObjectName(u"purchaseDialog")
        purchaseDialog.resize(700, 590)
        purchaseDialog.setMaximumSize(QSize(700, 590))
        self.verticalLayout = QVBoxLayout(purchaseDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(purchaseDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label, 0, Qt.AlignLeft)

        self.lineEdit_8 = QLineEdit(self.frame)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.horizontalLayout_2.addWidget(self.lineEdit_8, 0, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(purchaseDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cartTable = QTableWidget(self.frame_2)
        if (self.cartTable.columnCount() < 6):
            self.cartTable.setColumnCount(6)
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
        self.cartTable.setObjectName(u"cartTable")
        self.cartTable.horizontalHeader().setStretchLastSection(True)
        self.cartTable.verticalHeader().setVisible(False)

        self.horizontalLayout.addWidget(self.cartTable)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(purchaseDialog)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.confirmButton = QPushButton(self.frame_3)
        self.confirmButton.setObjectName(u"confirmButton")

        self.horizontalLayout_3.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(self.frame_3)
        self.cancelButton.setObjectName(u"cancelButton")

        self.horizontalLayout_3.addWidget(self.cancelButton)


        self.verticalLayout.addWidget(self.frame_3)


        self.retranslateUi(purchaseDialog)

        QMetaObject.connectSlotsByName(purchaseDialog)
    # setupUi

    def retranslateUi(self, purchaseDialog):
        purchaseDialog.setWindowTitle(QCoreApplication.translate("purchaseDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("purchaseDialog", u"Customer Name", None))
        ___qtablewidgetitem = self.cartTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("purchaseDialog", u"Product ID", None));
        ___qtablewidgetitem1 = self.cartTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("purchaseDialog", u"Product Name", None));
        ___qtablewidgetitem2 = self.cartTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("purchaseDialog", u"Quantity", None));
        ___qtablewidgetitem3 = self.cartTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("purchaseDialog", u"Category", None));
        ___qtablewidgetitem4 = self.cartTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("purchaseDialog", u"Price", None));
        ___qtablewidgetitem5 = self.cartTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("purchaseDialog", u"Action", None));
        self.confirmButton.setText(QCoreApplication.translate("purchaseDialog", u"Confirm Order", None))
        self.cancelButton.setText(QCoreApplication.translate("purchaseDialog", u"Cancel Order", None))
    # retranslateUi

