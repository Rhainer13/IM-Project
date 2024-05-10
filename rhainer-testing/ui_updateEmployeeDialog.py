# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateEmployeeDialog.ui'
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

class Ui_UpdateEmployeeDialog(object):
    def setupUi(self, UpdateEmployeeDialog):
        if not UpdateEmployeeDialog.objectName():
            UpdateEmployeeDialog.setObjectName(u"UpdateEmployeeDialog")
        UpdateEmployeeDialog.resize(610, 381)
        self.verticalLayout = QVBoxLayout(UpdateEmployeeDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.employeeName = QLabel(UpdateEmployeeDialog)
        self.employeeName.setObjectName(u"employeeName")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.employeeName)

        self.employeeNameInput = QLineEdit(UpdateEmployeeDialog)
        self.employeeNameInput.setObjectName(u"employeeNameInput")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.employeeNameInput)

        self.dateHired = QLabel(UpdateEmployeeDialog)
        self.dateHired.setObjectName(u"dateHired")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.dateHired)

        self.dateHiredInput = QLineEdit(UpdateEmployeeDialog)
        self.dateHiredInput.setObjectName(u"dateHiredInput")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.dateHiredInput)

        self.address = QLabel(UpdateEmployeeDialog)
        self.address.setObjectName(u"address")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.address)

        self.addressInput = QLineEdit(UpdateEmployeeDialog)
        self.addressInput.setObjectName(u"addressInput")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.addressInput)

        self.contact = QLabel(UpdateEmployeeDialog)
        self.contact.setObjectName(u"contact")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.contact)

        self.contactInput = QLineEdit(UpdateEmployeeDialog)
        self.contactInput.setObjectName(u"contactInput")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.contactInput)

        self.charge = QLabel(UpdateEmployeeDialog)
        self.charge.setObjectName(u"charge")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.charge)

        self.chargeInput = QLineEdit(UpdateEmployeeDialog)
        self.chargeInput.setObjectName(u"chargeInput")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.chargeInput)


        self.verticalLayout.addLayout(self.formLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.confirmButton = QPushButton(UpdateEmployeeDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(UpdateEmployeeDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout.addWidget(self.cancelButton)


        self.retranslateUi(UpdateEmployeeDialog)

        QMetaObject.connectSlotsByName(UpdateEmployeeDialog)
    # setupUi

    def retranslateUi(self, UpdateEmployeeDialog):
        UpdateEmployeeDialog.setWindowTitle(QCoreApplication.translate("UpdateEmployeeDialog", u"Dialog", None))
        self.employeeName.setText(QCoreApplication.translate("UpdateEmployeeDialog", u"Employee Name", None))
        self.dateHired.setText(QCoreApplication.translate("UpdateEmployeeDialog", u"Date Hired", None))
        self.address.setText(QCoreApplication.translate("UpdateEmployeeDialog", u"Address", None))
        self.contact.setText(QCoreApplication.translate("UpdateEmployeeDialog", u"Contact", None))
        self.charge.setText(QCoreApplication.translate("UpdateEmployeeDialog", u"Charge", None))
        self.confirmButton.setText(QCoreApplication.translate("UpdateEmployeeDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("UpdateEmployeeDialog", u"Cancel", None))
    # retranslateUi

