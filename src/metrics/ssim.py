import numpy as np
from skimage.metrics import structural_similarity

def ssim(original: np.ndarray, reconstructed: np.ndarray) -> float:
    """Calcula el índice SSIM entre dos imágenes. Devuelve 0.0 si el resultado es NaN."""
    score, _ = structural_similarity(
        original,
        reconstructed,
        full=True,
        data_range=original.max() - original.min()
    )
    return 0.0 if np.isnan(score) else float(score)

