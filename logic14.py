def main(a):
    """
    Given a two-digit integer a, check the following statement:
    "All digits sum is odd".

    Args:
        a (int): parameter a

    Returns:
        bool: True if the sum of digits is odd, False otherwise
    """
    a = abs(a)  # manfiy son bo'lsa, musbatga aylantiramiz
    digit_sum = a % 10 + a // 10  # birlik va o‘nlik raqamlarni yig‘amiz
    return digit_sum % 2 == 1  # yig‘indi toq bo‘lsa, True

# Foydalanuvchidan son olish
a = int(input("Sonni kiriting: "))
print(main(a))  # natijani chiqarish
