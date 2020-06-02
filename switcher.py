import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class aboutDialog(QDialog):
	def __init__(self, parent):
		super().__init__(parent)
		self.setFixedSize(280,280)
		self.setWindowTitle("About")

		abDialogLay = QVBoxLayout()
		logoLayout = QHBoxLayout()

		qtLogo = QLabel()
		qLogoPic = QPixmap()
		qLogoPic.load('dep/qt-logo.png')
		qLogoPic = qLogoPic.scaledToWidth(50)
		qtLogo.setPixmap(qLogoPic)
		qtLogo.setAlignment(Qt.AlignRight)
		logoLayout.addWidget(qtLogo)

		pyLogo = QLabel()
		pLogoPic = QPixmap()
		pLogoPic.load('dep/python-logo.png')
		pLogoPic = pLogoPic.scaledToWidth(50)
		pyLogo.setPixmap(pLogoPic)
		logoLayout.addWidget(pyLogo)

		aboutName = QLabel("Datenshi switcher")
		aboutSize = aboutName.font()
		aboutSize.setPointSize(15)
		aboutName.setFont(aboutSize)

		aboutCreate = QLabel("Created by TypicalNoob- using PyQt5 Library and Python 3 Programming language")
		aboutCreate.setWordWrap(True)

		aboutLicense = QLabel("This program is created under LGPL 3.0 license, modification is allowed by following the conditions provided by LGPL 3.0")
		aboutLicense.setWordWrap(True)

		okBtn = QPushButton("Ok")
		okBtn.clicked.connect(self.close)
		okBtn.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)

		abDialogLay.addLayout(logoLayout)
		abDialogLay.addWidget(aboutName)
		abDialogLay.addWidget(aboutCreate)
		abDialogLay.addWidget(aboutLicense)
		abDialogLay.addWidget(okBtn, alignment=Qt.AlignRight)
		abDialogLay.setAlignment(Qt.AlignCenter)

		self.setLayout(abDialogLay)

class installCertificate(QDialog):
	def __init__(self, parent):
		super().__init__(parent)
		self.setFixedSize(350,350)
		self.setWindowTitle("Installing Certificate")

		iCertLay = QVBoxLayout()

		enCertText = QLabel()
		sourc = open('dep/install-en.txt').read()
		enCertText.setText(sourc)
		enCertText.setWordWrap(True)
		iCertLay.addWidget(enCertText)

		exBtn = QPushButton("Close")
		exBtn.clicked.connect(self.close)
		iCertLay.addWidget(exBtn)

		self.setLayout(iCertLay)

class App(QWidget):
	def __init__(self):
		super().__init__()
		with open('/etc/hosts','r') as f:
				if "139.99.88.243" in f.read():
					self.serv = "you currently connected to Datenshi"
				else:
					self.serv = "you currently connected to Official Bancho Server"
		self.initUI()

	def initUI(self):
		self.setWindowTitle("Datenshi Switcher")

		warn = QLabel("PLEASE RUN AS ROOT!")
		siz = warn.font()
		siz.setPointSize(23)
		warn.setFont(siz)
		warn.setWordWrap(True)
		warn.setStyleSheet("background-color: white; border: 5px solid white; color: red")

		logo = QLabel("logo")
		logo.setPixmap(QPixmap('dep/datenshi.png'))

		date = QLabel("Welcome to Datenshi Switcher!")
		font = date.font()
		font.setPointSize(15)
		date.setFont(font)

		self.stat = QLabel(self.serv)

		pbtn = QPushButton("Swith to PPY", self)
		pbtn.setToolTip("Switch to Offical Bancho server")
		pbtn.clicked.connect(self.pb_click)

		dbtn = QPushButton("Switch to Datenshi", self)
		dbtn.setToolTip("Switch to Datneshi server")
		dbtn.clicked.connect(self.db_click)

		aboutBtn = QPushButton("about",self)
		aboutBtn.setFlat(True)
		aboutBtn.clicked.connect(self.ab_click)
		aboutBtn.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)

		self.cKonek()

		layH = QHBoxLayout()

		layH.addWidget(pbtn)
		layH.addWidget(dbtn)

		mLayout = QVBoxLayout()

		mLayout.addWidget(logo)
		mLayout.addWidget(date)
		mLayout.addWidget(self.stat)
		mLayout.addLayout(layH)
		mLayout.addWidget(self.konekBox)
		mLayout.addWidget(aboutBtn)

		wLayout = QVBoxLayout()
		wLayout.addWidget(warn)
		wLayout.setContentsMargins(0,0,0,0)

		if os.geteuid()==0:
			self.setLayout(mLayout)
			self.setFixedSize(350,250)
		else:
			self.setLayout(wLayout)
			self.setFixedSize(385,80)

		self.show()

	def cKonek(self):
		self.konekBox = QGroupBox("Server Checker")
		hoKoLayout = QHBoxLayout()

		tbtn = QPushButton("Check Server")
		tbtn.setToolTip("Check if server is Online")
		tbtn.clicked.connect(self.tb_click)
		hoKoLayout.addWidget(tbtn)

		self.stats = QLabel(self)
		self.stats.setText("Press the button")
		hoKoLayout.addWidget(self.stats)

		self.konekBox.setLayout(hoKoLayout)

	@pyqtSlot()
	def pb_click(self):
		with open("/etc/hosts", "r") as f:
			lines = f.readlines()
		with open("/etc/hosts", "w") as f:
			for line in lines:
				if line.strip("\n") != "139.99.88.243 osu.ppy.sh c.ppy.sh c1.ppy.sh c2.ppy.sh c3.ppy.sh c4.ppy.sh c5.ppy.sh c6.ppy.sh ce.ppy.sh a.ppy.sh i.ppy.sh":
					f.write(line)
		self.stat.setText("you currently connected to Official Bancho Server")


	@pyqtSlot()
	def db_click(self):
		with open("/etc/hosts", "a") as f:
			f.write("\n")
			f.write("139.99.88.243 osu.ppy.sh c.ppy.sh c1.ppy.sh c2.ppy.sh c3.ppy.sh c4.ppy.sh c5.ppy.sh c6.ppy.sh ce.ppy.sh a.ppy.sh i.ppy.sh")
		self.stat.setText("you currently connected to Datenshi")

		self.inCert = installCertificate(self)
		self.inCert.exec_()

	@pyqtSlot()
	def tb_click(self):
		address = "139.99.88.243"
		response = os.system("ping -c 1 " + address)
		if response == 0:
			self.stats.setText("Server is Online")
			self.stats.setStyleSheet("color: lime")
		else:
			self.stats.setText("Server is Offline")
			self.stats.setStyleSheet("color: orangered")

	@pyqtSlot()
	def ab_click(self):
		self.abDialog = aboutDialog(self)
		self.abDialog.show()
		


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())	