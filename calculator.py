import math


def calculate(expression):
    """
    Safely evaluates a mathematical expression.
    """

    allowed_names = {
        "sqrt": math.sqrt,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "log": math.log10,
        "ln": math.log,
        "abs": abs,
        "pi": math.pi,
        "e": math.e,
        "factorial": math.factorial
    }

    try:
        result = eval(expression, {"__builtins__": {}}, allowed_names)

        if not isinstance(result, (int, float)):
            return None, "Invalid result"

        if math.isnan(result) or math.isinf(result):
            return None, "Result is not a valid number"

        return result, None

    except ZeroDivisionError:
        return None, "Cannot divide by zero"

    except (ValueError, TypeError, SyntaxError, NameError):
        return None, "Invalid mathematical expression"

    except Exception:
        return None, "Something went wrong"
