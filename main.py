from readCsv import Csv
from plotChart import Plot
from leastSquares import LeastSquares
import sys

nPolygons = [500,1250,5000,8580,10000,15000,20000,30000,40000,50000]
vertMetrics = []
fragMetrics = []

if len(sys.argv) > 1:
    name = sys.argv[1]

    
    csv500 = Csv('csv/' + name + '/' + name + ' 500.csv',',')
    vertMetrics.append(csv500.getVertMetric())
    fragMetrics.append(csv500.getFragMetric())

    csv1250 = Csv('csv/' + name + '/' + name + ' 1250.csv',',')
    vertMetrics.append(csv1250.getVertMetric())
    fragMetrics.append(csv1250.getFragMetric())

    csv5000 = Csv('csv/' + name + '/' + name + ' 5000.csv',',')
    vertMetrics.append(csv5000.getVertMetric())
    fragMetrics.append(csv5000.getFragMetric())

    csv8580 = Csv('csv/' + name + '/' + name + ' 8580.csv',',')
    vertMetrics.append(csv8580.getVertMetric())
    fragMetrics.append(csv8580.getFragMetric())

    csv10000 = Csv('csv/' + name + '/' + name + ' 10000.csv',',')
    vertMetrics.append(csv10000.getVertMetric())
    fragMetrics.append(csv10000.getFragMetric())

    csv15000 = Csv('csv/' + name + '/' + name + ' 15000.csv',',')
    vertMetrics.append(csv15000.getVertMetric())
    fragMetrics.append(csv15000.getFragMetric())

    csv20000 = Csv('csv/' + name + '/' + name + ' 20000.csv',',')
    vertMetrics.append(csv20000.getVertMetric())
    fragMetrics.append(csv20000.getFragMetric())

    csv30000 = Csv('csv/' + name + '/' + name + ' 30000.csv',',')
    vertMetrics.append(csv30000.getVertMetric())
    fragMetrics.append(csv30000.getFragMetric())

    csv40000 = Csv('csv/' + name + '/' + name + ' 40000.csv',',')
    vertMetrics.append(csv40000.getVertMetric())
    fragMetrics.append(csv40000.getFragMetric())

    csv50000 = Csv('csv/' + name + '/' + name + ' 50000.csv',',')
    vertMetrics.append(csv50000.getVertMetric())
    fragMetrics.append(csv50000.getFragMetric())


    plot = Plot()
    plot.setChartTile(name.capitalize())
    plot.setVertTitle('Vertex Instructions / s')
    plot.setFragTitle('Fragment Instructions / s')
    plot.plotChart(nPolygons,vertMetrics,nPolygons,fragMetrics)
    lsq = LeastSquares()
    lsq.linearLeastSquares(False,True,nPolygons,fragMetrics)
    lsFrag = lsq.createExpEquation()
    lsq.linearLeastSquares(False,False,nPolygons,vertMetrics)
    lsVert = lsq.createLinearEquation()
    plot.plotLeastSquareChart(nPolygons,lsVert,nPolygons,lsFrag,vertMetrics,fragMetrics)

else:
    print 'You should enter the shader name'

