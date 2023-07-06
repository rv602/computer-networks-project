from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from create_page import CreatePage
from join_page import JoinPage
from PyQt5.QtCore import pyqtSignal

class MainPage(QMainWindow):
    join_page= False
    create_page = False
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.create.clicked.connect(self.show_create_page)
        self.ui.join.clicked.connect(self.show_join_page)

    def show_create_page(self):
        self.hide()
        self.create_page = CreatePage()
        self.create_page.ui.back.clicked.connect(self.show_main_page)
        self.create_page.show()

    def show_join_page(self):
        self.hide()
        self.join_page = JoinPage()
        self.join_page.ui.back.clicked.connect(self.show_main_page)
        self.join_page.show()

    def show_main_page(self):
        self.show()
        if self.create_page:
            self.create_page.close()
        if self.join_page:
            self.join_page.close()


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(465, 421)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.heading.setFont(font)
        self.heading.setTextFormat(QtCore.Qt.RichText)
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.verticalLayout.addWidget(self.heading)
        self.subheading = QtWidgets.QLabel(self.centralwidget)
        self.subheading.setAlignment(QtCore.Qt.AlignCenter)
        self.subheading.setObjectName("subheading")
        self.verticalLayout.addWidget(self.subheading)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create = QtWidgets.QPushButton(self.centralwidget)
        self.create.setObjectName("create")
        self.horizontalLayout.addWidget(self.create)
        self.join = QtWidgets.QPushButton(self.centralwidget)
        self.join.setObjectName("join")
        self.horizontalLayout.addWidget(self.join)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 465, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # self.create.clicked.connect(self.create_scr)
        # self.join.clicked.connect(self.join_scr)

    # def create_scr(self):
    #     self.Host = QtWidgets.QMainWindow()
    #     self.ui = Ui_Host()
    #     self.ui.setupUi(self.Host)
    #     self.hide()
    #     self.Host.show()

    # def join_scr(self):
    #     self.Join = QtWidgets.QMainWindow()
    #     self.ui = Ui_Join()
    #     self.ui.setupUi(self.Join)
    #     self.Join.show()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.heading.setText(_translate("MainWindow", "Welcome to ClipShare"))
        self.subheading.setText(_translate("MainWindow", "Share you clipboard easily with your other devices or friends."))
        self.create.setStatusTip(_translate("MainWindow", "Hosts the server for other to connect."))
        self.create.setText(_translate("MainWindow", "Create"))
        self.join.setStatusTip(_translate("MainWindow", "Join existing server."))
        self.join.setText(_translate("MainWindow", "Join"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    main_page = MainPage()
    main_page.show()
    sys.exit(app.exec_())


