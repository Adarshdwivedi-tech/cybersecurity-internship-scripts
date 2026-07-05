"""
File Backup & Restoration
------------------------------
A simple demonstration of creating a backup copy of a file and
restoring it later. This models the basic idea behind backup
strategies used in data security and disaster recovery.

Usage:
    Place a file named important.txt in the same folder, then run
    this script. It will create a backup copy and then restore it
    to a new file.
"""

import shutil

# ---------- CREATE BACKUP ----------

source = "important.txt"
backup = "backup_important.txt"

shutil.copy(source, backup)
print("Backup Created")

# ---------- RESTORE FROM BACKUP ----------

backup = "backup_important.txt"
restore = "restored.txt"

shutil.copy(backup, restore)
print("File Restored")
