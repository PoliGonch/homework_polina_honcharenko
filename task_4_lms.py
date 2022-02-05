def reverse(input_str: str) -> str:
    new_word = ''
    if len(input_str) == 1:
        return new_word.join(input_str)

    return new_word.join(input_str[-1]) + reverse(input_str[:-1])


print(reverse('hello'))
print(reverse('o'))

# """
# Function returns reversed input string
# >>> reverse("hello") == "olleh"
# True
# >>> reverse("o") == "o"
# True
# """
