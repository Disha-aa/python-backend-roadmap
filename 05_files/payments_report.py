def get_report_payments() -> None:
    payments_dir = "git_roadmap/05_files/payments.txt"
    failed_payments_dir = "git_roadmap/05_files/failed_payments.txt"

    with open(payments_dir, "r") as file:
        with open(failed_payments_dir, "a") as recording:

            for line in file:

                data = [x for x in line.split(",")]
                status = data[-1].strip()

                if status == "failed":
                    recording.write(f"{line.strip()}\n")

    return


def print_failed_payments() -> None:
    failed_payments_dir = "git_roadmap/05_files/failed_payments.txt"

    print("\nFailed payments:")
    with open(failed_payments_dir, "r") as file:

        for line in file:
            print(line.strip())

    return


def main():
    get_report_payments()
    print_failed_payments()


if __name__ == "__main__":
    main()
