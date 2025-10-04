# Truthiness
samples = [0,1,"", "text", [],{1},{},{'k': 1}, None]

for item in samples:
    if item:
        print(repr(item))
    else:
        print(repr(item))
    
        