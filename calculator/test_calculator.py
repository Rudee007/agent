from pkg.calculator import Calculator

calculator = Calculator()

# Test cases
test_expressions = [
    "1 + 2",
    "5 - 3",
    "2 * 4",
    "10 / 2",
    "1 + 2 * 3",
    "( 1 + 2 ) * 3", # This will fail with the current implementation as it doesn't handle parentheses
    "10 / 0", # This should raise a ZeroDivisionError
    "1 +", # Invalid expression
    "", # Empty expression
    "   ", # Whitespace expression
    "abc", # Invalid token
]

for expr in test_expressions:
    try:
        result = calculator.evaluate(expr)
        print(f"Expression: '{expr}' = {result}")
    except Exception as e:
        print(f"Expression: '{expr}' resulted in an error: {e}")
