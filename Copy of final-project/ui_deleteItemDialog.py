# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deleteItemDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_deleteItemDialog(object):
    def setupUi(self, deleteItemDialog):
        if not deleteItemDialog.objectName():
            deleteItemDialog.setObjectName(u"deleteItemDialog")
        deleteItemDialog.resize(322, 200)
        deleteItemDialog.setMinimumSize(QSize(322, 200))
        deleteItemDialog.setMaximumSize(QSize(322, 200))
        self.verticalLayout = QVBoxLayout(deleteItemDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.confirmation = QLabel(deleteItemDialog)
        self.confirmation.setObjectName(u"confirmation")
        self.confirmation.setWordWrap(True)

        self.verticalLayout.addWidget(self.confirmation, 0, Qt.AlignHCenter)

        self.confirmButton = QPushButton(deleteItemDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(deleteItemDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout.addWidget(self.cancelButton)


        self.retranslateUi(deleteItemDialog)

        QMetaObject.connectSlotsByName(deleteItemDialog)
    # setupUi

    def retranslateUi(self, deleteItemDialog):
        deleteItemDialog.setWindowTitle(QCoreApplication.translate("deleteItemDialog", u"Delete Item", None))
        self.confirmation.setText(QCoreApplication.translate("deleteItemDialog", u"Are you sure you want to delete this item?", None))
        self.confirmButton.setText(QCoreApplication.translate("deleteItemDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("deleteItemDialog", u"Cancel", None))
    # retranslateUi

