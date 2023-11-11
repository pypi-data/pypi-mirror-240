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


def printCheck(bamLoc, refLoc, outLoc, refGenome):

    print ("Basic Print Check")
    print ('bamLoc', bamLoc, 'refLoc', refLoc, 'outLoc', outLoc, 'refGenome', refGenome)

def respondCheck():
    print ('check success')






