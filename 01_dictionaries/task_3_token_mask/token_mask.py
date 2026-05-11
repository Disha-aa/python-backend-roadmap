def build_token_mask(text: str) -> dict[str, str]:

    unique_chars = set(text)
    token_mask = {}

    for char in unique_chars:
        if char == " ":
            continue
        token_mask[char] = text.replace(char, "")

    return token_mask


def main():

    while True:
        user_input = input("Enter a text: ").lower().strip()
        if not user_input:
            print("Error: Please enter a text")
            continue
        break

    masks = build_token_mask(user_input)

    print("\nToken Masking Results:")
    for char, mask in masks.items():
        print(f"{char} -> {mask}")

if __name__ == "__main__":
    main()