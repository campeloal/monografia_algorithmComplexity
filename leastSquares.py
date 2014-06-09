import numpy as np

class LeastSquares:
    np.set_printoptions(precision=14)
    mMatrixStr = ''
    yMatrixStr = ''
    mMatrix = []
    mtMatrix = []
    mtmMatrix = []
    mtmInvMatrix = []
    mtyMatrix = []
    yMatrix = []
    solution = []
    numberPolygons = []
    yValues = []
    linearVertEq = ""
    secdegVertEq = ""
    thirddegVertEq = ""
    expVertEq = ""
    linearFragEq = ""
    secdegFragEq = ""
    thirddegFragEq = ""
    expFragEq = ""
    
    def createMMatrix(self, withLog):
        self.mMatrixStr = ''
        for polygon in self.numberPolygons:
            if withLog:
                self.mMatrixStr += str(np.float64(1)) + " " + str(np.log(np.float64(polygon))) + ";"
            else:
                self.mMatrixStr +=  str(np.float64(1)) + " " + str(np.float64(polygon)) + ";"

        self.mMatrixStr = self.mMatrixStr[:-1]
        self.mMatrix = np.matrix(self.mMatrixStr,dtype=np.float64)

    def createSecDegMMatrix(self):
        self.mMatrixStr = ''
        for polygon in self.numberPolygons:
            self.mMatrixStr +=  str(np.float64(1)) + " " + str(np.float64(polygon)) + " " + str(np.power(np.float64(polygon),2)) + ";"
        self.mMatrixStr = self.mMatrixStr[:-1]
        self.mMatrix = np.matrix(self.mMatrixStr,dtype=np.float64)

    def createPolygonMatrixString(self, polygon, funcdegree):
        matrixString = '' 
        if(funcdegree == 'third'):
            polArray = np.array([np.power(polygon,3,dtype=np.float64)])
            matrixString = str(polArray)
            matrixString = matrixString[1:]
            matrixString = matrixString[:-1]

        return matrixString
        

    def createThirdDegMMatrix(self):
        self.mMatrixStr = ''
        
        for polygon in self.numberPolygons:
            self.mMatrixStr +=  str(1) + " " + str(polygon) + " " + str(np.power(np.float64(polygon),2))+ " " + self.createPolygonMatrixString(polygon,'third') + ";"
        
        self.mMatrixStr = self.mMatrixStr[:-1]
        self.mMatrix = np.matrix(self.mMatrixStr,dtype=np.float64)
        
    def createYMatrix(self, withLog):
        self.yMatrixStr = ''
        for value in self.yValues:
            if withLog:
                self.yMatrixStr += str(np.log(value)) + ";"
            else:
                self.yMatrixStr += str(value) + ";"
        self.yMatrixStr = self.yMatrixStr[:-1]
        self.yMatrix = np.matrix(self.yMatrixStr)  

    def linearLeastSquares(self,withLogM, withLogY,numberPolygons,yValues):
        self.numberPolygons = numberPolygons
        self.yValues = yValues
        self.createMMatrix(withLogM)
        self.createYMatrix(withLogY)
        self.mtMatrix = self.mMatrix.getT()
        self.mtmMatrix = (self.mtMatrix * self.mMatrix)
        self.mtmInvMatrix = self.mtmMatrix.getI()
        self.mtMatrix = self.mtMatrix
        self.mtyMatrix = self.mtMatrix * self.yMatrix
        self.solution = self.mtmInvMatrix * self.mtyMatrix

    def secondDegPolyLeastSquares(self,numberPolygons,yValues):
        self.numberPolygons = numberPolygons
        self.yValues = yValues
        self.createSecDegMMatrix()
        self.createYMatrix(False)
        self.mtMatrix = self.mMatrix.getT()
        self.mtmMatrix = (self.mtMatrix * self.mMatrix) 
        self.mtmInvMatrix = self.mtmMatrix.getI()
        self.mtMatrix = self.mtMatrix 
        self.mtyMatrix = self.mtMatrix * self.yMatrix
        self.solution = self.mtmInvMatrix * self.mtyMatrix

    def thirdDegPolyLeastSquares(self,numberPolygons,yValues):
        self.numberPolygons = numberPolygons
        self.yValues = yValues
        self.createThirdDegMMatrix()
        self.createYMatrix(False)
        self.mtMatrix = self.mMatrix.getT()
        self.mtmMatrix = (self.mtMatrix * self.mMatrix)
        self.mtmInvMatrix = self.mtmMatrix.getI()
        self.mtMatrix = self.mtMatrix
        self.mtyMatrix = self.mtMatrix * self.yMatrix
        self.solution = self.mtmInvMatrix * self.mtyMatrix

    def createExpEquation(self, eqType):
        c = np.exp(self.solution[0]) 
        c = np.array(c)[0][0] #convert back to number
        nK = self.solution[1]
        nK = np.array(nK)[0][0] #convert back to number
        yVal = []
        for polygon in self.numberPolygons:
            yVal.append(c * np.exp(nK*polygon))
        if eqType == "Vertex":
            self.expVertEq = "$y = " + str(c) + "e^{" + str(nK) + "t}$"
        else:
            self.expFragEq = "$y = " + str(c) + "e^{" + str(nK) + "t}$"
        return yVal

    def createLinearEquation(self,eqType):
        a = self.solution[0]
        a = np.array(a)[0][0] #convert back to number
        b = self.solution[1]
        b = np.array(b)[0][0] #convert back to number
        yVal = []
        for polygon in self.numberPolygons:
            yVal.append(a + (b*polygon))
        if eqType == "Vertex":
            self.linearVertEq = "$y = " + str(a) + " + " + str(b) + "t$"
        else:
            self.linearFragEq = "$y = " + str(a) + " + " + str(b) + "t$"   
        return yVal

    def createSecDegreeEquation(self, eqType):
        a0 = self.solution[0]
        a0 = np.array(a0)[0][0] #convert back to number
        a1 = self.solution[1]
        a1 = np.array(a1)[0][0] #convert back to number
        a2 = self.solution[2]
        a2 = np.array(a2)[0][0] #convert back to number
        yVal = []
        for polygon in self.numberPolygons:
            yVal.append(a0 + (a1*polygon) + (a2*polygon*polygon))
        if eqType == "Vertex":
            self.secdegVertEq = "$y = " + str(a0) + " + " + str(a1) + "t " + str(a2) + "t^2$"
        else:
            self.secdegFragEq = "$y = " + str(a0) + " + " + str(a1) + "t " + str(a2) + "t^2$"
        return yVal

    def createThirdDegreeEquation(self, eqType):
        a0 = self.solution[0]
        a0 = np.array(a0)[0][0] #convert back to number
        a1 = self.solution[1]
        a1 = np.array(a1)[0][0] #convert back to number
        a2 = self.solution[2]
        a2 = np.array(a2)[0][0] #convert back to number
        a3 = self.solution[3]
        a3 = np.array(a3)[0][0] #convert back to number
        
        yVal = []

        pol = 170000
        print "Value ", a0 + a1*pol + a2*pol*pol + a3*pol*pol*pol
    

        for polygon in self.numberPolygons:
            yVal.append(a0 + (a1*polygon) + (a2*polygon*polygon) + (a3*polygon*polygon*polygon))
        if eqType == "Vertex":
            self.thirddegVertEq = "$y = " + str(a0) + " + " + str(a1) + "t +" + str(a2) + "t^2 + " + str(a3) + "t^3$" 
        else:
            self.thirddegFragEq = "$y = " + str(a0) + " + " + str(a1) + "t +" + str(a2) + "t^2 +" + str(a3) + "t^3$"

        return yVal

    def calculateError(self,yToCompare, yAproximation):
        index = 0
        error = 0
        for value in yToCompare:
            error = error + np.power((value - yAproximation[index]), 2)
            index+=1
        return np.sqrt(error)

    def smallestError(self,errorHash):
        errorName = ""
        smallestError = 99999999999999999999
        for eqName in errorHash:
            if (errorHash[eqName] < smallestError):
                smallestError = errorHash[eqName]
                errorName = eqName
        errorNameVal = { errorName : smallestError}
        return errorNameVal

    def getLinearEqFormula(self, eqType):
        if eqType == "Vertex":
            return self.linearVertEq
        return self.linearFragEq

    def getSecDegEqFormula(self, eqType):
        if eqType == "Vertex":
            return self.secdegVertEq
        return self.secdegFragEq

    def getThirdDegEqFormula(self, eqType):
        if eqType == "Vertex":
            return self.thirddegVertEq
        return self.thirddegFragEq

    def getExpEqFormula(self, eqType):
        if eqType == "Vertex":
            return self.expVertEq
        return self.expFragEq
