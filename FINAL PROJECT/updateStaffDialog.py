# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateStaffDialog.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_UpdateStaffDialog(object):
    def setupUi(self, UpdateStaffDialog):
        if not UpdateStaffDialog.objectName():
            UpdateStaffDialog.setObjectName(u"UpdateStaffDialog")
        UpdateStaffDialog.resize(340, 217)
        self.verticalLayout = QVBoxLayout(UpdateStaffDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.formLayout_2 = QFormLayout()
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(UpdateStaffDialog)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.fname = QLineEdit(UpdateStaffDialog)
        self.fname.setObjectName(u"fname")
        self.fname.setMaxLength(25)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.fname)

        self.label_2 = QLabel(UpdateStaffDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lname = QLineEdit(UpdateStaffDialog)
        self.lname.setObjectName(u"lname")
        self.lname.setMaxLength(25)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.lname)

        self.label_3 = QLabel(UpdateStaffDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.mobileNum = QLineEdit(UpdateStaffDialog)
        self.mobileNum.setObjectName(u"mobileNum")
        self.mobileNum.setMaxLength(11)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.mobileNum)

        self.label_4 = QLabel(UpdateStaffDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.address = QLineEdit(UpdateStaffDialog)
        self.address.setObjectName(u"address")
        self.address.setMaxLength(50)

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.address)


        self.verticalLayout.addLayout(self.formLayout_2)

        self.frame = QFrame(UpdateStaffDialog)
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


        self.retranslateUi(UpdateStaffDialog)

        QMetaObject.connectSlotsByName(UpdateStaffDialog)
    # setupUi

    def retranslateUi(self, UpdateStaffDialog):
        UpdateStaffDialog.setWindowTitle(QCoreApplication.translate("UpdateStaffDialog", u"Edit Staff", None))
        self.label.setText(QCoreApplication.translate("UpdateStaffDialog", u"First Name", None))
        self.label_2.setText(QCoreApplication.translate("UpdateStaffDialog", u"Last Name", None))
        self.label_3.setText(QCoreApplication.translate("UpdateStaffDialog", u"Mobile Number", None))
        self.label_4.setText(QCoreApplication.translate("UpdateStaffDialog", u"Address", None))
        self.confirm.setText(QCoreApplication.translate("UpdateStaffDialog", u"Confirm", None))
        self.cancel.setText(QCoreApplication.translate("UpdateStaffDialog", u"Cancel", None))
    # retranslateUi

