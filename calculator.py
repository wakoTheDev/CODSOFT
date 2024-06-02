firstNumber = float(input("Enter the first number: "))
secondNumber = float(input("Enter the second number: "))
operation = input("Enter operation (+, -, *, /): ")


def calculator(firstNumber,secondNumber,operation):
    try:
        if operation == "+":
            result = firstNumber + secondNumber
        elif operation == "-":
            result = firstNumber - secondNumber
        elif operation == "*":
            result = firstNumber * secondNumber
        elif operation == "/":
            if secondNumber == 0:
                raise ZeroDivisionError
            else:
                result = firstNumber / secondNumber
        else:
            return "Invalid operation!"

        print(f"{firstNumber} {operation} {secondNumber} = {result}")

    except ValueError:
        raise ValueError


if __name__ == "__main__":
  calculator(firstNumber,secondNumber,operation)
