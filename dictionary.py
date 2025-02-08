alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0['color'] = 'yellow'
print(alien_0)

del alien_0['points']
print(alien_0)


p_val = alien_0.get('points', 'No points value assigned')
print(p_val)

user = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

print()

for key in sorted(user.keys(), reverse = True):
    print(key.title())

print()

for val in sorted(user.values()):
    print(val.title())

print()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for language in set(favorite_languages.values()):
    print(language.title())


