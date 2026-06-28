def analyze_request(raw_logs: list[str]) -> dict:
    result_dict = {}
    for log in raw_logs:
        words = log.split()

        for endpoint in words:
            if endpoint.startswith("/api"):
                result_dict[endpoint] = result_dict.get(endpoint, 0) + 1
                break

    return result_dict


def get_raw_logs_from_file() -> list[str]:
    logs_dir = "git_roadmap/05_files/logs.txt"

    with open(logs_dir, "r") as file:
        raw_logs = [log for log in file]

    return raw_logs


def main():
    raw_logs = get_raw_logs_from_file()
    result = analyze_request(raw_logs)

    print(result)


if __name__ == "__main__":
    main()
