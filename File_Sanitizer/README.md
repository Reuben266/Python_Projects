# 🛡️ Log File Sanitizer

A fast, lightweight Python utility designed to scan, sanitize, and redact sensitive information from server log files. It uses a combination of dynamic list processing and Regular Expressions (Regex) to ensure zero leaks of sensitive network data or internal state parameters.

---

## 🌟 Key Features

* **Dynamic Word Redaction:** Iterates through a configurable list of target keywords (`failed`, `token`, etc.) to sanitize static sensitive strings.
* **Regex Pattern Matching:** Uses Python's built-in `re` module to dynamically detect and redact variable patterns like IP addresses (`[REDACTED_IP]`).
* **Memory-Efficient File Streaming:** Reads and writes log files line-by-line using context managers (`with open`), keeping memory usage minimal even on large multi-hundred-line logs.
* **Metrics & Reporting:** Real-time counters track the exact number of redacted items and output a summary report upon completion.

---

## 🛠️ Concepts & Technologies Used

* **Python Standard Library:** `re` (Regular Expressions) for pattern matching and `sys` for argument handling.
* **File I/O Streams:** Efficient `with open()` double-file context managers for simultaneous reading and writing.
* **Data Structures:** Iterative list processing for scaling string replacement logic without code duplication.
* **State Management:** Live accumulation tracking for complete audit visibility.

---

## 🚀 How to Run

1. Clone or download the repository to your local directory.
2. Ensure your target log file (e.g., `sample_log.txt`) is present in the project folder.
3. Run the script in your terminal:

```bash
python3 sanitizer.py
.
├── sanitizer.py        # Core Python log sanitization engine
├── sample_log.txt      # Input raw log file containing sensitive data
├── cleaned_log.txt     # Output redacted log file (auto-generated)
└── README.md           # Project documentation
