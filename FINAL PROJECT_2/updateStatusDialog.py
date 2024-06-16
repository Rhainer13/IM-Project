# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'updateStatusDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_UpdateStatusDialog(object):
    def setupUi(self, UpdateStatusDialog):
        if not UpdateStatusDialog.objectName():
            UpdateStatusDialog.setObjectName(u"UpdateStatusDialog")
        UpdateStatusDialog.resize(223, 89)
        self.gridLayout = QGridLayout(UpdateStatusDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.completed = QPushButton(UpdateStatusDialog)
        self.completed.setObjectName(u"completed")

        self.verticalLayout.addWidget(self.completed)

        self.cancelled = QPushButton(UpdateStatusDialog)
        self.cancelled.setObjectName(u"cancelled")

        self.verticalLayout.addWidget(self.cancelled)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.retranslateUi(UpdateStatusDialog)

        QMetaObject.connectSlotsByName(UpdateStatusDialog)
    # setupUi

    def retranslateUi(self, UpdateStatusDialog):
        UpdateStatusDialog.setWindowTitle(QCoreApplication.translate("UpdateStatusDialog", u"Dialog", None))
        self.completed.setText(QCoreApplication.translate("UpdateStatusDialog", u"Completed", None))
        self.cancelled.setText(QCoreApplication.translate("UpdateStatusDialog", u"Cancelled", None))
    # retranslateUi

