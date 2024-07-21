
def arithmetic_operation(num1, num2, operator):
    """
    Perform an arithmetic operation based on the given operator.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operator (str): The arithmetic operator ('+', '-', '*', '/').

    Returns:
    float or str: The result of the operation or an error message if the operator is invalid or division by zero occurs.
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    else:
        return "Error: Invalid operator. Use '+', '-', '*', or '/'."

# Example usage:
num1 = 150
num2 = 30
operator = '+'
print(f"{num1} {operator} {num2} = {arithmetic_operation(num1, num2, operator)}")

operator = '/'
print(f"{num1} {operator} {num2} = {arithmetic_operation(num1, num2, operator)}")

num2 = 0
print(f"{num1} {operator} {num2} = {arithmetic_operation(num1, num2, operator)}")

operator = '%'
print(f"{num1} {operator} {num2} = {arithmetic_operation(num1, num2, operator)}")
