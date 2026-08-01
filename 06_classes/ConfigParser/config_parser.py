"""this script is needed for reading and updating settings in the config file"""

from pathlib import Path


class ConfigError(Exception):
    """custom exception for config's errors"""


class ConfigLoader:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self._config = {}

        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                for line in f:
                    key, value = line.strip().split("=", 1)
                    self._config[key.strip().upper()] = value
        except FileNotFoundError:
            raise ConfigError(f"Config file not found: {self.file_path}")
        except Exception as e:  # noqa: BLE001
            raise ConfigError(f"Error: {e}")

    def get_setting(self, option: str) -> str | None:
        return self._config.get(option)

    def update_config(self, key: str, value: str) -> None:
        clean_key = key.strip().upper()
        clean_val = value.strip()
        self._config[clean_key] = clean_val

        try:
            with open(self.file_path, "w", encoding="utf-8") as f:
                for k, v in self._config.items():  # noqa: FURB122
                    f.write(f"{k}={v}\n")
        except Exception:  # noqa: BLE001
            raise ConfigError(f"Config file not found: {self.file_path}")


def main():
    CONFIG_DIR = Path(__file__).resolve().parent / "config.txt"

    config = ConfigLoader(CONFIG_DIR)

    setting = config.get_setting(
        "PORT"
    )  # you can write here database, url, debug and max_connections (this is basic settings in config.txt)
    print(setting)

    config.update_config("latency", "10")  # you can write here what do you want


if __name__ == "__main__":
    main()
