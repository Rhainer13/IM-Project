# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'purchaseDialog.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_purchaseDialog(object):
    def setupUi(self, purchaseDialog):
        if not purchaseDialog.objectName():
            purchaseDialog.setObjectName(u"purchaseDialog")
        purchaseDialog.resize(500, 600)
        purchaseDialog.setMinimumSize(QSize(500, 600))
        purchaseDialog.setMaximumSize(QSize(500, 600))
        self.verticalLayout_4 = QVBoxLayout(purchaseDialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(purchaseDialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.customerName = QLabel(self.frame)
        self.customerName.setObjectName(u"customerName")

        self.horizontalLayout.addWidget(self.customerName)

        self.technicianDropdown_3 = QComboBox(self.frame)
        self.technicianDropdown_3.addItem("")
        self.technicianDropdown_3.addItem("")
        self.technicianDropdown_3.setObjectName(u"technicianDropdown_3")
        self.technicianDropdown_3.setMinimumSize(QSize(250, 0))

        self.horizontalLayout.addWidget(self.technicianDropdown_3)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.device = QLabel(self.frame)
        self.device.setObjectName(u"device")

        self.horizontalLayout_2.addWidget(self.device)

        self.technicianDropdown_2 = QComboBox(self.frame)
        self.technicianDropdown_2.addItem("")
        self.technicianDropdown_2.addItem("")
        self.technicianDropdown_2.addItem("")
        self.technicianDropdown_2.setObjectName(u"technicianDropdown_2")
        self.technicianDropdown_2.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_2.addWidget(self.technicianDropdown_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.technician = QLabel(self.frame)
        self.technician.setObjectName(u"technician")

        self.horizontalLayout_3.addWidget(self.technician)

        self.technicianDropdown = QComboBox(self.frame)
        self.technicianDropdown.addItem("")
        self.technicianDropdown.addItem("")
        self.technicianDropdown.setObjectName(u"technicianDropdown")
        self.technicianDropdown.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_3.addWidget(self.technicianDropdown)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.serviceType = QLabel(self.frame)
        self.serviceType.setObjectName(u"serviceType")

        self.horizontalLayout_4.addWidget(self.serviceType)

        self.serviceTypeDropdown = QComboBox(self.frame)
        self.serviceTypeDropdown.addItem("")
        self.serviceTypeDropdown.addItem("")
        self.serviceTypeDropdown.addItem("")
        self.serviceTypeDropdown.setObjectName(u"serviceTypeDropdown")
        self.serviceTypeDropdown.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_4.addWidget(self.serviceTypeDropdown)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.serviceType_2 = QLabel(self.frame)
        self.serviceType_2.setObjectName(u"serviceType_2")

        self.horizontalLayout_5.addWidget(self.serviceType_2)

        self.serviceTypeDropdown_2 = QComboBox(self.frame)
        self.serviceTypeDropdown_2.addItem("")
        self.serviceTypeDropdown_2.addItem("")
        self.serviceTypeDropdown_2.addItem("")
        self.serviceTypeDropdown_2.setObjectName(u"serviceTypeDropdown_2")
        self.serviceTypeDropdown_2.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_5.addWidget(self.serviceTypeDropdown_2)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.serviceType_3 = QLabel(self.frame)
        self.serviceType_3.setObjectName(u"serviceType_3")

        self.horizontalLayout_6.addWidget(self.serviceType_3)

        self.serviceTypeDropdown_3 = QComboBox(self.frame)
        self.serviceTypeDropdown_3.addItem("")
        self.serviceTypeDropdown_3.addItem("")
        self.serviceTypeDropdown_3.addItem("")
        self.serviceTypeDropdown_3.setObjectName(u"serviceTypeDropdown_3")
        self.serviceTypeDropdown_3.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_6.addWidget(self.serviceTypeDropdown_3)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.serviceType_4 = QLabel(self.frame)
        self.serviceType_4.setObjectName(u"serviceType_4")

        self.horizontalLayout_7.addWidget(self.serviceType_4)

        self.serviceTypeDropdown_4 = QComboBox(self.frame)
        self.serviceTypeDropdown_4.addItem("")
        self.serviceTypeDropdown_4.addItem("")
        self.serviceTypeDropdown_4.addItem("")
        self.serviceTypeDropdown_4.setObjectName(u"serviceTypeDropdown_4")
        self.serviceTypeDropdown_4.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_7.addWidget(self.serviceTypeDropdown_4)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.verticalLayout_4.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(purchaseDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.total = QLabel(self.frame_2)
        self.total.setObjectName(u"total")

        self.horizontalLayout_9.addWidget(self.total)

        self.totalOutput = QLineEdit(self.frame_2)
        self.totalOutput.setObjectName(u"totalOutput")
        self.totalOutput.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_9.addWidget(self.totalOutput, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.confirmButton = QPushButton(purchaseDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout_3.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(purchaseDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout_3.addWidget(self.cancelButton)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(purchaseDialog)

        QMetaObject.connectSlotsByName(purchaseDialog)
    # setupUi

    def retranslateUi(self, purchaseDialog):
        purchaseDialog.setWindowTitle(QCoreApplication.translate("purchaseDialog", u"Purchase", None))
        self.customerName.setText(QCoreApplication.translate("purchaseDialog", u"CPU", None))
        self.technicianDropdown_3.setItemText(0, QCoreApplication.translate("purchaseDialog", u"person1", None))
        self.technicianDropdown_3.setItemText(1, QCoreApplication.translate("purchaseDialog", u"person2", None))

        self.device.setText(QCoreApplication.translate("purchaseDialog", u"GPU", None))
        self.technicianDropdown_2.setItemText(0, QCoreApplication.translate("purchaseDialog", u"person1", None))
        self.technicianDropdown_2.setItemText(1, QCoreApplication.translate("purchaseDialog", u"person2", None))
        self.technicianDropdown_2.setItemText(2, QCoreApplication.translate("purchaseDialog", u"asdasdadadasdas", None))

        self.technician.setText(QCoreApplication.translate("purchaseDialog", u"Motherboard", None))
        self.technicianDropdown.setItemText(0, QCoreApplication.translate("purchaseDialog", u"person1", None))
        self.technicianDropdown.setItemText(1, QCoreApplication.translate("purchaseDialog", u"person2", None))

        self.serviceType.setText(QCoreApplication.translate("purchaseDialog", u"Storage", None))
        self.serviceTypeDropdown.setItemText(0, QCoreApplication.translate("purchaseDialog", u"Cleaning", None))
        self.serviceTypeDropdown.setItemText(1, QCoreApplication.translate("purchaseDialog", u"Repair", None))
        self.serviceTypeDropdown.setItemText(2, QCoreApplication.translate("purchaseDialog", u"Upgrade", None))

        self.serviceType_2.setText(QCoreApplication.translate("purchaseDialog", u"RAM", None))
        self.serviceTypeDropdown_2.setItemText(0, QCoreApplication.translate("purchaseDialog", u"Cleaning", None))
        self.serviceTypeDropdown_2.setItemText(1, QCoreApplication.translate("purchaseDialog", u"Repair", None))
        self.serviceTypeDropdown_2.setItemText(2, QCoreApplication.translate("purchaseDialog", u"Upgrade", None))

        self.serviceType_3.setText(QCoreApplication.translate("purchaseDialog", u"Case", None))
        self.serviceTypeDropdown_3.setItemText(0, QCoreApplication.translate("purchaseDialog", u"Cleaning", None))
        self.serviceTypeDropdown_3.setItemText(1, QCoreApplication.translate("purchaseDialog", u"Repair", None))
        self.serviceTypeDropdown_3.setItemText(2, QCoreApplication.translate("purchaseDialog", u"Upgrade", None))

        self.serviceType_4.setText(QCoreApplication.translate("purchaseDialog", u"Fan Cooler", None))
        self.serviceTypeDropdown_4.setItemText(0, QCoreApplication.translate("purchaseDialog", u"Cleaning", None))
        self.serviceTypeDropdown_4.setItemText(1, QCoreApplication.translate("purchaseDialog", u"Repair", None))
        self.serviceTypeDropdown_4.setItemText(2, QCoreApplication.translate("purchaseDialog", u"Upgrade", None))

        self.total.setText(QCoreApplication.translate("purchaseDialog", u"Total", None))
        self.confirmButton.setText(QCoreApplication.translate("purchaseDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("purchaseDialog", u"Cancel", None))
    # retranslateUi

