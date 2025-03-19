from gemini_api import debug_code

test_code = """
def add_numbers(a, b)
    result = a + b
    return result

print(add_numbers(5, 3))
"""

output = debug_code(test_code)
print(output)