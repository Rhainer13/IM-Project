# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailsDialog.ui'
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
    QGridLayout, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_DetailsDialog(object):
    def setupUi(self, DetailsDialog):
        if not DetailsDialog.objectName():
            DetailsDialog.setObjectName(u"DetailsDialog")
        DetailsDialog.resize(289, 245)
        self.verticalLayout = QVBoxLayout(DetailsDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DetailsDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.name = QLineEdit(DetailsDialog)
        self.name.setObjectName(u"name")
        self.name.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name)

        self.label_2 = QLabel(DetailsDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.price = QLineEdit(DetailsDialog)
        self.price.setObjectName(u"price")
        self.price.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.price)


        self.verticalLayout.addLayout(self.formLayout)

        self.stackedWidget = QStackedWidget(DetailsDialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.coreCount = QLineEdit(self.page)
        self.coreCount.setObjectName(u"coreCount")
        self.coreCount.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.coreCount)


        self.gridLayout_2.addLayout(self.formLayout_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_3 = QGridLayout(self.page_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_5)

        self.size = QLineEdit(self.page_2)
        self.size.setObjectName(u"size")
        self.size.setReadOnly(True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.size)


        self.gridLayout_3.addLayout(self.formLayout_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_4 = QGridLayout(self.page_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.formLayout_5 = QFormLayout()
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.label_6 = QLabel(self.page_3)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_5.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.formFactor = QLineEdit(self.page_3)
        self.formFactor.setObjectName(u"formFactor")
        self.formFactor.setReadOnly(True)

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.formFactor)


        self.gridLayout_4.addLayout(self.formLayout_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.frame = QFrame(DetailsDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.closeButton = QPushButton(self.frame)
        self.closeButton.setObjectName(u"closeButton")

        self.horizontalLayout.addWidget(self.closeButton)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(DetailsDialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DetailsDialog)
    # setupUi

    def retranslateUi(self, DetailsDialog):
        DetailsDialog.setWindowTitle(QCoreApplication.translate("DetailsDialog", u"Product Details", None))
        self.label.setText(QCoreApplication.translate("DetailsDialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("DetailsDialog", u"Price", None))
        self.label_3.setText(QCoreApplication.translate("DetailsDialog", u"Core Count", None))
        self.label_5.setText(QCoreApplication.translate("DetailsDialog", u"Size (GB)", None))
        self.label_6.setText(QCoreApplication.translate("DetailsDialog", u"Form Factor", None))
        self.closeButton.setText(QCoreApplication.translate("DetailsDialog", u"Close", None))
    # retranslateUi

