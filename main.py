import csv
import json
import math

# ANSI color codes
RED = "\033[1;31m"
YELLOW = "\033[0;33m"
GREEN = "\033[92m"
RESET = "\033[0m"

VERSION = "0.1.0"
AUTHOR = "Taha Noursalehi (TAH000k)"

# Error messages
NUM_RANGE_ERR = (
    "is neither prime nor composite. "
    "Prime numbers are defined for integers greater than 1."
)
POSITIVE_INT_ERR = "Invalid input! Please enter a positive integer."


def is_prime(n):
    """Return True if n is a prime integer."""
    if n <= 1:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    for divisor in range(3, math.isqrt(n) + 1, 2):
        if n % divisor == 0:
            return False

    return True


def ask_for_exit():
    """Ask whether the user wants to exit the program."""
    while True:
        answer = input(
            f"{RED}Exit?{RESET} (y/n): "
        ).strip().lower()

        if answer == "y":
            return True

        if answer == "n":
            return False

        print(f"{RED}Enter 'y' or 'n'.{RESET}")


def get_positive_integer(prompt):
    """Read a positive integer from the user."""
    try:
        value = int(input(prompt).strip())

        if value <= 0:
            raise ValueError

        return value

    except ValueError:
        print(f"{RED}{POSITIVE_INT_ERR}{RESET}")
        return None


def generate_primes(count):
    """Generate the first count prime numbers."""
    primes = []
    candidate = 2

    while len(primes) < count:
        if is_prime(candidate):
            primes.append(candidate)

        candidate += 1

    return primes


def save_primes(primes, mode, file_format):
    """Save prime numbers in the selected file format."""
    count = len(primes)
    filename = f"{count}_Primes_{mode}"

    if file_format == "1":
        filename += ".txt"

        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"=== Prime Number Utility V-{VERSION} ===\n")
            file.write(f"By {AUTHOR}\n\n")
            file.write(f"First {count} Prime Numbers ({mode}):\n\n")

            if mode == "OneByOne":
                for index, prime in enumerate(primes, start=1):
                    file.write(f"{index}: {prime}\n")
            else:
                file.write(f"{primes}\n")

            file.write(
                f"\nCopyright (c) 2026 {AUTHOR}\n"
                f"PNU_V-{VERSION}\n"
            )

    elif file_format == "2":
        filename += ".jsonc"

        data = {
            "version": VERSION,
            "mode": mode,
            "count": count,
            "primes": primes,
        }

        with open(filename, "w", encoding="utf-8") as file:
            file.write("// Prime Number Utility\n")
            file.write(f"// By {AUTHOR}\n")
            file.write(
                f"// Copyright (c) 2026 {AUTHOR}\n\n"
            )
            json.dump(data, file, indent=4)
            file.write("\n")

    elif file_format == "3" and mode == "OneByOne":
        filename += ".csv"

        with open(
            filename, "w", newline="", encoding="utf-8"
        ) as file:
            writer = csv.writer(file)
            writer.writerow(["Index", "Prime"])

            for index, prime in enumerate(primes, start=1):
                writer.writerow([index, prime])

    else:
        raise ValueError("Unsupported file format.")

    return filename


def check_number():
    """Handle the prime-checking option."""
    try:
        number = int(input("Enter an integer: ").strip())

    except ValueError:
        print(
            f"{RED}Invalid input! "
            f"Please enter a valid integer.{RESET}"
        )
        return

    if number <= 1:
        print(f"{YELLOW}{number} {NUM_RANGE_ERR}{RESET}")

    elif is_prime(number):
        print(f"{number} is a prime number.")

    else:
        print(f"{number} is a composite number.")


def generate_and_display():
    """Handle prime generation and optional file export."""
    count = get_positive_integer(
        "How many primes do you want? "
    )

    if count is None:
        return

    print("\nChoose an output mode:")
    print("1 : Print one by one")
    print("2 : Print all in a list")

    mode_choice = input("- ").strip()

    if mode_choice == "1":
        mode = "OneByOne"

    elif mode_choice == "2":
        mode = "InList"

    else:
        print(f"{RED}Enter 1 or 2.{RESET}")
        return

    save = input(
        "Do you want to save the numbers? (y/n): "
    ).strip().lower()

    if save not in ("y", "n"):
        print(f"{RED}Enter 'y' or 'n'.{RESET}")
        return

    file_format = None

    if save == "y":
        print("\nChoose a file format:")
        print("1 : .txt")
        print("2 : .jsonc")

        if mode == "OneByOne":
            print("3 : .csv")

        file_format = input("- ").strip()

        allowed_formats = (
            ("1", "2", "3")
            if mode == "OneByOne"
            else ("1", "2")
        )

        if file_format not in allowed_formats:
            print(f"{RED}Invalid file format selection.{RESET}")
            return

    print(f"\nGenerating the first {count} prime numbers...")
    primes = generate_primes(count)

    print(f"\nFirst {count} Prime Numbers ({mode}):\n")

    if mode == "OneByOne":
        for index, prime in enumerate(primes, start=1):
            print(f"{index}: {prime}")

    else:
        print(primes)

    if save == "y":
        try:
            filename = save_primes(
                primes, mode, file_format
            )

            print(f"\n{GREEN}Primes saved to {filename}{RESET}")

        except OSError as error:
            print(f"{RED}Could not save the file: {error}{RESET}")

        except ValueError as error:
            print(f"{RED}{error}{RESET}")


def show_patch_notes():
    """Display the current version's patch notes."""
    print(
        f"{GREEN}V-{VERSION} PATCH NOTES{RESET}\n"
        "-------------------------------\n"
        "You found an easter egg!\n"
        "More updates coming soon..."
    )


def show_about():
    """Display project credits."""
    print("About Prime Number Utility")
    print("-------------------------------")
    print(f"Version: {VERSION}")
    print(f"Idea & Code: {AUTHOR}")
    print("UI QA: Nika Nikbakht")
    print("\nTest & Advice:")
    print("Shaghayegh Maskout")
    print("Danial Ebadi")
    print(f"\n{YELLOW}Copyright (c) 2026 PNU{RESET}")


def main():
    """Run the main interactive menu."""
    print()
    print(
        f"{RED}={YELLOW}={GREEN}={RESET} "
        f"Prime Number Utility V-{VERSION} "
        f"{GREEN}={YELLOW}={RED}={RESET}"
    )
    print(f"{' ' * 13}By TAH000k")
    print(f"{' ' * 9}{YELLOW}(WORK IN PROGRESS){RESET}")

    while True:
        print("\nChoose an option:")
        print("1 : Check whether a number is prime")
        print("2 : Generate prime numbers")
        print("3 : Patch notes")
        print("4 : About PNU")
        print(f"0 : {RED}EXIT{RESET}")
        print("-" * 31)

        option = input("- ").strip()
        print()

        if option == "1":
            check_number()

        elif option == "2":
            generate_and_display()

        elif option == "3":
            show_patch_notes()

        elif option == "4":
            show_about()

        elif option == "0":
            print("Goodbye!")
            break

        else:
            print(
                f"{RED}Enter 1, 2, 3, 4 or 0.{RESET}"
            )
            continue

        print()

        if ask_for_exit():
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
    