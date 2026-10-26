# Password Safety Checker

A tiny beginner-friendly cybersecurity project that checks basic password characteristics and generates random passwords.

## Features
- Checks length, lowercase/uppercase letters, digits, and symbols.
- Flags a small built-in list of common passwords.
- Gives a simple rating: Very weak, Weak, Moderate, or Strong.
- Generates passwords with Python's `secrets` module.
- Runs locally and requires no third-party packages.

## Requirements
- Python 3.8 or newer
- No external libraries

## Run
1. Download or clone this project.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python PasswordSafetyChecker.py
   ```

4. Choose `1` to check a password or `2` to generate one.

## Dataset
No external dataset is used. The program contains a tiny illustrative set of common passwords directly in the source code. It is not a comprehensive password blacklist.

## Limitations
- This is an educational demonstration, not a professional password audit.
- It does not check whether a password has appeared in a data breach.
- The strength rating is a simple rule-based estimate and can be wrong.
- Do not enter a real password into a program unless you trust the code and environment.

## GitHub
After creating a repository on GitHub, add its URL here: `https://github.com/YOUR-USERNAME/password-safety-checker`
