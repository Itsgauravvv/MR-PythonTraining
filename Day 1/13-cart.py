cart_value = float(input("Enter cart value: "))
customer_type = input("Enter customer type (Regular/VIP): ")
coupon = input("Enter coupon code: ")
membership = input("Are you a Premium member? (yes/no): ").lower()
discount = 0
shipping_charge = 100

if cart_value > 5000:
    discount = cart_value * 0.20
elif cart_value > 2000:
    discount = cart_value * 0.10

if coupon == "AWESOME100":
    print("Valid Coupon Applied: ₹100 Discount")
    discount += 100
else:
    print("Invalid or No Coupon Applied")

if membership == "yes":
    shipping_charge = 0
    print("Free Shipping for Premium Member")

final_amt = cart_value - discount + shipping_charge

if final_amt < 0:
    final_amt = 0
print("Cart Value: ", cart_value)
print("Discount: ", discount)
print("Shipping Charge: ", shipping_charge)
print("Final Payable: ", final_amt)