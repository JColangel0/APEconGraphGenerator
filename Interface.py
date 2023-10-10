from tkinter import *
from tkinter import ttk
import GraphController as gc

root = Tk()

def createInterface():
    frame = Frame(root)
    frame.pack()

    defaultPPCButton = Button(frame, text = "New PPC Graph", command = lambda: DefaultPPCSetUp(frame))
    defaultPPCButton.pack()
    sdButton = Button(frame, text = "New Supply v Demand Graph", command = lambda: SDSetUp(frame))
    sdButton.pack()
    complexSDButton = Button(frame, text = "New Aggregate Supply v Demand Graph", command = lambda: complexSDSetUp(frame))
    complexSDButton.pack()

def clearAll(widget):
    widget.pack_forget()
    gc.close()
    createInterface()

def DefaultPPCSetUp(widget):
    widget.pack_forget()
    frame = Frame(root)
    frame.pack(padx=15, pady=15)

    typeLabel = Label(frame, text="Graph Type:")
    typeLabel.pack()
    type = ttk.Combobox(frame, values = ["Linear", "Increasing"])
    type.pack()
    calls = 0
    def option_selected(e):
        nonlocal calls
        selected_option = type.get()
        graphType = 0 if selected_option == "Linear" else 1
        calls += 1
        gc.createPPCGraphs(selected_option, graphType, calls)
    
    type.bind("<<ComboboxSelected>>", option_selected)

    returnButton = Button(frame, text="Back", command = lambda: clearAll(frame))
    returnButton.pack()

def SDSetUp(widget):
    widget.pack_forget()
    frame = Frame(root)
    frame.pack(padx=15, pady=15)

    supplyLabel = Label(frame, text = "Supply Curve Shifters")
    supplyLabel.pack()
    supplyShift = ttk.Combobox(frame, values=["Price of Inputs Increases", "Number of Sellers Increases", 
                                              "Technology Improves", "Taxes Increase", "Profit Expectations Increase",
                                              "Price of Inputs Decreases", "Number of Sellers Decreases",
                                              "Subsidies Increase", "Profit Expectations Decrease"], width = 25)
    supplyShift.pack()

    demandLabel = Label(frame, text = "Demand Curve Shifters")
    demandLabel.pack()
    demandShift = ttk.Combobox(frame, values=["Number of Consumers Increases", "Related Goods Get More Expensive",
                                              "Income Increases", "Future Expectations Improve", "Number of Consumers Decreases",
                                              "Related Goods Get Cheaper", "Income Decreases", "Future Expectations Deteriorate"], width = 25)
    demandShift.pack()
    gc.createSDGraphs()
    def demandCurveShift(e):
        shifts = {
            "Number of Consumers Increases" : 5, 
            "Related Goods Get More Expensive" : 5,
            "Income Increases" : 5, 
            "Future Expectations Improve" : 5, 
            "Number of Consumers Decreases" : -5,
            "Related Goods Get Cheaper" : -5, 
            "Income Decreases" : -5, 
            "Future Expectations Deteriorate" : -5
        }
        selected_option = demandShift.get()
        gc.updateSDGraphs("Demand", shifts[selected_option])

    def supplyCurveShift(e):
        shifts = {
        "Price of Inputs Increases" : -5, 
        "Number of Sellers Increases" : 5, 
        "Technology Improves" : 5, 
        "Taxes Increase" : -5, 
        "Profit Expectations Increase" : 5,
        "Price of Inputs Decreases" : 5, 
        "Number of Sellers Decreases" : -5,
        "Subsidies Increase" : 5, 
        "Profit Expectations Decrease": -5
        }
        selected_option = supplyShift.get()
        gc.updateSDGraphs("Supply", shifts[selected_option])

    demandShift.bind("<<ComboboxSelected>>", demandCurveShift)
    supplyShift.bind("<<ComboboxSelected>>", supplyCurveShift)

    returnButton = Button(frame, text="Back", command = lambda: clearAll(frame))
    returnButton.pack()

def complexSDSetUp(widget):
    widget.pack_forget()
    frame = Frame(root)
    frame.pack(padx=15, pady=15)

    supplyLabel = Label(frame, text = "Supply Curve Shifters")
    supplyLabel.pack()
    supplyShift = ttk.Combobox(frame, values=["Resource Prices Increase", "Resource Prices Decrease", 
                                              "Taxes Increase", "Taxes Decrease", "Subsidies Increase",
                                              "Subsidies Decrease", "Productivity Increase",
                                              "Productivity Decreases"], width = 25)
    supplyShift.pack()

    demandLabel = Label(frame, text = "Demand Curve Shifters")
    demandLabel.pack()
    demandShift = ttk.Combobox(frame, values=["Consumer Spending Increases", "Consumer Spending Decreases",
                                              "Investment Spending Increases", "Investment Spending Decreases", "Gov Spending Increases",
                                              "Gov Spending Decreases", "Net Exports Increase", "Net Exports Decrease"], width = 25)
    demandShift.pack()
    gc.createComplexSDGraphs()
    def demandCurveShift(e):
        shifts = {
            "Consumer Spending Increases" : 5, 
            "Consumer Spending Decreases" : -5,
            "Investment Spending Increases" : 5, 
            "Investment Spending Decreases" : -5, 
            "Gov Spending Increases" : 5,
            "Gov Spending Decreases" : -5, 
            "Net Exports Increase" : 5, 
            "Net Exports Decrease" : -5
        }
        selected_option = demandShift.get()
        gc.updateComplexSDGraphs("Demand", shifts[selected_option], "short")
        gc.updateComplexSDGraphs("Demand", shifts[selected_option], "long")

    def supplyCurveShift(e):
        shifts = {
            "Resource Prices Increase" : 5,
            "Resource Prices Decrease" : -5, 
            "Taxes Increase" : 5, 
            "Taxes Decrease" : -5, 
            "Subsidies Increase" : 5,
            "Subsidies Decrease" : -5, 
            "Productivity Increase" : 5,
            "Productivity Decreases" : -5
        }
        selected_option = supplyShift.get()
        gc.updateComplexSDGraphs("Supply", shifts[selected_option], "short")
        gc.updateComplexSDGraphs("Supply", shifts[selected_option], "long")

    demandShift.bind("<<ComboboxSelected>>", demandCurveShift)
    supplyShift.bind("<<ComboboxSelected>>", supplyCurveShift)

    returnButton = Button(frame, text="Back", command = lambda: clearAll(frame))
    returnButton.pack()

if __name__ == "__main__":
    createInterface()
    root.title("Graphs")
    root.mainloop()