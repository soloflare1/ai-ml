# slicing sequence types

# start end indexing
# list slicing  [start:end:step]
# Exclude the end index 
# Include the start index
# step is optional, default is 1


num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(num[0:5]) # [10, 20, 30, 40, 50]
print(num[1: 5]) # [20, 30, 40, 50]
print(num[0:5:2]) # [10, 30, 50]
print(num[0::]) # [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],from start to end
print(num[:5:]) # [10, 20, 30, 40, 50] ,from start to index 4
print(num[::2]) # [10, 30, 50, 70, 90] , from start to end with step 2
print(num[::-1]) # [100, 90, 80, 70, 60, 50, 40, 30, 20, 10], reverse the list
print(num[-1:-6:-1]) # [100, 90, 80, 70, 60], from end to start with step -1
print(num[:-3]) # [10, 20, 30, 40, 50, 60, 70], from start to index -4
print(num[-3:]) # [80, 90, 100], from index -3 to end
print(num[-5:-1]) # [60, 70, 80, 90], from index -5 to -2
