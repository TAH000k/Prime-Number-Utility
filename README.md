# Prime Number Utility (PNU)

A command-line utility written in Python for checking prime numbers and generating sequences of prime numbers.

**Version:** 0.1.0
**Status:** Work in Progress
**Author:** Taha Noursalehi ([TAH000k](https://github.com/TAH000k))

## Overview

Prime Number Utility (PNU) is a lightweight command-line application designed to perform basic prime number operations. It allows users to check whether an integer is prime and generate sequences of prime numbers using different output modes.

The project is built entirely with Python's standard library and does not require any third-party packages.

## Features

* **Prime Checking:** Determine whether an integer is prime.
* **Prime Generation:** Generate prime numbers up to a specified limit.
* **Multiple Output Modes:** Display generated prime numbers one by one or as a list.
* **File Export:** Save results in supported formats:

  * `.txt`
  * `.jsonc`
  * `.csv` (available in OneByOne mode only)
* **Colored Terminal Output:** Use ANSI escape sequences to improve readability.
* **Interactive Menu:** Access the program's features through a menu-driven interface.

## Requirements

* Python 3.8 or later
* No third-party dependencies

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/TAH000k/Prime-Number-Utility.git
```

### 2. Navigate to the Project Directory

```bash
cd Prime-Number-Utility
```

### 3. Run the Program

```bash
python main.py
```

On systems where Python 3 is invoked using `python3`, run:

```bash
python3 main.py
```

## Usage

Launch the program and follow the interactive menu to select an operation.

### Check a Number

Enter an integer to check whether it is prime.

A prime number is an integer greater than 1 that has exactly two positive divisors: 1 and itself.

Integers less than or equal to 1 are neither prime nor composite.

### Generate Prime Numbers

Choose the prime generation option and provide the requested limit.

The program supports two output modes:

* **OneByOne:** Display prime numbers individually.
* **InList:** Display the generated prime numbers together as a list.

Depending on the selected mode and export format, results can also be saved to a file.

## How It Works

Prime checking uses the trial division method.

The algorithm follows these basic steps:

1. Numbers less than or equal to 1 are classified as non-prime.
2. The number 2 is handled as a special case.
3. Even numbers greater than 2 are rejected as prime.
4. Odd divisors are checked up to the integer square root of the number.
5. If no divisor is found, the number is prime.

Checking divisors only up to the square root reduces the number of operations required compared with checking every possible divisor.

## Project Status

**Work in Progress**

PNU is an ongoing project. Potential future improvements include:

* More robust input validation and error handling
* Improved file handling and output formatting
* Performance optimizations
* Additional features and automated tests

## Author

**Taha Noursalehi** — [@TAH000k](https://github.com/TAH000k)

## License

This project is licensed under the [MIT License](LICENSE).
