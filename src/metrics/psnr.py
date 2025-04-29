import numpy as np

def psnr(original: np.ndarray, reconstructed: np.ndarray) -> float:
    """Calcula PSNR entre dos imágenes (dB)."""
    mse = np.mean((original.astype(float) - reconstructed.astype(float))**2)
    if mse == 0:
        return float('inf')
    MAX = 255.0
    return 20 * np.log10(MAX / np.sqrt(mse))

