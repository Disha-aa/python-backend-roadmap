def get_clean_analytics(logs: list) -> list:
    filtered_logs = filter(lambda log: log["count"] > 0, logs)
    return sorted(filtered_logs, key=lambda log: log["count"], reverse=True)


search_logs = [
    {
        "timestamp": 1717934400,
        "user": {"name": "Disha", "role": "student"},
        "request": {"query": "python deco", "category": "backend"},
        "count": 12,
    },
    {
        "timestamp": 1717934500,
        "user": {"name": "Anna", "role": "junior"},
        "request": {"query": "sql join", "category": "databases"},
        "count": 0,
    },
    {
        "timestamp": 1717934600,
        "user": {"name": "Disha", "role": "student"},
        "request": {"query": "yield explained", "category": "backend"},
        "count": 45,
    },
    {
        "timestamp": 1717934700,
        "user": {"name": "Guest_1", "role": "anonymous"},
        "request": {"query": "how to hack nasa", "category": "security"},
        "count": 0,
    },
    {
        "timestamp": 1717934800,
        "user": {"name": "Anna", "role": "junior"},
        "request": {"query": "fastapi tutorial", "category": "web"},
        "count": 90,
    },
]
result = get_clean_analytics(search_logs)

print(result)
