# learn iterator list

cars = ['bmw', 'audi', 'toyota', 'subaru']
for car in cars:
    print(car.title())


for val in range(1, 10):
    print(val)

cars = list(range(1, 10))
print(cars)


cars = list(range(1, 100, 10))
print(cars)

squares = []
for val in range(1, 11):
    squares.append(val ** 2)

print(squares)


squares = [val for val in range(1, 1_000_000)]
print(min(squares))
print(max(squares))
print(sum(squares))

# slice
cars = ['bmw', 'audi', 'toyota', 'subaru', 'honda', 'ford']
print(cars)
print(cars[0:3])

print(cars[:5])
print(cars)


