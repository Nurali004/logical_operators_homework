def main(a,b):
    """
    Given two integers a, b,  check the following statement "Each of the numbers 'a' and 'b' is odd".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    return a%2 !=0 and b%2 !=0

a=int(input("1-sonni kiriting:"))
b=int(input("2-sonni kiriting:"))
print(main(a,b))