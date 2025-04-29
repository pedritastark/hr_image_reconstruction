import numpy as np
from src.interpolation.bicubic import bicubic_interpolate

def test_bicubic_identity():
    img = np.random.randint(0,256,(6,6),dtype=np.uint8)
    out = bicubic_interpolate(img, 1.0)
    assert out.shape == img.shape
    assert np.array_equal(out, img)

def test_bicubic_scale2_simple():
    # Un pequeño parche de dos tonos
    img = np.array([[0,255],[255,0]],dtype=np.uint8)
    out = bicubic_interpolate(img, 2.0)
    # Esquinas
    assert out[0,0] == int(img[0,0])
    assert out[-1,-1] == int(img[1,1])
    # Centro aproximado (debería rondar el promedio)
    avg = int((int(img[0,0])+int(img[0,1])+int(img[1,0])+int(img[1,1]))/4)
    assert abs(int(out[1,1]) - avg) <= 5
