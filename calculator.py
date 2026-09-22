import ast
import math
import operator


# Supported binary operators
OPERATORS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}


# Supported scientific functions
FUNCTIONS = {
    "sqrt": math.sqrt,
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "log": math.log10,
    "ln": math.log,
}


# Constants
CONSTANTS = {
    "pi": math.pi,
    "e": math.e,
}


def evaluate(node):
    """
    Safely evaluate a mathematical expression.
    """

    # Numbers
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value

        raise ValueError("Invalid value.")

    # Negative numbers
    if isinstance(node, ast.UnaryOp):
        if isinstance(node.op, ast.USub):
            return -evaluate(node.operand)

        if isinstance(node.op, ast.UAdd):
            return evaluate(node.operand)

        raise ValueError("Invalid operator.")

    # Binary operations
    if isinstance(node, ast.BinOp):
        left = evaluate(node.left)
        right = evaluate(node.right)

        operation = OPERATORS.get(type(node.op))

        if operation is None:
            raise ValueError("Operator not supported.")

        return operation(left, right)

    # Constants such as pi and e
    if isinstance(node, ast.Name):
        if node.id in CONSTANTS:
            return CONSTANTS[node.id]

        raise ValueError(f"Unknown value: {node.id}")

    # Functions such as sqrt(25)
    if isinstance(node, ast.Call):

        if not isinstance(node.func, ast.Name):
            raise ValueError("Invalid function.")

        function_name = node.func.id

        if function_name not in FUNCTIONS:
            raise ValueError(
                f"Function '{function_name}' is not supported."
            )

        if len(node.args) != 1:
            raise ValueError(
                f"{function_name}() requires one argument."
            )

        argument = evaluate(node.args[0])

        return FUNCTIONS[function_name](argument)

    raise ValueError("Invalid expression.")


def calculate(expression):
    """
    Calculate an expression.

    Returns:
        result, error
    """

    try:

        if not expression.strip():
            return None, "Enter an expression first."

        # Convert calculator symbols to Python operators
        expression = expression.replace("×", "*")
        expression = expression.replace("÷", "/")

        # Parse expression
        tree = ast.parse(expression, mode="eval")

        # Evaluate safely
        result = evaluate(tree.body)

        # Check invalid results
        if not math.isfinite(result):
            return None, "Result is not a finite number."

        # Remove unnecessary .0
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        return result, None

    except ZeroDivisionError:
        return None, "Cannot divide by zero."

    except ValueError as error:
        return None, str(error)

    except SyntaxError:
        return None, "Invalid expression."

    except Exception:
        return None, "Something went wrong."
