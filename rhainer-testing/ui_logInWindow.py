# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logInWindow.ui'
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

class Ui_LogInWindow(object):
    def setupUi(self, LogInWindow):
        if not LogInWindow.objectName():
            LogInWindow.setObjectName(u"LogInWindow")
        LogInWindow.resize(1032, 638)
        LogInWindow.setMaximumSize(QSize(1032, 638))
        self.horizontalLayout = QHBoxLayout(LogInWindow)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(LogInWindow)
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

        self.frame = QFrame(LogInWindow)
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

        self.usernameInput = QLineEdit(self.frame)
        self.usernameInput.setObjectName(u"usernameInput")
        self.usernameInput.setMaxLength(20)
        self.usernameInput.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.usernameInput)

        self.passwordInput = QLineEdit(self.frame)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setMaxLength(20)
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.passwordInput.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.passwordInput)

        self.logInButton = QPushButton(self.frame)
        self.logInButton.setObjectName(u"logInButton")

        self.verticalLayout.addWidget(self.logInButton)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(LogInWindow)

        QMetaObject.connectSlotsByName(LogInWindow)
    # setupUi

    def retranslateUi(self, LogInWindow):
        LogInWindow.setWindowTitle(QCoreApplication.translate("LogInWindow", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.usernameInput.setPlaceholderText(QCoreApplication.translate("LogInWindow", u"Username", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("LogInWindow", u"Password", None))
        self.logInButton.setText(QCoreApplication.translate("LogInWindow", u"Log In", None))
    # retranslateUi

