# 📞 Local Contact Book

A lightweight, persistent CLI Contact Book application built in Python. This utility allows users to manage contacts cleanly through an interactive command-line menu while persisting data locally using JSON.

---

## 🌟 Key Features

* **Persistent Storage:** Automatically reads from and updates `contacts.json` to ensure contacts persist across sessions.
* **Full CRUD Functionality:** Easily Add, View, and Delete contacts.
* **Input Validation:** Built-in error handling guards against invalid menu selections and `FileNotFoundError`.
* **Standardized Lookup:** Case-insensitive search ensures reliable deletion and retrieval.

---

## 🛠️ Project Architecture & Concepts Used

* **Dictionaries (`dict`):** Used for key-value pair mapping of contact names to phone numbers.
* **JSON Serialization (`json` module):** Handles reading (`json.load`) and saving (`json.dump`) formatted data to local disk.
* **Error Handling (`try/except`):** Prevents script crashes during file operations and user input parsing.
* **State Management:** Manages dynamic updates during execution before writing back to persistent storage.

---

## 🚀 How to Run

1. Clone or download the repository to your local environment.
2. Open your terminal in the project directory.
3. Run the script using Python 3:

```bash
python contacts.py

.
├── contacts.py      # Core script containing CLI logic and state handling
├── contacts.json    # Local JSON storage file (auto-generated if missing)
└── README.md        # Project documentation