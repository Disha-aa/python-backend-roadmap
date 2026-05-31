def require_role(required_role: str):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            user = kwargs.get('user')
            if user and (user.get('role') == required_role or user.get('role') == 'admin'):
                return func(*args, **kwargs)
            else:
                raise PermissionError(f"Access denied. Required role: {required_role}")
        return wrapper
    return real_decorator

@require_role("premium")
def execute_secure_search(query: str, user: dict) -> str:
    return f"Result of search: {query}"

def main():
    USER_ANNA = {"name": "Anna", "role": "guest"}
    USER_MAX = {"name": "Max", "role": "premium"}
    USER_BOSS = {"name": "Oleg", "role": "admin"}
    while True:
        user_input = input("Enter your name (Anna, Max or Boss or '0' to stop): ").lower().strip()
        if user_input == "0":
            return
        
        if user_input == "max":
            user = USER_MAX
        elif user_input == "anna":
            user = USER_ANNA
        elif user_input == "boss":
            user = USER_BOSS
        else:
            print("Error: invalid user")
            continue
        
    
        try:
            result = execute_secure_search("Python", user = user)
            print(result)
        except PermissionError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()