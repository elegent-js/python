def greet_user(name):
    """Display a simple greeting."""
    print(f"Hello! {name.title()}")


greet_user("张三")

def describe_pet(pet_name, animal_type = 'dog'):
    """显示宠物的信息"""
    print(f"I have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}")

describe_pet(pet_name = "飞机")


# 传递任意数量的实参，使用*号
# 跟java的...一样，实际toppings是一个tuple
def make_pizza(*toppings):
    """打印顾客点的所有配料"""
    print(toppings)

make_pizza('pepperoni', 'mushrooms', 'green peppers')


# 使用**传递任意数量的关键字实参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    print(profile)