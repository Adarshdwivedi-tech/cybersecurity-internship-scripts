"""
Phishing Email Keyword Detector
------------------------------------
A basic heuristic scanner that checks pasted email text for common
phishing red-flag keywords (urgency, credential requests, fake
rewards, etc). This is NOT a substitute for real email security
tools - it's a simple demonstration of pattern-based detection.

Usage:
    Run the script and paste the suspicious email's text when
    prompted.
"""

email = input("Paste Email Text:\n")

keywords = [
    "urgent",
    "verify account",
    "click here",
    "password",
    "bank",
    "reward",
    "lottery",
]

found = False

for word in keywords:
    if word.lower() in email.lower():
        found = True
        print("Suspicious Keyword Found:", word)

if found:
    print("Possible Phishing Email")
else:
    print("Looks Safe (Manual Verification Needed)")
