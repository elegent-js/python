cars = ["bmw", "benz", "audi"]

if cars:
    for car in cars:
        if car == "bmw":
            print(car.upper())
            
        else:
            print(car.title())
else:
    print("no cars")


print("bmw" in cars)


age = 20

if age < 4:
    print("child")
elif age < 18:
    print("teenager")
else:
    print("adult")


