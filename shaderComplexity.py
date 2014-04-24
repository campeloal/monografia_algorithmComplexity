from readCsv import Csv
from plotChart import Plot
from leastSquares import LeastSquares
import sys

nPolygons = [1000,10000,20000,30000,40000,50000,60000]
vertMetrics = []
fragMetrics = []

if len(sys.argv) > 1:
    name = sys.argv[1]

    
    csv1000 = Csv('csv/' + name + '/' + name + '_1000.csv',',')
    vertMetrics.append(csv1000.getVertMetric())
    fragMetrics.append(csv1000.getFragMetric())

    csv10000 = Csv('csv/' + name + '/' + name + '_10000.csv',',')
    vertMetrics.append(csv10000.getVertMetric())
    fragMetrics.append(csv10000.getFragMetric())

    csv20000 = Csv('csv/' + name + '/' + name + '_20000.csv',',')
    vertMetrics.append(csv20000.getVertMetric())
    fragMetrics.append(csv20000.getFragMetric())

    csv30000 = Csv('csv/' + name + '/' + name + '_30000.csv',',')
    vertMetrics.append(csv30000.getVertMetric())
    fragMetrics.append(csv30000.getFragMetric())

    csv40000 = Csv('csv/' + name + '/' + name + '_40000.csv',',')
    vertMetrics.append(csv40000.getVertMetric())
    fragMetrics.append(csv40000.getFragMetric())

    csv50000 = Csv('csv/' + name + '/' + name + '_50000.csv',',')
    vertMetrics.append(csv50000.getVertMetric())
    fragMetrics.append(csv50000.getFragMetric())

    csv60000 = Csv('csv/' + name + '/' + name + '_60000.csv',',')
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
    lsFrag = lsq.createLinearEquation()
    lsq.linearLeastSquares(False,False,nPolygons,vertMetrics)
    lsVert = lsq.createLinearEquation()
    plot.plotLeastSquareChart(nPolygons,lsVert,nPolygons,lsFrag,vertMetrics,fragMetrics, 'Least Squares: Linear')

    #PLOT 3 - EXPONENTIAL
    lsq.linearLeastSquares(False,True,nPolygons,fragMetrics)
    lsFrag = lsq.createExpEquation()
    lsq.linearLeastSquares(False,True,nPolygons,vertMetrics)
    lsVert = lsq.createExpEquation()
    plot.plotLeastSquareChart(nPolygons,lsVert,nPolygons,lsFrag,vertMetrics,fragMetrics, 'Least Squares: Exponential')


    #PLOT4 - SECOND DEGREE
    lsq.secondDegPolyLeastSquares(nPolygons,fragMetrics)
    lsFrag = lsq.createSecDegreeEquation()
    lsq.secondDegPolyLeastSquares(nPolygons,vertMetrics)
    lsVert = lsq.createSecDegreeEquation()
    plot.plotLeastSquareChart(nPolygons,lsVert,nPolygons,lsFrag,vertMetrics,fragMetrics, 'Least Squares: Second Degree')

    #PLOT4 - THIRD DEGREE
    lsq.thirdDegPolyLeastSquares(nPolygons,fragMetrics)
    lsFrag = lsq.createThirdDegreeEquation()
    lsq.thirdDegPolyLeastSquares(nPolygons,vertMetrics)
    lsVert = lsq.createThirdDegreeEquation()
    plot.plotLeastSquareChart(nPolygons,lsVert,nPolygons,lsFrag,vertMetrics,fragMetrics, 'Least Squares: Third Degree')
    
else:
    print 'You should enter the shader name'

