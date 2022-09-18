# Respiratory Therapy

def durationOfFlow(tanksize: str, pressure: int, literflow: float) -> float:
    """
    Calculate oxygen tank duration of flow
    Duration = (Gauge Pressure x Tank Factor) / Liter Flow

    D cylinder: 0.16
    E cylinder: 0.28
    G cylinder: 2.41
    H cylinder: 3.14
    """

    tankfactor = 0.0
    tanksize = tanksize.upper()

    if tanksize == 'D':
        tankfactor = 0.16
    if tanksize == 'E':
        tankfactor = 0.28
    if tanksize == 'G':
        tankfactor = 2.41
    if tanksize == 'H':
        tankfactor = 3.14

    return (pressure * tankfactor) / literflow


def airwayResistance(pip: int, plateau: int , flow: int) -> int:
    """
    Calculate Airwary Resistance
    Raw = (PIP - Plateau Pressure) / Flow
    """

    return (pip - plateau) / flow


def minuteVentilation(rate, tidal_volume) -> float:
    """
    Calculate the minute ventilation
    rate x Tidal Volume
    """
    return rate * (tidal_volume / 1000)


def pfRatio(paO2, fiO2) -> int:
    """
    P/F Ratio
    PaO2 / FiO2
    """
    return paO2 / fiO2


def rapidShallowBreathingIndex(tidal_volume, respiratory_rate) -> int:
    """
    Rapid Shallow Breathing Index
    respiratory rate / tidal volums (400 is 0.400)
    """
    return respiratory_rate / (tidal_volume / 1000)


# Nursing Calculations
def universalDrugCalc(desired, onhand, output):
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

# Doctor Calculations


# Universal Medical Calculations
def farenheitToCelcius(farenheit: float) -> int:
    """
    Convert Farenheit To Celsius
    °C = (°F - 32) / 1.8
    """
    return ((farenheit - 32) / 1.8)