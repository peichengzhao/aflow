import math
from typing import List, Union, Optional, Dict, Any, Callable

# Define tool type
Tool = Dict[str, Any]

# Tool function definitions

def add(numbers: List[Union[int, float]]) -> Union[int, float]:
    """Addition operation: Calculate the sum of all numbers in the list"""
    if not numbers:
        return 0
    return sum(numbers)

def subtract(a: Union[int, float], b: Union[int, float]) -> Union[int, float]:
    """Subtraction operation: a - b"""
    return a - b

def multiply(numbers: List[Union[int, float]]) -> Union[int, float]:
    """Multiplication operation: Calculate the product of all numbers in the list"""
    if not numbers:
        return 0
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(a: Union[int, float], b: Union[int, float]) -> Optional[Union[int, float]]:
    """Division operation: a / b, handles division by zero error"""
    if b == 0:
        print("Error: Divisor cannot be zero")
        return None
    return a / b

def power(base: Union[int, float], exponent: Union[int, float]) -> Union[int, float]:
    """Exponentiation operation: base^exponent"""
    return base ** exponent

def square_root(x: Union[int, float]) -> Optional[float]:
    """Square root operation: √x"""
    if x < 0:
        print("Error: Cannot calculate square root of a negative number")
        return None
    return math.sqrt(x)

def factorial(n: int) -> Optional[int]:
    """Factorial operation: n!"""
    if n < 0:
        print("Error: Cannot calculate factorial of a negative number")
        return None
    if n == 0:
        return 1
    return math.factorial(n)

def percentage(value: Union[int, float], total: Union[int, float]) -> Optional[float]:
    """Percentage calculation: value as a percentage of total"""
    if total == 0:
        print("Error: Total cannot be zero")
        return None
    return (value / total) * 100

def average(numbers: List[Union[int, float]]) -> Optional[float]:
    """Calculate average value"""
    if not numbers:
        print("Error: List is empty")
        return None
    return sum(numbers) / len(numbers)

def max_min(numbers: List[Union[int, float]]) -> dict:
    """Find maximum and minimum values in a list"""
    if not numbers:
        return {"max": None, "min": None}
    return {"max": max(numbers), "min": min(numbers)}

def is_prime(n: int) -> bool:
    """Check if a number is prime"""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check all odd numbers from 3 to √n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def gcd(a: int, b: int) -> int:
    """Calculate greatest common divisor of two numbers"""
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a: int, b: int) -> int:
    """Calculate least common multiple of two numbers"""
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

def quadratic_solver(a: float, b: float, c: float) -> dict:
    """Solve quadratic equation ax² + bx + c = 0"""
    discriminant = b**2 - 4*a*c
    
    if discriminant < 0:
        return {
            "real_roots": 0,
            "complex_roots": 2,
            "roots": [
                complex(-b/(2*a), math.sqrt(-discriminant)/(2*a)),
                complex(-b/(2*a), -math.sqrt(-discriminant)/(2*a))
            ]
        }
    elif discriminant == 0:
        root = -b / (2*a)
        return {
            "real_roots": 1,
            "complex_roots": 0,
            "roots": [root, root]
        }
    else:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return {
            "real_roots": 2,
            "complex_roots": 0,
            "roots": [root1, root2]
        }

# Create tools list
tools: List[Tool] = []

# Add addition tool
tools.append({
    "name": "add",
    "description": "Addition operation: Calculate sum of numbers in list",
    "function": add,
    "parameters": {
        "numbers": {
            "type": "array",
            "items": {"type": "number"},
            "description": "List of numbers to add"
        }
    },
    "returns": {"type": "number"}
})

# Add subtraction tool
tools.append({
    "name": "subtract",
    "description": "Subtraction operation: a - b",
    "function": subtract,
    "parameters": {
        "a": {"type": "number", "description": "Minuend"},
        "b": {"type": "number", "description": "Subtrahend"}
    },
    "returns": {"type": "number"}
})

# Add multiplication tool
tools.append({
    "name": "multiply",
    "description": "Multiplication operation: Calculate product of numbers in list",
    "function": multiply,
    "parameters": {
        "numbers": {
            "type": "array",
            "items": {"type": "number"},
            "description": "List of numbers to multiply"
        }
    },
    "returns": {"type": "number"}
})

# Add division tool
tools.append({
    "name": "divide",
    "description": "Division operation: a / b, handles division by zero",
    "function": divide,
    "parameters": {
        "a": {"type": "number", "description": "Dividend"},
        "b": {"type": "number", "description": "Divisor"}
    },
    "returns": {"type": "number", "nullable": True}
})

