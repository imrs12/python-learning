customer_name= 'Ayush'
customer_order= "Mosambi ka juice"

print(f"Order for {customer_name} : {customer_order} pilado!")

#slicing
order_description = "Buttery and Delicious"

print(f"Every Nth word: {order_description[:9:3]}") # ::N gives every third element for the sliced string
print(f"First word: {order_description[:8]}") # :N slices the string till 8th charatcer 
print(f"Last word: {order_description[21:]}") # N: starts slicing from nth index to last index
print(f"Reverse String: {order_description[::-1]}") #Reverse the string

label_text= "Speciâl àpplê"
print(f"Normal text: {label_text}")

encode_label = label_text.encode("utf-8")
print(f"Encoded text: {encode_label} ")

decoded_label = encode_label.decode("utf-8")
print(f"Decoded text: {decoded_label}")

hindi_text= "नमस्ते दुनिया"
encoded_hindi= hindi_text.encode("utf-8")
print(f"encoded hindi text: {encoded_hindi}")

decoded_hindi= encoded_hindi.decode("utf-8")
print(f"decoded hindi text: {decoded_hindi}")
