import numpy as np
import os
from src.io.image_io import load_image, save_image

def test_load_and_save(tmp_path):
    # Genera un array sencillo
    arr = np.arange(16, dtype=np.uint8).reshape(4,4)
    p = tmp_path / 'test.png'
    # Guarda y recarga
    save_image(arr, str(p))
    img = load_image(str(p))
    assert img.shape == (4,4)
    assert img.dtype == np.uint8
    assert np.array_equal(img, arr)
