greet = "Hello World"
extented_greet = "Hello World" + " this is long greeting"

name = "John"

intreption = f"Hello, {name}"

greet_format = "Hello, {}"
formatted = greet_format.format(name)

print(greet)
print(extented_greet)
print(intreption) 
print(formatted)


print(formatted.upper())
print(formatted.lower())
print(formatted.replace("John", "Abhishek"))