#Topic: List -> A data structure to store data and is mutable.
#Similar to Arrays

ingredients= ["milk", "water", "ginger"]

ingredients.append("chai_patti")
print(f"Chai Ingredients: {ingredients}")

ingredients.remove("milk")
print(f"Chai Ingredients: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients= ["water", "chai_patti"]

chai_ingredients.extend(spice_options)
print(f"Ingredients: {chai_ingredients}")

chai_ingredients.insert(3, "masala")
print(f"Ingredients: {chai_ingredients}")

last_element = chai_ingredients.pop()
print(f"last element: {last_element}")

#reversing the list
chai_ingredients.reverse()
print(f'reversed chai: {chai_ingredients}')

chai_ingredients.sort()
print(f"sorted chai: {chai_ingredients}")

water_level = [1,2,3,4,5,6,7,8,9]
print(f"minimum: {min(water_level)}")
print(f'maximum: {max(water_level)}')
