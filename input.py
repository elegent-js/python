name = input('please input your name: ')
print(f'\n hello, {name}!')

age = input('please input your age: ')
age = int(age)
print(f'\n you are {age} years old.')

if age > 20:
    print('\n you are an adult.')
else:
    print('\n you are a teenager.')

number = input("please input a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f'\n the number {number} is even.')
else:
    print(f'\n the number {number} is odd.')