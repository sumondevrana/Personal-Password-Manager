🔐 Personal Password Manager

A simple command-line password manager built in Python. Save, view, generate, update, and delete passwords for different websites — all stored locally in a text file.

> ⚠️ **Note:** This is a beginner/learning project. Passwords are stored in **plain text** (not encrypted). Do not use this to store real, sensitive passwords. See [Future Improvements](#-future-improvements) for how to make it production-safe.

---

## ✨ Features

- **Save Password** — Add a new website and password.
- **View Passwords** — List all saved website/password pairs.
- **Generate Password** — Create a random, strong 8-character password.
- **Update Password** — Change an existing password after verifying the old one (manually or with an auto-generated one).
- **Delete Password** — Remove a saved website entry (with confirmation).
- **Persistent Storage** — All data is saved to `password.txt` and reloaded automatically when the program restarts.

---

## 📦 Requirements

- Python 3.x
- No external libraries needed (uses only Python's built-in `random` and `string` modules)

---

## 🚀 How to Run

1. Save the script as `password_manager.py`
2. Open a terminal in the same folder
3. Run:

```bash
python password_manager.py
```

4. Use the on-screen menu to manage your passwords.

---

## 🖥️ Menu Options

```
-----PERSONAL PASSWORD MANAGER---
1. Save Password
2. View Passwords
3. Generate Password
4. Update Password
5. Delete Password
6. Exit
```

| Option | Description |
|--------|-------------|
| **1** | Enter a website name and password to save it |
| **2** | View all saved website/password pairs |
| **3** | Generate a random secure password (letters, digits, symbols) |
| **4** | Update a password — requires the current password to confirm |
| **5** | Delete a saved entry — asks for confirmation before deleting |
| **6** | Exit the program |

---

## 📁 File Structure

```
password-manager/
│
├── password_manager.py   # Main script
├── password.txt           # Auto-created — stores saved passwords (site:password)
└── README.md              # This file
```

### `password.txt` format
Each line is stored as:
```
website:password
```
Example:
```
gmail.com:X9!kLp2$
github.com:aB3_qz88
```

---

## 🔧 How It Works (Logic Overview)

- **On startup**, the program reads `password.txt` (if it exists) and loads all saved entries into memory (a Python dictionary).
- **Save**: Adds the new entry to the dictionary and appends it to the file.
- **Update**: Verifies the current password before allowing a change. The new password can be typed manually or auto-generated. After updating, the entire file is rewritten to reflect the change.
- **Delete**: Asks for confirmation, then removes the entry from memory and rewrites the file.
- **Generate**: Creates a random 8-character password using uppercase, lowercase, digits, and special characters.

---

## 🛡️ Future Improvements

This project stores passwords in plain text for simplicity. For real-world use, consider adding:

- 🔒 **Encryption** — Use the `cryptography` library (e.g. `Fernet`) to encrypt passwords before saving.
- 🔑 **Master Password** — Require a master password to unlock the manager.
- 🧂 **Password Hashing** — For login-style verification, use `bcrypt` instead of plain comparison.
- 📋 **Clipboard Copy** — Use `pyperclip` to copy passwords instead of printing them to the screen.
- ✅ **Password Strength Meter** — Warn users if a manually entered password is weak.
- 🗃️ **Database Storage** — Use SQLite instead of a `.txt` file for better data handling.

---

## 📝 License

Free to use and modify for personal or educational purposes.
