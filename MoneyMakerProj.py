# Author: Aaron Alejo
# Date: Dec. 27, 2020

# Purpose: Helps user to figure out if a stock is selling at a good price
# Calculates the approximate Intrinsic value of a company by collected data 

# Other comments: These calculation is just an approximate evaluation of the 
# value of a company
# "It is better to be approximately right than precisely wrong" 
# -John Maynard Keynes

# Main Function
# Intrinsic Value calculator, caller function that asks user for input to 
# initialize values and call helper funtion to do the calculations
def main():
    """
        This function will take data from the user and calculate the instrinsic
    or real value of a stock, and then displays selling price of the stock.
    
    Parameter(s): None
    Return: None
    """
    
    # Data collected from any source is then inputted in the values below
    print("\n=== Intrinsic Value Calculator ===\n")
    
    ticker = (input("Ticker?: "))
    print("\nTicker: "+ ticker.upper())
    
    print("---------------------------------------------------\n")
    
    # Asks user for growth rate and error handles given data for validity
    growthRate = input("Approximate Growth Rate (1-5 years)(%): ")
    while type(growthRate) == str :
        
        if growthRate == "0" or growthRate == "":   # When empty
            return
        try:
            growthRate = float(growthRate)    # Converts input to an integer

            #if growthRate > 100:            # Checks if input is within range
                #print("Invalid value, please try again...")
                #growthRate = input("Approximate Growth Rate (1-5 years)(%): ")                
        except:
            print("Invalid value, please try again...")
            growthRate = input("Approximate Growth Rate (1-5 years)(%): ")
            
    print("---------------------------------------------------\n")
    # 10 year span of approximate growth rate of a company
    growthRate2 = input("Approximate Growth Rate(6-10 years)(%): ")
    while type(growthRate2) == str:
        
        if growthRate2 == "0" or growthRate2 == "":  # Empty value
            return 
        
        try:
            growthRate2 = float(growthRate2)    # Converts input to an integer

            #if growthRate2 > 100:            # Checks if input is within range
                #print("Invalid value, please try again...")
                #growthRate2 = input("Approximate Growth Rate(16-10 years)(%):")                
        except:
            print("Invalid value, please try again...")
            growthRate2 = input("Approximate Growth Rate(6-10 years)(%): ") 
            
    print("---------------------------------------------------\n")
    # Asks for user's preffered discount rate or percent the user wants to 
    # earn with the stock. OR the WACC which is the calculated rate of the stock
    # calculated from the asked values or from other sources
    answer = input("Do you know the WACC/Discount Rate?(Yes/NO): ")
    
    if answer.upper() == 'YES':
        discountRate = input("Discount Rate(%): ") 
        try:
            discountRate = float(discountRate)    # Converts input to an integer
    
            if discountRate > 100:            # Checks if input is within range
                print("Invalid value, please try again...")
                discountRate = input("Discount Rate(%): ") 
                
        except:
            print("Invalid value, please try again...")
            discountRate = input("Discount Rate(%): ")        
    
    else:  
        totalEq = input("Total Equity($Billions): ")# Total equity of the company
        
        while type(totalEq) == str or totalEq == "":
            try:
                totalEq = float(totalEq)
            except:
                print("Invalid value, please try again...")
                totalEq = input("Total Equity($Billions): ")
        
        # Total debt of the company
        totalDeb = input("Total Debt($Billions): ")
        while type(totalDeb) == str or totalDeb == "":
            try:
                totalDeb = float(totalDeb)
            except:
                print("Invalid value, please try again...")
                totalDeb = input("Total Debt($Billions): ")     
            
        # Cost of debt
        costDeb = input("Cost of Debt($): ")
        while type(costDeb) == str or costDeb == "":
            try:
                costDeb = float(costDeb)
            except:
                print("Invalid value, please try again...")
                costDeb = input("Cost of Debt($): ")
        
        # Cost of Equity  
        costEq = input("Cost of Equity($): ")
        while type(costEq) == str or costEq == "":
            try:
                costEq = float(costEq)
            except:
                print("Invalid value, please try again...")
                costEq = input("Cost of Equity($): ")
            
        # Corporate Tax rate
        corpTax = input("Corporate tax rate(%): ")
        while type(corpTax) == str or corpTax == "":
            try:
                corpTax = float(corpTax)
            except:
                print("Invalid value, please try again...")
                corpTax = input("Corporate tax rate(%): ")
        
        # Discount rate: rate of return user wants to get in the stock
        discountRate = waccCalc(totalEq, totalDeb, costDeb, costEq, corpTax)
        print("\nDiscount Rate(%): " + str(discountRate))        
    
    print("---------------------------------------------------\n")
    # This value represents the quality of the company, 10 = lower quality
    # 15 = higher quality
    terminalVal = input("Terminal Value (multiple of FCF, 10-15): ")
    while type(terminalVal) == str or terminalVal == "":
        try:
            terminalVal = int(terminalVal)    # Converts input to an integer
        
            # Checks if input is within range
            if terminalVal < 10 or terminalVal > 15 :
                print("Invalid value, please try again...")
                terminalVal = input("Terminal Value (multiple of FCF, 10-15): ")  
            
        except:
            print("Invalid value, please try again...")
            terminalVal = input("Terminal Value (multiple of FCF, 10-15): ")   
    
    print("---------------------------------------------------\n")
    # Year 1 company free cash flow
    # Pick value that is most representative of the company
    freeCashFlow = input("Year 1 Free Cash Flow($Billions): ")
    while type(freeCashFlow) == str or freeCashFlow == "": 
        try:
            freeCashFlow = float(freeCashFlow)    # Converts input to an integer
                
        except:
            print("Invalid value, please try again...")
            freeCashFlow = input("Year 1 Free Cash Flow($Billions): ")  
        
    print("---------------------------------------------------\n")
    # Net cash = Total cash - total debt
    netCash = input("Net cash($Billions): ")
    while type(netCash) == str or netCash == "": 
        try:
            netCash = float(netCash)    # Converts input to an integer
                    
        except:
            print("Invalid value, please try again...")
            netCash = input("Net cash($Billions): ")   
    
    print("---------------------------------------------------\n")
    # Outstanding shares. 
    outstandShre = input("Outstanding shares(Billions): ")
    while type(outstandShre) == str or outstandShre == "": 
        try:
            outstandShre = float(outstandShre)    # Converts input to an integer
                    
        except:
            print("Invalid value, please try again...")
            outstandShre = input("Outstanding shares(Billions): ")
    
    print("---------------------------------------------------\n")
    print(totalStockValue(freeCashFlow, growthRate, growthRate2, discountRate,\
                         terminalVal, netCash, outstandShre))

