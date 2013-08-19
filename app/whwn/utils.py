def ensure_positive(x):
    """Make sure a value positive"""
    if x < 0:
        raise ValueError("Quantity must be positive")

def ensure_greater_equal_than(x, y):
    """Ensure x is greater than y"""
    if x >= y:
        return True
    else:
        raise ValueError("Cannot checkout more quantity than " 
                              "is available to the user")
