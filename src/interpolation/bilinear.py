import numpy as np

def bilinear_interpolate(img: np.ndarray, alpha: float) -> np.ndarray:
    """
    Escala 'img' por factor 'alpha' usando interpolación bilineal.
    """
    M, N = img.shape
    M2, N2 = int(alpha*M), int(alpha*N)
    out = np.zeros((M2, N2), dtype=img.dtype)
    for i2 in range(M2):
        for j2 in range(N2):
            x = i2/alpha
            y = j2/alpha
            x0 = int(np.floor(x)); x1 = min(x0+1, M-1)
            y0 = int(np.floor(y)); y1 = min(y0+1, N-1)
            dx = x - x0; dy = y - y0
            v00 = img[x0, y0]; v10 = img[x1, y0]
            v01 = img[x0, y1]; v11 = img[x1, y1]
            val = (1-dx)*(1-dy)*v00 + dx*(1-dy)*v10 + (1-dx)*dy*v01 + dx*dy*v11
            out[i2, j2] = np.clip(val, 0, 255)
    return out
