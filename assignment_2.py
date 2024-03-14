names = ["Nameeee1", "name2", "Nameeee3"]

for name in names:
    print(len(name))
    if(len(name) >= 5):
        print(name)
    
    if("n" in name):
        print("n found in name " + name)
    if("N" in name):
        print("N found in name " + name)

not_empty = True
while not_empty:
    print(names.pop())
    if(len(names) == 0):
        not_empty = False
else:
    print("names gone!")
    