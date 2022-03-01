print(abs.__doc__)
print(int.__doc__)
print(input.__doc__)


def squareValue(n):
    """Return the square value of the input number.
    
    The input number must be integer.
    """
    return n ** 2


number = int(input("Enter a number: "))

print(squareValue(number))
