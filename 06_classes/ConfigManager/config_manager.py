from collections.abc import Iterator


class ConfigManager:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.__config = dict()

    def _read_log(self) -> Iterator[str]:
        with open(self.file_path, "r") as file:
            for line in file:
                yield line

    def _parse_env(self):
        for line in self._read_log():
            parse_logs = line.strip().split("=")

            if len(parse_logs) == 2:
                key, value = parse_logs
                self.__config[key] = value

    @property
    def port(self) -> int:
        return int(self.__config.get("PORT", 8000))

    @port.setter
    def port(self, new_port: int):
        if not isinstance(new_port, int):
            raise ValueError("Port must be an integer")
        if new_port <= 0 or new_port > 65535:
            raise ValueError("Incorrect port range")

        self.__config["PORT"] = str(new_port)

    @property
    def db_url(self) -> str:
        url = self.__config.get("DB_URL")
        if url is None:
            raise KeyError("[ERROR] db_url is missing")
        return url

    @property
    def debug(self) -> bool:
        return self.__config.get("DEBUG", "False") == "True"


def main():
    config = ConfigManager("config.env")
    config._parse_env()

    port = config.port
    db_url = config.db_url
    debug = config.debug

    print(port)
    print(db_url)
    print(debug)


if __name__ == "__main__":
    main()
