from string import punctuation


def stop_words(words_list: list[str]):
    def decorate_function(func):
        def wrap_stop_words(func_argument):
            new_string = ''
            temp_string = ''
            input_string = func(func_argument)
            for char in input_string:
                if temp_string in words_list:
                    new_string += '*'
                    temp_string = ''
                temp_string += str(char)
                if char == ' ' or char in punctuation:
                    new_string += temp_string
                    temp_string = ''
            return new_string

            # temp_string = func(func_argument)
            # for world in words_list:
            #     temp_string = temp_string.replace(world, '*')
            # return temp_string

        return wrap_stop_words

    return decorate_function


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
