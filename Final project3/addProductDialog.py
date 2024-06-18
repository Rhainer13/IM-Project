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
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpinBox, QStackedWidget, QVBoxLayout,
    QWidget)

class Ui_AddProductDialog(object):
    def setupUi(self, AddProductDialog):
        if not AddProductDialog.objectName():
            AddProductDialog.setObjectName(u"AddProductDialog")
        AddProductDialog.resize(391, 386)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AddProductDialog.sizePolicy().hasHeightForWidth())
        AddProductDialog.setSizePolicy(sizePolicy)
        AddProductDialog.setStyleSheet(u"QWidget{\n"
"background-color:rgb(183, 181, 151);\n"
"}")
        AddProductDialog.setSizeGripEnabled(True)
        self.verticalLayout = QVBoxLayout(AddProductDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(AddProductDialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.category = QComboBox(AddProductDialog)
        self.category.addItem("")
        self.category.addItem("")
        self.category.addItem("")
        self.category.setObjectName(u"category")
        self.category.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"\n"
"\n"
"font-size: 16px;\n"
"padding:2px;\n"
"text-align: center;\n"
"\n"
"\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.category)

        self.label_3 = QLabel(AddProductDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.name = QLineEdit(AddProductDialog)
        self.name.setObjectName(u"name")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)
        self.name.setMinimumSize(QSize(0, 0))
        self.name.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"\n"
"\n"
"font-size: 16px;\n"
"padding:2px;\n"
"text-align: center;\n"
"\n"
"\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"")
        self.name.setMaxLength(25)
        self.name.setClearButtonEnabled(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name)

        self.label_4 = QLabel(AddProductDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.price = QDoubleSpinBox(AddProductDialog)
        self.price.setObjectName(u"price")
        self.price.setStyleSheet(u"QDoubleSpinBox{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"\n"
"\n"
"font-size: 16px;\n"
"padding:2px;\n"
"text-align: center;\n"
"\n"
"\n"
"}\n"
"\n"
"QDoubleSpinBox:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"\n"
"")
        self.price.setMinimum(1.000000000000000)
        self.price.setMaximum(99999.990000000005239)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.price)

        self.label_10 = QLabel(AddProductDialog)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_10)

        self.quantity = QSpinBox(AddProductDialog)
        self.quantity.setObjectName(u"quantity")
        self.quantity.setStyleSheet(u"QSpinBox{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"\n"
"\n"
"font-size: 16px;\n"
"padding:2px;\n"
"text-align: center;\n"
"\n"
"\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.quantity)


        self.verticalLayout.addLayout(self.formLayout)

        self.stackedWidget = QStackedWidget(AddProductDialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.cpuBrand = QComboBox(self.page)
        self.cpuBrand.addItem("")
        self.cpuBrand.addItem("")
        self.cpuBrand.setObjectName(u"cpuBrand")
        self.cpuBrand.setStyleSheet(u"QComboBox{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"\n"
"\n"
"font-size: 16px;\n"
"padding:2px;\n"
"text-align: center;\n"
"\n"
"\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.cpuBrand)

        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.coreCount = QSpinBox(self.page)
        self.coreCount.setObjectName(u"coreCount")
        self.coreCount.setStyleSheet(u"QSpinBox{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"\n"
"\n"
"font-size: 16px;\n"
"padding:2px;\n"
"text-align: center;\n"
"\n"
"\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"\n"
"")
        self.coreCount.setMinimum(2)
        self.coreCount.setMaximum(300)
        self.coreCount.setSingleStep(2)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.coreCount)


        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.ramBrand = QComboBox(self.page_2)
        self.ramBrand.addItem("")
        self.ramBrand.addItem("")
        self.ramBrand.addItem("")
        self.ramBrand.addItem("")
        self.ramBrand.addItem("")
        self.ramBrand.addItem("")
        self.ramBrand.addItem("")
        self.ramBrand.addItem("")
        self.ramBrand.addItem("")
        self.ramBrand.addItem("")
        self.ramBrand.setObjectName(u"ramBrand")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.ramBrand)

        self.ramSize = QComboBox(self.page_2)
        self.ramSize.addItem("")
        self.ramSize.addItem("")
        self.ramSize.addItem("")
        self.ramSize.setObjectName(u"ramSize")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.ramSize)

        self.label_7 = QLabel(self.page_2)
        self.label_7.setObjectName(u"label_7")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_7)


        self.gridLayout_2.addLayout(self.formLayout_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_8 = QLabel(self.page_3)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_8)

        self.mbBrand = QComboBox(self.page_3)
        self.mbBrand.addItem("")
        self.mbBrand.addItem("")
        self.mbBrand.addItem("")
        self.mbBrand.addItem("")
        self.mbBrand.addItem("")
        self.mbBrand.addItem("")
        self.mbBrand.setObjectName(u"mbBrand")

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.mbBrand)

        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_9)

        self.mbSize = QComboBox(self.page_3)
        self.mbSize.addItem("")
        self.mbSize.addItem("")
        self.mbSize.addItem("")
        self.mbSize.setObjectName(u"mbSize")

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.mbSize)


        self.gridLayout_3.addLayout(self.formLayout_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.frame = QFrame(AddProductDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.confirm = QPushButton(self.frame)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(218, 211, 190);\n"
"color: black;\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"font-size: 16px;\n"
"padding:2px;\n"
"text-align: center;\n"
"margin-left: 25px;\n"
"margin-right:25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 0.3);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 0.1);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.confirm)

        self.cancel = QPushButton(self.frame)
        self.cancel.setObjectName(u"cancel")
        self.cancel.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(218, 211, 190);\n"
"\n"
"color: black;\n"
"border: 1px solid rgba(255, 255, 255, 0.5);\n"
"border-radius: 10px;\n"
"font-size: 16px;\n"
"padding:2px;\n"
"text-align: center;\n"
"margin-left: 25px;\n"
"margin-right:25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #e74c3c;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"background-color: #e74c3c;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.cancel)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(AddProductDialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(AddProductDialog)
    # setupUi

    def retranslateUi(self, AddProductDialog):
        AddProductDialog.setWindowTitle(QCoreApplication.translate("AddProductDialog", u"Add Product", None))
        self.label.setText(QCoreApplication.translate("AddProductDialog", u"Category", None))
        self.category.setItemText(0, QCoreApplication.translate("AddProductDialog", u"CPU", None))
        self.category.setItemText(1, QCoreApplication.translate("AddProductDialog", u"RAM", None))
        self.category.setItemText(2, QCoreApplication.translate("AddProductDialog", u"Motherboard", None))

        self.label_3.setText(QCoreApplication.translate("AddProductDialog", u"Name", None))
        self.name.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("AddProductDialog", u"Price", None))
        self.label_10.setText(QCoreApplication.translate("AddProductDialog", u"Quantity", None))
        self.label_2.setText(QCoreApplication.translate("AddProductDialog", u"Brand", None))
        self.cpuBrand.setItemText(0, QCoreApplication.translate("AddProductDialog", u"Intel", None))
        self.cpuBrand.setItemText(1, QCoreApplication.translate("AddProductDialog", u"AMD", None))

        self.label_5.setText(QCoreApplication.translate("AddProductDialog", u"Core Count", None))
        self.label_6.setText(QCoreApplication.translate("AddProductDialog", u"Brand", None))
        self.ramBrand.setItemText(0, QCoreApplication.translate("AddProductDialog", u"ADATA", None))
        self.ramBrand.setItemText(1, QCoreApplication.translate("AddProductDialog", u"Corsair", None))
        self.ramBrand.setItemText(2, QCoreApplication.translate("AddProductDialog", u"Crucial", None))
        self.ramBrand.setItemText(3, QCoreApplication.translate("AddProductDialog", u"G.Skill", None))
        self.ramBrand.setItemText(4, QCoreApplication.translate("AddProductDialog", u"HyperX", None))
        self.ramBrand.setItemText(5, QCoreApplication.translate("AddProductDialog", u"Kingston", None))
        self.ramBrand.setItemText(6, QCoreApplication.translate("AddProductDialog", u"Micron", None))
        self.ramBrand.setItemText(7, QCoreApplication.translate("AddProductDialog", u"Patriot Memory", None))
        self.ramBrand.setItemText(8, QCoreApplication.translate("AddProductDialog", u"Samsung", None))
        self.ramBrand.setItemText(9, QCoreApplication.translate("AddProductDialog", u"SK hynix", None))

        self.ramSize.setItemText(0, QCoreApplication.translate("AddProductDialog", u"4", None))
        self.ramSize.setItemText(1, QCoreApplication.translate("AddProductDialog", u"8", None))
        self.ramSize.setItemText(2, QCoreApplication.translate("AddProductDialog", u"16", None))

        self.label_7.setText(QCoreApplication.translate("AddProductDialog", u"Size (GB)", None))
        self.label_8.setText(QCoreApplication.translate("AddProductDialog", u"Brand", None))
        self.mbBrand.setItemText(0, QCoreApplication.translate("AddProductDialog", u"ASRock", None))
        self.mbBrand.setItemText(1, QCoreApplication.translate("AddProductDialog", u"Asus", None))
        self.mbBrand.setItemText(2, QCoreApplication.translate("AddProductDialog", u"Biostar", None))
        self.mbBrand.setItemText(3, QCoreApplication.translate("AddProductDialog", u"EVGA", None))
        self.mbBrand.setItemText(4, QCoreApplication.translate("AddProductDialog", u"Gigabyte", None))
        self.mbBrand.setItemText(5, QCoreApplication.translate("AddProductDialog", u"MSI", None))

        self.label_9.setText(QCoreApplication.translate("AddProductDialog", u"Form Factor", None))
        self.mbSize.setItemText(0, QCoreApplication.translate("AddProductDialog", u"ATX", None))
        self.mbSize.setItemText(1, QCoreApplication.translate("AddProductDialog", u"Micro-ATX", None))
        self.mbSize.setItemText(2, QCoreApplication.translate("AddProductDialog", u"Mini-ITX", None))

        self.confirm.setText(QCoreApplication.translate("AddProductDialog", u"Confirm", None))
        self.cancel.setText(QCoreApplication.translate("AddProductDialog", u"Cancel", None))
    # retranslateUi

