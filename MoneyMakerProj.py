# Author: Aaron Alejo
# Date: Dec. 27, 2020
# Assignment: Create an Investment data calculator

# Purpose: Helps user to figure out if a stock is a buy
# Calculates the approximate Intrinsic value of a company by collected data 


# Other comments: These calculation is just an approximate evaluation of the 
# value of a company
# "It is better to be approximately right than precisely wrong" 
# -John Maynard Keynes

# Intrinsic Value calculator
def IntrinsicCalc():
    """
        This function will take data from the user and calculate the instrinsic
    or real value of a stock, and then displays and compares the value to the
    current selling price of the stock.
    
    Parameter(s): None
    Return: Decision, whether its a buy or not
    """
    
    # Data collected from any source is then inputted in the values below
    print("\n=== Intrinsic Value Calculator ===\n")
    
    ticker = (input("Ticker?: "))
    print("\nTicker: "+ ticker.upper())
    
    print("---------------------------------------------------\n")
    
    # Asks user for growth rate and error handles given data for validity
    growthRate = input("Approximate Growth Rate (1-5 years)(%): ")
    while type(growthRate) == str or int(growthRate) > 100:
        
        if growthRate == "0" or growthRate == "":   # When empty
            return
        try:
            growthRate = int(growthRate)    # Converts input to an integer

            if growthRate > 100:            # Checks if input is within range
                print("Invalid value, please try again...")
                growthRate = input("Approximate Growth Rate (1-5 years)(%): ")                
        except:
            print("Invalid value, please try again...")
            growthRate = input("Approximate Growth Rate (1-5 years)(%): ")
            
    print("---------------------------------------------------\n")
    # 10 year span of approximate growth rate of a company
    growthRate2 = input("Approximate Growth Rate(6-10 years)(%): ")
    while type(growthRate2) == str or int(growthRate2) > 100:
        
        if growthRate2 == "0" or growthRate == "":  # Empty value
            return 
        
        try:
            growthRate2 = int(growthRate2)    # Converts input to an integer

            if growthRate2 > 100:            # Checks if input is within range
                print("Invalid value, please try again...")
                growthRate2 = input("Approximate Growth Rate(16-10 years)(%): ")                
        except:
            print("Invalid value, please try again...")
            growthRate2 = input("Approximate Growth Rate(6-10 years)(%): ") 
            
    print("---------------------------------------------------\n")
    # This will depend personally. The Lower the % is the Higher the intrinsic
    # value is going to be, thus the return will be lower, and vice versa
    discountRate = input("Discount Rate(%): ")
    
    try:
        discountRate = int(discountRate)    # Converts input to an integer

        if discountRate > 100:            # Checks if input is within range
            print("Invalid value, please try again...")
            discountRate = input("Discount Rate(%): ") 
            
    except:
        print("Invalid value, please try again...")
        discountRate = input("Discount Rate(%): ")
    
    print("---------------------------------------------------\n")
    # This value represents the quality of the company, 10 = lower quality
    # 15 = higher quality
    terminalVal = input("Terminal Value (multiple of FCF, 10-15): ")
    
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
    
    try:
        freeCashFlow = float(freeCashFlow)    # Converts input to an integer
                
    except:
        print("Invalid value, please try again...")
        freeCashFlow = input("Year 1 Free Cash Flow($Billions): ")  
        
    print("---------------------------------------------------\n")
    # Net cash = Total cash - total debt
    netCash = input("Net cash($Billions): ")
    
    try:
        netCash = int(netCash)    # Converts input to an integer
                
    except:
        print("Invalid value, please try again...")
        netCash = input("Net cash($Billions): ")   
    
    print(totalFreeCash(freeCashFlow, growthRate, growthRate2, discountRate,\
                         terminalVal))

# Total Cash flow in 10 years
def totalFreeCash(cash, gr, gr2, discount, termVal):
    """
        Calculates the total free Cash flow in 10 years multiplied by the 
    terminal value of the company
    
    Parameter(s): cash: float: annual company cash flow 
                  gr: int: growth rate in 1-5 year span
                  gr2: int: growth rate in 6-10 year span
                  discount: int: cutoff based on the risk tolerance of the user
                  termVal: int: rank of quality of the company
                  
    Return: 10th year Free Cash Flow * terminal value
    """
    
    # Initialize variables based from the parameters
    yearlyCash = cash
    totalCash1 = cash
    presentVal = cash/(1+(discount/100)**1)
    freeCashlist = [cash]
    for years in range(2, 6):
        
        yearlyCash += yearlyCash * (gr/100)
        totalCash1 += round(yearlyCash)
        freeCashlist.append(round(yearlyCash))
        
    totalCash2 = totalCash1
    for years2 in range(6, 11):
        
        yearlyCash += yearlyCash * (gr2/100)
        totalCash2 += round(yearlyCash)
        freeCashlist.append(round(yearlyCash))
        
    total = round((yearlyCash*termVal) / .9906)
    presentValofFutCashflow = round(total/(1 + (discount/100))**10)
    
    years3 = 1
    presentVallst = []
    for cashVal in freeCashlist:
        
        presentVal = round(cashVal)/(1+(discount/100))**years3
        years3 += 1
        presentVallst.append(round(presentVal))
    
    return("\nIntrinsic Value = $"+ \
           str((round((sum(presentVallst)+presentValofFutCashflow)))))
    
IntrinsicCalc()
