import os

def ensure_dir(path):
    """Create folder if it doesn't exist"""
    os.makedirs(path, exist_ok=True)
