"""
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys


class Valentina_web(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(Valentina_web, self).__init__(*args, **kwargs)
        ## self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
        self.tabs.currentChanged.connect(self.current_tab_changed)
        self.tabs.setTabsClosable(False)
        self.tabs.tabCloseRequested.connect(self.close_current_tab)
        self.setCentralWidget(self.tabs)
        # self.status = QStatusBar()
        # self.setStatusBar(self.status)
        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)
        back_btn = QAction("Back", self)
        back_btn.setStatusTip("Back to previous page")
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        navtb.addAction(back_btn)
        next_btn = QAction("Forward", self)
        next_btn.setStatusTip("Forward to next page")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)
        reload_btn = QAction("Reload", self)
        reload_btn.setStatusTip("Reload page")
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)
        home_btn = QAction("Home", self)
        home_btn.setStatusTip("Go home")
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)
        navtb.addSeparator()
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)
        stop_btn = QAction("Stop", self)
        stop_btn.setStatusTip("Stop loading current page")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        self.add_new_tab(QUrl('http://www.yandex.ru'), 'Homepage')
        self.show()
        self.setWindowTitle("Valentina Web")

    def add_new_tab(self, qurl=None, label="Blank"):
        if qurl is None:
            qurl = QUrl('http://www.yandex.ru')
        browser = QWebEngineView()
        browser.setUrl(qurl)
        i = self.tabs.addTab(browser, label)
        self.tabs.setCurrentIndex(i)
        browser.urlChanged.connect(lambda qurl, browser=browser:
                                   self.update_urlbar(qurl, browser))
        browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                     self.tabs.setTabText(i, browser.page().title()))

    def tab_open_doubleclick(self, i):
        if i == -1:
            self.add_new_tab()

    def current_tab_changed(self, i):
        qurl = self.tabs.currentWidget().url()
        self.update_urlbar(qurl, self.tabs.currentWidget())
        self.update_title(self.tabs.currentWidget())

    def close_current_tab(self, i):
        if self.tabs.count() < 2:
            return
        self.tabs.removeTab(i)

    def update_title(self, browser):
        if browser != self.tabs.currentWidget():
            return
        title = self.tabs.currentWidget().page().title()
        self.setWindowTitle("% s - Geek PyQt5" % title)

    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl("http://www.yandex.ru"))

    def navigate_to_url(self):
        q = QUrl(self.urlbar.text())
        if q.scheme() == "":
            q.setScheme("http")
        self.tabs.currentWidget().setUrl(q)

    def update_urlbar(self, q, browser=None):
        if browser != self.tabs.currentWidget():
            return
        self.urlbar.setText(q.toString())
        self.urlbar.setCursorPosition(0)

from PyQt5 import QtGui, QtWidgets, QtCore, QtWebEngineWidgets
import sys


class UiValentina(object):
    def setupUi(self, Valentina):
        Valentina.setObjectName("Valentina")
        Valentina.setAutoFillBackground(False)
        Valentina.resize(856, 480)

        self.centralwidget = QtWidgets.QWidget(Valentina)
        self.centralwidget.setObjectName("centralwidget")

        self.interf = QtWidgets.QVer

        self.url_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.url_edit.setGeometry(0, 0, 856, 25)

        self.browser = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.browser.setGeometry(0, 25, 856, 480)
        self.browser.setUrl(QtCore.QUrl("http://www.yandex.ru"))

        Valentina.setCentralWidget(self.centralwidget)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = UiValentina()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""

from PyQt5 import QtCore, QtGui, QtWidgets, QtWebEngineWidgets


class Ui_VBrowser(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("VBrowser")
        MainWindow.resize(1280, 720)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/Valentina.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # +++
        #       self.url_area = QtWidgets.QTextEdit(self.centralwidget)
        # ------------------------------> v^v^v^v^v
        self.url_area = QtWidgets.QLineEdit(self.centralwidget)  # +++

        self.url_area.setGeometry(QtCore.QRect(160, 0, 791, 41))
        self.url_area.setObjectName("url_area")

        self.refresh_btn = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_btn.setGeometry(QtCore.QRect(80, 0, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.refresh_btn.setFont(font)
        self.refresh_btn.setObjectName("refresh_btn")

        self.back_btn = QtWidgets.QPushButton(self.centralwidget)
        self.back_btn.setGeometry(QtCore.QRect(0, 0, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.back_btn.setFont(font)
        self.back_btn.setObjectName("back_btn")

        self.forward_btn = QtWidgets.QPushButton(self.centralwidget)
        self.forward_btn.setGeometry(QtCore.QRect(40, 0, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.forward_btn.setFont(font)
        self.forward_btn.setObjectName("forward_btn")

        self.home_btn = QtWidgets.QPushButton(self.centralwidget)
        self.home_btn.setGeometry(QtCore.QRect(120, 0, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.home_btn.setFont(font)
        self.home_btn.setObjectName("home_btn")

        self.web = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.web.setGeometry(QtCore.QRect(0, 40, 1271, 671))
        self.web.setObjectName("web")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_VBrowser()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
