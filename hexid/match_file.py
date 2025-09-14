def match_file(hexdata: str, file_type, file_path, plugins) -> str:
    for plugin in plugins:
        if hexdata and file_type in [file_type.lower() for file_type in plugin.get("file_types", [])]:
            for hex_pattern in plugin.get("hex", []):
                if hex_pattern in hexdata:
                    return "[bold green]MATCH"
        
        mod = plugin.get("plugin")
        if mod and hasattr(mod, "check_file"):
            # print(f"Running plugin for {plugin['name']} on {file_path}")
            result = mod.check_file(file_path, file_type)
            match(result):
                case 1:
                    return "[bold green]MATCH"
                case 2:
                    return "[bold yellow]POSSIBLE MATCH"
                case 3:
                    return "[bold red]NO MATCH"
                case _:
                    return "[bold red]NO MATCH"
    
    return "[bold red]NO MATCH"