import math

def reverse_string(s: str):
    if s == "":
        return s
    return reverse_string(s[1:]) + s[0]


print(reverse_string("Hello"))


def is_palindrome(s: str):
    if str == "" or len(s) == 1:
        return True
    if s[0].lower() == s[-1].lower():
        return is_palindrome(s[1:-1])
    return False


print(is_palindrome("Sahas"))


def get_quotient_reminder(num: int, divideBy: int):
    deci = num // divideBy
    rem = num % divideBy
    return deci, rem


def decimal_to_binary(num: int, result: str):
    if num == 0:
        return result
    deci, rem = get_quotient_reminder(num, 2)
    result = str(rem) + result
    print(f"input - {num}, quotient - {deci}, reminder - {rem}, result - {result}")
    return decimal_to_binary(deci, result)


print(decimal_to_binary(2, ""))


def recursive_summation(num: int):
    if num <= 1:
        return num
    return num + recursive_summation(num - 1)

def normal_summation(num: int):
    return (num * (num + 1)) // 2

print(recursive_summation(100))
print(normal_summation(59))

# def binary_search(sorted_list: list, n: int):
#     mid = math.floor(len(sorted_list) / 2)
#     if sorted_list[mid] == n:
#         return mid
#
#     if sorted_list[mid] > n:
#         return binary_search(sorted_list[0:mid], n)
#
#     if sorted_list[mid] < n:
#         return binary_search(sorted_list[mid:-1], n)

