from mlproject.tools import haversine

def test_tools():
    assert haversine(1,1,1,1) == 0
    assert haversine(0,0,0,1) == 1
    assert haversine(0,0,1,0) == 1
    # assert haversine(0,0,1,1) == 1
    # assert haversine(1,2,3,4) == 0
