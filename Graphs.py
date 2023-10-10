import matplotlib.pyplot as plt

class PPC:
    def __init__(self, title, x = [], y = [], color="green"):
        self.x = x
        self.y = y
        self.xlabel = "Guns"
        self.ylabel = "Butter"
        self.title = title
        self.color = color

    def createGraph(self):
        plt.plot(self.x, self.y, color="green")
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)

    def createDefaultGraph(self, type):
        if type == "linear":
            self.x = [20, 16, 12, 8, 4, 0]
            self.y = [0, 4, 8, 12, 16, 20]
        elif type == "increasing":
            self.x = [0, 1, 1.75, 2.25, 2.5, 2.63, 2.69]
            self.y = [20, 19, 17, 14, 10, 5, 0]
        self.createGraph()

class SD:
    def __init__(self, label1 = "Supply", label2 = "Demand", title = "Supply vs Demand"):
        self.xlabel = "Quantity"
        self.ylabel = "Price"
        self.title = title
        self.label1 = label1
        self.label2 = label2
        self.demandCurves = []
        self.supplyCurves = []
        self.intersections = []

    def formGraph(self):
        self.createEquilibriumGraph()
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.legend(bbox_to_anchor=(1,1.1), loc='upper left')
        plt.tight_layout()

    def markIntersections(self, max, modifier, curve):
        intersectX = max / 2
        intersectY = intersectX - modifier
        curve.append(plt.plot([0,intersectX], [intersectY,intersectY], linestyle="--", color="green"))
        curve.append(plt.plot([intersectX,intersectX], [intersectY,0], linestyle="--", color="green"))
    
    def createEquilibriumGraph(self):
        plt.plot([0,20], [20,0], label = self.label2)
        plt.plot([0,20], [0,20], label = self.label1)
        self.markIntersections(20, 0, self.intersections)
        plt.plot([10],[10], label = "Market Equilibrium", marker = "o", markerfacecolor="black")

    def demandShift(self, shiftAmount = 5):
        if shiftAmount < 0:
            self.demandCurves.append(plt.plot([0,20+shiftAmount], [20+shiftAmount,0], label=self.label2+"2"))
        else:
            self.demandCurves.append(plt.plot([shiftAmount, 20], [20, shiftAmount], label=self.label2+"2"))
        self.markIntersections(20+shiftAmount, 0, self.demandCurves)

    def clearDemandCurves(self):
        while len(self.demandCurves) > 0:
            val = self.demandCurves[0].pop(0)
            val.remove()
            self.demandCurves.pop(0)

    def supplyShift(self, shiftAmount = 5):
        if shiftAmount < 0:
            self.supplyCurves.append(plt.plot([0,20+shiftAmount], [-shiftAmount,20], label=self.label1+"2"))
        else:
            self.supplyCurves.append(plt.plot([shiftAmount, 20], [0,20-shiftAmount], label=self.label1+"2"))
        self.markIntersections(20+shiftAmount, shiftAmount, self.supplyCurves)

    def clearSupplyCurves(self):
        while len(self.supplyCurves) > 0:
            val = self.supplyCurves[0].pop(0)
            val.remove()
            self.supplyCurves.pop(0)

class ComplexSD(SD):
    def __init__(self, label1 = "SRAS", label2 = "AD", title = "Supply vs Demand"):
        super().__init__(label1, label2, title)

    def complexEquilibriumGraph(self):
        plt.plot([10,10], [0,20], label="LRAS")

    def demandShiftShortRun(self, shiftAmount = 5):
        self.complexEquilibriumGraph()
        self.demandShift(shiftAmount)
    
    def supplyShiftShortRun(self, shiftAmount = 5):
        self.complexEquilibriumGraph()
        self.supplyShift(shiftAmount)

    def longRunDemandShift(self, shiftAmount = 5):
        self.demandShiftShortRun(shiftAmount)
        self.supplyShift(-shiftAmount)
        plt.plot([10],[10+shiftAmount], label = "New Market Equilibrium", marker = "o", markerfacecolor="black")
        plt.plot([0,10], [10+shiftAmount,10+shiftAmount], linestyle = "--", color = "green")

    def longRunSupplyShift(self, shiftAmount = 5):
        self.supplyShiftShortRun(shiftAmount)
        self.demandShift(-shiftAmount)
        plt.plot([10],[10-shiftAmount], label = "New Market Equilibrium", marker = "o", markerfacecolor="black")
        plt.plot([0,10], [10-shiftAmount,10-shiftAmount], linestyle = "--", color = "green")

    def longRunEquilibriumShift(self, shiftAmount = 5):
        self.demandShiftShortRun(shiftAmount)
        self.supplyShiftShortRun(shiftAmount)
        plt.plot([15],[10], label = "New Market Equilibrium", marker = "o", markerfacecolor="black")
        plt.plot([0,15], [10,10], linestyle = "--", color = "green")
        plt.plot([15,15], [0,20], label="LRAS2")

# linearPPC = PPC("Linear PPC")
# linearPPC.createDefaultGraph("linear")

# increasingPPC = PPC("Increasing PPC")
# increasingPPC.createDefaultGraph("increasing")

# sd = SD()
# sd.formGraph()
# sd.supplyShift(-5)
# sd.clearSupplyCurves()
# sd.formGraph()
# sd.supplyShift(5)
# sd.formGraph()
# sd.demandShift(5)
# sd.formGraph()
# sd.demandShift(-5)
# sd.formGraph()

# csd = ComplexSD()

# fig1 = plt.figure(1, figsize = (10,6))
# csd.complexEquilibriumGraph()
# csd.formGraph()

# fig2 = plt.figure(2, figsize = (10,6))

# csd.longRunEquilibriumShift()
# csd.formGraph()

# plt.show()