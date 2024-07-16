alien = {'color': 'green', 'points': 5}

print(alien['color'])
print(alien['points'])

alien['x_position'] = 0
alien['y_position'] = 25

print(alien)


# for each dictionary, you can store an unlimited amount of information
for k, v in alien.items():
    print(f"\nKey: {k}")
    print(f"Value: {v}")

# for each key in the dictionary
for k in alien.keys():
    print(f"\nKey: {k}")