# Helper function that does the calculation
def totalStockValue(cash, gr, gr2, discount, termVal, netC, outShre):
    """
        Calculates and displays company value, share value, and margin of 
    safety.
    
    Parameter(s): cash: float: annual company cash flow 
                  gr: int: growth rate in 1-5 year span
                  gr2: int: growth rate in 6-10 year span
                  discount: int: cutoff based on the risk tolerance of the user
                  termVal: int: rank of quality of the company
                  netC: int: annual net cash of the company
                  outShre: float: shares outstanding
                  
    Return: Present Value of Future Cash flos in billions
            Intrinsic Value of the company in billions
            Intrinsic Value of each share
            30% Margin of safety 
            50% Margin of safety
    """
    
    # Initialize variables based from the parameters
    yearlyCash = cash
    totalCash1 = cash
    presentVal = cash/(1+(discount/100)**1)
    freeCashlist = [cash]
    
    # Calculates the approximate yearly cash flow of the company in 5 year span
    for years in range(2, 6):        
        yearlyCash += yearlyCash * (gr/100)
        totalCash1 += round(yearlyCash)
        freeCashlist.append(round(yearlyCash))
    
    # Calculates the approximate yearly cash flow of the company in 10 year span
    totalCash2 = totalCash1
    for years2 in range(6, 11):
        yearlyCash += yearlyCash * (gr2/100)
        totalCash2 += round(yearlyCash)
        freeCashlist.append(round(yearlyCash))
    
    # Represents present values relative to yearly free cash flow
    # which is then used to calculate intrinsic values
    total = round((yearlyCash*termVal) / .9906)
    presentValofFutCashflow = round(total/(1 + (discount/100))**10)
    years3 = 1
    presentVallst = []       # Keep track of present values throughout the years
    for cashVal in freeCashlist:  # Relation to yearly free cash flow        
        presentVal = round(cashVal)/(1+(discount/100))**years3
        years3 += 1
        presentVallst.append(round(presentVal))
    
    # Calculation of values
    presentValFut = round((sum(presentVallst)+presentValofFutCashflow))
    intrinsComp = round(presentValFut+netC)
    intrinShre = round(intrinsComp/outShre)
    
    # Margin of safeties. 30% and 50%
    margin30 = intrinShre*0.7
    margin50 = intrinShre*0.5

    return("\nPresent Value of Future Cash Flows (Billions) = $"+ \
           str(presentValFut) + "\nIntrinsic Value ($Billions) = $" + \
           str(intrinsComp) + "\nIntrinsic Value (per share) = $" +\
           str(intrinShre) + "\n30% Margin of Safety = $" + str(margin30) + \
           "\n50% Margin of Safety = $" + str(margin50))

# Discount rate calculator helper function
# Did not realize it's going to be a one-liner prior to writing everything
# So I'm just going to stick with it lol
def waccCalc(E, D, Rd, Re, Tc):
    """
        Called by the main function. Asks user for several values needed to
    calculate the weighted average cost of capital(WACC) or the discount rate.
    
    Paremeter(s): Total debt(D): float: total debt of the company in billions
                  Total Equity(E): float: total equity of company in billions
                  Cost of debt(Rd): float: the effective interest rate a 
                                            company pays on its debts
                  Cost of Equity(Re): float: the return a firm theoretically
                                             pays to its equity investor
                  Corporate Tax Rate(Tc): float: 
    Return: (totalEq / (totalEq + debt)) * costEq + \
            (debt/(totalEq + debt)) * costDeb * (1 - corpTax) 
    """
    
    return((E / (E + D)) * Re + (D/(E + D)) * Rd * (1 - Tc))   
    
if __name__ =="__main__":
    main()
