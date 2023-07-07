from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication
from create_page import CreatePage
from join_page import JoinPage
import netifaces
import peer
import clipboard as c

class MainPage(QMainWindow):
    join_page = False
    create_page = False
    peer = ''
    previous_clipboard_text = ""

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.create.clicked.connect(self.show_create_page)
        self.ui.join.clicked.connect(self.show_join_page)
    
    def get_local_network_ip(self):
        interfaces = netifaces.interfaces()
        for interface in interfaces:
            addresses = netifaces.ifaddresses(interface)
            if netifaces.AF_INET in addresses:
                ipv4_addresses = addresses[netifaces.AF_INET]
                for addr in ipv4_addresses:
                    ip = addr['addr']
                    if not ip.startswith('127.'):
                        return ip
        return None

    def show_create_page(self):
        local_ip = self.get_local_network_ip()
        if local_ip:
            peer1 = peer.Peer(local_ip, 6001)
            peer1.start()
            self.create_page = CreatePage()
            self.create_page.set_local_ip(local_ip)
            self.create_page.ui.back.clicked.connect(self.show_main_page)
            self.create_page.show()

            while self.create_page.isVisible():
                QtWidgets.QApplication.processEvents()

                current_clipboard_text = c.paste()
                if current_clipboard_text != self.previous_clipboard_text:
                    self.previous_clipboard_text = current_clipboard_text
                    peer1.send_data(current_clipboard_text)

            print('create page closed')
        
        else:
            self.show_main_page()

    def show_join_page(self):
        local_ip = self.get_local_network_ip()
        if local_ip:
            self.hide()
            peer2 = peer.Peer(local_ip, 6001)
            self.join_page = JoinPage()
            self.join_page.show()
            self.peer = peer2
            self.join_page.join_signal.connect(self.handle_join_input)
            
            self.join_page.ui.back.clicked.connect(self.show_main_page)
        else:
            self.show_main_page()

    def handle_join_input(self, input_text):
        print(input_text)
        self.peer.connect(input_text,6002)
        self.peer.send_data('hello there')

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
        self.heading.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.heading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.heading.setObjectName("heading")
        self.verticalLayout.addWidget(self.heading)
        self.subheading = QtWidgets.QLabel(self.centralwidget)
        self.subheading.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.heading.setText(_translate("MainWindow", "Welcome to ClipShare"))
        self.subheading.setText(
            _translate("MainWindow", "Share your clipboard easily with your other devices or friends.")
        )
        self.create.setStatusTip(_translate("MainWindow", "Host the server for others to connect."))
        self.create.setText(_translate("MainWindow", "Create"))
        self.join.setStatusTip(_translate("MainWindow", "Join an existing server."))
        self.join.setText(_translate("MainWindow", "Join"))


if __name__ == "__main__":
    import sys
    app = QApplication([])
    main_page = MainPage()
    main_page.show()
    sys.exit(app.exec())

