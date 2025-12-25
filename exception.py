def set(age):
    if age < 0:
        raise ValueError("age cannot be negative.")
    print(f"age set to {age}")
    
try:
    set(-5)
except ValueError as e:
    print(e)