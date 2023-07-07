from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow

class CreatePage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Host()
        self.ui.setupUi(self)
        self._local_ip = None

    def set_local_ip(self, local_ip):
        self._local_ip = local_ip
        if self._local_ip:
            self.ui.ip_addr.setText(f"Your IP address is {self._local_ip}")
        else:
            self.ui.ip_addr.setText("Connection failed. Please try again.")

    def get_local_ip(self):
        return self._local_ip

    

class Ui_Host(object):
    def setupUi(self, Host):
        Host.setObjectName("Host")
        Host.resize(512, 505)
        self.centralwidget = QtWidgets.QWidget(Host)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.heading = QtWidgets.QLabel(self.centralwidget)
        self.heading.setMinimumSize(QtCore.QSize(400, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.heading.setFont(font)
        self.heading.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.heading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.heading.setObjectName("heading")
        self.verticalLayout.addWidget(self.heading)
        self.subheading = QtWidgets.QLabel(self.centralwidget)
        self.subheading.setMinimumSize(QtCore.QSize(0, 30))
        self.subheading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.subheading.setObjectName("subheading")
        self.verticalLayout.addWidget(self.subheading)
        self.ip_addr = QtWidgets.QLabel(self.centralwidget)
        self.ip_addr.setMinimumSize(QtCore.QSize(0, 30))
        self.ip_addr.setObjectName("ip_addr")
        self.verticalLayout.addWidget(self.ip_addr)
        self.clipboard = QtWidgets.QLabel(self.centralwidget)
        self.clipboard.setMinimumSize(QtCore.QSize(0, 20))
        self.clipboard.setObjectName("clipboard")
        self.verticalLayout.addWidget(self.clipboard)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMaximumSize(QtCore.QSize(5000, 400))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.back = QtWidgets.QPushButton(self.centralwidget)
        self.back.setMinimumSize(QtCore.QSize(200, 0))
        self.back.setMaximumSize(QtCore.QSize(200, 50))
        self.back.setObjectName("back")
        self.verticalLayout.addWidget(self.back)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        Host.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Host)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 22))
        self.menubar.setObjectName("menubar")
        Host.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Host)
        self.statusbar.setObjectName("statusbar")
        Host.setStatusBar(self.statusbar)

        self.retranslateUi(Host)
        QtCore.QMetaObject.connectSlotsByName(Host)

    def retranslateUi(self, Host):
        _translate = QtCore.QCoreApplication.translate
        Host.setWindowTitle(_translate("Host", "MainWindow"))
        self.heading.setText(_translate("Host", "ClipShare"))
        self.subheading.setText(_translate("Host", "Share this IP address with other computers."))
        self.ip_addr.setText(_translate("Host", "Your IP address is ..."))
        self.clipboard.setText(_translate("Host", "Clipboard"))
        self.back.setText(_translate("Host", "Back"))
