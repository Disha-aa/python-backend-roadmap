def make_banner(banner: str, size: int) -> str:
    new_text = f" {banner} "
    padding = (size - len(new_text)) // 2
    half_banner = new_text.rjust(padding + len(new_text), "=")
    banner_result = half_banner.ljust(size, "=")

    return banner_result

def main():
    banner_name = input("Enter the name of the banner: ")
    while True:
        try:
            banner_size = int(input("Enter the size of the banner: "))
            if banner_size <= len(f" {banner_name} "):
                print(f"Size must be greater than {len(f' {banner_name} ')} (text with padding)")
                continue
            break
        except ValueError:
            print("Please enter a number")

    cli_banner = make_banner(banner_name, banner_size)
    print(cli_banner)

if __name__ == "__main__":
    main()