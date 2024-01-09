import argparse

def calculate(operation, num1, num2):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    else:
        raise ValueError("Invalid operation. Please use 'add' or 'subtract'.")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="A simple calculator for addition or subtraction.")
    
    # Define the operation flag
    parser.add_argument('-o', '--operation', required=True, choices=['add', 'subtract'], help='Operation: add or subtract')
    
    # Define the number arguments
    parser.add_argument('num1', type=float, help='First number')
    parser.add_argument('num2', type=float, help='Second number')
    
    # Help flag
    parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS, help='Show this help message and exit')
    
    # Parse the command-line arguments
    args = parser.parse_args()
    
    # Perform the calculation
    result = calculate(args.operation, args.num1, args.num2)
    
    # Print the result
    print(f"Result: {result}")
