# Simple Calculator App 🧮

A Python-based command-line calculator that performs basic arithmetic operations: addition, subtraction, multiplication, and division of Two Numbers.

## Features ✨
- ➕ Addition (A)
- ➖ Subtraction (S)
- ✖️ Multiplication (M)
- ➗ Division (D)
- 🔄 Continuous operation until user quits
- ❌ Input validation and error handling

## Installation ⚙️
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/calculator-app.git
   ```
   ```
   cd calculator-app
   ```
Run the calculator (Python 3 required):

```
python calculator.py
```

Sample Output 🖥️
```
Welcome to my Calculator App that performs only Addition, Subtraction, Multiplication & Division
Type in the first number you want to do arithmetic with: 5
Type in the second number you want to do arithmetic with: 3
What arithmetic operation do you want to perform?:
 Type A -> ADDITION
 Type S -> SUBTRACTION
 Type D -> DIVISION
 Type M -> MULTIPLICATION:
 A
THE ANSWER IS 8
```

Controls
Type q at any input prompt to quit

Only numbers 0-9 are accepted as input

Operation selection is case-insensitive (A/a, S/s, etc.)


Code Structure 📂
```
calculator.py
├── add(a, b)            # Returns sum of two numbers
├── subtract(a, b)       # Returns difference
├── multiply(a, b)       # Returns product
├── divide(a, b)         # Returns quotient
└── main loop            # Handles user interaction
```

How to Contribute 🤝
Fork the project

Create your feature branch (git checkout -b feature/AmazingFeature)

Commit your changes (git commit -m 'Add some amazing feature')

Push to the branch (git push origin feature/AmazingFeature)

Open a Pull Request

License 📄
This project is licensed under the MIT License - see the LICENSE file for details
