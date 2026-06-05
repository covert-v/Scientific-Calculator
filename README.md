# Scientific Calculator

A scientific calculator built entirely in Python using **CustomTkinter** as the GUI framework. Features a clean, warm-toned design with both standard arithmetic and scientific functions.

---

## Screenshots

| Default | Mid-Operation | Result |
|--------|---------------|--------|
| ![Default state](https://i.imgur.com/uFiMNBg.png) | ![Mid-operation](https://i.imgur.com/taT1JGg.png) | ![Result](https://i.imgur.com/dwSV81b.png) |

---

## Features

**Standard Operations**
- Addition, subtraction, multiplication, division
- Decimal input and percentage calculation
- Sign toggle (`+/-`)
- Backspace and clear

**Scientific Functions**
- Trigonometry: `sin`, `cos`, `tan`
- Square root (`√`) and exponentiation (`x²`, `xʸ`)
- Logarithms: `log` (base 10), `ln` (natural log)

**Quality of Life**
- **DEG / RAD toggle** — switch angle units on the fly
- **Calculation history** — last two operations displayed above the main screen
- **Expression label** — shows the in-progress expression (e.g. `2 +`) while entering the second operand
- **Clipboard copy** — click the display to copy the current value; a brief "Copied!" confirmation appears
- **Keyboard support** — full numpad and keyboard input including operators, Enter, Backspace, and Escape
- **Floating-point cleanup** — results rounded to 10 significant figures to suppress noise (e.g. no `0.9999999999`)
- **Comma formatting** — large numbers display with thousands separators for readability

---

## Installation

**Requirements**
- Python 3.8+
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

**Install dependencies**
```bash
pip install customtkinter
```

**Run**
```bash
python Scientific_Calculator.py
```

---

## Keyboard Shortcuts

| Key | Action |
|-----|--------|
| `0–9`, `.` | Number input |
| `+`, `-`, `*`, `/` | Arithmetic operators |
| `Enter` / `KP_Enter` | Equals |
| `Backspace` | Delete last character |
| `Escape` | Clear |
| `%` | Percent |
| Numpad keys | Full numpad support |

---

## Project Structure

```
Scientific_Calculator.py   # Main application — single file
```

---

## Built With

- [Python](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)
- [math](https://docs.python.org/3/library/math.html) (standard library)

---

*Codebase by Covert-v*
