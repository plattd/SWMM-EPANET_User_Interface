# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\dev\Python\dev-ui-py3qt5\src\ui\SWMM\frmDynamicWaveDesigner.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_frmDynamicWave(object):
    def setupUi(self, frmDynamicWave):
        frmDynamicWave.setObjectName("frmDynamicWave")
        frmDynamicWave.resize(345, 449)
        font = QtGui.QFont()
        font.setPointSize(10)
        frmDynamicWave.setFont(font)
        self.centralWidget = QtWidgets.QWidget(frmDynamicWave)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame1 = QtWidgets.QFrame(self.centralWidget)
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.formLayout_2 = QtWidgets.QFormLayout(self.frame1)
        self.formLayout_2.setContentsMargins(11, 11, 11, 11)
        self.formLayout_2.setSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.lblInertial = QtWidgets.QLabel(self.frame1)
        self.lblInertial.setObjectName("lblInertial")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblInertial)
        self.cboInertial = QtWidgets.QComboBox(self.frame1)
        self.cboInertial.setMinimumSize(QtCore.QSize(50, 0))
        self.cboInertial.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cboInertial.setObjectName("cboInertial")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cboInertial)
        self.lblNormal = QtWidgets.QLabel(self.frame1)
        self.lblNormal.setObjectName("lblNormal")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblNormal)
        self.cboNormal = QtWidgets.QComboBox(self.frame1)
        self.cboNormal.setMinimumSize(QtCore.QSize(50, 0))
        self.cboNormal.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cboNormal.setObjectName("cboNormal")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cboNormal)
        self.lblForce = QtWidgets.QLabel(self.frame1)
        self.lblForce.setObjectName("lblForce")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblForce)
        self.cboForce = QtWidgets.QComboBox(self.frame1)
        self.cboForce.setMinimumSize(QtCore.QSize(50, 0))
        self.cboForce.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cboForce.setObjectName("cboForce")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cboForce)
        self.lblSurcharge = QtWidgets.QLabel(self.frame1)
        self.lblSurcharge.setObjectName("lblSurcharge")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblSurcharge)
        self.cboSurcharge = QtWidgets.QComboBox(self.frame1)
        self.cboSurcharge.setMaximumSize(QtCore.QSize(150, 16777215))
        self.cboSurcharge.setObjectName("cboSurcharge")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cboSurcharge)
        self.verticalLayout.addWidget(self.frame1)
        self.frame2 = QtWidgets.QFrame(self.centralWidget)
        self.frame2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame2.setObjectName("frame2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cbxUseVariable = QtWidgets.QCheckBox(self.frame2)
        self.cbxUseVariable.setObjectName("cbxUseVariable")
        self.horizontalLayout_2.addWidget(self.cbxUseVariable)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lblAdjusted = QtWidgets.QLabel(self.frame2)
        self.lblAdjusted.setObjectName("lblAdjusted")
        self.horizontalLayout_2.addWidget(self.lblAdjusted)
        self.sbxAdjusted = QtWidgets.QSpinBox(self.frame2)
        self.sbxAdjusted.setObjectName("sbxAdjusted")
        self.horizontalLayout_2.addWidget(self.sbxAdjusted)
        self.lblPercent = QtWidgets.QLabel(self.frame2)
        self.lblPercent.setObjectName("lblPercent")
        self.horizontalLayout_2.addWidget(self.lblPercent)
        self.verticalLayout.addWidget(self.frame2)
        self.frame3 = QtWidgets.QFrame(self.centralWidget)
        self.frame3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame3.setObjectName("frame3")
        self.formLayout = QtWidgets.QFormLayout(self.frame3)
        self.formLayout.setContentsMargins(11, 11, 11, 11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName("formLayout")
        self.lblMinimum = QtWidgets.QLabel(self.frame3)
        self.lblMinimum.setObjectName("lblMinimum")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblMinimum)
        self.txtMinimum = QtWidgets.QLineEdit(self.frame3)
        self.txtMinimum.setObjectName("txtMinimum")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtMinimum)
        self.lblTimeStep = QtWidgets.QLabel(self.frame3)
        self.lblTimeStep.setObjectName("lblTimeStep")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblTimeStep)
        self.txtLengthening = QtWidgets.QLineEdit(self.frame3)
        self.txtLengthening.setObjectName("txtLengthening")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtLengthening)
        self.lblSurface = QtWidgets.QLabel(self.frame3)
        self.lblSurface.setObjectName("lblSurface")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblSurface)
        self.txtSurfaceArea = QtWidgets.QLineEdit(self.frame3)
        self.txtSurfaceArea.setObjectName("txtSurfaceArea")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtSurfaceArea)
        self.lblMaximum = QtWidgets.QLabel(self.frame3)
        self.lblMaximum.setObjectName("lblMaximum")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.lblMaximum)
        self.sbxTrials = QtWidgets.QSpinBox(self.frame3)
        self.sbxTrials.setObjectName("sbxTrials")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.sbxTrials)
        self.lblHead = QtWidgets.QLabel(self.frame3)
        self.lblHead.setObjectName("lblHead")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.lblHead)
        self.txtTolerance = QtWidgets.QLineEdit(self.frame3)
        self.txtTolerance.setObjectName("txtTolerance")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.txtTolerance)
        self.lblThreads = QtWidgets.QLabel(self.frame3)
        self.lblThreads.setObjectName("lblThreads")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.lblThreads)
        self.cboThreads = QtWidgets.QComboBox(self.frame3)
        self.cboThreads.setObjectName("cboThreads")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.cboThreads)
        self.verticalLayout.addWidget(self.frame3)
        self.fraButtons = QtWidgets.QFrame(self.centralWidget)
        self.fraButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fraButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fraButtons.setObjectName("fraButtons")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.fraButtons)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(142, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.cmdOK = QtWidgets.QPushButton(self.fraButtons)
        self.cmdOK.setObjectName("cmdOK")
        self.horizontalLayout.addWidget(self.cmdOK)
        self.cmdCancel = QtWidgets.QPushButton(self.fraButtons)
        self.cmdCancel.setObjectName("cmdCancel")
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.verticalLayout.addWidget(self.fraButtons)
        frmDynamicWave.setCentralWidget(self.centralWidget)

        self.retranslateUi(frmDynamicWave)
        QtCore.QMetaObject.connectSlotsByName(frmDynamicWave)
        frmDynamicWave.setTabOrder(self.cboInertial, self.cboNormal)
        frmDynamicWave.setTabOrder(self.cboNormal, self.cboForce)
        frmDynamicWave.setTabOrder(self.cboForce, self.cbxUseVariable)
        frmDynamicWave.setTabOrder(self.cbxUseVariable, self.sbxAdjusted)
        frmDynamicWave.setTabOrder(self.sbxAdjusted, self.txtMinimum)
        frmDynamicWave.setTabOrder(self.txtMinimum, self.txtLengthening)
        frmDynamicWave.setTabOrder(self.txtLengthening, self.txtSurfaceArea)
        frmDynamicWave.setTabOrder(self.txtSurfaceArea, self.sbxTrials)
        frmDynamicWave.setTabOrder(self.sbxTrials, self.txtTolerance)
        frmDynamicWave.setTabOrder(self.txtTolerance, self.cboThreads)
        frmDynamicWave.setTabOrder(self.cboThreads, self.cmdOK)
        frmDynamicWave.setTabOrder(self.cmdOK, self.cmdCancel)

    def retranslateUi(self, frmDynamicWave):
        _translate = QtCore.QCoreApplication.translate
        frmDynamicWave.setWindowTitle(_translate("frmDynamicWave", "SWMM Dynamic Wave Options"))
        self.lblInertial.setText(_translate("frmDynamicWave", "Inertial Terms"))
        self.lblNormal.setText(_translate("frmDynamicWave", "Normal Flow Criterion"))
        self.lblForce.setText(_translate("frmDynamicWave", "Force Main Equation"))
        self.lblSurcharge.setText(_translate("frmDynamicWave", "Surcharge Method"))
        self.cbxUseVariable.setText(_translate("frmDynamicWave", "Use Variable Time Steps"))
        self.lblAdjusted.setText(_translate("frmDynamicWave", "Adjusted By"))
        self.lblPercent.setText(_translate("frmDynamicWave", "%"))
        self.lblMinimum.setText(_translate("frmDynamicWave", "Minimum Variable Time Step (sec)"))
        self.lblTimeStep.setText(_translate("frmDynamicWave", "Time Step for Conduit Lengthening (sec)"))
        self.lblSurface.setText(_translate("frmDynamicWave", "Minimum Nodal Surface Area (sq feet)"))
        self.lblMaximum.setText(_translate("frmDynamicWave", "Maximum Trials Per Time Step"))
        self.lblHead.setText(_translate("frmDynamicWave", "Head Convergence Tolerance (feet)"))
        self.lblThreads.setText(_translate("frmDynamicWave", "Number of Threads"))
        self.cmdOK.setText(_translate("frmDynamicWave", "OK"))
        self.cmdCancel.setText(_translate("frmDynamicWave", "Cancel"))

