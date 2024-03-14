name = input("Name: ")
age = input("Age: ")

def combine(arg1, arg2): 
    return arg1 + " " + arg2

def get_decades(age):
    return int(int(age) / 10)

print(combine(name, age))
print("Decades lived: ")
print(get_decades(age))