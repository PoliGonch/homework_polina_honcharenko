sample_string = input('write something')
if len(sample_string) >= 2:
    expected_string = sample_string[:2] + sample_string[-2:]
else:
    expected_string = ''
print(expected_string)
