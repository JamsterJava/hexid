from pathlib import Path
import json
import importlib.util

base_dir = Path(__file__).parent

plugins_dir = base_dir / "plugins"
plugins = []

def load_plugins():
    """Load plugins from the plugins directory."""
    plugins.clear()
    
    for plugin_folder in plugins_dir.iterdir():
        if plugin_folder.is_dir():
            json_file = plugin_folder / f"{plugin_folder.name}.json"
            plugin_file = plugin_folder / f"{plugin_folder.name}.py"
            
            data = {}
            if json_file.exists():
                with open(json_file, "r") as jf:
                    data = json.load(jf)
                    
            plugin = None
            if plugin_file.exists():
                try:
                    spec = importlib.util.spec_from_file_location(plugin_folder.name, plugin_file)
                    module = importlib.util.module_from_spec(spec)
                    spec.loader.exec_module(module)
                    plugin = module
                except Exception as e:
                    print(f"Failed to load plugin {plugin_file}: {e}")
                
            plugins.append({
                "name": plugin_folder.name,
                "description": data.get("description", ""),
                "author": data.get("author", ""),
                "file_types": data.get("file_types", []),
                "hex": data.get("hex", []),
                "plugin": plugin
            })
            
    return plugins