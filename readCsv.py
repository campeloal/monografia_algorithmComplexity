from numpy import genfromtxt

class Csv:

    fileName = "" 
    data = []
    vertMetric = []
    fragMetric = []
    averageVert = 0
    averageFrag = 0

    def __init__(self,name, delimiter):
        self.fileName = name
        self.readCsv(self.fileName, delimiter)

    def readCsv(self,name, delimiter):
        self.data = genfromtxt(name, delimiter=delimiter)
        self.getColumns()

    def getColumns(self):
        del self.vertMetric[0:len(self.vertMetric)]
        del self.vertMetric[0:len(self.vertMetric)]
      
        for row in self.data:
            self.vertMetric.append(row[1])
            self.fragMetric.append(row[2])

    def sumMetrics(self, metricArray):
        sumMetric = 0
        for metric in metricArray:
            sumMetric += metric
        return sumMetric
            
    def getAverageMetric(self,metricArray):        
        return self.sumMetrics(metricArray)/len(metricArray)

    def getVertMetric(self):
        self.averageVert = self.getAverageMetric(self.vertMetric)
        return self.averageVert

    def getFragMetric(self):
        self.averageFrag = self.getAverageMetric(self.fragMetric)
        return self.averageFrag
