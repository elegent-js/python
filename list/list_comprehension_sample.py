# 列表推导式（list comprehension）

square = [val ** 2 for val in range(1, 100)]
print(square)

# equals

squares = []
for val in range(1, 100):
    squares.append(val ** 2)

print(squares)
