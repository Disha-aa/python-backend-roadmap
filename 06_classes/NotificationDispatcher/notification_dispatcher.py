from pathlib import Path


class BaseNotification:
    def send(self, receiver: str, message: str, file_path: Path):
        raise NotImplementedError


class EmailNotification(BaseNotification):
    def send(self, receiver: str, message: str, file_path: Path) -> None:
        with open(file_path, "a") as f:
            f.write(f"[EMAIL] Sent to {receiver}: {message}\n")


class SMSNotification(BaseNotification):
    def send(self, receiver: str, message: str, file_path: Path) -> None:
        with open(file_path, "a") as f:
            f.write(f"[SMS] Sent to {receiver}: {message}\n")


class TelegramNotification(BaseNotification):
    def send(self, receiver: str, message: str, file_path: Path) -> None:
        with open(file_path, "a") as f:
            f.write(f"[Telegram] Sent to {receiver}: {message}\n")


class NotificationDispatcher:
    def __init__(self, file_path: Path):
        self.file_path = file_path

    def send_bulk(self, notification: list[dict]) -> None:
        for data_dict in notification:
            channel = data_dict.get("channel")
            receiver = data_dict.get("receiver")
            message = data_dict.get("message")

            if not channel:
                continue

            try:
                channel.send(receiver, message, self.file_path)
            except NotImplementedError as e:
                print(f"[ERROR] {e}")


def main():
    CURRENT_DIR = Path(__file__).resolve().parent
    DELIVERY_PATH = CURRENT_DIR / "delivery_status.log"

    notification_list = [
        {
            "channel": EmailNotification(),
            "receiver": "disha@mail.com",
            "message": "hello",
        },
        {
            "channel": SMSNotification(),
            "receiver": "+48123456789",
            "message": "my name is disha",
        },
        {
            "channel": TelegramNotification(),
            "receiver": "@disha",
            "message": "how are you",
        },
    ]

    dispatcher = NotificationDispatcher(DELIVERY_PATH)
    dispatcher.send_bulk(notification_list)


if __name__ == "__main__":
    main()
