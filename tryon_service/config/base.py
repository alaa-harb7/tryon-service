from pathlib import Path

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Configuration Directory
CONFIG_DIR = PROJECT_ROOT / "configs"

# Environment File
ENV_FILE = PROJECT_ROOT / ".env.example"

# Logs Directory
LOGS_DIR = PROJECT_ROOT / "logs"

# Temporary Files
TEMP_DIR = PROJECT_ROOT / "temp"

# Uploaded Files
UPLOADS_DIR = PROJECT_ROOT / "uploads"

# Generated Images
GENERATED_DIR = PROJECT_ROOT / "generated"

# Cache Directory
CACHE_DIR = PROJECT_ROOT / "cache"