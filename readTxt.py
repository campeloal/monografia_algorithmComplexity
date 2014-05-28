class Txt:
    
    renderTime = []
    numberPolygons = []

    def readTxt(self,name):
        file = open(name, 'r')
        line = file.readline()
        self.renderTime = line.split()
        line = file.readline()
        self.numberPolygons = line.split()

    def getRenderTime(self):
        i = 0
        for time in self.renderTime:
            self.renderTime[i] = float(time)
            i = i + 1
        return self.renderTime

    def getNumberPolygons(self):
        i = 0
        for polygon in self.numberPolygons:
            self.numberPolygons[i] = float(polygon)
            i = i + 1
        return self.numberPolygons
