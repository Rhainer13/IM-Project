# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'serviceReportDialog.ui'
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

class Ui_serviceReportDialog(object):
    def setupUi(self, serviceReportDialog):
        if not serviceReportDialog.objectName():
            serviceReportDialog.setObjectName(u"serviceReportDialog")
        serviceReportDialog.resize(500, 500)
        serviceReportDialog.setMinimumSize(QSize(500, 500))
        serviceReportDialog.setMaximumSize(QSize(500, 500))
        self.verticalLayout_4 = QVBoxLayout(serviceReportDialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(serviceReportDialog)
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

        self.customerNameInput = QLineEdit(self.frame)
        self.customerNameInput.setObjectName(u"customerNameInput")
        self.customerNameInput.setMinimumSize(QSize(250, 0))

        self.horizontalLayout.addWidget(self.customerNameInput, 0, Qt.AlignRight)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.device = QLabel(self.frame)
        self.device.setObjectName(u"device")

        self.horizontalLayout_2.addWidget(self.device)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_2.addWidget(self.comboBox)


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


        self.verticalLayout_4.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.frame_2 = QFrame(serviceReportDialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.total = QLabel(self.frame_2)
        self.total.setObjectName(u"total")

        self.horizontalLayout_6.addWidget(self.total)

        self.totalOutput = QLineEdit(self.frame_2)
        self.totalOutput.setObjectName(u"totalOutput")
        self.totalOutput.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_6.addWidget(self.totalOutput, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.confirmButton = QPushButton(serviceReportDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout_3.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(serviceReportDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout_3.addWidget(self.cancelButton)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(serviceReportDialog)

        QMetaObject.connectSlotsByName(serviceReportDialog)
    # setupUi

    def retranslateUi(self, serviceReportDialog):
        serviceReportDialog.setWindowTitle(QCoreApplication.translate("serviceReportDialog", u"Service Report", None))
        self.customerName.setText(QCoreApplication.translate("serviceReportDialog", u"Customer Name", None))
        self.device.setText(QCoreApplication.translate("serviceReportDialog", u"Device", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("serviceReportDialog", u"Phone", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("serviceReportDialog", u"Laptop", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("serviceReportDialog", u"Desktop PC", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("serviceReportDialog", u"Console", None))

        self.technician.setText(QCoreApplication.translate("serviceReportDialog", u"Technician", None))
        self.technicianDropdown.setItemText(0, QCoreApplication.translate("serviceReportDialog", u"person1", None))
        self.technicianDropdown.setItemText(1, QCoreApplication.translate("serviceReportDialog", u"person2", None))

        self.serviceType.setText(QCoreApplication.translate("serviceReportDialog", u"Service Type", None))
        self.serviceTypeDropdown.setItemText(0, QCoreApplication.translate("serviceReportDialog", u"Cleaning", None))
        self.serviceTypeDropdown.setItemText(1, QCoreApplication.translate("serviceReportDialog", u"Repair", None))
        self.serviceTypeDropdown.setItemText(2, QCoreApplication.translate("serviceReportDialog", u"Upgrade", None))

        self.total.setText(QCoreApplication.translate("serviceReportDialog", u"Total", None))
        self.confirmButton.setText(QCoreApplication.translate("serviceReportDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("serviceReportDialog", u"Cancel", None))
    # retranslateUi

