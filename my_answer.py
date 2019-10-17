#!/usr/bin/python

"""
Python Statements
"""


def add_binary(a, b):
    if a=="" or b=="":
        return None
    for i in a:
        if i!="1" and i!="0":
            return None
    for i in b:
        if i!="1" and i!="0":
            return None
    item1 = int(a, 2)
    item2 = int(b, 2)
    result = bin(item1 + item2)[2:]
    return result


def plus_one(digits):
    s = len(digits)
    item = 1
    if digits[s-1]!=9:
        digits[s - 1] = digits[s - 1] + 1
    else:
        for i in range(s-2,-1,-1):
            if digits[i]==9:
                item=item+1
        digits[s-1-item]=digits[s-1-item]+1
        for i in range(1,item+1):
            digits[s - 1 - item+i]=0
        if item==s:
            digits[0]=1
            digits.append(0)
    return digits


def roman_to_integers(roman_string):
    integer = 0
    res = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        item = roman_string[i]
        integer = integer + res[item]
    for i in range(len(roman_string) - 1):
        if roman_string[i] == 'I' and (roman_string[i + 1] == 'V' or roman_string[i + 1] == 'X'):
            integer = integer - 2
            i = i + 1
        if roman_string[i] == 'X' and (roman_string[i + 1] == 'L' or roman_string[i + 1] == 'C'):
            integer = integer - 20
            i = i + 1
        if roman_string[i] == 'C' and (roman_string[i + 1] == 'D' or roman_string[i + 1] == 'M'):
            integer = integer - 200
            i = i + 1


    """
    This is to review loops, if statements and dictionaries
    ============================================================
    Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000
    For example, two is written as II in Roman numeral, just two one's added together.
    Twelve is written as, XII, which is simply X + II. The number twenty seven is written
    as XXVII, which is XX + V + II.
    Roman numerals are usually written largest to smallest from left to right. However,
    the numeral for four is not IIII. Instead, the number four is written as IV. Because
    the one is before the five we subtract it making four. The same principle applies to
    the number nine, which is written as IX. There are six instances where subtraction is used:
    - I can be placed before V (5) and X (10) to make 4 and 9.
    - X can be placed before L (50) and C (100) to make 40 and 90.
    - C can be placed before D (500) and M (1000) to make 400 and 900.
    Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
    Example 1:
        Input: "III"
        Output: 3
    Example 2:
        Input: "IV"
        Output: 4
    Example 3:
        Input: "IX"
        Output: 9
    Example 4:
        Input: "LVIII"
        Output: 58
        Explanation: C = 100, L = 50, XXX = 30 and III = 3.
    Example 5:
        Input: "MCMXCIV"
        Output: 1994
        Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
    """
    return integer