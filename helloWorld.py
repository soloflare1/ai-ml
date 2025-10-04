# print() funtion automatically adds a new line at the end
print('Hello')
print('world')
print('Good bye')


# if you want to avoid that, you can use the 'end' parameter, 
# so that it ends with a space instead of a new line

# to print in the same line as HelloworldGood bye  without spaces
print('Hello', end='')
print('world', end='')
print('Good bye', end='')

# to print in the same line as Hello world Good bye with spaces
print('Hello ', end='')
print('world ', end='')
print('Good bye ', end='')


