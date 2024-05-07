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

class Ui_ServiceReportDialog(object):
    def setupUi(self, ServiceReportDialog):
        if not ServiceReportDialog.objectName():
            ServiceReportDialog.setObjectName(u"ServiceReportDialog")
        ServiceReportDialog.resize(500, 500)
        ServiceReportDialog.setMinimumSize(QSize(500, 500))
        ServiceReportDialog.setMaximumSize(QSize(500, 500))
        self.verticalLayout_4 = QVBoxLayout(ServiceReportDialog)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame = QFrame(ServiceReportDialog)
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

        self.deviceDropdown = QComboBox(self.frame)
        self.deviceDropdown.addItem("")
        self.deviceDropdown.addItem("")
        self.deviceDropdown.addItem("")
        self.deviceDropdown.addItem("")
        self.deviceDropdown.setObjectName(u"deviceDropdown")
        self.deviceDropdown.setMinimumSize(QSize(250, 0))

        self.horizontalLayout_2.addWidget(self.deviceDropdown)


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

        self.frame_2 = QFrame(ServiceReportDialog)
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
        self.totalOutput.setEnabled(False)
        self.totalOutput.setMinimumSize(QSize(250, 0))
        self.totalOutput.setReadOnly(True)

        self.horizontalLayout_6.addWidget(self.totalOutput, 0, Qt.AlignRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)


        self.verticalLayout_4.addWidget(self.frame_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.confirmButton = QPushButton(ServiceReportDialog)
        self.confirmButton.setObjectName(u"confirmButton")

        self.verticalLayout_3.addWidget(self.confirmButton)

        self.cancelButton = QPushButton(ServiceReportDialog)
        self.cancelButton.setObjectName(u"cancelButton")

        self.verticalLayout_3.addWidget(self.cancelButton)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.retranslateUi(ServiceReportDialog)

        QMetaObject.connectSlotsByName(ServiceReportDialog)
    # setupUi

    def retranslateUi(self, ServiceReportDialog):
        ServiceReportDialog.setWindowTitle(QCoreApplication.translate("ServiceReportDialog", u"Service Report", None))
        self.customerName.setText(QCoreApplication.translate("ServiceReportDialog", u"Customer Name", None))
        self.device.setText(QCoreApplication.translate("ServiceReportDialog", u"Device", None))
        self.deviceDropdown.setItemText(0, QCoreApplication.translate("ServiceReportDialog", u"Phone", None))
        self.deviceDropdown.setItemText(1, QCoreApplication.translate("ServiceReportDialog", u"Laptop", None))
        self.deviceDropdown.setItemText(2, QCoreApplication.translate("ServiceReportDialog", u"Desktop PC", None))
        self.deviceDropdown.setItemText(3, QCoreApplication.translate("ServiceReportDialog", u"Console", None))

        self.technician.setText(QCoreApplication.translate("ServiceReportDialog", u"Technician", None))
        self.technicianDropdown.setItemText(0, QCoreApplication.translate("ServiceReportDialog", u"person1", None))
        self.technicianDropdown.setItemText(1, QCoreApplication.translate("ServiceReportDialog", u"person2", None))

        self.serviceType.setText(QCoreApplication.translate("ServiceReportDialog", u"Service Type", None))
        self.serviceTypeDropdown.setItemText(0, QCoreApplication.translate("ServiceReportDialog", u"Cleaning", None))
        self.serviceTypeDropdown.setItemText(1, QCoreApplication.translate("ServiceReportDialog", u"Repair", None))
        self.serviceTypeDropdown.setItemText(2, QCoreApplication.translate("ServiceReportDialog", u"Upgrade", None))

        self.total.setText(QCoreApplication.translate("ServiceReportDialog", u"Total Payment", None))
        self.confirmButton.setText(QCoreApplication.translate("ServiceReportDialog", u"Confirm", None))
        self.cancelButton.setText(QCoreApplication.translate("ServiceReportDialog", u"Cancel", None))
    # retranslateUi

