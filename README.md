# 🔐 Password Guessing Simulator

A Python-based password guessing simulator that demonstrates how dictionary attacks and brute-force algorithms work.

The project was created to explore Python programming, password security, algorithm performance, and execution time.

## Features

- **Password validation:** Accepts passwords between 2 and 6 characters.
- **Supported characters:** Lowercase letters (a–z) and digits (0–9).
- **Dictionary search:** Checks passwords against the RockYou wordlist.
- **Brute-force simulation:** Generates possible combinations using Python's `itertools.product()`.
- **Progress tracking:** Displays the percentage of combinations tested.
- **Performance measurement:** Measures total execution time and counts password attempts.

## How It Works

The program uses two methods:

**1. Dictionary Search**

The program first checks the entered test password against the RockYou wordlist.

If a match is found, the program displays the number of attempts.

**2. Brute-Force Simulation**

If the password is not found in RockYou, the program generates combinations containing 2–6 characters using lowercase letters and numbers.

Each combination is compared with the simulated password until a match is found.

The program also displays search progress and execution time.

## Requirements

- Python 3.10 or newer (recommended)
- RockYou password wordlist

No third-party Python packages are required.

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/Sixten1/Password-Solver.git
```

**2. Download the RockYou wordlist**

The RockYou wordlist is not included in this repository.

Download SecLists from:

https://github.com/danielmiessler/SecLists

Navigate to:

`Passwords/Leaked-Databases/`

Extract the RockYou archive and place `rockyou.txt` in your project folder.

**3. Run the program**

```bash
python main.py
```

## Project Structure

```text
password-guessing-simulator/
├── main.py
├── README.md
├── .gitignore
└── rockyou.txt   # Download separately
```

## Example Output

```text
Write your password: abc123

couldnt find password... tried 14344391 passwords
Progress: 10.25%
Progress: 20.50%
...

Ditt lösenord är abc123
Tried 1234567 passwords
Exekveringstid: 12.3456 sekunder
```

*The output above is illustrative. Actual attempts, progress updates, and execution times will vary.*

## Technologies Used

- Python
- itertools
- string
- time
- File handling
- Object-oriented programming (OOP)

## Limitations

- Only supports passwords containing 2–6 characters.
- Input is converted to lowercase.
- Does not support special characters.
- Exhaustive combination searches can take a long time.
- Requires a local copy of RockYou.
- Designed for local simulations, not real account authentication.

## Disclaimer

This project is intended for educational purposes only.

It demonstrates password-guessing concepts using simulated passwords supplied by the user. It should not be used to access accounts or systems without authorization.

## Future Improvements

- Improved performance benchmarking
- Better progress reporting
- Additional unit tests
- Improved error handling
- More detailed statistics