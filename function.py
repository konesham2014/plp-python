#function
def calculate_discount(price, discount_percent):
    """Return final price after discount if discount is 20% or higher,
    otherwise return original price."""
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

#inputs
try:
    original_price = float(input("Enter the original price: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(original_price, discount_percent)

    print(f"The final price is: {final_price:.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values.")
