# Python Object-Oriented Programming (OOP) Practice Suite 🚀

A collections of Python projects demonstrating core Object-Oriented Programming principles, including class initialization, state tracking, inheritance, method execution, and validation checks.

---

## 📁 Project Overview

This repository contains three distinct modules modeling real-world domain logic and game mechanics:

1. **Player Tracking System** (`player.py`)
2. **Banking & Financial System** (`banking.py`)
3. **Weapon & Combat System** (`weapon.py`)

---

## 🛠️ Modules & Features

### 1. Player Tracking System (`player.py`)
Models player state, health tracking, and dynamic point scoring.

* **Core Capabilities:**
  * Tracks player profile details including username, health status, and running score.
  * Handles health reduction based on damage taken.
  * Rewards points and updates cumulative score status.

---

### 2. Banking & Financial System (`banking.py`)
Models bank account management, transaction processing, simple interest loan calculations, and account specialization via inheritance.

* **Core Capabilities:**
  * Manages customer profile metrics including contact information and account balances.
  * Processes balance deposits while rejecting non-positive transaction amounts.
  * Handles cash withdrawals while preventing overdrafts and negative amounts.
  * Computes simple interest loans over specified durations and credits funds directly to the account balance.
  * Extends base account functionalities to calculate annual interest yields for savings accounts.

---

### 3. Weapon & Combat System (`weapon.py`)
Models equipment durability, attack actions, item repairs, and ammo consumption for ranged equipment using class inheritance.

* **Core Capabilities:**
  * Tracks weapon damage attributes and durability states.
  * Manages melee attack actions while reducing durability and blocking actions when broken.
  * Restores equipment integrity through repairs up to maximum capacity limits.
  * Extends weapon functionality for ranged equipment to handle ammunition consumption and shot execution.

---

## 🚀 Usage Example

Execute the scripts using Python 3:

```bash
python player.py
python banking.py
python weapon.py
```