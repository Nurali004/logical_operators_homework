def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a%10 == a//10

a=int(input("sonni kiriting:"))
print(main(a))