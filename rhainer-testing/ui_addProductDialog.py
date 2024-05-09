# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addProductDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QFrame, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_AddProductDialog(object):
    def setupUi(self, AddProductDialog):
        if not AddProductDialog.objectName():
            AddProductDialog.setObjectName(u"AddProductDialog")
        AddProductDialog.resize(483, 316)
        AddProductDialog.setMaximumSize(QSize(483, 316))
        self.verticalLayout_2 = QVBoxLayout(AddProductDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(AddProductDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.productNameInput = QLineEdit(AddProductDialog)
        self.productNameInput.setObjectName(u"productNameInput")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.productNameInput)

        self.label_2 = QLabel(AddProductDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.quantityInput = QLineEdit(AddProductDialog)
        self.quantityInput.setObjectName(u"quantityInput")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.quantityInput)

        self.label_3 = QLabel(AddProductDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.priceInput = QLineEdit(AddProductDialog)
        self.priceInput.setObjectName(u"priceInput")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.priceInput)

        self.label_4 = QLabel(AddProductDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.categoryChoice = QComboBox(AddProductDialog)
        self.categoryChoice.addItem("")
        self.categoryChoice.addItem("")
        self.categoryChoice.addItem("")
        self.categoryChoice.addItem("")
        self.categoryChoice.addItem("")
        self.categoryChoice.addItem("")
        self.categoryChoice.addItem("")
        self.categoryChoice.setObjectName(u"categoryChoice")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.categoryChoice)


        self.verticalLayout_2.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame = QFrame(AddProductDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.confirmButton = QPushButton(self.frame)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(self.frame)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout.addWidget(self.cancelButton)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(AddProductDialog)

        QMetaObject.connectSlotsByName(AddProductDialog)
    # setupUi

    def retranslateUi(self, AddProductDialog):
        AddProductDialog.setWindowTitle(QCoreApplication.translate("AddProductDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("AddProductDialog", u"Product Name", None))
        self.label_2.setText(QCoreApplication.translate("AddProductDialog", u"Quantity", None))
        self.label_3.setText(QCoreApplication.translate("AddProductDialog", u"Price", None))
        self.label_4.setText(QCoreApplication.translate("AddProductDialog", u"Category", None))
        self.categoryChoice.setItemText(0, QCoreApplication.translate("AddProductDialog", u"CPU", None))
        self.categoryChoice.setItemText(1, QCoreApplication.translate("AddProductDialog", u"GPU", None))
        self.categoryChoice.setItemText(2, QCoreApplication.translate("AddProductDialog", u"RAM", None))
        self.categoryChoice.setItemText(3, QCoreApplication.translate("AddProductDialog", u"Motherboard", None))
        self.categoryChoice.setItemText(4, QCoreApplication.translate("AddProductDialog", u"Power Supply", None))
        self.categoryChoice.setItemText(5, QCoreApplication.translate("AddProductDialog", u"Fan Coller", None))
        self.categoryChoice.setItemText(6, QCoreApplication.translate("AddProductDialog", u"Tower Case", None))

        self.confirmButton.setText(QCoreApplication.translate("AddProductDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("AddProductDialog", u"Cancel", None))
    # retranslateUi