# Add exponentiation tool
tools.append({
    "name": "power",
    "description": "Exponentiation operation: base^exponent",
    "function": power,
    "parameters": {
        "base": {"type": "number", "description": "Base number"},
        "exponent": {"type": "number", "description": "Exponent"}
    },
    "returns": {"type": "number"}
})

# Add square root tool
tools.append({
    "name": "square_root",
    "description": "Square root operation: √x",
    "function": square_root,
    "parameters": {
        "x": {"type": "number", "description": "Number to calculate square root"}
    },
    "returns": {"type": "number", "nullable": True}
})

# Add factorial tool
tools.append({
    "name": "factorial",
    "description": "Factorial operation: n!",
    "function": factorial,
    "parameters": {
        "n": {"type": "integer", "description": "Number to calculate factorial"}
    },
    "returns": {"type": "integer", "nullable": True}
})

# Add percentage tool
tools.append({
    "name": "percentage",
    "description": "Percentage calculation: value as percentage of total",
    "function": percentage,
    "parameters": {
        "value": {"type": "number", "description": "Partial value"},
        "total": {"type": "number", "description": "Total value"}
    },
    "returns": {"type": "number", "nullable": True}
})

# Add average tool
tools.append({
    "name": "average",
    "description": "Calculate average value",
    "function": average,
    "parameters": {
        "numbers": {
            "type": "array",
            "items": {"type": "number"},
            "description": "List of numbers to average"
        }
    },
    "returns": {"type": "number", "nullable": True}
})

# Add max-min tool
tools.append({
    "name": "max_min",
    "description": "Find maximum and minimum values in list",
    "function": max_min,
    "parameters": {
        "numbers": {
            "type": "array",
            "items": {"type": "number"},
            "description": "List of numbers to search"
        }
    },
    "returns": {
        "type": "object",
        "properties": {
            "max": {"type": "number", "nullable": True},
            "min": {"type": "number", "nullable": True}
        }
    }
})

# Add prime check tool
tools.append({
    "name": "is_prime",
    "description": "Check if a number is prime",
    "function": is_prime,
    "parameters": {
        "n": {"type": "integer", "description": "Number to check"}
    },
    "returns": {"type": "boolean"}
})

# Add GCD tool
tools.append({
    "name": "gcd",
    "description": "Calculate greatest common divisor of two numbers",
    "function": gcd,
    "parameters": {
        "a": {"type": "integer", "description": "First number"},
        "b": {"type": "integer", "description": "Second number"}
    },
    "returns": {"type": "integer"}
})

# Add LCM tool
tools.append({
    "name": "lcm",
    "description": "Calculate least common multiple of two numbers",
    "function": lcm,
    "parameters": {
        "a": {"type": "integer", "description": "First number"},
        "b": {"type": "integer", "description": "Second number"}
    },
    "returns": {"type": "integer"}
})

# Add quadratic solver tool
tools.append({
    "name": "quadratic_solver",
    "description": "Solve quadratic equation ax² + bx + c = 0",
    "function": quadratic_solver,
    "parameters": {
        "a": {"type": "number", "description": "Quadratic coefficient"},
        "b": {"type": "number", "description": "Linear coefficient"},
        "c": {"type": "number", "description": "Constant term"}
    },
    "returns": {
        "type": "object",
        "properties": {
            "real_roots": {"type": "integer"},
            "complex_roots": {"type": "integer"},
            "roots": {
                "type": "array",
                "items": {"type": "number"}
            }
        }
    }
})

# Tool calling function
def call_tool(tool_name: str, **kwargs) -> Any:
    """Call specified tool"""
    for tool in tools:
        if tool["name"] == tool_name:
            return tool["function"](**kwargs)
    raise ValueError(f"Tool '{tool_name}' does not exist")

# Example usage
if __name__ == "__main__":
    # Call addition tool
    result = call_tool("add", numbers=[1, 2, 3, 4, 5])
    print(f"Addition result: {result}")
    
    # Call square root tool
    result = call_tool("square_root", x=16)
    print(f"Square root result: {result}")
    
    # Call prime check tool
    result = call_tool("is_prime", n=17)
    print(f"Prime check result: {result}")
    
    # Call quadratic solver tool
    result = call_tool("quadratic_solver", a=1, b=-3, c=2)
    print(f"Equation solution result: {result}")
    
    # Print all available tools
    print("\nAvailable tools:")
    for tool in tools:
        print(f"- {tool['name']}: {tool['description']}")