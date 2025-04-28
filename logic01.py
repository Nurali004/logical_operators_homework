def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    return (a>b>c) or (c>a>b)


a=int(input("1-sonni kiriting:"))
b=int(input("2-sonni kiriting:"))
c=int(input("3-sonni kiriting:"))
print(main(a,b,c))