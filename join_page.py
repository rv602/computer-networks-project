from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class JoinPage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Join()
        self.ui.setupUi(self)


class Ui_Join(object):
    def setupUi(self, Join):
        Join.setObjectName("Join")
        Join.resize(473, 529)
        self.centralwidget = QtWidgets.QWidget(Join)
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
        self.heading.setTextFormat(QtCore.Qt.RichText)
        self.heading.setAlignment(QtCore.Qt.AlignCenter)
        self.heading.setObjectName("heading")
        self.verticalLayout.addWidget(self.heading)
        self.subheading = QtWidgets.QLabel(self.centralwidget)
        self.subheading.setMinimumSize(QtCore.QSize(0, 30))
        self.subheading.setAlignment(QtCore.Qt.AlignCenter)
        self.subheading.setObjectName("subheading")
        self.verticalLayout.addWidget(self.subheading)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
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
        Join.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Join)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 473, 22))
        self.menubar.setObjectName("menubar")
        Join.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Join)
        self.statusbar.setObjectName("statusbar")
        Join.setStatusBar(self.statusbar)

        self.retranslateUi(Join)
        QtCore.QMetaObject.connectSlotsByName(Join)
        
    def retranslateUi(self, Join):
        _translate = QtCore.QCoreApplication.translate
        Join.setWindowTitle(_translate("Join", "Join"))
        self.heading.setText(_translate("Join", "ClipShare"))
        self.subheading.setText(_translate("Join", "Enter host Ip address"))
        self.label.setText(_translate("Join", "You are connected or not connected"))
        self.clipboard.setText(_translate("Join", "Clipboard"))
        self.back.setText(_translate("Join", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Join = QtWidgets.QMainWindow()
    ui = Ui_Join()
    ui.setupUi(Join)
    Join.show()
    sys.exit(app.exec_())
