import sys
import numpy as np

from .process import runProcessFull
from .runBAM import runAllSteps
from .scaler import scalorRunAll
from .scaler import saveReformatCSV
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
    saveReformatCSV(outLoc)

def scriptRunEverything():
    import sys
    keyList = ['-input', '-ref', '-output', '-refGenome']
    listIn = np.array(sys.argv)
    values1 = getValuesSYS(listIn, keyList)
    bamLoc, refLoc, outLoc, refGenome = values1[0], values1[1], values1[2], values1[3]
    runEverything(bamLoc, refLoc, outLoc, refGenome)


def printCheck(bamLoc, refLoc, outLoc, refGenome):
    print ("Basic Print Check")
    print ('bamLoc', bamLoc, 'refLoc', refLoc, 'outLoc', outLoc, 'refGenome', refGenome)

def scriptCheck():
    import sys
    print (sys.argv)


def respondCheck():
    print ('check success')






