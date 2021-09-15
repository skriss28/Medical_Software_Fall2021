import pytest

@pytest.mark.parametrize("HDL_value, expected", [
    (65, "Normal"),
    (45, "Borderline Low"),
    (15, "Low"),
    (70, "Normal")])
def test_HDL_Anlysis(HDL_value, expected):
    from Blood_Calculator import HDL_Analysis
    answer = HDL_Analysis(HDL_value)
    assert answer == expected
    