cat_attributes = {
    "intelligence": 10,
    "energy": 50,
    "weight": 10,
    # change the inital values above
}

print("Welcome to my cat game!")

# Take the user inputs for name and colour:
name = input("Enter name:")
# ...

# start the while loop
while True:
    # Finish the string below
    option = input("What would you like to do? 1. Play with your cat 2. Train your cat 3. show stats")

    if option == '1':
        cat_attributes['intelligence']+=1
        cat_attributes['energy']-=10
        cat_attributes['weight']-=1
        pass
    elif option == '2':
        cat_attributes['intelligence']+=10
        cat_attributes['energy']-=10
        cat_attributes['weight']-=10
        pass
    # elif ...
    else:
        print (cat_attributes.values())
        pass

    # finish off the if statements below
    if cat_attributes['energy'] < 0:
        endloop
        print('dead cat')
        pass
    