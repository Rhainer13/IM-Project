# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'editProductDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QDoubleSpinBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_EditProductDialog(object):
    def setupUi(self, EditProductDialog):
        if not EditProductDialog.objectName():
            EditProductDialog.setObjectName(u"EditProductDialog")
        EditProductDialog.resize(419, 465)
        self.verticalLayout = QVBoxLayout(EditProductDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(EditProductDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_3 = QLabel(EditProductDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)

        self.name = QLineEdit(EditProductDialog)
        self.name.setObjectName(u"name")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name)

        self.label_4 = QLabel(EditProductDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.price = QDoubleSpinBox(EditProductDialog)
        self.price.setObjectName(u"price")
        self.price.setMinimum(1.000000000000000)
        self.price.setMaximum(99999.990000000005239)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.price)

        self.category = QLineEdit(EditProductDialog)
        self.category.setObjectName(u"category")
        self.category.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.category)

        self.label_2 = QLabel(EditProductDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_2)

        self.quantity = QSpinBox(EditProductDialog)
        self.quantity.setObjectName(u"quantity")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.quantity)


        self.verticalLayout.addLayout(self.formLayout)

        self.frame = QFrame(EditProductDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.confirm = QPushButton(self.frame)
        self.confirm.setObjectName(u"confirm")

        self.horizontalLayout.addWidget(self.confirm)

        self.cancel = QPushButton(self.frame)
        self.cancel.setObjectName(u"cancel")

        self.horizontalLayout.addWidget(self.cancel)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(EditProductDialog)

        QMetaObject.connectSlotsByName(EditProductDialog)
    # setupUi

    def retranslateUi(self, EditProductDialog):
        EditProductDialog.setWindowTitle(QCoreApplication.translate("EditProductDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("EditProductDialog", u"Category", None))
        self.label_3.setText(QCoreApplication.translate("EditProductDialog", u"Name", None))
        self.name.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("EditProductDialog", u"Price", None))
        self.label_2.setText(QCoreApplication.translate("EditProductDialog", u"Quantity", None))
        self.confirm.setText(QCoreApplication.translate("EditProductDialog", u"Confirm", None))
        self.cancel.setText(QCoreApplication.translate("EditProductDialog", u"Cancel", None))
    # retranslateUi

