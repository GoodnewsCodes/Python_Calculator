def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

print("Welcome to my Calculator App that performs "
"only Addition, Subtracton, Multiplication & Division")
while True:
    a = input("Type in the first number you want to do arithmetics with: ")
    if a != "q":
        b = input("Type in the second number you want to do arithmetics with: ")

        if b != "q":
            try:
                a = int(a)
                b = int(b)
            except ValueError:
                print("Please enter a number between 0-9 or 'q' to quit.")
                continue

            arithmetic = input("What arithmetic operation do you want to perform?: "
                "\n Type A -> ADDITION"
                "\n Type S -> SUBTRACTION"
                "\n Type D -> DIVISION"
                "\n Type M -> MULTIPLICATION: "
                "\n ").strip().upper()
                


            if arithmetic == "A":
                result = add(a, b)
                print(f"THE ANSWER IS {result}")

            elif arithmetic == "S":
                result =  subtract(a, b)
                print(f"THE ANSWER IS {result}")

            elif arithmetic == "D":
                result = divide(a, b)
                print(f"THE ANSWER IS {result}")

            elif arithmetic == "M":
                result = multiply(a, b)
                print(f"THE ANSWER IS {result}")
            else:
                print("Please a letter, either A, S, D, or M"
                "\n Let's try that again")
                
        else:
            print("Calculator was stopped!")
            break
    else:
        print("Calculator was stopped!")
        break