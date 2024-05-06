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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_AddEmployeeDialog(object):
    def setupUi(self, AddEmployeeDialog):
        if not AddEmployeeDialog.objectName():
            AddEmployeeDialog.setObjectName(u"AddEmployeeDialog")
        AddEmployeeDialog.resize(600, 350)
        AddEmployeeDialog.setMinimumSize(QSize(600, 350))
        AddEmployeeDialog.setMaximumSize(QSize(600, 350))
        self.verticalLayout_3 = QVBoxLayout(AddEmployeeDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(AddEmployeeDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.employeeName = QLabel(self.frame)
        self.employeeName.setObjectName(u"employeeName")

        self.horizontalLayout.addWidget(self.employeeName)

        self.employeeNameInput = QLineEdit(self.frame)
        self.employeeNameInput.setObjectName(u"employeeNameInput")
        self.employeeNameInput.setMinimumSize(QSize(250, 0))

        self.horizontalLayout.addWidget(self.employeeNameInput, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.dateHired = QLabel(self.frame)
        self.dateHired.setObjectName(u"dateHired")

        self.horizontalLayout_2.addWidget(self.dateHired)

        self.dateHiredInput = QLineEdit(self.frame)
        self.dateHiredInput.setObjectName(u"dateHiredInput")
        self.dateHiredInput.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_2.addWidget(self.dateHiredInput, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.address = QLabel(self.frame)
        self.address.setObjectName(u"address")

        self.horizontalLayout_3.addWidget(self.address)

        self.addressInput = QLineEdit(self.frame)
        self.addressInput.setObjectName(u"addressInput")
        self.addressInput.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_3.addWidget(self.addressInput, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.contactNumber = QLabel(self.frame)
        self.contactNumber.setObjectName(u"contactNumber")

        self.horizontalLayout_4.addWidget(self.contactNumber)

        self.contactNumberInput = QLineEdit(self.frame)
        self.contactNumberInput.setObjectName(u"contactNumberInput")
        self.contactNumberInput.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_4.addWidget(self.contactNumberInput, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.charge = QLabel(self.frame)
        self.charge.setObjectName(u"charge")

        self.horizontalLayout_5.addWidget(self.charge)

        self.chargeInput = QLineEdit(self.frame)
        self.chargeInput.setObjectName(u"chargeInput")
        self.chargeInput.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_5.addWidget(self.chargeInput, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.verticalLayout_3.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.confirmButton = QPushButton(AddEmployeeDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout_2.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(AddEmployeeDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout_2.addWidget(self.cancelButton)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(AddEmployeeDialog)

        QMetaObject.connectSlotsByName(AddEmployeeDialog)
    # setupUi

    def retranslateUi(self, AddEmployeeDialog):
        AddEmployeeDialog.setWindowTitle(QCoreApplication.translate("AddEmployeeDialog", u"Add Employee", None))
        self.employeeName.setText(QCoreApplication.translate("AddEmployeeDialog", u"Employee Name", None))
        self.dateHired.setText(QCoreApplication.translate("AddEmployeeDialog", u"Date Hired", None))
        self.address.setText(QCoreApplication.translate("AddEmployeeDialog", u"Address", None))
        self.contactNumber.setText(QCoreApplication.translate("AddEmployeeDialog", u"Contact Number", None))
        self.charge.setText(QCoreApplication.translate("AddEmployeeDialog", u"Charge", None))
        self.confirmButton.setText(QCoreApplication.translate("AddEmployeeDialog", u"Add", None))
        self.cancelButton.setText(QCoreApplication.translate("AddEmployeeDialog", u"Cancel", None))
    # retranslateUi

