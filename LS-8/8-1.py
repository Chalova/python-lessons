# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("1")
    print("2")
    print("3")


greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print((f"How are you, {name}?"))

greet_with_name("Ania")

def greet_with(name, location):
    print(f"Hello, {name}. How is it like in {location}?")

greet_with('Ania', 'Israael')

greet_with(location='Swiss', name='Anna')