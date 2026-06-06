def make_progress_bar(progress: int, total: int, width: int) -> str:
    filled = int((progress / total) * width)
    current_progress = ">".rjust(filled, "=")
    percent = int((progress / total) * 100)
    prog_bar = f"[{current_progress:<{width}}] - {percent}% ({progress}/{total})"
    return prog_bar

def main():
    while True:
        try:
            progress = int(input("Enter current progress (0-100): ")) 
            total = int(input("Enter total: "))
            width = int(input("Enter width: "))
        except ValueError:
            print("Enter a integer")
            continue

        if progress < 0 or progress > total:
            print("Invalid values")
            continue
        break

    progress_bar = make_progress_bar(progress, total, width)
    print(progress_bar)
    
if __name__ == "__main__":
    main()