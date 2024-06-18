# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deleteProductDialog.ui'
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

class Ui_DeleteProductDialog(object):
    def setupUi(self, DeleteProductDialog):
        if not DeleteProductDialog.objectName():
            DeleteProductDialog.setObjectName(u"DeleteProductDialog")
        DeleteProductDialog.resize(318, 336)
        DeleteProductDialog.setStyleSheet(u"QWidget{\n"
"background-color:rgb(183, 181, 151);\n"
"}")
        self.verticalLayout = QVBoxLayout(DeleteProductDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(DeleteProductDialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel {\n"
"    font: 700 ;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(DeleteProductDialog)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.category = QLineEdit(DeleteProductDialog)
        self.category.setObjectName(u"category")
        self.category.setStyleSheet(u"QLineEdit{\n"
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
"\n"
"")
        self.category.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.category)

        self.label_3 = QLabel(DeleteProductDialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.name = QLineEdit(DeleteProductDialog)
        self.name.setObjectName(u"name")
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
"\n"
"")
        self.name.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name)

        self.label_4 = QLabel(DeleteProductDialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.price = QLineEdit(DeleteProductDialog)
        self.price.setObjectName(u"price")
        self.price.setStyleSheet(u"QLineEdit{\n"
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
"\n"
"")
        self.price.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.price)


        self.verticalLayout.addLayout(self.formLayout)

        self.stackedWidget = QStackedWidget(DeleteProductDialog)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel {\n"
"    font: 800;\n"
"    color: black; /* Sets the font color to black */\n"
"}\n"
"")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_7)

        self.cpuBrand = QLineEdit(self.page)
        self.cpuBrand.setObjectName(u"cpuBrand")
        self.cpuBrand.setStyleSheet(u"QLineEdit{\n"
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
        self.cpuBrand.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.cpuBrand)

        self.coreCount = QLineEdit(self.page)
        self.coreCount.setObjectName(u"coreCount")
        self.coreCount.setStyleSheet(u"QLineEdit{\n"
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
        self.coreCount.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.coreCount)


        self.gridLayout.addLayout(self.formLayout_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_2 = QGridLayout(self.page_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_2 = QLabel(self.page_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.ramBrand = QLineEdit(self.page_2)
        self.ramBrand.setObjectName(u"ramBrand")
        self.ramBrand.setReadOnly(True)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.ramBrand)

        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.ramSize = QLineEdit(self.page_2)
        self.ramSize.setObjectName(u"ramSize")
        self.ramSize.setReadOnly(True)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.ramSize)


        self.gridLayout_2.addLayout(self.formLayout_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_3 = QGridLayout(self.page_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.formLayout_4 = QFormLayout()
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")

        self.formLayout_4.setWidget(0, QFormLayout.LabelRole, self.label_9)

        self.mbBrand = QLineEdit(self.page_3)
        self.mbBrand.setObjectName(u"mbBrand")
        self.mbBrand.setReadOnly(True)

        self.formLayout_4.setWidget(0, QFormLayout.FieldRole, self.mbBrand)

        self.label_10 = QLabel(self.page_3)
        self.label_10.setObjectName(u"label_10")

        self.formLayout_4.setWidget(1, QFormLayout.LabelRole, self.label_10)

        self.mbSize = QLineEdit(self.page_3)
        self.mbSize.setObjectName(u"mbSize")
        self.mbSize.setReadOnly(True)

        self.formLayout_4.setWidget(1, QFormLayout.FieldRole, self.mbSize)


        self.gridLayout_3.addLayout(self.formLayout_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)

        self.verticalLayout.addWidget(self.stackedWidget)

        self.frame = QFrame(DeleteProductDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.confirm = QPushButton(self.frame)
        self.confirm.setObjectName(u"confirm")
        self.confirm.setStyleSheet(u"QPushButton{\n"
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
"                    background-color: #2980b9; /* Darker blue on hover */\n"
"                }\n"
"                QPushButton:pressed {\n"
"                    background-color: #1f618d; /* Even darker blue when pressed */\n"
"                }")

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


        self.retranslateUi(DeleteProductDialog)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(DeleteProductDialog)
    # setupUi

    def retranslateUi(self, DeleteProductDialog):
        DeleteProductDialog.setWindowTitle(QCoreApplication.translate("DeleteProductDialog", u"Delete Product", None))
        self.label_6.setText(QCoreApplication.translate("DeleteProductDialog", u"Are you sure you want to delete?", None))
        self.label.setText(QCoreApplication.translate("DeleteProductDialog", u"Category", None))
        self.label_3.setText(QCoreApplication.translate("DeleteProductDialog", u"Name", None))
        self.name.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("DeleteProductDialog", u"Price", None))
        self.label_5.setText(QCoreApplication.translate("DeleteProductDialog", u"Core Count", None))
        self.label_7.setText(QCoreApplication.translate("DeleteProductDialog", u"Brand", None))
        self.label_2.setText(QCoreApplication.translate("DeleteProductDialog", u"Brand", None))
        self.label_8.setText(QCoreApplication.translate("DeleteProductDialog", u"Size (GB)", None))
        self.label_9.setText(QCoreApplication.translate("DeleteProductDialog", u"Brand", None))
        self.label_10.setText(QCoreApplication.translate("DeleteProductDialog", u"Form Factor", None))
        self.confirm.setText(QCoreApplication.translate("DeleteProductDialog", u"Confirm", None))
        self.cancel.setText(QCoreApplication.translate("DeleteProductDialog", u"Cancel", None))
    # retranslateUi

