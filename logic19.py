def main(x):
    """
    Given a two digit integer x, return true if x is palindrome integer.
    An integer is a palindrome, when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    x=abs(x)
    return x//10 == x%10

x=int(input("sonni kiriting:"))
print(main(x))


