# Truthiness
samples = [0,1,"", "text", [],{1},{},{'k': 1}, None]

for item in samples:
    if item:
        print(repr(item))
    else:
        print(repr(item))

# Output:
# 1 
# 'text'
# {1}
# {'k': 1}      
# False values: 0, '', [], {}, None
# True values: 1, 'text', {1}, {'k': 1}


# for item in samples:
#     if item:
#         print(item)
#     else:
#         print(item), without repr, the same output but without quotes for strings
    