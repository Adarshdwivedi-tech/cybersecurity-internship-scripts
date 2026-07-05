"""
Password Strength Checker
--------------------------
Checks a user-entered password against 5 basic security criteria
and scores it as Weak, Medium, or Strong.

Criteria checked:
1. Minimum length of 8 characters
2. Contains an uppercase letter
3. Contains a lowercase letter
4. Contains a digit
5. Contains a special character
"""

import re

password = input("Enter Password: ")
score = 0

if len(password) >= 8:
    score += 1
if re.search(r"[A-Z]", password):
    score += 1
if re.search(r"[a-z]", password):
    score += 1
if re.search(r"\d", password):
    score += 1
if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1

if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Medium Password")
else:
    print("Strong Password")
