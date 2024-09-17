
# Alexander J. Jackson
# restaurant_selector.py

vegetarian = False

vegan = False

gluten_free = False

response_1 = input('Is anyone in your party a vegetarian? ')
if response_1 == 'yes':
    vegetarian = True

response_2 = input('Is anyone in your party vegan? ')
if response_2 == 'yes':
    vegan = True

response_3 = input('Is anyone in your party gluten free? ')
if response_3 == 'yes':
    gluten_free = True

print()
print("Here are your restaureant choices")
print()
if vegetarian == False and vegan == False and gluten_free == False:
    print("Joe's Gourmet Burgers")
    print("Mama's Fine Italian")
    print("Main Street Pizza")

elif vegetarian == True and vegan == False and gluten_free == False:
    print("Mama's Fine Italian")
    print("Main Street Pizza")

elif vegetarian == False and vegan == False and gluten_free == True:
    print("Main Street Pizza")

elif vegetarian == True and vegan == False and gluten_free == True:
    print("Main Street Pizza")

print("Corner Cafe")
print("Chef's Kitchen")

