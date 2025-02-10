def user_profile(first, last, **user_info):
    '''Build a dictionary containing everything we know about a user.'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = user_profile('john', 'doe', location = 'new york', field = 'computer science')
print(user_profile)

# 演示recursion
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
    
print(fact(5))
print(fact(10))
print(fact(0))
print(fact(15))