def load_env_file():
    settings = {}
    try:
        with open(".env", "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line == "" or line.startswith("#"):
                    continue
                if "=" in line:
                    key, value = line.split("=", 1)
                    settings[key] = value
    except FileNotFoundError:
        print("Archivo .env no encontrado")
    return settings

settings = load_env_file()

def get_setting(key, default=""):
    return settings.get(key, default)
