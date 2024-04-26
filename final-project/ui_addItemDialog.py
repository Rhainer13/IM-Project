# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addItemDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_addItemDialog(object):
    def setupUi(self, addItemDialog):
        if not addItemDialog.objectName():
            addItemDialog.setObjectName(u"addItemDialog")
        addItemDialog.resize(500, 300)
        addItemDialog.setMinimumSize(QSize(500, 300))
        addItemDialog.setMaximumSize(QSize(500, 300))
        self.verticalLayout_2 = QVBoxLayout(addItemDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(addItemDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.itemName = QLabel(self.frame)
        self.itemName.setObjectName(u"itemName")

        self.horizontalLayout.addWidget(self.itemName)

        self.itemNameInput = QLineEdit(self.frame)
        self.itemNameInput.setObjectName(u"itemNameInput")
        self.itemNameInput.setMinimumSize(QSize(250, 0))
        self.itemNameInput.setMaxLength(30)
        self.itemNameInput.setFrame(True)

        self.horizontalLayout.addWidget(self.itemNameInput, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.quantity = QLabel(self.frame)
        self.quantity.setObjectName(u"quantity")

        self.horizontalLayout_3.addWidget(self.quantity)

        self.quantityInput = QLineEdit(self.frame)
        self.quantityInput.setObjectName(u"quantityInput")
        self.quantityInput.setMinimumSize(QSize(250, 0))
        self.quantityInput.setMaxLength(30)

        self.horizontalLayout_3.addWidget(self.quantityInput, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.price = QLabel(self.frame)
        self.price.setObjectName(u"price")

        self.horizontalLayout_4.addWidget(self.price)

        self.priceInput = QLineEdit(self.frame)
        self.priceInput.setObjectName(u"priceInput")
        self.priceInput.setMinimumSize(QSize(250, 0))
        self.priceInput.setMaxLength(30)

        self.horizontalLayout_4.addWidget(self.priceInput, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.category = QLabel(self.frame)
        self.category.setObjectName(u"category")

        self.horizontalLayout_5.addWidget(self.category)

        self.categoryDropdown = QComboBox(self.frame)
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.setObjectName(u"categoryDropdown")
        self.categoryDropdown.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_5.addWidget(self.categoryDropdown, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_2.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.confirmButton = QPushButton(addItemDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout_3.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(addItemDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout_3.addWidget(self.cancelButton)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)


        self.retranslateUi(addItemDialog)

        QMetaObject.connectSlotsByName(addItemDialog)
    # setupUi

    def retranslateUi(self, addItemDialog):
        addItemDialog.setWindowTitle(QCoreApplication.translate("addItemDialog", u"Add Item", None))
        self.itemName.setText(QCoreApplication.translate("addItemDialog", u"Item Name", None))
        self.itemNameInput.setText("")
        self.itemNameInput.setPlaceholderText("")
        self.quantity.setText(QCoreApplication.translate("addItemDialog", u"Quantity", None))
        self.quantityInput.setText("")
        self.price.setText(QCoreApplication.translate("addItemDialog", u"Price", None))
        self.category.setText(QCoreApplication.translate("addItemDialog", u"Category", None))
        self.categoryDropdown.setItemText(0, QCoreApplication.translate("addItemDialog", u"CPU", None))
        self.categoryDropdown.setItemText(1, QCoreApplication.translate("addItemDialog", u"GPU", None))
        self.categoryDropdown.setItemText(2, QCoreApplication.translate("addItemDialog", u"Motherboard", None))
        self.categoryDropdown.setItemText(3, QCoreApplication.translate("addItemDialog", u"RAM", None))
        self.categoryDropdown.setItemText(4, QCoreApplication.translate("addItemDialog", u"Storage", None))
        self.categoryDropdown.setItemText(5, "")

        self.confirmButton.setText(QCoreApplication.translate("addItemDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("addItemDialog", u"Cancel", None))
    # retranslateUi

