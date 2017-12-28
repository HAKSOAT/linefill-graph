import os.path
import pandas as pd
import matplotlib.pyplot as mpyplot

class File(object):
    
    def __init__(self):
        self.fileName = None
    
    def getName(self):
        self.fileName = input("\n\nType in the name of file \n *Case Sensitive: ")
    
    def checkExists(self):
        print("\n\nChecking if {} exists.".format(self.fileName))
        if os.path.isfile(self.fileName):
            print("\n\nFile exists....Progressing")
            return True
        else:
            print("\n\nFile does not exist")
            return False
    
    
class Data(object):
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.dataFrame = None
    
    def make(self):
        print("\n\nReading Excel file....")
        self.dataFrame = pd.read_excel(self.fileName)
    
    def printOut(self):
        print("\n\nPrinting read data....\n\n")
        print(self.dataFrame)
        
class ExcelToGraph(object):
    
    def __init__(self, dataFrame):
        self.primaryYColumnName = None
        self.secondaryYColumnName = None
        self.primaryXColumnName = None
        self.dataFrame = dataFrame
    
        
    def selectPrimaryYColumnName(self):
        self.primaryYColumnName = input("\n\nPlease enter the name of column for primary y axis from the excel file.\nCase Sensitive: ")
    
    def checkPrimaryYColumnName(self):
        print("\n\nChecking if {} exists.".format(self.primaryYColumnName))
        if self.primaryYColumnName in self.dataFrame:
            print("\n\nColumn exists....Progressing")
            return True
        else:
            print("\n\nColumn does not exist")
            return False
    
    def selectSecondaryYColumnName(self):
        self.secondaryYColumnName = input("\n\nPlease enter the name of column for secondary y axis from the excel file.\nCase Sensitive: ")
    
    def checkSecondaryYColumnName(self):
        print("\n\nChecking if {} exists.".format(self.secondaryYColumnName))
        if self.secondaryYColumnName in self.dataFrame:
            print("\n\nColumn exists....Progressing")
            return True
        else:
            print("\n\nColumn does not exist")
            return False
    
    def selectPrimaryXColumnName(self):
        self.primaryXColumnName = input("\n\nPlease enter the name of column for primary x axis from the excel file.\nCase Sensitive: ")
    
    def checkPrimaryXColumnName(self):
        print("\n\nChecking if {} exists.".format(self.primaryXColumnName))
        if self.primaryXColumnName in self.dataFrame:
            print("\n\nColumn exists....Progressing")
            return True
        else:
            print("\n\nColumn does not exist")
            return False
    
    
class Graph(object):
    
    def __init__(self, dataFrame, yPrimaryName, ySecondaryName, xPrimaryName):
        self.dataFrame = dataFrame
        self.primaryYAxis = self.dataFrame[yPrimaryName]
        self.secondaryYAxis = self.dataFrame[ySecondaryName]
        self.xAxis = self.dataFrame[xPrimaryName]
        self.xPrimaryName = xPrimaryName
        self.yPrimaryName = yPrimaryName
        self.ySecondaryName = ySecondaryName
        figure = mpyplot.figure()
        self.linegraphplot = figure.add_subplot(111)
        mpyplot.xticks(rotation = 60)
        mpyplot.tight_layout()
        mpyplot.tick_params(axis = 'both', which = 'major', labelsize = 12)
        self.fillgraphplot = self.linegraphplot.twinx()
        
    def makeLine(self):
        self.linegraphplot.plot(self.xAxis, self.primaryYAxis, '-r', label = self.yPrimaryName)
        self.linegraphplot.set_ylim(ymin = 1020)
    
    def makeFill(self):
        self.fillgraphplot.fill(self.xAxis, self.secondaryYAxis, 'b', label = self.ySecondaryName, alpha = 0.1)
        
    def makeFillIndexInvincible(self):
        unseenAxis = mpyplot.gca()
        unseenAxis.axes.get_yaxis().set_visible(False)
    
    def addLegends(self):
        self.fillgraphplot.legend(loc = 'lower right')
        self.linegraphplot.legend(loc = 'lower left')
        
    def addTitles(self):
        self.linegraphplot.set_xlabel(self.xPrimaryName)
        self.linegraphplot.set_ylabel(self.yPrimaryName)
        self.linegraphplot.set_title("Money Supply")
        
    def show(self):
        mpyplot.show()

file = File()
file.getName()
while file.checkExists() != True:
    file.getName()
    
    
data = Data(file.fileName)
data.make()

exceltograph = ExcelToGraph(data.dataFrame)
exceltograph.selectPrimaryYColumnName()
while exceltograph.checkPrimaryYColumnName() != True:
    exceltograph.selectPrimaryYColumnName()
    
exceltograph.selectSecondaryYColumnName()
while exceltograph.checkSecondaryYColumnName() != True:
    exceltograph.selectSecondaryYColumnName()
    
exceltograph.selectPrimaryXColumnName()
while exceltograph.checkPrimaryXColumnName() != True:
    exceltograph.selectPrimaryXColumnName()

graph = Graph(data.dataFrame, exceltograph.primaryYColumnName, 
              exceltograph.secondaryYColumnName, exceltograph.primaryXColumnName)

graph.makeLine()
graph.makeFill()
graph.makeFillIndexInvincible()
graph.addLegends()
graph.addTitles()
graph.show()