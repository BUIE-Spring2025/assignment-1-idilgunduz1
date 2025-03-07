def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """

    roman_dict = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }
    if not 1 <= num <= 3999:
        print("Number must be between 1 and 3999")
    
    roman_version = ""
    for value, numeral in roman_dict.items():
        while num >= value:
            roman_version += numeral
            num -= value
    return roman_version