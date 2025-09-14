from os.path import getctime, getmtime
from os import chdir
from pathlib import Path
import datetime

from rich.table import Table
from rich.progress import Progress

from hexid.match_file import match_file
from time import sleep

progress = Progress()

def resetTable():
    global recursiveResultsTable

    recursiveResultsTable = Table()
    
    recursiveResultsTable.add_column("ID")
    recursiveResultsTable.add_column("Filename")
    recursiveResultsTable.add_column("Date Modified", justify="right")
    recursiveResultsTable.add_column("Date Created", justify="right")
    recursiveResultsTable.add_column("Status", justify="right")

def process_files(search_dir, file_type, recursive, debug, console, plugins):
    """Process files in the specified directory and return a table of results."""
    chdir(search_dir)
    
    files = []
    folders = [search_dir]
    
    resetTable()
    
    if recursive == True:
        for path in search_dir.rglob("*"):
            if path.is_file():
                files.append(path)
            elif path.is_dir():
                folders.append(path)
    else:
        for path in search_dir.iterdir():
            if path.is_file():
                files.append(path)
            elif path.is_dir():
                folders.append(path)
                
    with Progress() as progress:
        task = progress.add_task("Scanning files for match...", total=len(files))   
                
        if recursive == True:
            for folder in folders:
                if folder.name == search_dir.name:
                    console.print("")
                    console.print("")
                    console.print(f"[bold blue]{folder.name}/ (root)[/]")
                else:
                    console.print(f"[bold blue]{folder.name}/[/]")
                
                resetTable()
                for idx, x in enumerate(files):
                    if x.parent == folder:
                        add_file(recursiveResultsTable, progress, task, file_type.lower(), debug, console, x, idx, plugins)
                
                console.print("")
                console.print(recursiveResultsTable)
                console.print("")
            
        if recursive == False:
            resetTable()
            for idx, x in enumerate(files):
                add_file(recursiveResultsTable, progress, task, file_type.lower(), debug, console, x, idx, plugins)

        progress.stop()
        console.print(f"Scan complete. Scanned [bold green]{len(files)}[/bold green] files in total.", style="bold white")
        console.print("")
        return recursiveResultsTable


def add_file(table, progress, task, file_type, debug, console, x, idx, plugins):
    with open(x, "rb") as file:
        hexdata = file.read(4096).hex()
                
        name = Path(x).name
                
        c_time = getctime(x)
        dt_c = datetime.datetime.fromtimestamp(c_time).strftime("%d %B %Y, %H:%M")
                
        m_time = getmtime(x)
        dt_m = datetime.datetime.fromtimestamp(m_time).strftime("%d %B %Y, %H:%M")
                
        if debug:
            console.print("")
            console.print(f"File: ", style="bold yellow", end="")
            console.print(f"{name}", style="bold green")
                    
            console.print(f"Raw File Creation Date: {c_time}", style="bold yellow")
            console.print(f"Formatted File Creation Date: {dt_c}", style="bold yellow")
                    
            console.print(f"Raw File Last Modified Date: {m_time}", style="bold yellow")
            console.print(f"Formatted File Last Modified Date: {dt_m}", style="bold yellow")
            console.print("")
            
        status = match_file(hexdata=hexdata, file_type=file_type.lower(), file_path=x, plugins=plugins)
                
        table.add_row(
            f"{idx}", # ID
            f"{name}", # Filename
            f"{dt_m}", # Date Modified
            f"{dt_c}", # Date Created
            f"{status}", # Status
        )
                
        progress.update(task, advance=1)
        if debug: 
            sleep(0.5)  # Slow down for debugging purposes