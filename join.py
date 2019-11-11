str1 = ['a','b','c','d']

new_string = ''
for char in str1:
    new_string = new_string + char + ','

print(new_string)

new_string = ",".join(str1)
print(new_string)