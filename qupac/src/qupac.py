#!/usr/bin/python
import sys, os
#import signal
import popen2
import time
from PyQt4 import QtCore, QtGui
from MainWindow import Ui_MainWindow
from PackageWidget import Ui_PackageWidget
import os.path

import pexpect

version="0.1.3"

if not os.path.exists("/var/lib/tupac"):
	print "tupac cache dir does not exist, calling tupac as superuser."
	os.system("konsole -e sudo tupac")

def getNextRole():
	global roleCount
	try:
		roleCount+=1
	except NameError:
		roleCount=QtCore.Qt.UserRole
	return roleCount

RoleRepo=getNextRole()
RoleName=getNextRole()
RoleVersion=getNextRole()

class Package(Ui_PackageWidget):
	def __init__(self, line):
		Ui_PackageWidget.__init__(self)
		line=line.split('||')
		self.repo=line[1]
		self.name=line[2]
		self.version=line[3]
		self.installed=line[4]
		self.description=line[5]
		self.safe=line[6]
		self.setText(self.createText())
	def setupUi(self, PackageWidget):
		Ui_PackageWidget.setupUi(self, PackageWidget)
	def createText(self):
		return self.repo+"/"+self.name+" - "+self.version+" ("+self.installed+") "+self.description+self.safe

class TupacTalker():
	def __init__(self):
		print "Starting tupac"
		self.tupacInstance = pexpect.spawn('tupac --console --lang machine')
		self.tupacInstance.setecho(False)
		try:
			self.tupacInstance.expect_exact('$ ')
		except EOF:
			print "tupac finished unespectedly:"
			print self.tupacInstance.before
			sys.exit()
		except TIMEOUT:
			print "tupac is taking too long to respond."
			self.tupacInstance.terminate()
			sys.exit()
	def send(self,msg):
		self.tupacInstance.write(msg+"\n")
	def receive(self):
		self.tupacInstance.expect_exact('$ ')
		return self.tupacInstance.before
	def ask(self,msg):
		self.send(msg)
		return self.receive()
	def end(self):
		print "Exiting tupac"
		#self.tupacInstance.terminate()
		self.send("exit")
	def update(self):
		self.ask("u")
	def getPackageList(self,query):
		resp=[]
		rawData=self.ask(query)
		lines=rawData.splitlines()
		for line in lines:
			resp.append(Package(line))
		return resp



class TupacWindow(Ui_MainWindow):
	def __init__(self,tupacTalker):
		Ui_MainWindow.__init__(self)
		self.tupacTalker=tupacTalker
	def setupUi(self, MainWindow):
		global version
		Ui_MainWindow.setupUi(self, MainWindow)
		MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "qupac "+version, None, QtGui.QApplication.UnicodeUTF8))
		self.connect(self.searchField,QtCore.SIGNAL("cursorPositionChanged(int,int)"),self.search)
		self.connect(self.searchField,QtCore.SIGNAL("returnPressed()"),self.searchAur)
		self.connect(self.searchButton,QtCore.SIGNAL("pressed()"),self.searchAur)
		self.connect(self.installButton,QtCore.SIGNAL("pressed()"),self.doInstall)
		self.oldSearchString=""
	def search(self,  old,  new):
		words=self.searchField.text()
		if words==self.oldSearchString:
			return
		else:
			self.oldSearchString=words
		
		if len(words)>2:
			self.searchResults.clear()
			packages=self.tupacTalker.getPackageList("s "+words)
			for package in packages:
				self.searchResults.addItem(package)
		else:
			self.searchResults.clear()
	def searchAur(self):
		words=self.searchField.text()
		self.oldSearchString=words
		
		if len(words)>1:
			self.searchResults.clear()
			packages=self.tupacTalker.getPackageList("sa "+words)
			for package in packages:
				self.searchResults.addItem(package)
		else:
			self.searchResults.clear()
	def doInstall(self):
		pacman_str=""
		aur_str=""
		for p_index in range(0,self.installQueue.count(),1):
			package=str(self.installQueue.item(p_index).text())
			part=package.split(" ")[0].split("/")
			repo=part[0]
			name=part[1]
			if repo=="aur":
				aur_str+=repo+"/"+name+" "
			elif repo!="_NO_REPO_":
				pacman_str+=repo+"/"+name+" "
		if pacman_str<>"":
			#os.system(str(self.terminalEmulator.text().replace("%c","pacman -S "+pacman_str)))
			os.system("konsole -e sudo pacman -S "+pacman_str)
		if aur_str<>"":
			#os.system(str(self.terminalEmulator.text().replace("%c","yaourt -S "+aur_str)))
			os.system("konsole -e yaourt -S "+aur_str)
		self.tupacTalker.update()



# Forking is used to:
# - Kill tupac if a
r, w = os.pipe()
pid=os.fork()
if pid:
	os.close(w)
	r = os.fdopen(r)
	tupacPid=int(r.read())
	#print "Tupac running with pid "+str(tupacPid)
	os.waitpid(pid, 0)
	try:
		os.kill(tupacPid,15)
	except OSError, err:
		sys.exit(0)
	print "Terminating tupac"
else:
	os.close(r)
	w = os.fdopen(w, 'w')
	tupacTalker=TupacTalker()
	w.write(str(tupacTalker.tupacInstance.pid))
	w.close()
	
	app = QtGui.QApplication(sys.argv)
	window = QtGui.QMainWindow()
	ui = TupacWindow(tupacTalker)
	ui.setupUi(window)
	
	window.show()
	app.exec_()
	
	tupacTalker.end()
	
