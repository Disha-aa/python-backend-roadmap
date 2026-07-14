from pathlib import Path


class LogStreamer:
    def __init__(self, file_path: Path):
        self.file_path = file_path
        self.target_statuses = ["CRITICAL", "ERROR", "WARNING", "MALWARE"]

    def stream_suspicious_logs(self):
        with open(self.file_path, "r", encoding="utf-8") as f:
            for line in f:
                found_statuses = [
                    status for status in self.target_statuses if status in line
                ]

                if found_statuses:
                    yield found_statuses, line.strip()


def main():
    CURRENT_DIR = Path(__file__).resolve().parent
    LOG_PATH = CURRENT_DIR / "chat_logs.txt"

    streamer = LogStreamer(LOG_PATH)

    for statuses, bad_log in streamer.stream_suspicious_logs():
        print(f"Triggered status: {statuses}")
        print(f"A threat has been detected: {bad_log} ")


if __name__ == "__main__":
    main()
