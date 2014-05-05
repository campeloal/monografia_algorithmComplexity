from readCsv import Csv
from plotChart import Plot
from leastSquares import LeastSquares
import sys

nPolygons = [1000,5000,10000,15000,20000,25000,30000,35000,40000,45000,50000,55000,60000]
vertMetrics = []
fragMetrics = []

if len(sys.argv) > 1:
    name = sys.argv[1]
    
    csv1000 = Csv('csv/' + "/" + name + '/' + name + '_1000.csv',',')
    vertMetrics.append(csv1000.getVertMetric())
    fragMetrics.append(csv1000.getFragMetric())

    csv5000 = Csv('csv/' + "/" + name + '/' + name + '_5000.csv',',')
    vertMetrics.append(csv5000.getVertMetric())
    fragMetrics.append(csv5000.getFragMetric())

    csv10000 = Csv('csv/' + "/" + name + '/' + name + '_10000.csv',',')
    vertMetrics.append(csv10000.getVertMetric())
    fragMetrics.append(csv10000.getFragMetric())

    csv15000 = Csv('csv/' + "/" + name + '/' + name + '_15000.csv',',')
    vertMetrics.append(csv15000.getVertMetric())
    fragMetrics.append(csv15000.getFragMetric())

    csv20000 = Csv('csv/' + "/" + name + '/' + name + '_20000.csv',',')
    vertMetrics.append(csv20000.getVertMetric())
    fragMetrics.append(csv20000.getFragMetric())

    csv25000 = Csv('csv/' + "/" + name + '/' + name + '_25000.csv',',')
    vertMetrics.append(csv25000.getVertMetric())
    fragMetrics.append(csv25000.getFragMetric()) 

    csv30000 = Csv('csv/' + "/" + name + '/' + name + '_30000.csv',',')
    vertMetrics.append(csv30000.getVertMetric())
    fragMetrics.append(csv30000.getFragMetric())

    csv35000 = Csv('csv/' + "/" + name + '/' + name + '_35000.csv',',')
    vertMetrics.append(csv35000.getVertMetric())
    fragMetrics.append(csv35000.getFragMetric())

    csv40000 = Csv('csv/' + "/" + name + '/' + name + '_40000.csv',',')
    vertMetrics.append(csv40000.getVertMetric())
    fragMetrics.append(csv40000.getFragMetric())

    csv45000 = Csv('csv/' + "/" + name + '/' + name + '_45000.csv',',')
    vertMetrics.append(csv45000.getVertMetric())
    fragMetrics.append(csv45000.getFragMetric())

    csv50000 = Csv('csv/' + "/" + name + '/' + name + '_50000.csv',',')
    vertMetrics.append(csv50000.getVertMetric())
    fragMetrics.append(csv50000.getFragMetric())

    csv55000 = Csv('csv/' + "/" + name + '/' + name + '_55000.csv',',')
    vertMetrics.append(csv55000.getVertMetric())
    fragMetrics.append(csv55000.getFragMetric())

    csv60000 = Csv('csv/' + "/" + name + '/' + name + '_60000.csv',',')
    vertMetrics.append(csv60000.getVertMetric())
    fragMetrics.append(csv60000.getFragMetric())

    plot = Plot()
    plot.setChartTile(name.capitalize())
    plot.setVertTitle('Vertex Instructions / s')
    plot.setFragTitle('Fragment Instructions / s')

    #PLOT 1 - NORMAL
    plot.plotChart(nPolygons,vertMetrics,nPolygons,fragMetrics)
    lsq = LeastSquares()

    #PLOT 2 - LINEAR
    lsq.linearLeastSquares(False,False,nPolygons,fragMetrics)
    lsFrag = lsq.createLinearEquation("Vertex")
    lsq.linearLeastSquares(False,False,nPolygons,vertMetrics)
    lsVert = lsq.createLinearEquation("Frag")
    lsVertFormula = lsq.getLinearEqFormula("Vertex")
    lsFragFormula = lsq.getLinearEqFormula("Frag")
    plot.plotLeastSquareChart(nPolygons,lsVert,nPolygons,lsFrag,vertMetrics,fragMetrics, 'Least Squares: Linear',lsVertFormula,lsFragFormula)
    linearVertError = lsq.calculateError(vertMetrics,lsVert)
    linearFragError = lsq.calculateError(fragMetrics,lsFrag)

    #PLOT 3 - EXPONENTIAL
    lsq.linearLeastSquares(False,True,nPolygons,fragMetrics)
    lsFrag = lsq.createExpEquation("Vertex")
    lsq.linearLeastSquares(False,True,nPolygons,vertMetrics)
    lsVert = lsq.createExpEquation("Frag")
    lsVertFormula = lsq.getExpEqFormula("Vertex")
    lsFragFormula = lsq.getExpEqFormula("Frag")
    plot.plotLeastSquareChart(nPolygons,lsVert,nPolygons,lsFrag,vertMetrics,fragMetrics, 'Least Squares: Exponential',lsVertFormula,lsFragFormula)
    expVertError = lsq.calculateError(vertMetrics,lsVert)
    expFragError = lsq.calculateError(fragMetrics,lsFrag)
    

    #PLOT4 - SECOND DEGREE
    lsq.secondDegPolyLeastSquares(nPolygons,fragMetrics)
    lsFrag = lsq.createSecDegreeEquation("Vertex")
    lsq.secondDegPolyLeastSquares(nPolygons,vertMetrics)
    lsVert = lsq.createSecDegreeEquation("Frag")
    lsVertFormula = lsq.getSecDegEqFormula("Vertex")
    lsFragFormula = lsq.getSecDegEqFormula("Frag")
    plot.plotLeastSquareChart(nPolygons,lsVert,nPolygons,lsFrag,vertMetrics,fragMetrics, 'Least Squares: Second Degree',lsVertFormula,lsFragFormula)
    secdegVertError = lsq.calculateError(vertMetrics,lsVert)
    secdegFragError = lsq.calculateError(fragMetrics, lsFrag)

    #PLOT4 - THIRD DEGREE
    lsq.thirdDegPolyLeastSquares(nPolygons,fragMetrics)
    lsFrag = lsq.createThirdDegreeEquation("Vertex")
    lsq.thirdDegPolyLeastSquares(nPolygons,vertMetrics)
    lsVert = lsq.createThirdDegreeEquation("Frag")
    lsVertFormula = lsq.getThirdDegEqFormula("Vertex")
    lsFragFormula = lsq.getThirdDegEqFormula("Frag")
    plot.plotLeastSquareChart(nPolygons,lsVert,nPolygons,lsFrag,vertMetrics,fragMetrics, 'Least Squares: Third Degree', lsVertFormula,lsFragFormula)
    thirddegVertError = lsq.calculateError(vertMetrics,lsVert)
    thirddegFragError = lsq.calculateError(fragMetrics,lsFrag)

    #Calculate Smallest Error
    vertErrors = {"Linear":linearVertError,"Exponential":expVertError,"Second Degree":secdegVertError,"Third Degree":thirddegVertError}
    errorNameValue = lsq.smallestError(vertErrors)
    for name, value in errorNameValue.iteritems():
        print "SMALLEST VERTEX ERROR - ", name, ": ", value 

    fragErrors = {"Linear":linearFragError,"Exponential":expFragError,"Second Degree":secdegFragError,"Third Degree":thirddegFragError}
    errorNameValue = lsq.smallestError(fragErrors)
    for name, value in errorNameValue.iteritems():
        print "SMALLEST FRAGMENT ERROR - ", name, ": ", value 
    
else:
    print 'You should enter the shader name'

