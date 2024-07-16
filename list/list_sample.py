bicycles = ["trek", "giant", "redline", 'specialized']

print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])
print(bicycles[-1].title())
print(bicycles[-2])

messages = f"my first bicycle was a {bicycles[0].title()}"
print(messages)


bicycles.append('cannondale')
print(bicycles) 

bicycles.insert(1, "cannondale")
print(bicycles)

del bicycles[1]
print(bicycles)

popped_bicycle = bicycles.pop()
print(f"the last motor I owned was a {popped_bicycle.title()}")

bicycles.remove('redline')
print(bicycles)