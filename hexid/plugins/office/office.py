from pathlib import Path
import zipfile

def check_file(file_path: Path, file_type: str) -> int:
    """
    Optional plugin check for Microsoft Office files.
    """
    
    try:
        match file_type.lower():
            case "docx":
                if detect_office_zip(file_path, "word"):
                    return 1
            case "xlsx":
                if detect_office_zip(file_path, "xl"):
                    return 1
            case "pptx":
                if detect_office_zip(file_path, "ppt"):
                    return 1
        return 0
    except Exception:
        return -1
    
def detect_office_zip(file_path: str, doc_type: str) -> bool:
    """Check if a file is an office file based on its magic number and by checking the content of the ZIP archive."""
    
    if doc_type not in ["word", "xl", "ppt"]:
        return False
    
    if doc_type == "word":
        xml_file = "word/document.xml"
    elif doc_type == "xl":
        xml_file = "xl/workbook.xml"
    elif doc_type == "ppt":
        xml_file = "ppt/presentation.xml"
    
    if not zipfile.is_zipfile(file_path):
        return False
    
    with zipfile.ZipFile(file_path, "r") as zf:
        namelist = zf.namelist()
        
        if f"{xml_file}" in namelist and "[Content_Types].xml" in namelist:
            return True
    
    return False