# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edledit/edledit.ui'
#
# Created: Sat Jul 16 10:56:41 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(714, 480)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/edledit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.player = VideoPlayer(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.player.sizePolicy().hasHeightForWidth())
        self.player.setSizePolicy(sizePolicy)
        self.player.setMinimumSize(QtCore.QSize(320, 180))
        self.player.setBaseSize(QtCore.QSize(640, 360))
        self.player.setObjectName(_fromUtf8("player"))
        self.gridLayout.addWidget(self.player, 0, 0, 1, 1)
        self.edlWidget = EDLWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edlWidget.sizePolicy().hasHeightForWidth())
        self.edlWidget.setSizePolicy(sizePolicy)
        self.edlWidget.setMinimumSize(QtCore.QSize(0, 30))
        self.edlWidget.setAutoFillBackground(True)
        self.edlWidget.setObjectName(_fromUtf8("edlWidget"))
        self.gridLayout.addWidget(self.edlWidget, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 714, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName(_fromUtf8("menu_File"))
        self.menu_Help = QtGui.QMenu(self.menubar)
        self.menu_Help.setObjectName(_fromUtf8("menu_Help"))
        self.menu_Go = QtGui.QMenu(self.menubar)
        self.menu_Go.setObjectName(_fromUtf8("menu_Go"))
        self.menu_Edit = QtGui.QMenu(self.menubar)
        self.menu_Edit.setObjectName(_fromUtf8("menu_Edit"))
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(16, 16))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.BottomToolBarArea, self.toolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSaveEDL = QtGui.QAction(MainWindow)
        self.actionSaveEDL.setEnabled(False)
        self.actionSaveEDL.setObjectName(_fromUtf8("actionSaveEDL"))
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionSkipForward = QtGui.QAction(MainWindow)
        self.actionSkipForward.setEnabled(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/control_fastforward.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSkipForward.setIcon(icon1)
        self.actionSkipForward.setIconVisibleInMenu(True)
        self.actionSkipForward.setObjectName(_fromUtf8("actionSkipForward"))
        self.actionSkipBackwards = QtGui.QAction(MainWindow)
        self.actionSkipBackwards.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/control_rewind.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSkipBackwards.setIcon(icon2)
        self.actionSkipBackwards.setIconVisibleInMenu(True)
        self.actionSkipBackwards.setObjectName(_fromUtf8("actionSkipBackwards"))
        self.actionPreviousCutBoundary = QtGui.QAction(MainWindow)
        self.actionPreviousCutBoundary.setEnabled(False)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/control_start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionPreviousCutBoundary.setIcon(icon3)
        self.actionPreviousCutBoundary.setIconVisibleInMenu(True)
        self.actionPreviousCutBoundary.setObjectName(_fromUtf8("actionPreviousCutBoundary"))
        self.actionNextCutBoundary = QtGui.QAction(MainWindow)
        self.actionNextCutBoundary.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/control_end.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionNextCutBoundary.setIcon(icon4)
        self.actionNextCutBoundary.setIconVisibleInMenu(True)
        self.actionNextCutBoundary.setObjectName(_fromUtf8("actionNextCutBoundary"))
        self.actionPlayPause = QtGui.QAction(MainWindow)
        self.actionPlayPause.setCheckable(True)
        self.actionPlayPause.setEnabled(False)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/control_play.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/control_pause.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionPlayPause.setIcon(icon5)
        self.actionPlayPause.setIconVisibleInMenu(True)
        self.actionPlayPause.setObjectName(_fromUtf8("actionPlayPause"))
        self.actionStartCut = QtGui.QAction(MainWindow)
        self.actionStartCut.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/cut_start.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStartCut.setIcon(icon6)
        self.actionStartCut.setIconVisibleInMenu(True)
        self.actionStartCut.setObjectName(_fromUtf8("actionStartCut"))
        self.actionStopCut = QtGui.QAction(MainWindow)
        self.actionStopCut.setEnabled(False)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/cut_stop.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStopCut.setIcon(icon7)
        self.actionStopCut.setIconVisibleInMenu(True)
        self.actionStopCut.setObjectName(_fromUtf8("actionStopCut"))
        self.actionDeleteCut = QtGui.QAction(MainWindow)
        self.actionDeleteCut.setEnabled(False)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/cross.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDeleteCut.setIcon(icon8)
        self.actionDeleteCut.setIconVisibleInMenu(True)
        self.actionDeleteCut.setObjectName(_fromUtf8("actionDeleteCut"))
        self.actionIncreaseStep = QtGui.QAction(MainWindow)
        self.actionIncreaseStep.setObjectName(_fromUtf8("actionIncreaseStep"))
        self.actionDecreaseStep = QtGui.QAction(MainWindow)
        self.actionDecreaseStep.setObjectName(_fromUtf8("actionDecreaseStep"))
        self.actionDecreaseStepAndSkipForward = QtGui.QAction(MainWindow)
        self.actionDecreaseStepAndSkipForward.setObjectName(_fromUtf8("actionDecreaseStepAndSkipForward"))
        self.actionDecreaseStepAndSkipBackwards = QtGui.QAction(MainWindow)
        self.actionDecreaseStepAndSkipBackwards.setObjectName(_fromUtf8("actionDecreaseStepAndSkipBackwards"))
        self.actionCutSetActionSkip = QtGui.QAction(MainWindow)
        self.actionCutSetActionSkip.setEnabled(False)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/cut_red.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCutSetActionSkip.setIcon(icon9)
        self.actionCutSetActionSkip.setIconVisibleInMenu(True)
        self.actionCutSetActionSkip.setObjectName(_fromUtf8("actionCutSetActionSkip"))
        self.actionCutSetActionMute = QtGui.QAction(MainWindow)
        self.actionCutSetActionMute.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/sound_mute.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCutSetActionMute.setIcon(icon10)
        self.actionCutSetActionMute.setIconVisibleInMenu(True)
        self.actionCutSetActionMute.setObjectName(_fromUtf8("actionCutSetActionMute"))
        self.menu_File.addAction(self.actionOpen)
        self.menu_File.addAction(self.actionSaveEDL)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionPlayPause)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.actionQuit)
        self.menu_Help.addAction(self.actionAbout)
        self.menu_Go.addAction(self.actionSkipForward)
        self.menu_Go.addAction(self.actionSkipBackwards)
        self.menu_Go.addAction(self.actionDecreaseStepAndSkipForward)
        self.menu_Go.addAction(self.actionDecreaseStepAndSkipBackwards)
        self.menu_Go.addSeparator()
        self.menu_Go.addAction(self.actionIncreaseStep)
        self.menu_Go.addAction(self.actionDecreaseStep)
        self.menu_Go.addSeparator()
        self.menu_Go.addAction(self.actionNextCutBoundary)
        self.menu_Go.addAction(self.actionPreviousCutBoundary)
        self.menu_Edit.addAction(self.actionStartCut)
        self.menu_Edit.addAction(self.actionStopCut)
        self.menu_Edit.addSeparator()
        self.menu_Edit.addAction(self.actionDeleteCut)
        self.menu_Edit.addAction(self.actionCutSetActionSkip)
        self.menu_Edit.addAction(self.actionCutSetActionMute)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Edit.menuAction())
        self.menubar.addAction(self.menu_Go.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())
        self.toolBar.addAction(self.actionPreviousCutBoundary)
        self.toolBar.addAction(self.actionSkipBackwards)
        self.toolBar.addAction(self.actionPlayPause)
        self.toolBar.addAction(self.actionSkipForward)
        self.toolBar.addAction(self.actionNextCutBoundary)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionStartCut)
        self.toolBar.addAction(self.actionStopCut)
        self.toolBar.addAction(self.actionDeleteCut)
        self.toolBar.addAction(self.actionCutSetActionSkip)
        self.toolBar.addAction(self.actionCutSetActionMute)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionQuit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QObject.connect(self.actionOpen, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.actionFileOpen)
        QtCore.QObject.connect(self.actionSaveEDL, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.actionFileSaveEDL)
        QtCore.QObject.connect(self.actionAbout, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.actionHelpAbout)
        QtCore.QObject.connect(self.actionNextCutBoundary, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.seekNextBoundary)
        QtCore.QObject.connect(self.actionPreviousCutBoundary, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.seekPrevBoundary)
        QtCore.QObject.connect(self.actionSkipBackwards, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.seekBackwards)
        QtCore.QObject.connect(self.actionSkipForward, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.seekForward)
        QtCore.QObject.connect(self.actionPlayPause, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.togglePlayPause)
        QtCore.QObject.connect(self.actionDeleteCut, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.cutDelete)
        QtCore.QObject.connect(self.actionStartCut, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.cutStart)
        QtCore.QObject.connect(self.actionStopCut, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.cutStop)
        QtCore.QObject.connect(self.actionIncreaseStep, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.stepUp)
        QtCore.QObject.connect(self.actionDecreaseStep, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.stepDown)
        QtCore.QObject.connect(self.actionDecreaseStepAndSkipForward, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.smartSeekForward)
        QtCore.QObject.connect(self.actionDecreaseStepAndSkipBackwards, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.smartSeekBackwards)
        QtCore.QObject.connect(self.actionCutSetActionSkip, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.cutSetActionSkip)
        QtCore.QObject.connect(self.actionCutSetActionMute, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.cutSetActionMute)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "EDL Editor", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Help.setTitle(QtGui.QApplication.translate("MainWindow", "&Help", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Go.setTitle(QtGui.QApplication.translate("MainWindow", "&Go", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_Edit.setTitle(QtGui.QApplication.translate("MainWindow", "&Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "&About...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "&Open movie...", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+O", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveEDL.setText(QtGui.QApplication.translate("MainWindow", "&Save EDL", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveEDL.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "&Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSkipForward.setText(QtGui.QApplication.translate("MainWindow", "Skip &Forward", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSkipForward.setShortcut(QtGui.QApplication.translate("MainWindow", "Right", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSkipBackwards.setText(QtGui.QApplication.translate("MainWindow", "Skip &Backwards", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSkipBackwards.setShortcut(QtGui.QApplication.translate("MainWindow", "Left", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreviousCutBoundary.setText(QtGui.QApplication.translate("MainWindow", "&Previous Cut Boundary", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPreviousCutBoundary.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+Left", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNextCutBoundary.setText(QtGui.QApplication.translate("MainWindow", "&Next Cut Boundary", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNextCutBoundary.setShortcut(QtGui.QApplication.translate("MainWindow", "Alt+Right", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlayPause.setText(QtGui.QApplication.translate("MainWindow", "&Play/Pause", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPlayPause.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Space", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStartCut.setText(QtGui.QApplication.translate("MainWindow", "&Start cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStartCut.setShortcut(QtGui.QApplication.translate("MainWindow", "[", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStopCut.setText(QtGui.QApplication.translate("MainWindow", "S&top cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionStopCut.setShortcut(QtGui.QApplication.translate("MainWindow", "]", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteCut.setText(QtGui.QApplication.translate("MainWindow", "&Delete current cut", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDeleteCut.setShortcut(QtGui.QApplication.translate("MainWindow", "Del", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIncreaseStep.setText(QtGui.QApplication.translate("MainWindow", "&Increase step", None, QtGui.QApplication.UnicodeUTF8))
        self.actionIncreaseStep.setShortcut(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDecreaseStep.setText(QtGui.QApplication.translate("MainWindow", "&Decrease step", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDecreaseStep.setShortcut(QtGui.QApplication.translate("MainWindow", "-", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDecreaseStepAndSkipForward.setText(QtGui.QApplication.translate("MainWindow", "Decrease step and skip forward", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDecreaseStepAndSkipForward.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Right", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDecreaseStepAndSkipBackwards.setText(QtGui.QApplication.translate("MainWindow", "Decrease step and skip backwards", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDecreaseStepAndSkipBackwards.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+Left", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCutSetActionSkip.setText(QtGui.QApplication.translate("MainWindow", "Set current cut action to S&kip", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCutSetActionSkip.setShortcut(QtGui.QApplication.translate("MainWindow", "S", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCutSetActionMute.setText(QtGui.QApplication.translate("MainWindow", "Set current cut action to &Mute", None, QtGui.QApplication.UnicodeUTF8))
        self.actionCutSetActionMute.setShortcut(QtGui.QApplication.translate("MainWindow", "M", None, QtGui.QApplication.UnicodeUTF8))

from edlwidget import EDLWidget
from PhononClasses import VideoPlayer
import edledit_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
