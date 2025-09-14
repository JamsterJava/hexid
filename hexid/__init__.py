# hexid/__init__.py

from hexid.file_type_validator import file_type_validator
from hexid.process_files import process_files, resetTable, add_file
from hexid.plugins import load_plugins
from hexid.match_file import match_file
from hexid.cli import main