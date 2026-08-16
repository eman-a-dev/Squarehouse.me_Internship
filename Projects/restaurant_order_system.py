# User se food item lo.
# Program ko:
# Check karna hai ke item menu mein hai ya nahi.
# Agar hai → uska index find karo.
# Usi index se price nikalo.
# Price ke basis par:
# >= 700 → "Expensive item"
# >= 400 → "Medium priced item"
# otherwise → "Affordable item"
# Finally print karo:

# Pizza costs Rs. 800
# Expensive item

print("==========================================")
print("          RESTAURANT ORDER SYSTEM         ")
print("==========================================")


menu = ("Burger", "Pizza", "Pasta", "Fries", "Sandwich")
prices = (500, 800, 600, 300, 450)

item = input("Please enter your food item you want to order: ")

if item in menu:
    item_index = menu.index(item)
    if(prices[item_index] >= 700):
        print(menu[item_index] ,"costs Rs. " , prices[item_index])
        print("Expensive Item")
    elif(prices[item_index] >= 400):
        print(menu[item_index] ,"costs Rs. " , prices[item_index])
        print("Medium priced item")
    else:
        print(menu[item_index] ,"costs Rs. " , prices[item_index])
        print("Affordable Item")
else:
    print("Item not available")


