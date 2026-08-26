# MIT License
# Copyright (c) 2026 Taha Noursalehi (TAH000k)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
# of the Software, and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

# -------------------------------
# Import "math" library (helpful for finding prime numbers)
# -------------------------------
import math

# -------------------------------
# ANSI color codes for terminal output
# -------------------------------
RED = '\033[1;31m'
YELLOW = '\033[0;33m'
GREEN = '\033[92m'

RESET = '\033[0m'

# -------------------------------
# Start message
# -------------------------------
print("")
chap = (f"{RED}={YELLOW}={GREEN}={RESET}")
rast = (f"{GREEN}={YELLOW}={RED}={RESET}")
print(f"{chap} Prime Number Utility {GREEN}V-0.1{RESET} {rast}")
print(f"{13*" "}By TAH000k")

print(f"{9*" "}{YELLOW}(WORK IN PROGRESS){RESET}") # It will be deleted on the final version

# -------------------------------
# Define long error messages
# -------------------------------
num_range_err = ("is neither prime nor composite. "
                +"Prime numbers are defined only for natural numbers (> 1)")

positive_int_err = "Invalid input! Please enter a positive integer."

# -------------------------------
# Function to check if a number is prime
# -------------------------------
def is_prime(n):
    n = int(n)

    # Numbers <= 1 are not prime
    if n <= 1:
        return False

    # 2 is the only even prime number
    if n == 2:
        return True

    # Any other even number is not prime
    if n % 2 == 0:
        return False

    # Check divisibility from 3 up to sqrt(n), skipping even numbers
    for i in range(3, math.isqrt(n) + 1, 2):
        if n % i == 0:   # If divisible, it's not prime
            return False

    return True  # If no divisors found, it's prime

# -------------------------------
# Function to check if user wants to end the program
# -------------------------------
def ask_for_exit():
    while True: # Wihe loop for invalid input
        msg = input(f"{RED}Exit?{RESET} (y/n): ").strip().lower()
        
        if msg == "y":
            return(1) # Exit
        elif msg == "n":
            return(0) # Continue
        else:
            print(f"{RED}Enter 'y' or 'n'{RESET}") # Invalid input (ask again)

# -------------------------------
# Main program starts here
# -------------------------------

