def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    
    return 1000 <= a <=99999


a=int(input("sonni kiriting:"))
print(main(a))