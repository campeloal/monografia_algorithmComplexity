import numpy as np

class LeastSquares:
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
            #multiply by 0.1 because the np.matrix can't handle big numbers
            if withLog:
                self.mMatrixStr += str(1 * 0.1) + " " + str(np.log(polygon * 0.1)) + ";"
            else:
                self.mMatrixStr +=  str(1 * 0.1) + " " + str(polygon * 0.1) + ";"
        self.mMatrixStr = self.mMatrixStr[:-1]
        self.mMatrix = np.matrix(self.mMatrixStr)

    def createSecDegMMatrix(self):
        self.mMatrixStr = ''
        for polygon in self.numberPolygons:
            #multiply by 0.1 because the np.matrix can't handle big numbers
            self.mMatrixStr +=  str(1 * 0.1) + " " + str(polygon * 0.1) + " " + str(polygon * polygon * 0.1) + ";"
        self.mMatrixStr = self.mMatrixStr[:-1]
        self.mMatrix = np.matrix(self.mMatrixStr)

    def createThirdDegMMatrix(self):
        self.mMatrixStr = ''
        for polygon in self.numberPolygons:
            #multiply by 0.1 because the np.matrix can't handle big numbers
            self.mMatrixStr +=  str(1 * 0.1) + " " + str(polygon * 0.1) + " " + str(polygon * polygon * polygon * 0.1) + ";"
        self.mMatrixStr = self.mMatrixStr[:-1]
        self.mMatrix = np.matrix(self.mMatrixStr)
        
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
        self.mtmMatrix = (self.mtMatrix * self.mMatrix) * 100 #multiply back
        self.mtmInvMatrix = self.mtmMatrix.getI()
        self.mtMatrix = self.mtMatrix * 10 #multiply back
        self.mtyMatrix = self.mtMatrix * self.yMatrix
        self.solution = self.mtmInvMatrix * self.mtyMatrix

    def secondDegPolyLeastSquares(self,numberPolygons,yValues):
        self.numberPolygons = numberPolygons
        self.yValues = yValues
        self.createSecDegMMatrix()
        self.createYMatrix(False)
        self.mtMatrix = self.mMatrix.getT()
        self.mtmMatrix = (self.mtMatrix * self.mMatrix) * 100 #multiply back
        self.mtmInvMatrix = self.mtmMatrix.getI()
        self.mtMatrix = self.mtMatrix * 10 #multiply back
        self.mtyMatrix = self.mtMatrix * self.yMatrix
        self.solution = self.mtmInvMatrix * self.mtyMatrix

    def thirdDegPolyLeastSquares(self,numberPolygons,yValues):
        self.numberPolygons = numberPolygons
        self.yValues = yValues
        self.createThirdDegMMatrix()
        self.createYMatrix(False)
        self.mtMatrix = self.mMatrix.getT()
        self.mtmMatrix = (self.mtMatrix * self.mMatrix) * 100 #multiply back
        self.mtmInvMatrix = self.mtmMatrix.getI()
        self.mtMatrix = self.mtMatrix * 10 #multiply back
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
        a3 = self.solution[2]
        a3 = np.array(a3)[0][0] #convert back to number
        yVal = []
        for polygon in self.numberPolygons:
            yVal.append(a0 + (a1*polygon) + (a2*polygon*polygon) + (a3*polygon*polygon*polygon))
        if eqType == "Vertex":
            self.thirddegVertEq = "$y = " + str(a0) + " + " + str(a1) + "t " + str(a2) + "t^2 " + str(a3) + "t^3$" 
        else:
            self.thirddegFragEq = "$y = " + str(a0) + " + " + str(a1) + "t " + str(a2) + "t^2 " + str(a3) + "t^3$"
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