while True:
    print("")
    print("Choose an option:")
    print("1 : It's prime or not")       # Option 1: Check primality of a single number
    print("2 : Generate prime numbers")  # Option 2: Generate a list of prime numbers
    print(31*"-")
    #print(f"3 : {GREEN}V-0.1 PATCH NOTES{RESET}") # (What's new?)
    print("4 : About PNU")
    print(f"0 : {RED}EXIT{RESET}") # Exit
    
    option = input("- ")  # Read user choice as string
    print("")

    # -------------------------------
    # Option 1: Check if a single number is prime
    # -------------------------------
    if option == "1":
        try: # try-except method for value errors
            num = float(input("Enter a number: "))  # Read the number to check

            if (num <= 1) or (num%1 != 0):
                # Special cases (Not prime, neither composite)
                if num%1 != 0:
                    print(f"{YELLOW}{num} {num_range_err}{RESET}")
                else:
                    print(f"{YELLOW}{int(num)} {num_range_err}{RESET}")

            elif is_prime(num):
                # If function returns True → prime
                print(f"{int(num)} is a prime number.")
            else:
                # Otherwise → composite
                print(f"{int(num)} is a composite number.")

        except ValueError:
            print(f"{RED}Invalid input! Please enter a valid number.{RESET}")

    # -------------------------------
    # Option 2: Generate N prime numbers
    # -------------------------------
    elif option == "2":
        try:
            count = int(input("How many primes do you want? "))  # Number of primes to generate
            
            if count <= 0: # (Why?)
                print(f"{RED}{positive_int_err}{RESET}")

            else:
                # Output options
                print("")
                print("Choose an option for output:")
                print("1 : Print one by one")
                print("2 : Calculate all and print in a list")    
                
                opo = input("- ") # Get user input
                print("")

                if opo == "1":
                    mode = "OneByOne"
                elif opo == "2":
                    mode = "InList"

                # Ask for save
                save = input("Do you want to save numbers? (y/n): ").strip().lower()
                
                if save == "y":
                    # Save formats
                    print("Choose a format:")
                    
                    print("1. .txt")
                    print("2. .jsonc")
                    
                    if mode == "OneByOne":
                        print("3. .csv")
                        
                    save_format = input("- ").strip().lower()

                    # Create a .txt file
                    if save_format == "1":
                        # Create file
                        file = open(f"{count}_Primes_{mode}.txt", "w+")

                        # File title
                        file.write(f"=== Prime Number Utility V-0.1 ===\n")
                        file.write(f"{13*" "}By TAH000k\n\n")
                        file.write(f"First {count} Prime Numbers {mode}:\n\n")

                    # Create a .jsonc file    
                    elif save_format == "2":
                        # Create file
                        file = open(f"{count}_Primes_{mode}.jsonc", "w+")

                        # File title
                        file.write("// === Prime Number Utility V-0.1 ===\n")
                        file.write("//              By TAH000k\n\n")

                        # .jsonc syntax
                        file.write("{\n")
                        file.write(f"  \"First {count} Prime Numbers {mode}\":\n")
                        file.write("    ")

                    # Create a .csv file 
                    elif save_format == "3":
                        if mode == "OneByOne":
                            #Create file
                            file = open(f"{count}_Primes_{mode}.csv", "w+")
                            
                            # File title
                            file.write("\"Prime Number Utility V-0.1\"\n")
                            file.write(f"\"         By TAH000k\"\n\n")
                            file.write(f"\"First {count} Prime Numbers {mode}\"\n\n")
                            
                        else:
                            print(f"{RED}Enter 1 or 2.{RESET}")
                            save = "n" 
                            
                    else: # Invalid input
                        
                        if mode == "OneByOne":
                            print(f"{RED}Enter 1, 2 or 3.{RESET}")
                            
                        elif mode == "InList":
                            print(f"{RED}Enter 1 or 2.{RESET}")
                            
                        save = "n"

                print("")

                print(f"First {count} Prime Numbers {mode}:") # Title
                print("")

                # OneByOne method
                if opo == "1":
                    primes_found = 0   # Counter for how many primes found so far
                    candidate = 2      # Start checking from 2

                    # Keep looping until we find 'count' primes
                    while primes_found < count:
                        if is_prime(candidate):  # If candidate is prime

                            print(f"{primes_found+1}: {candidate}")  # Print with index

                            if save == "y":
                                # .txt
                                if save_format == "1":
                                    file.write(f"{primes_found+1}: {candidate}\n") # Write with index in the file

                                # .jsonc    
                                elif save_format == "2":
                                    if primes_found == 0: # Is it the first?
                                        file.write("  {")
                                        file.write(f"\n    \"{primes_found+1}\": {candidate}") # Write with index in the file
                                    else:
                                        file.write(f",\n    \"{primes_found+1}\": {candidate}") # Write with index in the file
                                
                                # .csv
                                elif save_format == "3":
                                    file.write(f"\"{primes_found+1}\",\"{candidate}\"\n") # Write with index in the file

                            primes_found += 1   # Increase counter
                        candidate += 1  # Move to next number

                    # .jsonc syntax    
                    if save == "y":
                        if save_format == "2":
                            file.write("\n  }\n")

                # InList method    
                elif opo == "2":
                    primes_found = 0   # Counter for how many primes found so far
                    candidate = 2      # Start checking from 2
                    prime_list = []    # Make a list for primes

                    print(f"\rGenerating...", end="", flush=True) # It will be deleted when all primes found

                    # Keep looping until we find 'count' primes
                    while primes_found < count:
                        if is_prime(candidate):  # If candidate is prime
                            prime_list.append(candidate)  # Add to the list
                            primes_found += 1   # Increase counter
                        candidate += 1  # Move to next number

                    print(f"\r{prime_list}") # Print the list

                    if save == "y":
                        file.write(f"{prime_list}\n") # Write list in the file

                # Invalid input
                else:
                    print(f"{RED}Enter 1 or 2.{RESET}")

                if save == "y":
                    # .txt
                    if save_format == "1":
                        file.write(f"\nCopyright (c) 2026 Taha Noursalehi (TAH000k)\n"
                                   +"PNU_V-0.1")
                        file.close() # Close file 
                        print("")
                        print(f"Primes saved in {count}_Primes_{mode}.txt")

                    # .jsonc   
                    elif save_format == "2":
                        file.write("}\n")
                        file.write(f"\n// Copyright (c) 2026 Taha Noursalehi (TAH000k)\n"
                                   +"// PNU_V-0.1")
                        file.close() # Close file 
                        print("")
                        print(f"Primes saved in {count}_Primes_{mode}.jsonc")
                    
                    # .csv
                    elif save_format == "3":
                        file.write(f"\n\"Copyright (c) 2026 Taha Noursalehi (TAH000k)\"\n"
                                   +"\"PNU_V-0.1\"")
                        file.close() # Close file 
                        print("")
                        print(f"Primes saved in {count}_Primes_{mode}.csv")

        except ValueError:
            print(f"{RED}{positive_int_err}{RESET}")

    # -------------------------------
    # Option 3: V-0.1 PATCH NOTES
    # -------------------------------
    elif option == "3":
        print(f"{GREEN}V-0.1{RESET} PATCH NOTES:\n"
              +"-------------------------------\n"
              +"You found an easter egg!\n"
              +"Nothing here yet...")

    # -------------------------------
    # Option 4: About PNU
    # -------------------------------
    elif option == "4":
        print("Our Team:")
        print("-------------------------------")
        print("Idea & Code: Taha Noursalehi (TAH000k)")
        print("UI QA: Nika Nikbakht") # <3
        print("\nTest & Advice:")
        print("Shaghayegh Maskout")
        print(f"{GREEN}YOUR NAME HERE!{RESET}") # YOUR NAME HERE!
        print("\nSpecial thanks: Danial Ebadi")
        print(f"\n{YELLOW}Copyright (c) 2026 Prime Number Utility{RESET}")

    # -------------------------------
    # Option 5(0): Exit
    # -------------------------------
    elif option == "0":
        break

    # -------------------------------
    # Invalid option handling
    # -------------------------------
    else:
        print(f"{RED}Enter 1, 2, 3, 4 or 0.{RESET}")  # If user entered something else

    # -------------------------------
    # Ask for exit
    # -------------------------------
    print("")

    if ask_for_exit():
        break
    else:
        continue
