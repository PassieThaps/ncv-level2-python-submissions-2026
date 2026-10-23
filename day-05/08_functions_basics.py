def order(item):
    print("Your order is: ", item)
    
def get_order():
    print("Preparing order")
    return("Order ready")

def calc_total(item):
    base_price = 25.5
    vat = 1.15
    total_price = (base_price + len(item))* vat
    return(f'Your order amount is: R{round(total_price,2)}')
    
place_order = input("Enter order: ")

print("------------------")
print(get_order())#use when there is a return statment
order(place_order)

order_total = calc_total(place_order)
print(calc_total(order_total))

print("------------------")
print("Please collect your", place_order)
