def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return 100 <=abs(a) <=999

a=int(input("sonni kiriting:"))
print(main(a))