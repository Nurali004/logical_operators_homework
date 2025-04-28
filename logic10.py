def main(a):
    """
    Given integer a,  check the following statement "The integer is two-digit numb
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return 10 <= abs(a) <=99

a=int(input("sonni kiriting:"))
print(main(a))