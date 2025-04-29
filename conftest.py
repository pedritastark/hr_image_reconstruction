import sys
from pathlib import Path

# Añadir src/ al inicio de sys.path para que pytest lo reconozca
sys.path.insert(0, str(Path(__file__).parent / 'src'))
