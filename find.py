import sys
from PyQt4 import QtGui, QtCore

class findDialog(QtGui.QDialog):
	def __init__(self, parent = None):
		QtGui.QDialog.__init__(self, parent)
		self.findLabel = QtGui.QLabel("Find &what: ")

		self.caseCheckBox = QtGui.QCheckBox("Match &case")

		self.backwardCheckBox = QtGui.QCheckBox("Search &backward")

		self.lineEdit = QtGui.QLineEdit()
		self.findLabel.setBuddy(self.lineEdit)

		self.findButton = QtGui.QPushButton("&Find")
		self.findButton.setDefault(True)
		self.findButton.setEnabled(False)

		self.closeButton = QtGui.QPushButton("&Close")

		self.connect(self.lineEdit, QtCore.SIGNAL("textChanged(const QString&)"),
			self.enableFindButton)
		self.connect(self.findButton, QtCore.SIGNAL("clicked()"),
			self.findclicked)
		self.connect(self.closeButton, QtCore.SIGNAL("clicked()"),
			self, QtCore.SLOT("close()"))

		self.layout()

	def layout(self):
		self.leftupLayout = QtGui.QHBoxLayout()
		self.leftupLayout.addWidget(self.findLabel)
		self.leftupLayout.addWidget(self.lineEdit)

		self.leftdownLayout = QtGui.QVBoxLayout()
		self.leftdownLayout.addWidget(self.caseCheckBox)
		self.leftdownLayout.addWidget(self.backwardCheckBox)

		self.leftLayout = QtGui.QVBoxLayout()
		self.leftLayout.addLayout(self.leftupLayout)
		self.leftLayout.addLayout(self.leftdownLayout)

		self.rightLayout = QtGui.QVBoxLayout()
		self.rightLayout.addWidget(self.findButton)
		self.rightLayout.addWidget(self.closeButton)

		self.Layout = QtGui.QHBoxLayout()
		self.Layout.addLayout(self.leftLayout)
		self.Layout.addLayout(self.rightLayout)
		self.setLayout(self.Layout)

	def enableFindButton(self,text):
		self.findButton.setEnabled(text.isEmpty() == False)

	def findclicked(self):
		value = self.lineEdit.text()
		cs = Qt.CaseSensitive  if self.caseCheckBox.isChecked() == True  else Qt.CaseInsensitive 
		if self.backwardCheckBox.isChecked():
			QtCore.emit.findPrevious(value, cs)
		else:
			QtCore.emit.findNext(value,cs)

app = QtGui.QApplication(sys.argv)
dialog = findDialog()
dialog.show()
sys.exit(app.exec_())
