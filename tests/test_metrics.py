import numpy as np
from src.metrics.ssim import ssim


def test_ssim_perfect():
    img = np.random.randint(0,256,(10,10),dtype=np.uint8)
    assert ssim(img, img) == 1.0


def test_ssim_complement():
    img = np.zeros((10,10),dtype=np.uint8)
    inv = np.full((10,10),255,dtype=np.uint8)
    # Con imágenes totalmente opuestas, SSIM suele ser bajo (<0.1)
    score = ssim(img, inv)
    assert 0.0 <= score < 0.2

