#!/usr/bin/env python3
"""
IMAGE RECONSTRUCTOR
by: Juan Sebastián Pedraza
"""

import subprocess
import sys
from tqdm import tqdm

# Librerías para ASCII art y color
from pyfiglet import Figlet
from colorama   import init, Fore, Style

# Inicializa colorama
init(autoreset=True)

def print_banner():
    f = Figlet(font="larry3d")
    banner = f.renderText("RhinoRes")
    print(Fore.CYAN + banner)
    print(Fore.YELLOW + Style.BRIGHT + "            by Juan Sebastián Pedraza\n" + Style.RESET_ALL)

# Define aquí cada tarea: descripción y comando a ejecutar

TASKS = [
    ("1. Obtener imágenes de ejemplo",
     ["python3", "scripts/generate_sample_images.py"]),
    ("2. Generar imágenes downsampled",
     ["python3", "scripts/downsample_images.py"]),
    ("3. Ejecutar notebook de experimentos",
     ["jupyter", "nbconvert",
      "--to", "notebook",
      "--execute", "notebooks/01_experiments.ipynb",
      "--output", "01_experiments_executed.ipynb",
      "--output-dir", "notebooks",
      "--ExecutePreprocessor.timeout=600"]),
]



def run_task(desc, cmd):
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    return p.returncode, p.stdout

def main():
    # Título grande
    print_banner()

    for desc, cmd in tqdm(TASKS, unit="task"):
        tqdm.write(f"\n↳ {desc}")
        code, out = run_task(desc, cmd)
        if code != 0:
            tqdm.write(Fore.RED + f"[✖] '{desc}' falló (código {code})")
            tqdm.write(out)
            sys.exit(code)
        else:
            tqdm.write(Fore.GREEN + f"[✔] '{desc}' completado.")

    print(Fore.GREEN + Style.BRIGHT + "\n✅  ¡Todas las tareas finalizadas con éxito!")
    print("   - Las imágenes de alta resolución están en `data/results/`")
    print("   - Notebook ejecutado en `notebooks/01_experiments_executed.ipynb`\n")

if __name__ == "__main__":
    main()
