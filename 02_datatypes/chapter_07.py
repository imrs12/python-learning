Coffee_ingredients = ('coffee_powder', 'water', "milk", 'sugar') # --> Tuple
#Tuple is an data structure to store elements and is immutable

(ingredient1, ingredient2,  ingredient3, ingredient4) = Coffee_ingredients # known as spreading

print(f"Cofffe I1 {ingredient1} : I2 {ingredient2} : I3 {ingredient3} : I4 {ingredient4}" )


coffee_ratio, water_ratio = 1, 2
print(f"coffee and water ratio {coffee_ratio}:{water_ratio}")

coffee_ratio, water_ratio = water_ratio , coffee_ratio #swapping values
print(f"coffee and water ratio {coffee_ratio}:{water_ratio}")

# membership testing --> check whether a element is part of a set

print(f"Is milk in coffee ingrediant? {'milk' in Coffee_ingredients}") # case sensitive 'Milk' will result false

