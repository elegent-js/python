dimensions = (100, 200)
print(dimensions)
print(dimensions[0])
print(dimensions[1])

for item in dimensions:
    if item == 100 or item == 200:
        print(item)
    elif item == 300:
        print('yes')    
    else:
        print('no')

print(100 in dimensions)
print(300 in dimensions)
print(300 not in dimensions)



