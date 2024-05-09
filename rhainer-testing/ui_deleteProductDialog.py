# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deleteProductDialog.ui'
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

class Ui_DeleteProductDialog(object):
    def setupUi(self, DeleteProductDialog):
        if not DeleteProductDialog.objectName():
            DeleteProductDialog.setObjectName(u"DeleteProductDialog")
        DeleteProductDialog.resize(400, 237)
        self.verticalLayout = QVBoxLayout(DeleteProductDialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(DeleteProductDialog)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.confirmButton = QPushButton(DeleteProductDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(DeleteProductDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout.addWidget(self.cancelButton)


        self.retranslateUi(DeleteProductDialog)

        QMetaObject.connectSlotsByName(DeleteProductDialog)
    # setupUi

    def retranslateUi(self, DeleteProductDialog):
        DeleteProductDialog.setWindowTitle(QCoreApplication.translate("DeleteProductDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DeleteProductDialog", u"Are you sure you want to delete {product name} ?", None))
        self.confirmButton.setText(QCoreApplication.translate("DeleteProductDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("DeleteProductDialog", u"Cancel", None))
    # retranslateUi

