NAMES = ["Abhishek","Amrita","Akshit","Abheek"]
AGES = [40,36,10,4]

i=0
while i < len(NAMES):
    print(NAMES[i], AGES[i])
    i+=1

for name in NAMES:
    print(name)

for name, age in zip(NAMES, AGES):
    print(f"{name}, {age}")


for name in reversed(NAMES):
    print(name)

for i in range(5):
    print(i)


# enumerate
for i, name in enumerate(NAMES):
    print(f"{i}, {name}")