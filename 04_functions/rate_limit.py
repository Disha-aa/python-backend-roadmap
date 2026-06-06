import time
from typing import Union


def rate_limit(max_calls: int, period_seconds: int) -> callable:
    """
    Limits the number of function calls to max_calls per period_seconds
    Uses a short-circuit condition to isolate call counters
    """

    def decorator(func: callable) -> callable:
        calls_history = []

        def wrapper(*args: any, **kwargs: any) -> Union[any, dict]:
            now = time.time()

            calls_history[:] = [t for t in calls_history if t > now - period_seconds]
            if len(calls_history) < max_calls:
                calls_history.append(now)
                result = func(*args, **kwargs)

                return result
            else:
                oldest_call = calls_history[0]
                wait_time = int(period_seconds - (now - oldest_call))
                return {"error": "Too many requests", "retry_after": f"{wait_time}"}

        return wrapper

    return decorator


@rate_limit(max_calls=2, period_seconds=10)
def execute_secure_search(query: str) -> str:
    return f"Result of search: {query}"


def main():
    while True:

        user_input = input("Enter your query (or '0' to stop): ")

        if user_input == "0":
            return

        result = execute_secure_search(user_input)
        print(result)


if __name__ == "__main__":
    main()
