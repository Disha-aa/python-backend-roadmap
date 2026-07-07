import secrets
import time


class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id: int) -> str:
        expire_time = time.time() + 60
        token = secrets.token_hex(16)

        self.sessions[token] = (user_id, expire_time)

        return token

    def is_valid(self, token: str) -> bool:
        if token not in self.sessions:
            return False

        now = time.time()
        user_id, expire_time = self.sessions[token]

        if expire_time < now:
            del self.sessions[token]
            return False

        return True

    def delete_session(self, token: str) -> None:
        self.sessions.pop(token, None)

    def clean_expired_sessions(self) -> int:
        now = time.time()
        expired_tokens = []

        for token, (user_id, expire_time) in self.sessions.items():
            if expire_time < now:
                expired_tokens.append(token)

        for token in expired_tokens:
            del self.sessions[token]

        return len(expired_tokens)


def main():
    session = SessionManager()

    token = session.create_session(777)
    is_valid = session.is_valid(token)

    print(f"Token was created: {token}")
    if is_valid:
        print("Your token is valid")
    else:
        print("Your token isn't valid")

    dead_token = session.create_session(666)
    session.sessions[dead_token] = (999, time.time() - 100)

    clean_expired = session.clean_expired_sessions()

    print(f"Number of deleted expired sessions: {clean_expired}")


if __name__ == "__main__":
    main()
