import numpy as np

def _cubic_kernel(t: float) -> float:
    """Núcleo de convolución cúbica de Keys (a = -0.5)"""
    a = -0.5
    t = abs(t)
    if t <= 1:
        return (a+2)*t**3 - (a+3)*t**2 + 1
    elif t < 2:
        return a*t**3 - 5*a*t**2 + 8*a*t - 4*a
    else:
        return 0.0

def bicubic_interpolate(img: np.ndarray, alpha: float) -> np.ndarray:
    """Escala 'img' por factor 'alpha' usando interpolación bicúbica."""
    M, N = img.shape
    M2, N2 = int(alpha*M), int(alpha*N)
    out = np.zeros((M2, N2), dtype=img.dtype)
    for i2 in range(M2):
        for j2 in range(N2):
            x = i2/alpha
            y = j2/alpha
            x0 = int(np.floor(x))
            y0 = int(np.floor(y))
            val = 0.0
            for m in range(-1, 3):
                for n in range(-1, 3):
                    xm = min(max(x0+m, 0), M-1)
                    yn = min(max(y0+n, 0), N-1)
                    w = _cubic_kernel(x - (x0+m)) * _cubic_kernel(y - (y0+n))
                    val += img[xm, yn] * w
            out[i2, j2] = np.clip(val, 0, 255)
    return out
