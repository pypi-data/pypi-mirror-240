import sys
import numpy as np

from .process import runProcessFull
from .runBAM import runAllSteps
from .scaler import scalorRunAll
from .scaler import saveReformatCSV
from .scaler import scalorRunBins
from .scaler import runNaiveCopy
from .RLCNA import easyRunRL



def getValuesSYS(listIn, keyList):

    valueList = []
    for key1 in keyList:
        arg1 = np.argwhere(listIn == key1)[0, 0]
        value1 = listIn[arg1+1]
        valueList.append(value1)
    return valueList


def runEverything(bamLoc, refLoc, outLoc, refGenome):

    runAllSteps(bamLoc, refLoc, outLoc, refGenome)
    runProcessFull(outLoc, refLoc, refGenome)
    scalorRunAll(outLoc)
    easyRunRL(outLoc)
    saveReformatCSV(outLoc, isNaive=False)

def scriptRunEverything():
    import sys
    listIn = np.array(sys.argv)
    if not '-step' in listIn:

        keyList = ['-input', '-ref', '-output', '-refGenome']
        
        values1 = getValuesSYS(listIn, keyList)
        bamLoc, refLoc, outLoc, refGenome = values1[0], values1[1], values1[2], values1[3]
        runEverything(bamLoc, refLoc, outLoc, refGenome)

    else:

        keyList = ['-input', '-ref', '-output', '-refGenome', '-step']
        values1 = getValuesSYS(listIn, keyList)
        bamLoc, refLoc, outLoc, refGenome, stepVal = values1[0], values1[1], values1[2], values1[3], values1[4]

        if stepVal == 'processing':
            runAllSteps(bamLoc, refLoc, outLoc, refGenome)
            runProcessFull(outLoc, refLoc, refGenome)
            scalorRunBins(outLoc)
        
        if stepVal == 'NaiveCopy':
            runNaiveCopy(outLoc)

        if stepVal == 'DeepCopy':
            easyRunRL(outLoc)
            saveReformatCSV(outLoc, isNaive=False)
        

        if stepVal == 'processBams':
            runAllSteps(bamLoc, refLoc, outLoc, refGenome)
        
        if stepVal == 'variableBins':
            runProcessFull(outLoc, refLoc, refGenome)
            scalorRunBins(outLoc)






def printCheck(bamLoc, refLoc, outLoc, refGenome):
    print ("Basic Print Check")
    print ('bamLoc', bamLoc, 'refLoc', refLoc, 'outLoc', outLoc, 'refGenome', refGenome)

def scriptCheck():
    import sys
    print (sys.argv)


def respondCheck():
    print ('check success')






