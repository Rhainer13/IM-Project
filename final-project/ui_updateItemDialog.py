# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateItemDialog.ui'
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

class Ui_updateItemDialog(object):
    def setupUi(self, updateItemDialog):
        if not updateItemDialog.objectName():
            updateItemDialog.setObjectName(u"updateItemDialog")
        updateItemDialog.resize(527, 320)
        self.verticalLayout_6 = QVBoxLayout(updateItemDialog)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(updateItemDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.itemName = QLabel(self.frame)
        self.itemName.setObjectName(u"itemName")

        self.horizontalLayout_9.addWidget(self.itemName)

        self.itemNameInput = QLineEdit(self.frame)
        self.itemNameInput.setObjectName(u"itemNameInput")
        self.itemNameInput.setMinimumSize(QSize(250, 0))
        self.itemNameInput.setMaxLength(30)
        self.itemNameInput.setFrame(True)

        self.horizontalLayout_9.addWidget(self.itemNameInput, 0, Qt.AlignRight)


        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.quantity = QLabel(self.frame)
        self.quantity.setObjectName(u"quantity")

        self.horizontalLayout_10.addWidget(self.quantity)

        self.quantityInput = QLineEdit(self.frame)
        self.quantityInput.setObjectName(u"quantityInput")
        self.quantityInput.setMinimumSize(QSize(250, 0))
        self.quantityInput.setMaxLength(30)

        self.horizontalLayout_10.addWidget(self.quantityInput, 0, Qt.AlignRight)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.price = QLabel(self.frame)
        self.price.setObjectName(u"price")

        self.horizontalLayout_11.addWidget(self.price)

        self.priceInput = QLineEdit(self.frame)
        self.priceInput.setObjectName(u"priceInput")
        self.priceInput.setMinimumSize(QSize(250, 0))
        self.priceInput.setMaxLength(30)

        self.horizontalLayout_11.addWidget(self.priceInput, 0, Qt.AlignRight)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.category = QLabel(self.frame)
        self.category.setObjectName(u"category")

        self.horizontalLayout_12.addWidget(self.category)

        self.categoryDropdown = QComboBox(self.frame)
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.addItem("")
        self.categoryDropdown.setObjectName(u"categoryDropdown")
        self.categoryDropdown.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_12.addWidget(self.categoryDropdown, 0, Qt.AlignRight)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_6.addWidget(self.frame)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.confirmButton = QPushButton(updateItemDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout_5.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(updateItemDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout_5.addWidget(self.cancelButton)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)


        self.retranslateUi(updateItemDialog)

        QMetaObject.connectSlotsByName(updateItemDialog)
    # setupUi

    def retranslateUi(self, updateItemDialog):
        updateItemDialog.setWindowTitle(QCoreApplication.translate("updateItemDialog", u"Update Item", None))
        self.itemName.setText(QCoreApplication.translate("updateItemDialog", u"Item Name", None))
        self.itemNameInput.setText("")
        self.itemNameInput.setPlaceholderText("")
        self.quantity.setText(QCoreApplication.translate("updateItemDialog", u"Quantity", None))
        self.quantityInput.setText("")
        self.price.setText(QCoreApplication.translate("updateItemDialog", u"Price", None))
        self.category.setText(QCoreApplication.translate("updateItemDialog", u"Category", None))
        self.categoryDropdown.setItemText(0, QCoreApplication.translate("updateItemDialog", u"CPU", None))
        self.categoryDropdown.setItemText(1, QCoreApplication.translate("updateItemDialog", u"GPU", None))
        self.categoryDropdown.setItemText(2, QCoreApplication.translate("updateItemDialog", u"Motherboard", None))
        self.categoryDropdown.setItemText(3, QCoreApplication.translate("updateItemDialog", u"RAM", None))
        self.categoryDropdown.setItemText(4, QCoreApplication.translate("updateItemDialog", u"Storage", None))
        self.categoryDropdown.setItemText(5, "")

        self.confirmButton.setText(QCoreApplication.translate("updateItemDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("updateItemDialog", u"Cancel", None))
    # retranslateUi

