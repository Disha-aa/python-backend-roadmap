import time


class RateLimiter:
    def __init__(self, limit: int = 5):
        self.limit = limit
        self.users = {}

    def is_allowed(self, user_id: int) -> bool:
        now = time.time()
        if user_id not in self.users:
            self.users[user_id] = []
        requests = self.users[user_id]

        self.users[user_id] = [req for req in requests if req + 60 > now]
        requests = self.users[user_id]

        if len(requests) >= self.limit:
            return False

        requests.append(now)
        return True


def limit_requests(limiter: RateLimiter):
    def decorator(func):
        def wrapper(*args, **kwargs):

            user_id = kwargs.get("user_id") or (args[0] if args else None)

            if user_id is None:
                return func(*args, **kwargs)

            if limiter.is_allowed(user_id):
                return func(*args, **kwargs)

            return {"ERROR": "Too many requests"}

        return wrapper

    return decorator


now = time.time()

limiter = RateLimiter(limit=5)


@limit_requests(limiter)
def fetch_user_data(user_id: int):
    return {"status": "success", "data": f"Data for user {user_id}"}


def main():
    user = 42
    for i in range(5):
        result = fetch_user_data(user)
        print(result)

    for i in range(5):
        result = fetch_user_data(user)
        print(result)
        time.sleep(2)


if __name__ == "__main__":
    main()
