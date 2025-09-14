from pathlib import Path

def check_file(file_path: Path, file_type: str) -> int:
    """
    Optional plugin check for text files.
    """
    
    try:    
        if detect_text_file(file_path) == True:
            return 2
        else:
            return 0
    except Exception:
        return -1

def detect_text_file(file_path: Path) -> bool:
    try:
        with open(Path(file_path), "rb") as f:
            sample = f.read(4096)
            if sample.startswith(b'\xef\xbb\xbf'):
                sample = sample[3:]
            sample.decode("utf-8")
            return True
    except UnicodeDecodeError:
        return False