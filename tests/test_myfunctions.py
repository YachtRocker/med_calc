from medcalclib import myfunctions

def  test_minuteventilation():
    assert myfunctions.minuteventilation(22, 325)

def test_airwayresistance():
    assert myfunctions.airwayresistance(32, 24, 65)

def test_pfratio():
    assert myfunctions.pfratio(67, 98)