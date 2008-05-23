# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Sun Jan 27 11:28:18 2008
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(QtGui.QMainWindow):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,860,574).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setDockNestingEnabled(False)

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridlayout = QtGui.QGridLayout(self.centralwidget)
        self.gridlayout.setObjectName("gridlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.searchField = QtGui.QLineEdit(self.centralwidget)
        self.searchField.setObjectName("searchField")
        self.hboxlayout.addWidget(self.searchField)

        self.searchButton = QtGui.QPushButton(self.centralwidget)
        self.searchButton.setObjectName("searchButton")
        self.hboxlayout.addWidget(self.searchButton)

        self.showUpdated = QtGui.QCheckBox(self.centralwidget)
        self.showUpdated.setChecked(True)
        self.showUpdated.setObjectName("showUpdated")
        self.hboxlayout.addWidget(self.showUpdated)

        self.showOutdated = QtGui.QCheckBox(self.centralwidget)
        self.showOutdated.setChecked(True)
        self.showOutdated.setObjectName("showOutdated")
        self.hboxlayout.addWidget(self.showOutdated)

        self.showNotInstalled = QtGui.QCheckBox(self.centralwidget)
        self.showNotInstalled.setChecked(True)
        self.showNotInstalled.setObjectName("showNotInstalled")
        self.hboxlayout.addWidget(self.showNotInstalled)

        self.activeRepo = QtGui.QComboBox(self.centralwidget)
        self.activeRepo.setObjectName("activeRepo")
        self.hboxlayout.addWidget(self.activeRepo)
        self.gridlayout.addLayout(self.hboxlayout,0,0,1,1)

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")

        self.gridlayout1 = QtGui.QGridLayout(self.tab)
        self.gridlayout1.setObjectName("gridlayout1")

        self.searchResults = QtGui.QListWidget(self.tab)
        self.searchResults.setLineWidth(1)
        self.searchResults.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.searchResults.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.searchResults.setEditTriggers(QtGui.QAbstractItemView.DoubleClicked|QtGui.QAbstractItemView.EditKeyPressed|QtGui.QAbstractItemView.NoEditTriggers)
        self.searchResults.setDragEnabled(False)
        self.searchResults.setDragDropOverwriteMode(False)
        self.searchResults.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.searchResults.setAlternatingRowColors(False)
        self.searchResults.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.searchResults.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.searchResults.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.searchResults.setHorizontalScrollMode(QtGui.QAbstractItemView.ScrollPerPixel)
        self.searchResults.setMovement(QtGui.QListView.Free)
        self.searchResults.setFlow(QtGui.QListView.TopToBottom)
        self.searchResults.setResizeMode(QtGui.QListView.Adjust)
        self.searchResults.setLayoutMode(QtGui.QListView.SinglePass)
        self.searchResults.setSpacing(0)
        self.searchResults.setViewMode(QtGui.QListView.ListMode)
        self.searchResults.setModelColumn(0)
        self.searchResults.setWordWrap(True)
        self.searchResults.setSelectionRectVisible(False)
        self.searchResults.setSortingEnabled(False)
        self.searchResults.setObjectName("searchResults")
        self.gridlayout1.addWidget(self.searchResults,0,0,1,1)
        self.tabWidget.addTab(self.tab,"")

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.gridlayout2 = QtGui.QGridLayout(self.tab_2)
        self.gridlayout2.setObjectName("gridlayout2")

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.useLiveSearch = QtGui.QCheckBox(self.tab_2)
        self.useLiveSearch.setChecked(True)
        self.useLiveSearch.setObjectName("useLiveSearch")
        self.hboxlayout1.addWidget(self.useLiveSearch)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem)
        self.gridlayout2.addLayout(self.hboxlayout1,0,0,1,1)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.omitAur = QtGui.QCheckBox(self.tab_2)
        self.omitAur.setObjectName("omitAur")
        self.hboxlayout2.addWidget(self.omitAur)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem1)
        self.gridlayout2.addLayout(self.hboxlayout2,1,0,1,1)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.liveSearchInAur = QtGui.QCheckBox(self.tab_2)
        self.liveSearchInAur.setObjectName("liveSearchInAur")
        self.hboxlayout3.addWidget(self.liveSearchInAur)

        spacerItem2 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem2)
        self.gridlayout2.addLayout(self.hboxlayout3,2,0,1,1)

        self.hboxlayout4 = QtGui.QHBoxLayout()
        self.hboxlayout4.setObjectName("hboxlayout4")

        self.minSearchLength = QtGui.QSpinBox(self.tab_2)
        self.minSearchLength.setMinimum(2)
        self.minSearchLength.setMaximum(5)
        self.minSearchLength.setProperty("value",QtCore.QVariant(3))
        self.minSearchLength.setObjectName("minSearchLength")
        self.hboxlayout4.addWidget(self.minSearchLength)

        self.label = QtGui.QLabel(self.tab_2)
        self.label.setObjectName("label")
        self.hboxlayout4.addWidget(self.label)

        spacerItem3 = QtGui.QSpacerItem(547,27,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout4.addItem(spacerItem3)
        self.gridlayout2.addLayout(self.hboxlayout4,3,0,1,1)

        self.hboxlayout5 = QtGui.QHBoxLayout()
        self.hboxlayout5.setObjectName("hboxlayout5")

        self.terminalEmulator = QtGui.QLineEdit(self.tab_2)
        self.terminalEmulator.setObjectName("terminalEmulator")
        self.hboxlayout5.addWidget(self.terminalEmulator)

        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setObjectName("label_2")
        self.hboxlayout5.addWidget(self.label_2)

        spacerItem4 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout5.addItem(spacerItem4)
        self.gridlayout2.addLayout(self.hboxlayout5,4,0,1,1)

        spacerItem5 = QtGui.QSpacerItem(20,41,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout2.addItem(spacerItem5,5,0,1,1)
        self.tabWidget.addTab(self.tab_2,"")
        self.gridlayout.addWidget(self.tabWidget,1,0,1,1)

        self.tabWidget_2 = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget_2.setObjectName("tabWidget_2")

        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")

        self.gridlayout3 = QtGui.QGridLayout(self.tab_3)
        self.gridlayout3.setObjectName("gridlayout3")

        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")

        self.installQueue = QtGui.QListWidget(self.tab_3)
        self.installQueue.setDragEnabled(False)
        self.installQueue.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.installQueue.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.installQueue.setObjectName("installQueue")
        self.vboxlayout.addWidget(self.installQueue)

        self.installButton = QtGui.QPushButton(self.tab_3)
        self.installButton.setObjectName("installButton")
        self.vboxlayout.addWidget(self.installButton)
        self.gridlayout3.addLayout(self.vboxlayout,0,0,1,1)

        self.gridlayout4 = QtGui.QGridLayout()
        self.gridlayout4.setObjectName("gridlayout4")

        self.installNoDeps = QtGui.QCheckBox(self.tab_3)
        self.installNoDeps.setObjectName("installNoDeps")
        self.gridlayout4.addWidget(self.installNoDeps,1,0,1,1)

        self.installIgnoreFileConflicts = QtGui.QCheckBox(self.tab_3)
        self.installIgnoreFileConflicts.setObjectName("installIgnoreFileConflicts")
        self.gridlayout4.addWidget(self.installIgnoreFileConflicts,2,0,1,1)

        self.downloadOnly = QtGui.QCheckBox(self.tab_3)
        self.downloadOnly.setObjectName("downloadOnly")
        self.gridlayout4.addWidget(self.downloadOnly,3,0,1,1)

        spacerItem6 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout4.addItem(spacerItem6,0,0,1,1)

        spacerItem7 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout4.addItem(spacerItem7,5,0,1,1)

        self.checkBox = QtGui.QCheckBox(self.tab_3)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridlayout4.addWidget(self.checkBox,4,0,1,1)
        self.gridlayout3.addLayout(self.gridlayout4,0,1,1,1)
        self.tabWidget_2.addTab(self.tab_3,"")

        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")

        self.gridlayout5 = QtGui.QGridLayout(self.tab_4)
        self.gridlayout5.setObjectName("gridlayout5")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.removeQueue = QtGui.QListWidget(self.tab_4)
        self.removeQueue.setDragEnabled(False)
        self.removeQueue.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.removeQueue.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.removeQueue.setObjectName("removeQueue")
        self.vboxlayout1.addWidget(self.removeQueue)

        self.removeButton = QtGui.QPushButton(self.tab_4)
        self.removeButton.setObjectName("removeButton")
        self.vboxlayout1.addWidget(self.removeButton)
        self.gridlayout5.addLayout(self.vboxlayout1,0,0,1,1)

        self.vboxlayout2 = QtGui.QVBoxLayout()
        self.vboxlayout2.setObjectName("vboxlayout2")

        spacerItem8 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem8)

        self.removeRecursive = QtGui.QCheckBox(self.tab_4)
        self.removeRecursive.setChecked(True)
        self.removeRecursive.setObjectName("removeRecursive")
        self.vboxlayout2.addWidget(self.removeRecursive)

        self.removeCascade = QtGui.QCheckBox(self.tab_4)
        self.removeCascade.setObjectName("removeCascade")
        self.vboxlayout2.addWidget(self.removeCascade)

        self.removeNoDeps = QtGui.QCheckBox(self.tab_4)
        self.removeNoDeps.setObjectName("removeNoDeps")
        self.vboxlayout2.addWidget(self.removeNoDeps)

        spacerItem9 = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.vboxlayout2.addItem(spacerItem9)
        self.gridlayout5.addLayout(self.vboxlayout2,0,1,1,1)
        self.tabWidget_2.addTab(self.tab_4,"")
        self.gridlayout.addWidget(self.tabWidget_2,2,0,1,1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,860,25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "tupac", None, QtGui.QApplication.UnicodeUTF8))
        self.searchButton.setText(QtGui.QApplication.translate("MainWindow", "Search", None, QtGui.QApplication.UnicodeUTF8))
        self.showUpdated.setText(QtGui.QApplication.translate("MainWindow", "Updated", None, QtGui.QApplication.UnicodeUTF8))
        self.showOutdated.setText(QtGui.QApplication.translate("MainWindow", "Outdated", None, QtGui.QApplication.UnicodeUTF8))
        self.showNotInstalled.setText(QtGui.QApplication.translate("MainWindow", "Not installed", None, QtGui.QApplication.UnicodeUTF8))
        self.activeRepo.addItem(QtGui.QApplication.translate("MainWindow", "all repos", None, QtGui.QApplication.UnicodeUTF8))
        self.activeRepo.addItem(QtGui.QApplication.translate("MainWindow", "core", None, QtGui.QApplication.UnicodeUTF8))
        self.activeRepo.addItem(QtGui.QApplication.translate("MainWindow", "extra", None, QtGui.QApplication.UnicodeUTF8))
        self.activeRepo.addItem(QtGui.QApplication.translate("MainWindow", "comunity", None, QtGui.QApplication.UnicodeUTF8))
        self.activeRepo.addItem(QtGui.QApplication.translate("MainWindow", "aur", None, QtGui.QApplication.UnicodeUTF8))
        self.activeRepo.addItem(QtGui.QApplication.translate("MainWindow", "_NO_REPO_", None, QtGui.QApplication.UnicodeUTF8))
        self.searchResults.setStyleSheet(QtGui.QApplication.translate("MainWindow", "background-color: qlineargradient(x1: 0, y1: 0, x2: 0.5, y2: 0.5, stop: 0 #FF92BB, stop: 1 white);", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Results", None, QtGui.QApplication.UnicodeUTF8))
        self.useLiveSearch.setText(QtGui.QApplication.translate("MainWindow", "Use Live search (search as you type)", None, QtGui.QApplication.UnicodeUTF8))
        self.omitAur.setText(QtGui.QApplication.translate("MainWindow", "Never search in AUR", None, QtGui.QApplication.UnicodeUTF8))
        self.liveSearchInAur.setText(QtGui.QApplication.translate("MainWindow", "Live search also searches in AUR (not recommended)", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Number of characters to start Live searching (recommened 3 at least)", None, QtGui.QApplication.UnicodeUTF8))
        self.terminalEmulator.setText(QtGui.QApplication.translate("MainWindow", "konsole -e %c", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Terminal emulator (%c = command to execute)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.installButton.setText(QtGui.QApplication.translate("MainWindow", "Install", None, QtGui.QApplication.UnicodeUTF8))
        self.installNoDeps.setText(QtGui.QApplication.translate("MainWindow", "Ignore dependencies", None, QtGui.QApplication.UnicodeUTF8))
        self.installIgnoreFileConflicts.setText(QtGui.QApplication.translate("MainWindow", "ingore file conflicts", None, QtGui.QApplication.UnicodeUTF8))
        self.downloadOnly.setText(QtGui.QApplication.translate("MainWindow", "Only download", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox.setText(QtGui.QApplication.translate("MainWindow", "Pre-download (recommended)", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Install queue", None, QtGui.QApplication.UnicodeUTF8))
        self.removeButton.setText(QtGui.QApplication.translate("MainWindow", "Remove", None, QtGui.QApplication.UnicodeUTF8))
        self.removeRecursive.setText(QtGui.QApplication.translate("MainWindow", "Recursive (recommended)", None, QtGui.QApplication.UnicodeUTF8))
        self.removeCascade.setText(QtGui.QApplication.translate("MainWindow", "Cascade (carefully)", None, QtGui.QApplication.UnicodeUTF8))
        self.removeNoDeps.setText(QtGui.QApplication.translate("MainWindow", "Ignore dependencies", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QtGui.QApplication.translate("MainWindow", "Remove queue", None, QtGui.QApplication.UnicodeUTF8))

