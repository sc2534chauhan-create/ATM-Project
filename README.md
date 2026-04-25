# ATM Project 🏧

A simple command-line ATM simulation built with Python.

## Features

- 🔐 PIN-based login with 3 attempts
- 💰 Check account balance
- ➕ Deposit money
- ➖ Withdraw money
- 📄 View transaction history

## Project Structure

```
ATM_PROJECT/
├── main.py              # Entry point
├── services/
│   ├── __init__.py
│   ├── auth.py          # PIN login logic
│   └── atm.py           # ATM operations (balance, deposit, withdraw, statement)
└── README.md
```

## How to Run

```bash
python main.py
```

## Default PIN

```
1234
```

## Requirements

- Python 3.x (no external libraries needed)
