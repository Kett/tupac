# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PackageWidget.ui'
#
# Created: Sun Jan 27 01:05:15 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PackageWidget(QtGui.QListWidgetItem):
    def setupUi(self, PackageWidget):
        PackageWidget.setObjectName("PackageWidget")
        PackageWidget.resize(QtCore.QSize(QtCore.QRect(0,0,701,112).size()).expandedTo(PackageWidget.minimumSizeHint()))

        self.gridlayout = QtGui.QGridLayout(PackageWidget)
        self.gridlayout.setObjectName("gridlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.repoLabel = QtGui.QLabel(PackageWidget)
        self.repoLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.NoTextInteraction|QtCore.Qt.TextSelectableByMouse)
        self.repoLabel.setObjectName("repoLabel")
        self.hboxlayout.addWidget(self.repoLabel)

        self.packageLabel = QtGui.QLabel(PackageWidget)
        self.packageLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.NoTextInteraction|QtCore.Qt.TextSelectableByMouse)
        self.packageLabel.setObjectName("packageLabel")
        self.hboxlayout.addWidget(self.packageLabel)

        self.versionLabel = QtGui.QLabel(PackageWidget)
        self.versionLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.NoTextInteraction|QtCore.Qt.TextSelectableByMouse)
        self.versionLabel.setObjectName("versionLabel")
        self.hboxlayout.addWidget(self.versionLabel)

        self.installedLabel = QtGui.QLabel(PackageWidget)
        self.installedLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.NoTextInteraction|QtCore.Qt.TextSelectableByMouse)
        self.installedLabel.setObjectName("installedLabel")
        self.hboxlayout.addWidget(self.installedLabel)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.detailSlider = QtGui.QSlider(PackageWidget)
        self.detailSlider.setOrientation(QtCore.Qt.Horizontal)
        self.detailSlider.setObjectName("detailSlider")
        self.hboxlayout.addWidget(self.detailSlider)
        self.gridlayout.addLayout(self.hboxlayout,0,0,1,1)

        self.descriptionLabel = QtGui.QLabel(PackageWidget)
        self.descriptionLabel.setFrameShape(QtGui.QFrame.StyledPanel)
        self.descriptionLabel.setLineWidth(1)
        self.descriptionLabel.setTextFormat(QtCore.Qt.RichText)
        self.descriptionLabel.setScaledContents(False)
        self.descriptionLabel.setWordWrap(True)
        self.descriptionLabel.setMargin(3)
        self.descriptionLabel.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.NoTextInteraction|QtCore.Qt.TextSelectableByMouse)
        self.descriptionLabel.setObjectName("descriptionLabel")
        self.gridlayout.addWidget(self.descriptionLabel,1,0,1,1)

        self.retranslateUi(PackageWidget)
        QtCore.QMetaObject.connectSlotsByName(PackageWidget)

    def retranslateUi(self, PackageWidget):
        PackageWidget.setWindowTitle(QtGui.QApplication.translate("PackageWidget", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.repoLabel.setText(QtGui.QApplication.translate("PackageWidget", "repo", None, QtGui.QApplication.UnicodeUTF8))
        self.packageLabel.setText(QtGui.QApplication.translate("PackageWidget", "package", None, QtGui.QApplication.UnicodeUTF8))
        self.versionLabel.setText(QtGui.QApplication.translate("PackageWidget", "X.X.X", None, QtGui.QApplication.UnicodeUTF8))
        self.installedLabel.setText(QtGui.QApplication.translate("PackageWidget", "X.X.X", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionLabel.setText(QtGui.QApplication.translate("PackageWidget", "En un lugar de l am En un lugar de l am En un lugar de l am En un lugar de l am En un lugar de l am En un lugar de l am En un lugar de l am En un lugar de l am En un lugar de l am En un lugar de l am En un lugar de l am En un lugar de l am En un lugar de l am En un lugar de l am En un lugar de l am En un lugar de l am ", None, QtGui.QApplication.UnicodeUTF8))

