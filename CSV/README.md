# 📊 Python Sales Data & Regional Analytics Engines

A pair of lightweight, zero-dependency Python utilities designed to parse, aggregate, and summarize transactional CSV data. These projects demonstrate data processing, type casting, dynamic dictionary aggregation, and dual-file stream reporting.

---

## 📁 Projects Included

### 1. 🛒 Retail Sales Data Aggregator
Scans and processes multi-line retail transactional records (`sales_data.csv`) to compute total financial metrics across product categories and identify top-performing inventory items.

* **Key Concepts:** Standard `csv.DictReader` file streaming, category-based conditional revenue summation, and dictionary-based item volume tracking.
* **Input File:** `sales_data.csv`
* **Output Artifact:** `sales_summary.txt`

### 2. 🎮 Regional Gaming Sales Analyzer
Processes international gaming accessory sales records (`game_sales.csv`) to evaluate revenue performance across regions (North America, Europe, Asia) and identify global product demand using precise float math.

* **Key Concepts:** Multi-file context management (`with open()`), exact floating-point precision, dictionary max-key extraction via `max(dict, key=dict.get)`, and formatted summary reporting.
* **Input File:** `game_sales.csv`
* **Output Artifact:** `game_summary.txt`

---

## 🛠️ Concepts & Technologies Used

* **Python Standard Library:** `csv` module (`csv.DictReader`) for standard CSV parsing.
* **File Stream Management:** Context managers (`with open()`) for simultaneous input reading and output writing.
* **Data Structures & Algorithms:**
  * Dictionary aggregation using `.get(key, 0)` for zero-key-error counter accumulation.
  * Extrema lookup via `max()` with key extraction lambdas/methods.
* **Data Precision:** Post-processing rounding (`round()`) to preserve exact arithmetic sums across large datasets.

---

## 🚀 How to Run

1. Open your terminal in the project directory.
2. Ensure the required input CSV files (`sales_data.csv` or `game_sales.csv`) are in the root directory.
3. Run either analysis script:

```bash
# Run the retail sales aggregator
python3 sales_aggregator.py

# Run the regional gaming sales analyzer
python3 game_sales.py
