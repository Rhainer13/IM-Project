# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addEmployeeDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_AddEmployeeDialog(object):
    def setupUi(self, AddEmployeeDialog):
        if not AddEmployeeDialog.objectName():
            AddEmployeeDialog.setObjectName(u"AddEmployeeDialog")
        AddEmployeeDialog.resize(610, 381)
        self.verticalLayout = QVBoxLayout(AddEmployeeDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.employeeName = QLabel(AddEmployeeDialog)
        self.employeeName.setObjectName(u"employeeName")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.employeeName)

        self.employeeNameInput = QLineEdit(AddEmployeeDialog)
        self.employeeNameInput.setObjectName(u"employeeNameInput")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.employeeNameInput)

        self.dateHired = QLabel(AddEmployeeDialog)
        self.dateHired.setObjectName(u"dateHired")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.dateHired)

        self.dateHiredInput = QLineEdit(AddEmployeeDialog)
        self.dateHiredInput.setObjectName(u"dateHiredInput")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dateHiredInput)

        self.address = QLabel(AddEmployeeDialog)
        self.address.setObjectName(u"address")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.address)

        self.addressInput = QLineEdit(AddEmployeeDialog)
        self.addressInput.setObjectName(u"addressInput")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.addressInput)

        self.contact = QLabel(AddEmployeeDialog)
        self.contact.setObjectName(u"contact")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.contact)

        self.contactInput = QLineEdit(AddEmployeeDialog)
        self.contactInput.setObjectName(u"contactInput")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.contactInput)

        self.charge = QLabel(AddEmployeeDialog)
        self.charge.setObjectName(u"charge")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.charge)

        self.chargeInput = QLineEdit(AddEmployeeDialog)
        self.chargeInput.setObjectName(u"chargeInput")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.chargeInput)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.confirmButton = QPushButton(AddEmployeeDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(AddEmployeeDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout.addWidget(self.cancelButton)


        self.retranslateUi(AddEmployeeDialog)

        QMetaObject.connectSlotsByName(AddEmployeeDialog)
    # setupUi

    def retranslateUi(self, AddEmployeeDialog):
        AddEmployeeDialog.setWindowTitle(QCoreApplication.translate("AddEmployeeDialog", u"Dialog", None))
        self.employeeName.setText(QCoreApplication.translate("AddEmployeeDialog", u"Employee Name", None))
        self.dateHired.setText(QCoreApplication.translate("AddEmployeeDialog", u"Date Hired", None))
        self.address.setText(QCoreApplication.translate("AddEmployeeDialog", u"Address", None))
        self.contact.setText(QCoreApplication.translate("AddEmployeeDialog", u"Contact", None))
        self.charge.setText(QCoreApplication.translate("AddEmployeeDialog", u"Charge", None))
        self.confirmButton.setText(QCoreApplication.translate("AddEmployeeDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("AddEmployeeDialog", u"Cancel", None))
    # retranslateUi

