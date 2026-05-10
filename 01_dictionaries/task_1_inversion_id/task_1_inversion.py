def get_n_from_user() -> list[int]:
    while True:
        try:
            n = input("Enter a number: ").strip(",")
            numbers=[int(x) for x in n.split(",")]
            if any(x<=0 for x in numbers):
                print("Error: Please enter a positive integer")
                continue
            return numbers
        except ValueError:
            print("Error: Please enter an integer number")
            continue

def build_inverted_index(numbers: list[int]) -> dict[int, dict[int, int]]:
    dictionary = {
        n: {x: n - x + 1 for x in range(1, n + 1)}
        for n in numbers
    }

    return dictionary

def main():
    numbers = get_n_from_user()
    result = build_inverted_index(numbers)
    print(result)

if __name__ == "__main__":
    main()