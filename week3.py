#Q1:

def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return price - (price * discount_percent / 100)
    else:
        return price

#Q2
# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))
    
# Calculate the final price
final_price = calculate_discount(original_price, discount_percentage)
    
    # printing the result
if final_price < original_price:
    print(f"The final price after applying the discount is: Ksh.{final_price}")
else:
    print(f"No discount applied. The original price is: Ksh.{original_price}")