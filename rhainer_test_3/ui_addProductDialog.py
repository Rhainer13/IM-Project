# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addProductDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpinBox, QStackedWidget, QVBoxLayout, QWidget)

class Ui_AddProductDialog(object):
    def setupUi(self, AddProductDialog):
        if not AddProductDialog.objectName():
            AddProductDialog.setObjectName(u"AddProductDialog")
        AddProductDialog.resize(233, 300)
        self.verticalLayout = QVBoxLayout(AddProductDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_4 = QLabel(AddProductDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.pcPartDropdown = QComboBox(AddProductDialog)
        self.pcPartDropdown.addItem("")
        self.pcPartDropdown.addItem("")
        self.pcPartDropdown.addItem("")
        self.pcPartDropdown.setObjectName(u"pcPartDropdown")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.pcPartDropdown)


        self.verticalLayout.addLayout(self.formLayout_3)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(AddProductDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.name = QLineEdit(AddProductDialog)
        self.name.setObjectName(u"name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.name)

        self.label_2 = QLabel(AddProductDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.price = QDoubleSpinBox(AddProductDialog)
        self.price.setObjectName(u"price")
        self.price.setMinimum(1.000000000000000)
        self.price.setMaximum(99999.990000000005239)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.price)

        self.label_7 = QLabel(AddProductDialog)
        self.label_7.setObjectName(u"label_7")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_7)

        self.quantity = QSpinBox(AddProductDialog)
        self.quantity.setObjectName(u"quantity")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.quantity)


        self.verticalLayout.addLayout(self.formLayout)

        self.stackedWidget = QStackedWidget(AddProductDialog)
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

        self.coreCount = QSpinBox(self.page)
        self.coreCount.setObjectName(u"coreCount")
        self.coreCount.setMinimum(1)
        self.coreCount.setMaximum(300)

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

        self.size = QComboBox(self.page_2)
        self.size.addItem("")
        self.size.addItem("")
        self.size.addItem("")
        self.size.setObjectName(u"size")

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

        self.formFactor = QComboBox(self.page_3)
        self.formFactor.addItem("")
        self.formFactor.addItem("")
        self.formFactor.addItem("")
        self.formFactor.setObjectName(u"formFactor")

        self.formLayout_5.setWidget(0, QFormLayout.FieldRole, self.formFactor)


        self.gridLayout_4.addLayout(self.formLayout_5, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.frame = QFrame(AddProductDialog)
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


        self.retranslateUi(AddProductDialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AddProductDialog)
    # setupUi

    def retranslateUi(self, AddProductDialog):
        AddProductDialog.setWindowTitle(QCoreApplication.translate("AddProductDialog", u"Add Product", None))
        self.label_4.setText(QCoreApplication.translate("AddProductDialog", u"PC Part", None))
        self.pcPartDropdown.setItemText(0, QCoreApplication.translate("AddProductDialog", u"CPU", None))
        self.pcPartDropdown.setItemText(1, QCoreApplication.translate("AddProductDialog", u"RAM", None))
        self.pcPartDropdown.setItemText(2, QCoreApplication.translate("AddProductDialog", u"MOTHERBOARD", None))

        self.label.setText(QCoreApplication.translate("AddProductDialog", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("AddProductDialog", u"Price", None))
        self.label_7.setText(QCoreApplication.translate("AddProductDialog", u"Quantity", None))
        self.label_3.setText(QCoreApplication.translate("AddProductDialog", u"Core Count", None))
        self.label_5.setText(QCoreApplication.translate("AddProductDialog", u"Size (GB)", None))
        self.size.setItemText(0, QCoreApplication.translate("AddProductDialog", u"4", None))
        self.size.setItemText(1, QCoreApplication.translate("AddProductDialog", u"8", None))
        self.size.setItemText(2, QCoreApplication.translate("AddProductDialog", u"16", None))

        self.label_6.setText(QCoreApplication.translate("AddProductDialog", u"Form Factor", None))
        self.formFactor.setItemText(0, QCoreApplication.translate("AddProductDialog", u"ATX", None))
        self.formFactor.setItemText(1, QCoreApplication.translate("AddProductDialog", u"Micro-ATX", None))
        self.formFactor.setItemText(2, QCoreApplication.translate("AddProductDialog", u"Mini-ITX", None))

        self.confirmButton.setText(QCoreApplication.translate("AddProductDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("AddProductDialog", u"Cancel", None))
    # retranslateUi

