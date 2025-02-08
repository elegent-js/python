def greet_user(name, age = 18):
    '''Display a simple greeting.'''
    print(f"Welcome aboard: name-{name}, age-{age}")


greet_user(name = 'John')

## 以*标识的变量将会创建一个元组
def print_user(*users):
    for user in users:
        print(user)


print_user('John', 'Jane', 'Doe', 'Smith')