"""Practice with dictionary syntax"""

#Create a new dictionary
ice_cream: dict[str, int] = {"chocolate": 12, "vanilla": 8, "strawberry": 5}
print("create a dictionary:")
print(ice_cream)

#adding a key,value pair
ice_cream["mint"] = 3
print("added mint to dictionary:")
print(ice_cream)

#removing a value from dictionary
ice_cream.pop("mint")
print("removed mint from dictionary:")
print(ice_cream)

#access a value from dictionary
print(f"there are {ice_cream['chocolate']} orders of chocolate")

#modify a value in dictionary
ice_cream["vanilla"] = 10
print("update vanilla value in dictionary:")
print(ice_cream)

#print the length of the dictionary
print(f"there are {len(ice_cream)} key,value pairs")

#check for presence in dictionary
print("chocolate in dictionary?")
print("chocolate" in ice_cream)
print("mint in dictionary?")
print("mint" in ice_cream)

#using "in" in a conditional
if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint.")

#loop through the dictionary and print out each flavor and number of orders
for flavor in ice_cream:
    #print out <flavor> has <num orders> orders
    print(f"{flavor} has {ice_cream['flavor']} orders") #FIX