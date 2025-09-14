import click
from pathlib import Path
from sys import exit

from rich.console import Console

from hexid.file_type_validator import file_type_validator
from hexid.process_files import process_files
from hexid.plugins import load_plugins

# Load file type definitions from the plugins directory
plugins = load_plugins()

# Define console for rich output
console = Console(record=True)
error_console = Console(stderr=True, style="bold red")

# Main command-line interface function

@click.command()
@click.option("-d", "--dir", default="./", help="The directory to search in.")
@click.option("-f", "--file-type", help="The extension to match to.", required=True)
@click.option("-r", "--recursive/--non-recursive", default=True, help="Scans recursively (i.e. in subfolders).")
@click.option("--debug/--no-debug", default=False, help="Prints extra information for debugging purposes.")
@click.option("--show-plugins/--do-not-show-plugins", default=False, help="Prints information about the loaded plugin.")

def main(dir, file_type, recursive, debug, show_plugins):
    """Simple tool that searches a directory for files of the specified type. Matches by file data, not the extension."""
    
    if show_plugins:
        for plugin in plugins:
            console.print()
            
            console.print("Name: ", end="", style="bold blue")
            console.print(plugin["name"])
            
            console.print("Description: ", end="", style="bold blue")
            console.print(plugin["description"])
            
            console.print("Author: ", end="", style="bold blue")
            console.print(plugin["author"])
            
            console.print("Matches the following file types: ", end="", style="bold blue")
            console.print(", ".join(plugin["file_types"]))
                
            console.print()
        exit()
    
    search_dir = Path(dir).resolve()
    if not search_dir.is_dir():
        error_console.print(f"ERROR: The directory '{dir}' does not exist or is not a directory.")
        exit()
    
    # Validates that the extension provided is valid and can be matched against.
    file_type_validator(file_type.lower(), plugins, console)
    
    console.print("")
    console.print(f"Searching in directory: {dir}", style="bold white")
    
    console.print("Matching files that correspond to the following file format: ", style="bold white", end="")
    console.print(f"{file_type.lower()}", style="bold green")
    
    console.print("")
    results = process_files(
        search_dir=search_dir, 
        file_type=file_type.lower(),
        recursive=recursive,
        debug=debug,
        console=console,
        plugins=plugins
    )
    
    if recursive == False:
        console.print(results)
        
    if file_type == "txt":
        console.print("")
        console.print("Note: ", style="bold white", end="")
        console.print("POSSIBLE MATCH ", style="bold yellow", end="")
        console.print("is displayed for text files. Text files do not have a universal signature, so they cannot be reliably matched.", style="white")
        console.print("Certain files may be matched incorrectly as they are valid text, e.g. some DOS programs, some XML files etc.", style="white")
        console.print("")
    
if __name__ == '__main__':
    main()