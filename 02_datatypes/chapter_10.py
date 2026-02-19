chai_order = dict(type="Masala Chai", size="Medium", sugar=1)
print(f"Chai ka order: {chai_order}")

chai_recipe = {}
chai_recipe['base'] ="black tea"
chai_recipe['liquid'] = "milk"

print(f"chai recipe {chai_recipe}")
print(f"Recipe base: {chai_recipe['base']}")

del chai_recipe['base']
print(f"chai recipe {chai_recipe}")

print(f"Is sugar in the order? {'sugar' in chai_order}")

chai_order= {"type":"Normal", "size": "Small", "sugar": 2}
print(f"chai order details keys only : {chai_order.keys()}")
print(f"chai order values  : {chai_order.values()}")
print(f"chai order items : {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"cardamom": "crushed" , "ginger": "grated" }
chai_recipe.update(extra_spices)
print(f"updated chai recipe: {chai_recipe}")

chai_size = chai_order['size']
#chai_size = chai_order['customer_note'] here it will crash because customer_note key is not in chai_order
print(f"chai size is: {chai_size}")

customer_note = chai_order.get("note", "No not present") #if key not present then return other value raher crashing
print(f"chai order customer note: {customer_note}") 
