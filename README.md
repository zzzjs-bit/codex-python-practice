# codex-python-practice

A safe practice repository for learning Codex with Python.

## JPY to CNY converter

This project provides a small command-line tool that converts Japanese yen (JPY)
to Chinese yuan (CNY) using a user-provided exchange rate.

## Install dependencies

```bash
python -m pip install -r requirements.txt
```

## Run the program

```bash
python main.py --jpy 10000 --rate 0.046
```

Expected output:

```text
10000 JPY ≈ 460.00 CNY
```

## Run tests

```bash
python -m pytest
```
