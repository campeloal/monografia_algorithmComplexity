import matplotlib.pyplot as plt

class Plot:

    chartTitle = '' 
    vertTitle = ''
    fragTitle = ''

    def plotChart(self, xVertAxis, yVertAxis, xFragAxis, yFragAxis):
        plt.subplot(211)
        plt.title(self.chartTitle + ' Shader')
        plt.xlabel('Number of Polygons')
        plt.ylabel(self.vertTitle)
        plt.plot(xVertAxis, yVertAxis, 'b-')
        plt.plot(xVertAxis, yVertAxis, 'ro')

        plt.subplot(212)
        plt.xlabel('Number of Polygons')
        plt.ylabel(self.fragTitle)
        plt.plot(xFragAxis, yFragAxis, 'g-')
        plt.plot(xFragAxis, yFragAxis, 'ro')
        plt.show()

    def plotLeastSquareChart(self, xVertAxis, yVertAxis, xFragAxis, yFragAxis, yVertOrig, yFragOrig, equationName):
        plt.subplot(211)
        plt.title(self.chartTitle + ' Shader' + ' - ' + equationName)
        plt.xlabel('Number of Polygons')
        plt.ylabel(self.vertTitle)
        plt.plot(xVertAxis, yVertAxis, 'y-',xVertAxis, yVertOrig, 'b-')
        plt.plot(xVertAxis, yVertAxis, 'bo',xVertAxis, yVertOrig, 'ro')

        plt.subplot(212)
        plt.xlabel('Number of Polygons')
        plt.ylabel(self.fragTitle)
        plt.plot(xFragAxis, yFragAxis, 'r-',xFragAxis,yFragOrig,'g-' )
        plt.plot(xFragAxis, yFragAxis, 'bo',xFragAxis,yFragOrig,'ro')
        plt.show()

    def setVertTitle(self,vertTitle):
        self.vertTitle = vertTitle

    def setFragTitle(self,fragTitle):
        self.fragTitle = fragTitle

    def setChartTile(self,chartTitle):
        self.chartTitle = chartTitle
