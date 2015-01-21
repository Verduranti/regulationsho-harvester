#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui

from mainwindow import *

import urllib
import urllib2
import csv
import datetime

#print "Welcome to the FINRA Regulation SHO Data Harvester"

#TODO LIST
#Calendar interface for the dates
#Better error handling
#Error running straight from google code

#Error handling for http
#Options for updated vs not

class Harvester(QtGui.QWidget, Ui_MainWindow):
	baseurl = "http://regsho.finra.org/"

	def __init__(self, ui):
		super(Harvester, self).__init__()
		self.ui = ui
		self.setConnect()

	def setConnect(self):
		self.ui.cbAllMkts.stateChanged.connect(self.allMkts)
		self.ui.harvestButton.clicked[bool].connect(self.harvest)
		
	def allMkts(self, state):
		if state == QtCore.Qt.Checked:
			self.ui.cbNasdaq.setChecked(True)
			self.ui.cbNYSE.setChecked(True)
			self.ui.cbADF.setChecked(True)
			self.ui.cbORF.setChecked(True)
			
	def harvest(self, pressed):
		includeNasdaq = False
		includeNYSE = False
		includeADF = False
		includeORF = False
		includeAll = False
		if self.ui.cbAllMkts.isChecked() or self.ui.cbEverything.isChecked():
			includeAll = True
		if includeAll or self.ui.cbNasdaq.isChecked():
			includeNasdaq = True
		if includeAll or self.ui.cbNYSE.isChecked():
			includeNYSE = True
		if includeAll or self.ui.cbADF.isChecked():
			includeADF = True
		if includeAll or self.ui.cbORF.isChecked():
			includeORF = True
			
		
		if self.ui.cbEverything.isChecked():
			self.startdatestring = "20110601"
			self.enddatestring = datetime.date.today().strftime("%Y%m%d")
		else:	
			self.startdatestring = self.ui.startDate.date().toString("yyyyMMdd")
			self.enddatestring = self.ui.endDate.date().toString("yyyyMMdd")
				
		self.startdate = datetime.date(int(self.startdatestring[0:4]), int(self.startdatestring[4:6]), int(self.startdatestring[6:8]))
		self.enddate = datetime.date(int(self.enddatestring[0:4]), int(self.enddatestring[4:6]), int(self.enddatestring[6:8]))
		
		#Swap dates if startdate is after enddate
		if self.startdate > self.enddate:
			self.temp = self.startdate
			self.startdate = self.enddate
			self.enddate = self.temp
			
		self.maxdate = datetime.date.today()

		if self.startdate > self.maxdate:
			self.startdate = self.maxdate
			
		if self.enddate > self.maxdate:
			self.enddate = self.maxdate
			
		self.dateCounter = self.startdate
		
		while self.dateCounter <= self.enddate:
			if self.dateCounter.weekday() == 5 or self.dateCounter.weekday() == 6:
				self.dateCounter = self.dateCounter + datetime.timedelta(days=1)
				continue
				
			if includeNasdaq:
				data = None
				if self.ui.cbUseUpdated.isChecked():
					self.fullurl = self.baseurl + "FNSQshvol" + self.dateCounter.strftime("%Y%m%d") + "X.txt"
					data = self.openPage(self.fullurl)
				if data == None:
					self.fullurl = self.baseurl + "FNSQshvol" + self.dateCounter.strftime("%Y%m%d") + ".txt"
					data = self.openPage(self.fullurl)
				if data != None:
					self.convertToCSV(data)
			if includeNYSE:
				data = None
				if self.ui.cbUseUpdated.isChecked():
					self.fullurl = self.baseurl + "FNYXshvol" + self.dateCounter.strftime("%Y%m%d") + "X.txt"
					data = self.openPage(self.fullurl)
				if data == None:
					self.fullurl = self.baseurl + "FNYXshvol" + self.dateCounter.strftime("%Y%m%d") + ".txt"
					data = self.openPage(self.fullurl)
				if data != None:
					self.convertToCSV(data)
			if includeADF:
				data = None
				if self.ui.cbUseUpdated.isChecked():
					self.fullurl = self.baseurl + "FNRAshvol" + self.dateCounter.strftime("%Y%m%d") + "X.txt"
					data = self.openPage(self.fullurl)
				if data == None:
					self.fullurl = self.baseurl + "FNRAshvol" + self.dateCounter.strftime("%Y%m%d") + ".txt"
					data = self.openPage(self.fullurl)
				if data != None:
					self.convertToCSV(data)
			if includeORF:
				data = None
				if self.ui.cbUseUpdated.isChecked():
					self.fullurl = self.baseurl + "FORFshvol" + self.dateCounter.strftime("%Y%m%d") + "X.txt"
					data = self.openPage(self.fullurl)
				if data == None:
					self.fullurl = self.baseurl + "FORFshvol" + self.dateCounter.strftime("%Y%m%d") + ".txt"
					data = self.openPage(self.fullurl)
				if data != None:
					self.convertToCSV(data)
				
			self.dateCounter = self.dateCounter + datetime.timedelta(days=1)
			
	def openPage(self, url):
		#make the request using the request object as an argument, store response in a variable
		try:
			response = urllib2.urlopen(url)
			#store request response in a string
			html_string = response.read()
			return html_string
  		except urllib2.HTTPError, exception_variable:
   			#prints the HTTP error code that was given
			outFile = open("ErrorDates.txt", 'ab')
			outFile.write(url + " " + str(exception_variable.code) + "\n")
			return None
		except urllib2.URLError, exception_variable:
   			#prints the reason for failure out to help debugging
			outFile = open("ErrorDates.txt", 'ab')
			outFile.write(url + " " + str(exception_variable.code) + "\n")
  			return None
	
	def convertToCSV(self, datastring):
		csv_string = datastring.replace('|', ',')
		dataList = csv_string.split("\n")
		#Clear header
		dataList.pop(0)

		if dataList:
			if dataList[0].count(",") == 0:
				return
		
		#Clear item count
		dataList.pop()
		dataList.pop()
		
		csvFilename = "Data.csv"
		outFile = open(csvFilename, 'ab')
		
		for item in dataList:
			outFile.write(item)


def main():
	#Set up GUI
	app = QtGui.QApplication(sys.argv)
	MainWindow = QtGui.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	MainWindow.show()
	hv = Harvester(ui)
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
	