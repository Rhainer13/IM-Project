# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logIn.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_logInWindow(object):

    def setupUi(self, logInWindow):
        if not logInWindow.objectName():
            logInWindow.setObjectName(u"logInWindow")
        logInWindow.resize(877, 622)
        logInWindow.setMaximumSize(QSize(997, 622))
        self.exitlogin = logInWindow
        self.horizontalLayout = QHBoxLayout(logInWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftHalf = QFrame(logInWindow)
        self.leftHalf.setObjectName(u"leftHalf")
        self.leftHalf.setMaximumSize(QSize(600, 600))
        self.leftHalf.setFrameShape(QFrame.StyledPanel)
        self.leftHalf.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.leftHalf)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.technicianImage = QLabel(self.leftHalf)
        self.technicianImage.setObjectName(u"technicianImage")
        self.technicianImage.setPixmap(QPixmap(u"images/technicianBackground.png"))
        self.technicianImage.setScaledContents(True)

        self.gridLayout_2.addWidget(self.technicianImage, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.leftHalf)

        self.rightHalf = QFrame(logInWindow)
        self.rightHalf.setObjectName(u"rightHalf")
        self.rightHalf.setFrameShape(QFrame.StyledPanel)
        self.rightHalf.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.rightHalf)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pttFrame = QFrame(self.rightHalf)
        self.pttFrame.setObjectName(u"pttFrame")
        self.pttFrame.setFrameShape(QFrame.StyledPanel)
        self.pttFrame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.pttFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pttImage = QLabel(self.pttFrame)
        self.pttImage.setObjectName(u"pttImage")
        self.pttImage.setMaximumSize(QSize(200, 200))
        self.pttImage.setPixmap(QPixmap(u"images/ptt-logo.png"))
        self.pttImage.setScaledContents(True)

        self.gridLayout.addWidget(self.pttImage, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.pttFrame)

        self.logInForm = QFrame(self.rightHalf)
        self.logInForm.setObjectName(u"logInForm")
        self.logInForm.setFrameShape(QFrame.StyledPanel)
        self.logInForm.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.logInForm)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.logInForm)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(180, 0))
        self.lineEdit.setMaxLength(20)
        self.lineEdit.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.lineEdit)

        self.passwordInput = QLineEdit(self.logInForm)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setMinimumSize(QSize(180, 0))
        self.passwordInput.setMaxLength(20)
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.passwordInput)

        self.logInButton = QPushButton(self.logInForm)
        self.logInButton.setObjectName(u"logInButton")
        self.logInButton.setMinimumSize(QSize(180, 0))


        self.verticalLayout.addWidget(self.logInButton)


        self.verticalLayout_2.addWidget(self.logInForm)


        self.horizontalLayout.addWidget(self.rightHalf)


        self.retranslateUi(logInWindow)

        QMetaObject.connectSlotsByName(logInWindow)
    # setupUi

    def retranslateUi(self, logInWindow):
        logInWindow.setWindowTitle(QCoreApplication.translate("logInWindow", u"Log In", None))
        self.technicianImage.setText("")
        self.pttImage.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("logInWindow", u"Username", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("logInWindow", u"Password", None))
        self.logInButton.setText(QCoreApplication.translate("logInWindow", u"Log In", None))
    # retranslateUi

