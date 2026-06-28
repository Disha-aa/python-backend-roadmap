from collections import defaultdict
from collections.abc import Iterator


class LogAnalyzer:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_log(self) -> Iterator[str]:
        with open(self.file_path, "r") as file:
            for line in file:
                yield line

    def get_endpoint_stats(self) -> dict[str, int]:
        result_dict = defaultdict(int)

        for log in self.read_log():
            words = log.split()

            api_words = [w for w in words if w.startswith("/api")]
            if api_words:
                endpoint = api_words[0]
                result_dict[endpoint] += 1

        return dict(result_dict)


def main():
    log_analyzer = LogAnalyzer(file_path="logs.txt")

    result = log_analyzer.get_endpoint_stats()

    print(result)


if __name__ == "__main__":
    main()
