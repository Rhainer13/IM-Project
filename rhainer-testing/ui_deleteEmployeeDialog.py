# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deleteEmployeeDialog.ui'
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

class Ui_DeleteEmployeeDialog(object):
    def setupUi(self, DeleteEmployeeDialog):
        if not DeleteEmployeeDialog.objectName():
            DeleteEmployeeDialog.setObjectName(u"DeleteEmployeeDialog")
        DeleteEmployeeDialog.resize(400, 237)
        self.verticalLayout = QVBoxLayout(DeleteEmployeeDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DeleteEmployeeDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.confirmButton = QPushButton(DeleteEmployeeDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(DeleteEmployeeDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout.addWidget(self.cancelButton)


        self.retranslateUi(DeleteEmployeeDialog)

        QMetaObject.connectSlotsByName(DeleteEmployeeDialog)
    # setupUi

    def retranslateUi(self, DeleteEmployeeDialog):
        DeleteEmployeeDialog.setWindowTitle(QCoreApplication.translate("DeleteEmployeeDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DeleteEmployeeDialog", u"Are you sure you want to delete {employee name} ?", None))
        self.confirmButton.setText(QCoreApplication.translate("DeleteEmployeeDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("DeleteEmployeeDialog", u"Cancel", None))
    # retranslateUi

