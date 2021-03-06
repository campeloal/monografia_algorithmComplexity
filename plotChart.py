import matplotlib.pyplot as plt
#font = {'family' : 'normal',
#        'weight' : 'bold',
#        'size'   : 29}
#plt.rc('font', **font)

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

    def plotChartRT(self, numberPolygons, renderTime):
        plt.title(self.chartTitle + ' Shader')
        plt.xlabel('Number of Polygons') #, fontsize = 32)
        plt.ylabel(self.vertTitle) #, fontsize = 35)
        plt.plot(numberPolygons, renderTime, 'b-')
        plt.plot(numberPolygons, renderTime, 'ro')
        plt.show()

    def plotLeastSquareChart(self, xVertAxis, yVertAxis, xFragAxis, yFragAxis, yVertOrig, yFragOrig, equationName,eqVertFormula, eqFragFormula):
        plt.subplot(211)
        plt.title(self.chartTitle + ' Shader' + ' - ' + equationName)
        plt.xlabel('Number of Polygons')
        plt.ylabel(self.vertTitle)
        plt.plot(xVertAxis, yVertAxis, 'y-',label=eqVertFormula)
        plt.plot(xVertAxis, yVertAxis, 'bo') #add a blue dot
        plt.plot(xVertAxis, yVertOrig, 'b-', label = "original")
        plt.plot(xVertAxis, yVertOrig, 'ro') #add a red dot
        plt.legend(loc="upper left", bbox_to_anchor=[0.5, 0.5],
           ncol=1, shadow=True, title="Legend")

        plt.subplot(212)
        plt.xlabel('Number of Polygons')
        plt.ylabel(self.fragTitle)
        plt.plot(xFragAxis, yFragAxis, 'r-', label = eqFragFormula)
        plt.plot(xFragAxis, yFragAxis, 'bo') #add a blue dot
        plt.plot(xFragAxis,yFragOrig,'g-', label = "original")
        plt.plot(xFragAxis,yFragOrig,'ro') #add a red dot
        plt.legend(loc="upper left", bbox_to_anchor=[0.5, 0.5],
           ncol=1, shadow=True, title="Legend")
        plt.show()

    def plotLeastSquareChartRT(self, numberPolygons,lsRenderTime, renderTime,equationName,eqVertFormula):
        plt.title(self.chartTitle + ' Shader' + ' - ' + equationName)
        plt.xlabel('Number of Polygons')
        plt.ylabel(self.vertTitle)
        plt.plot(numberPolygons, lsRenderTime, 'y-',label=eqVertFormula)#, linewidth=2)
        plt.plot(numberPolygons, lsRenderTime, 'bo') #add a blue dot
        plt.plot(numberPolygons, renderTime, 'b-', label = "original") #, linewidth=2)
        plt.plot(numberPolygons, renderTime, 'ro') #add a red dot
        plt.legend(loc="upper left", bbox_to_anchor=[0.4, 0.4],
           ncol=1, shadow=True, title="Legend") #, prop={'size':30})
        
        plt.show()


    

    def setVertTitle(self,vertTitle):
        self.vertTitle = vertTitle

    def setFragTitle(self,fragTitle):
        self.fragTitle = fragTitle

    def setChartTile(self,chartTitle):
        self.chartTitle = chartTitle
