def add(a, b):
    return a + b


def subtract(a, b):
    return a - b
# pinskiy sin sluhi

if __name__ == "__main__":
    print("Calculator")
    
    a = int(input("First number: "))
    b = int(input("Second number: "))
    
    print("Sum:", add(a, b))
    print("Subtract:", subtract(a, b))
