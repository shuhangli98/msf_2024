import numpy as np
import msf_2024

def test_calculate_angle():
    rA = np.array([0, 0, -1])
    rB = np.array([0, 0, 0])
    rC = np.array([1, 0, 0])
    assert msf_2024.calculate_angle(rA, rB, rC) == np.pi / 2
    assert msf_2024.calculate_angle(rA, rB, rC, degrees=True) == 90.0