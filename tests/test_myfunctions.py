from medcalclib import myfunctions


def test_minuteVentilation():
    assert myfunctions.minuteVentilation(22, 325)


def test_airwayResistance():
    assert myfunctions.airwayResistance(32, 24, 65)


def test_pfRatio():
    assert myfunctions.pfRatio(67, 98)


def test_universalDrugCalc():
    assert myfunctions.universalDrugCalc(750, 250, 'tablets')


def test_rapidShallowBreathingIndex():
    assert myfunctions.rapidShallowBreathingIndex(12, 400)
