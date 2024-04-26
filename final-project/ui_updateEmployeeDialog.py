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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_updateEmployeeDialog(object):
    def setupUi(self, updateEmployeeDialog):
        if not updateEmployeeDialog.objectName():
            updateEmployeeDialog.setObjectName(u"updateEmployeeDialog")
        updateEmployeeDialog.resize(600, 350)
        updateEmployeeDialog.setMinimumSize(QSize(600, 350))
        updateEmployeeDialog.setMaximumSize(QSize(600, 16777215))
        self.verticalLayout_3 = QVBoxLayout(updateEmployeeDialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(updateEmployeeDialog)
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
        self.dateTerminated = QLabel(self.frame)
        self.dateTerminated.setObjectName(u"dateTerminated")

        self.horizontalLayout_2.addWidget(self.dateTerminated)

        self.dateTerminatedInput = QLineEdit(self.frame)
        self.dateTerminatedInput.setObjectName(u"dateTerminatedInput")
        self.dateTerminatedInput.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_2.addWidget(self.dateTerminatedInput, 0, Qt.AlignRight)


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

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.confirmButton = QPushButton(updateEmployeeDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout_2.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(updateEmployeeDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout_2.addWidget(self.cancelButton)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(updateEmployeeDialog)

        QMetaObject.connectSlotsByName(updateEmployeeDialog)
    # setupUi

    def retranslateUi(self, updateEmployeeDialog):
        updateEmployeeDialog.setWindowTitle(QCoreApplication.translate("updateEmployeeDialog", u"Update Employee", None))
        self.employeeName.setText(QCoreApplication.translate("updateEmployeeDialog", u"Employee Name", None))
        self.dateTerminated.setText(QCoreApplication.translate("updateEmployeeDialog", u"Date Terminated", None))
        self.address.setText(QCoreApplication.translate("updateEmployeeDialog", u"Address", None))
        self.contactNumber.setText(QCoreApplication.translate("updateEmployeeDialog", u"Contact Number", None))
        self.charge.setText(QCoreApplication.translate("updateEmployeeDialog", u"Charge", None))
        self.confirmButton.setText(QCoreApplication.translate("updateEmployeeDialog", u"Update", None))
        self.cancelButton.setText(QCoreApplication.translate("updateEmployeeDialog", u"Cancel", None))
    # retranslateUi

