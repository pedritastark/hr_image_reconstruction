# RhinoScale

> Implementación en Python de un pipeline de super-resolución de imágenes  
> Interpolación bilineal y bicúbica (Keys) con validación PSNR/SSIM

---

## Descripción

RhinoScale permite transformar imágenes de baja resolución en versiones de alta resolución preservando bordes y texturas. El proyecto incluye:

- **Descarga y generación de datos**: scripts para obtener imágenes de ejemplo y crear versiones reducidas al 50 %.  
- **Módulos de interpolación**: bilineal y bicúbica (Keys, \(a=-0.5\)).  
- **Métricas de calidad**: PSNR y SSIM para cuantificar precisión y percepción.  
- **Notebook de experimentos**: pipeline completo con visualizaciones y tablas comparativas.  
- **CLI orquestador**: `__main__.py` con barra de progreso (`tqdm`), arte ASCII (`pyfiglet`) y colores (`colorama`).

---

## Requisitos

- Python ≥ 3.8  
- pip  
- Git  

---

## Instalación

```bash
git clone https://github.com/pedritastark/hr_image_reconstruction.git
cd hr_image_reconstruction

# 1. Crear y activar entorno virtual
python3 -m venv venv
source venv/bin/activate   # Unix/macOS
# .\venv\Scripts\activate  # Windows PowerShell

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Dar permisos de ejecución al CLI
chmod +x __main__.py

---

## Uso 

./__main__.py
