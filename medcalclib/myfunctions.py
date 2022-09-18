# Respiratory Therapy

def durationOfFlow(tanksize: str, pressure: int, literflow: float) -> float:
    """
    Calculate oxygen tank duration of flow
    Duration = (Gauge Pressure x Tank Factor) / Liter Flow

    Tank Sizes
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


def staticCompliance(tidal_volume: int, plateau_pressure: int, peep: int) -> int:
    """
    Static Lung Compliance fomula: tidal_volume / (plateau_pressure - peep)
        example: 500 / (25 - 5) = 25
    """
    return (tidal_volume / (plateau_pressure - peep))


def dynamicCompliance(tidal_volume: int, peak_insp_pressure: int, peep: int) -> int:
    """
    Dynamic Lung Compliance formula: tidal_volume / (peak_insp_pressure - peep)
        example: 500 / (25 - 5) = 25
    """
    return (tidal_volume / (peak_insp_pressure - peep))


def alveolarGasEquation(FiO2: float, pb: int, PaCO2: float) -> float:
    """
    Alveolar Gas Equation: PAO2 = FiO2(PB - PH2O) - PaCO2/RQ
    
    FiO2 example: 21% enter as 0.21

    The alveolar gas equation is a formula used to approximate the partial pressure of oxygen in the alveolus (PAO2)
    PB is the barometric pressure, PH2O is the water vapor pressure (usually 47 mmHg), FiO2 is the fractional concentration of inspired oxygen, 
    and R is the gas exchange ratio. (The rate of CO2 production to O2 use is usually around 0.8 at rest.)
    """
    ph20 = 47
    rq = 0.8

    ans = (FiO2*(pb - ph20)) - (PaCO2 / rq)

    return (round(ans, 1))


# Nursing Calculations
def universalDrugCalc(desired: float, onhand: float, quantity: int):
    """
    Universal Formula Drug Calculation 
    In the universal formula (or “desired over have method”), the desired amount (D) is the dose  prescribed and the amount on hand (H)
     or the amount you “have” is the available dose or concentration. The quantity (Q) is the form and amount in which the drug is supplied 
     (i.e. tablet, capsule, liquid). To calculate the dose, take the desired amount and divide it by the amount on hand, then multiply it by 
     the quantity, like this:
    
    (desired / onhand) * quantity = Dose    
    output is the Unit output

    example: 1 Tablet = 250mg
        Desired                 750 mg
        ------- * Quantity =    ------ = x 1 Tablet = 3 Tablets     Returns 3
        On Hand                 250 mg

    return total to use
    """
    return ((desired / onhand) * quantity)

# Doctor Calculations


# Universal Medical Calculations
def farenheitToCelcius(farenheit: float) -> int:
    """
    Convert Farenheit To Celsius
    °C = (°F - 32) / 1.8
    """
    return ((farenheit - 32) / 1.8)