import Graphs as g


def createPPCGraphs(title, graphType, numCalls):
    ppc = g.PPC(title)
    fig = g.plt.figure(numCalls, figsize = (10,6))
    if graphType == 0:
        ppc.createDefaultGraph("linear")
    elif graphType == 1:
        ppc.createDefaultGraph("increasing")
    g.plt.show()

sd = g.SD()

def createSDGraphs():
    fig = g.plt.figure(1, figsize = (10,6))
    sd.formGraph()

def updateSDGraphs(shiftType, shiftAmount):
    if shiftType == "Demand":
        sd.clearDemandCurves()
        sd.demandShift(shiftAmount)
    elif shiftType == "Supply":
        sd.clearSupplyCurves()
        sd.supplyShift(shiftAmount)
    g.plt.legend(bbox_to_anchor=(1,1.1), loc='upper left')
    g.plt.show()

def close():
    g.plt.close("all")

csd = g.ComplexSD()
def createComplexSDGraphs():
    fig = g.plt.figure(1, figsize=(10,6))
    csd.complexEquilibriumGraph()
    csd.formGraph()

def updateComplexSDGraphs(shiftType, shiftAmount, term):
    if shiftType == "Demand":
        csd.clearDemandCurves()
        if term == "short":
            csd.demandShiftShortRun(shiftAmount)
        else:
            csd.longRunDemandShift(shiftAmount)
    else:
        csd.clearSupplyCurves()
        if term == "short":
            csd.supplyShiftShortRun(shiftAmount)
        else:
            csd.longRunSupplyShift(shiftAmount)

    g.plt.legend(bbox_to_anchor=(1,1.1), loc='upper left')
    g.plt.show()
