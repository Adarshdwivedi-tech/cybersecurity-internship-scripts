"""
Two-Factor Authentication (2FA) - TOTP Generator
----------------------------------------------------
Generates a random secret key and a Time-based One-Time Password
(TOTP), the same mechanism used by apps like Google Authenticator.

Requirements:
    pip install pyotp

Usage:
    Run the script. It prints a secret key (used to set up 2FA on
    an account) and the current valid OTP for that secret.
"""

import pyotp

# Generate a random base32 secret (this is what you'd normally
# scan as a QR code when enabling 2FA on an account)
secret = pyotp.random_base32()

totp = pyotp.TOTP(secret)

print("Secret Key:", secret)
print("Current OTP:", totp.now())
