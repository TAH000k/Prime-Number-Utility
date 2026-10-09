# Prime Number Utility (PNU)

A command-line utility written in Python for checking prime numbers and generating sequences of prime numbers.

**Version:** `0.1` — Work in Progress
**Author:** Taha Noursalehi (`TAH000k`)

## Overview

Prime Number Utility (PNU) is a beginner-friendly Python project that provides an interactive terminal interface for working with prime numbers.

The project is currently under development. Some features and output formats may change in future releases.

## Features

* **Prime Checking:** Determine whether an integer is prime or composite.
* **Prime Generation:** Generate the first `N` prime numbers.
* **Multiple Output Modes:** Display prime numbers one by one or as a list.
* **File Export:** Save generated results in supported formats:

  * `.txt`
  * `.jsonc`
  * `.csv` (available in the one-by-one output mode)
* **Colored Terminal Output:** Use ANSI escape codes to make terminal messages easier to distinguish.
* **Interactive Menu:** Navigate the program through a simple command-line interface.

## Requirements

* Python 3.8 or later
* No third-party Python packages required

The program uses Python's built-in `math` module.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/TAH000k/Prime-Number-Utility.git
```

### 2. Navigate to the project directory

```bash
cd Prime-Number-Utility
```

### 3. Run the program

```bash
python main.py
```

If your system uses `python3` to launch Python, run:

```bash
python3 main.py
```

> Make sure the main script is named `main.py`, or replace the filename in the command with the actual filename.

## Usage

After launching the program, select an option from the main menu.

### Check a Number

Enter an integer to check whether it is prime or composite.

Numbers less than or equal to 1 are not considered prime or composite by this program.

### Generate Prime Numbers

Enter how many prime numbers you want to generate, choose an output mode, and optionally save the results to a file.

Available output modes:

1. **One by One:** Print each prime number with its index.
2. **In List:** Generate the numbers and display them as a Python list.

## How It Works

The primality-checking function uses trial division:

1. Numbers less than or equal to 1 are rejected as prime numbers.
2. The number 2 is handled as a special case.
3. Other even numbers are rejected.
4. Odd divisors are checked up to the integer square root of the number.

This approach avoids checking every integer up to the input number.

## Project Status

**Work in Progress**

Planned improvements may include:

* More robust input validation
* Improved file handling and output formatting
* Performance improvements for large prime-number sequences
* Additional features and tests

## Author

**Taha Noursalehi**
GitHub: [@TAH000k](https://github.com/TAH000k)

## License

This project is licensed under the MIT License. See the LICENSE file for details.
