import os
from skimage import io, img_as_ubyte
from skimage.transform import resize

# Factor de reducción (50%)
alpha = 0.5
os.makedirs('data/downsampled', exist_ok=True)

for fname in ['retina.png','hubble.png','astronaut.png']:
    # Carga color o escala de grises según corresponda
    img = io.imread(f'data/raw/{fname}')
    # Calcula nuevo tamaño
    M, N = img.shape[:2]
    new_shape = (int(M * alpha), int(N * alpha))
    # Redimensiona con antialiasing
    img_rs = resize(img, new_shape, anti_aliasing=True)
    # Convierte a 8-bits y guarda
    io.imsave(f'data/downsampled/{fname}', img_as_ubyte(img_rs))

print('Downsampling completado')

