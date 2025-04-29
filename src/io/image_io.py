from skimage import io, color
import numpy as np

def load_image(path: str) -> np.ndarray:
    """
    Carga una imagen en escala de grises (uint8) desde 'path'.
    Si la imagen está en color, la convierte a gris.
    """
    img = io.imread(path)
    if img.ndim == 3:
        # pasa de RGB a gris [0,1]
        img = color.rgb2gray(img)
        # escala a [0,255]
        img = (img * 255).astype(np.uint8)
    return img.astype(np.uint8)

def save_image(img: np.ndarray, path: str) -> None:
    """
    Guarda un array (2D uint8) como imagen en 'path'.
    """
    io.imsave(path, img)

