# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_LoginPage(object):
    def setupUi(self, LoginPage):
        if not LoginPage.objectName():
            LoginPage.setObjectName(u"LoginPage")
        LoginPage.resize(1032, 638)
        LoginPage.setMaximumSize(QSize(1032, 638))
        self.horizontalLayout = QHBoxLayout(LoginPage)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(LoginPage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(635, 616))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"images/technicianBackground.png"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.frame_2)

        self.frame = QFrame(LoginPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 350))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u"images/ptt-logo.png"))
        self.label_2.setScaledContents(True)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)

        self.username = QLineEdit(self.frame)
        self.username.setObjectName(u"username")
        self.username.setMaxLength(20)
        self.username.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.username)

        self.password = QLineEdit(self.frame)
        self.password.setObjectName(u"password")
        self.password.setMaxLength(20)
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.password)

        self.notification = QLabel(self.frame)
        self.notification.setObjectName(u"notification")

        self.verticalLayout.addWidget(self.notification)

        self.login = QPushButton(self.frame)
        self.login.setObjectName(u"login")

        self.verticalLayout.addWidget(self.login)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(LoginPage)

        QMetaObject.connectSlotsByName(LoginPage)
    # setupUi

    def retranslateUi(self, LoginPage):
        LoginPage.setWindowTitle(QCoreApplication.translate("LoginPage", u"Log In", None))
        self.label.setText("")
        self.label_2.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("LoginPage", u"Username", None))
        self.password.setPlaceholderText(QCoreApplication.translate("LoginPage", u"Password", None))
        self.notification.setText("")
        self.login.setText(QCoreApplication.translate("LoginPage", u"Log In", None))
    # retranslateUi

