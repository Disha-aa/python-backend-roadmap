def analyze_frequency(text: str) -> dict[str, int]:
    char_map = {}
    for char in text:
        current_count=char_map.get(char,0)
        char_map[char] = current_count + 1
    return char_map

def main():
    user_input = input("Enter a string: ").strip().lower()
    if not user_input:
        print("Please enter a string")
        return

    result = analyze_frequency(user_input)

    print("\nFrequency results:")
    for char, count in result.items():
        print(f"'{char}': {count}")

if __name__ == "__main__":
    main()