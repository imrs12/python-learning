#Topic: Sets, contains only unique values and no duplicates

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices
print(f"common spices: {common_spices}")

present_in_essential_only = essential_spices - optional_spices
print(f"spices: {present_in_essential_only}")


#Membership testing, same as in tuples

print(f"is Cardamom present in essential spices: { 'cardamom' in essential_spices}")
