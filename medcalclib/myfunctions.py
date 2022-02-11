# Respiratory Therapy
def minuteventilation (rate, tidal_volume) -> float :
    """
    Calculate the minute ventilation   
    rate x Tidal Volume 
    """    
    return rate * (tidal_volume / 1000)

def airwayresistance (pip, plateau, flow) -> int:
    """
    Calculate Airwary Resistance
    Raw = (PIP - Plateau Pressure) / Flow
    """

    return (pip - plateau) / flow

def pfratio (PaO2, FiO2) -> int:
    """
    P/F Ratio
    PaO2 / FiO2
    """
    return PaO2 / FiO2

# Nursing Calculations
def univeralsdrugcalc (desired, onhand, output):
    dose = []
    """
    Universal Formula Drug Calcation 
    In the universal formula (or “desired over have method”), the desired amount (D) is the dose  prescribed and the amount on hand (H)
     or the amount you “have” is the available dose or concentration. The quantity (Q) is the form and amount in which the drug is supplied 
     (i.e. tablet, capsule, liquid). To calculate the dose, take the desired amount and divide it by the amount on hand, then multiply it by 
     the quantity, like this:
    
    (desired / onhand) * quantity = Dose    
    output is the Unit output

    return a list with dose and unit
    """    
    dose.append((desired / onhand) * 1)    
    dose.append(output)

    return dose

# Doctor Calcuations
