freeCashFlow = 21.2
growthRate = 20
growthRate2 = 10
discountRate = 10
terminalVal = 15
# Total Cash flow in 10 years
def totalFreeCash(cash, gr, gr2, discount, termVal):
    """
        Calculates the total free Cash flow in 10 years multiplied by the 
    terminal value of the company
    
    Parameter(s): None
    Return: 10th year Free Cash Flow * terminal value
    """
    
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
    
    print(round((sum(presentVallst)+presentValofFutCashflow)))
    
totalFreeCash(freeCashFlow, growthRate, growthRate2, discountRate, terminalVal)