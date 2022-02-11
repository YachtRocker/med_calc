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

# Doctor Calcuations
