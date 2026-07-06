# Cybersecurity Internship Scripts

Python scripts written during a 15-day Cybersecurity & IoT internship (June 2026), covering practical security concepts: encryption, hashing, authentication, and basic threat detection.

## Scripts

| File | Description |
|---|---|
| `password_strength_checker.py` | Scores a password's strength based on length, casing, digits, and special characters |
| `fernet_encryption.py` | Encrypts and decrypts a text file using symmetric (Fernet) encryption |
| `sha256_file_comparator.py` | Generates SHA-256 hashes of two files and checks if they're identical (file integrity verification) |
| `2fa_totp_generator.py` | Generates a 2FA secret key and time-based one-time password (TOTP), the mechanism behind apps like Google Authenticator |
| `backup_and_restore.py` | Demonstrates basic file backup creation and restoration |
| `phishing_email_detector.py` | Scans pasted email text for common phishing red-flag keywords |


## Arduino / IoT

| File | Description |
|---|---|
| `led_blink.ino` | Alternates 3 LEDs (pins 3, 4, 5) on and off every second. Built and tested in Tinkercad simulation, then verified on real Arduino Uno hardware with a simplified LED circuit. |

## Requirements

Most scripts use only Python's standard library. Two require external packages:

```bash
pip install cryptography pyotp
```

- `fernet_encryption.py` requires `cryptography`
- `2fa_totp_generator.py` requires `pyotp`

## Usage

Each script is standalone. Run any of them directly:

```bash
python3 password_strength_checker.py
```

For `fernet_encryption.py`, place a `sample.txt` file in the same folder before running.
For `backup_and_restore.py`, place an `important.txt` file in the same folder before running.
`led_blink.ino` requires the Arduino IDE (or Tinkercad's simulator) and an Arduino Uno with 3 LEDs wired to pins 3, 4, and 5, each with a current-limiting resistor.

## Notes

These scripts were built during a hands-on internship as an introduction to core security concepts — encryption, hashing, authentication, and basic phishing detection heuristics. They're intentionally simple and meant as learning/demonstration tools rather than production-grade security software.
