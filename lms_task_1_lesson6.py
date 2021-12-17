s = input('write something')
if len(s) >= 2:
    e = s[:2] + s[-2:]
else:
    e = 'Empty String'
print(e)
