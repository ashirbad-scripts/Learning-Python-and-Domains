# function.
def catchErrors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error occured: ", {e})
    return wrapper

@catchErrors
def divide(a,b):
    return a / b
print(divide(10,2))
print(divide(10,0))