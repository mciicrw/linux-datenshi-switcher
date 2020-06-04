import os
import sys
import qdarkstyle
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class aboutDialog(QDialog):
	def __init__(self, parent):
		super().__init__(parent)
		self.setFixedSize(300,315)
		self.setWindowTitle("About")

		abDialogLay = QVBoxLayout()
		logoLayout = QHBoxLayout()
		buttonLayout = QHBoxLayout()

		creatorBox = QGroupBox("About Switcher")
		creatorBoxLayout = QVBoxLayout()

		licenseBox = QGroupBox("About License")
		licenseBoxLayout = QVBoxLayout()

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
		creatorBoxLayout.addWidget(aboutCreate)
		creatorBoxLayout.setContentsMargins(3,3,3,3)

		creatorBox.setLayout(creatorBoxLayout)

		aboutLicense = QLabel("This program is created under LGPL 3.0 license, modification is allowed by following the conditions provided by LGPL 3.0")
		aboutLicense.setWordWrap(True)
		licenseBoxLayout.addWidget(aboutLicense)
		licenseBoxLayout.setContentsMargins(3,3,3,3)

		licenseBox.setLayout(licenseBoxLayout)

		versionLabel = QLabel("Alpha 3-r9")
		vLabelFont = versionLabel.font()
		vLabelFont.setPointSize(8)
#		versionLabel.setTextFormat("Bold")
		versionLabel.setFont(vLabelFont)
		buttonLayout.addWidget(versionLabel)

		okBtn = QPushButton("Ok")
		okBtn.clicked.connect(self.close)
		okBtn.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
		buttonLayout.addWidget(okBtn, alignment=Qt.AlignRight)

		abDialogLay.addLayout(logoLayout)
		abDialogLay.addWidget(aboutName)
		abDialogLay.addWidget(creatorBox)
		abDialogLay.addWidget(licenseBox)
		abDialogLay.addLayout(buttonLayout)
		abDialogLay.setAlignment(Qt.AlignCenter)
		abDialogLay.setSpacing(1)

		self.setLayout(abDialogLay)

class installCertificate(QDialog):
	def __init__(self, parent):
		super().__init__(parent)
		self.setFixedSize(400,420)
		self.setWindowTitle("Installing Certificate")
		self.lang = 1

		iCertLay = QVBoxLayout()
		butCertLay = QHBoxLayout()

		installBox = QGroupBox("How to install certificate")
		installBoxLayout = QVBoxLayout()

		self.certText = QLabel()
		sourc = open('dep/install-en.txt').read()
		self.certText.setText(sourc)
		self.certText.setWordWrap(True)
		installBoxLayout.addWidget(self.certText)

		installBoxLayout.setContentsMargins(4,4,4,4)

		installBox.setLayout(installBoxLayout)

		iCertLay.addWidget(installBox)

		langBtn = QPushButton("Language")
		langBtn.clicked.connect(self.lang_handler)
		langBtn.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
		butCertLay.addWidget(langBtn)

		exBtn = QPushButton("Close")
		exBtn.clicked.connect(self.close)
		exBtn.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
		butCertLay.addWidget(exBtn, alignment=Qt.AlignRight)

		iCertLay.addLayout(butCertLay)

		self.setLayout(iCertLay)

	@pyqtSlot()
	def lang_handler(self):
		enLang = open('dep/install-en.txt').read()
		idLang = open('dep/install-id.txt').read() 
		if self.lang == 1:
			self.certText.setText(idLang)
			self.lang = 2
		else:
			self.certText.setText(enLang)
			self.lang = 1


class App(QWidget):
	def __init__(self):
		super().__init__()
		with open('../hosts','r') as f:
				if "139.99.88.243 osu.ppy.sh" in f.read():
					self.serv = "Datenshi"
				elif '*' + "osu.ppy.sh" in f.read():
					self.serv = "Other Private Server"
				else:
					self.serv = "Official Bancho Server"
		self.initUI()

	def initUI(self):
		self.setWindowTitle("Datenshi Switcher")

		warn = QLabel("PLEASE RUN AS ROOT!")
		siz = warn.font()
		siz.setPointSize(23)
		warn.setFont(siz)
		warn.setWordWrap(True)
		warn.setStyleSheet("color: red")
		warn.setAlignment(Qt.AlignCenter)

		logo = QLabel("logo")
		logo.setPixmap(QPixmap('dep/datenshi.png'))

		date = QLabel("Welcome to Datenshi Switcher!")
		font = date.font()
		font.setPointSize(15)
		date.setFont(font)

		self.stat = QLabel("You currently connected to " + self.serv)

		pbtn = QPushButton("Swith to PPY")
		pbtn.setToolTip("Switch to Offical Bancho server")
		pbtn.clicked.connect(self.pb_click)

		dbtn = QPushButton("Switch to Datenshi")
		dbtn.setToolTip("Switch to Datneshi server")
		dbtn.clicked.connect(self.db_click)

		aboutBtn = QPushButton("about")
		aboutBtn.setFlat(True)
		aboutBtn.clicked.connect(self.ab_click)
		aboutBtn.setSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)

		self.cKonek()

		layH = QHBoxLayout()

		layH.addWidget(pbtn)
		layH.addWidget(dbtn)
		#layH.setContentsMargins(6,3,6,3)

		mLayout = QVBoxLayout()

		mLayout.addWidget(logo, alignment=Qt.AlignCenter)
		mLayout.addWidget(date)
		mLayout.addWidget(self.stat)
		mLayout.addLayout(layH)
		mLayout.addWidget(self.konekBox)
		mLayout.addWidget(aboutBtn)
		mLayout.setSpacing(1)
		mLayout.setContentsMargins(6,3,6,6)

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
		hoKoLayout.setContentsMargins(3,3,3,3)

		self.konekBox.setLayout(hoKoLayout)

	@pyqtSlot()
	def pb_click(self):
		with open("../hosts", "r") as f:
			lines = f.readlines()
		with open("../hosts", "w") as f:
			for line in lines:
				if line.strip("\n") != "139.99.88.243 osu.ppy.sh c.ppy.sh c1.ppy.sh c2.ppy.sh c3.ppy.sh c4.ppy.sh c5.ppy.sh c6.ppy.sh ce.ppy.sh a.ppy.sh i.ppy.sh":
					f.write(line)

		with open("../hosts", "r") as f:
			file_out = []
			for line in f:
				file_out.append(line)

		while file_out[-1] == '\n':
			file_out.pop(-1)

		with open("../hosts", "w") as f:
			f.write(''.join(file_out))

		self.stat.setText("You currently connected to Official Bancho Server")


	@pyqtSlot()
	def db_click(self):
		with open("../hosts", "a") as f:
			f.write("\n")
			f.write("139.99.88.243 osu.ppy.sh c.ppy.sh c1.ppy.sh c2.ppy.sh c3.ppy.sh c4.ppy.sh c5.ppy.sh c6.ppy.sh ce.ppy.sh a.ppy.sh i.ppy.sh")
		self.stat.setText("You currently connected to Datenshi")

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
    dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
    app = QApplication(sys.argv)
    app.setStyleSheet(dark_stylesheet)
    ex = App()
    sys.exit(app.exec_())	