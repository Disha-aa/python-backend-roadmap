def reverse_path(path: str) -> str:
    path_log = path.split("/")
    reversed_path = path_log[1:][::-1]

    return path_log[0] + "/" +"/".join(reversed_path )

def normalize_path(path: str) -> str:
    parts = [part.strip() for part in path.split("/") if part.strip()]
    return "/" + "/".join(parts)

def main():
    print("Enter '0' to stop")
    while True:
        user_input = input("Enter a valid log (ex: '/api/v1/users/profile'): ")
        if user_input == "0":
            return
        elif not user_input or not user_input.startswith("/"):
            print("Error: invalid log")
            continue
        elif len(user_input.strip("/")) == 0:
            print("Error: empty path")
            continue

        normal_log = normalize_path(user_input)
        result = reverse_path(normal_log)
        print(result)

if __name__ == "__main__":
    main()