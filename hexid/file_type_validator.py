from sys import exit

def file_type_validator(file_type, plugins, console) -> str:
    """Validates the file type input by the user."""
    
    valid_file_types = []
    
    for plugin in plugins:
        for file_type in plugin.get("file_types", []):
            if file_type.lower() not in valid_file_types:
                valid_file_types.append(file_type.lower())    

    if file_type.lower() not in valid_file_types:
        console.print()
        console.print(" ERROR ", style="bold red reverse", end="")
        console.print(f" Invalid file type. Choose from the following:")
        console.print(f"{', '.join(valid_file_types)}", style="blue")
        console.print()
        exit()
    
    return file_type.lower()