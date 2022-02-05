# # from typing import Optional
# def check_is_palindrome(looking_str: str, index: int = 0) -> bool:
#     if len(looking_str) <= 1:
#         return True
#     if looking_str[0] == looking_str[-1]:
#         return check_is_palindrome(looking_str[1:-2])
#     else:
#         return False
#
# print(check_is_palindrome('mama'))
# print(check_is_palindrome('lool'))

def check_is_palindrome(looking_str: str, index: int = 0) -> bool:
    if index == len(looking_str) // 2:
        return True

    if looking_str[index] == looking_str[-index - 1]:
        return check_is_palindrome(looking_str, index + 1)
    else:
        return False


print(check_is_palindrome('mamaamamm'))
print(check_is_palindrome('lolk'))
