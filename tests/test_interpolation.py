import numpy as np
from src.interpolation.bilinear import bilinear_interpolate

def test_bilinear_identity():
    img = np.random.randint(0,256,(5,5),dtype=np.uint8)
    out = bilinear_interpolate(img, 1.0)
    assert out.shape == img.shape
    assert np.array_equal(out, img)

def test_bilinear_scale2():
    img = np.array([[0,255],[255,0]],dtype=np.uint8)
    out = bilinear_interpolate(img, 2.0)
    # Esquinas coinciden
    assert out[0,0] == int(img[0,0])
    assert out[3,3] == int(img[1,1])
    # Centro: promedio de los cuatro vértices
    s = int(img[0,0]) + int(img[0,1]) + int(img[1,0]) + int(img[1,1])
    expected = s / 4
    assert abs(int(out[1,1]) - int(expected)) <= 1

