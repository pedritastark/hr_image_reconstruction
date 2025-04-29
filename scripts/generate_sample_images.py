from skimage import data, io, img_as_ubyte
import os

os.makedirs("data/raw", exist_ok=True)

# Telemedicina: retina
retina = img_as_ubyte(data.retina())
io.imsave("data/raw/retina.png", retina)

# Teledetección: Hubble Deep Field
hubble = img_as_ubyte(data.hubble_deep_field())
io.imsave("data/raw/hubble.png", hubble)

# Fotografía digital: astronauta
astro = img_as_ubyte(data.astronaut())
io.imsave("data/raw/astronaut.png", astro)

print("Imágenes generadas en data/raw/")
