# CCweek3_Expt3_PES1UG22CS622

## cart/__init__.py : Optimizations and reasoning:

1. Replaced eval with json.loads in get_cart:
   
   **Reason**: `eval` is unsafe as it can execute arbitrary code. Using `json.loads` is safer for parsing JSON strings.

2. Introduced @classmethod for Cart.load:
   
   **Reason**: Using `@classmethod` improves readability and follows object-oriented principles for creating instances from dictionaries.

3. Used list comprehension in get_cart:
   
   **Reason**: Simplifies the code by replacing explicit loops with a concise, Pythonic approach.

4. Added type annotations:
   
   **Reason**: Enhances code clarity and ensures the function signatures are well-documented.

5. Formatted imports and removed unused ones:
    
   **Reason**: Keeps the code clean and ensures only necessary dependencies are included.


## products/__init__.py : Optimizations and reasoning:

1. Replaced explicit loop with list comprehension in list_products:
   
   **Reason**: List comprehensions make the code concise and more efficient.

2. Removed unnecessary blank lines in the Product class:
   
   **Reason**: Improves readability by keeping the class definition compact.

3. Ensured consistency in formatting and type annotations:
   
   **Reason**: Uniform formatting enhances code readability and maintainability.

4. Retained existing logic for unchanged functions (get_product, add_product, update_qty):
   
   **Reason**: These functions were already optimized and followed best practices.
