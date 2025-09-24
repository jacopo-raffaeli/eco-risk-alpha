from pathlib import Path
import sys

# Set project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Define common directories
DATA_DIR = PROJECT_ROOT / "data"
MODEL_DIR = PROJECT_ROOT / "models"

# Optional: add src to sys.path so notebooks/scripts can import modules easily
sys.path.append(str(PROJECT_ROOT / "src"))
