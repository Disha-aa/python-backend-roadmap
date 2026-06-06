def get_n_from_user() -> list[int]:
    while True:
        try:
            numbers = input("Enter numbers separated by spaces: ")
            original_list = [int(x) for x in numbers.split()]
            return original_list
        except ValueError:
            print("Please enter a number")
            continue

def main():
    numbers = get_n_from_user()
    unique_numbers = set(numbers)

    sum_of_unique_numbers = sum(unique_numbers)
    sum_of_numbers = sum(numbers)

    print(f"Unique elements: {unique_numbers}")
    print(f"Sum of all numbers: {sum_of_numbers}")
    print(f"Sum of unique numbers: {sum_of_unique_numbers}")
    print(f"The difference in the total amount:"
          f" {sum_of_numbers}-{sum_of_unique_numbers}={sum_of_numbers - sum_of_unique_numbers}")

if __name__ == "__main__":
    main()