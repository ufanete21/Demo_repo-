def calculate_discount(price, discount_percent):
    if int(discount_percent) >= 20:
        discount = (int(price) - (int(price) * int(discount_percent) / 100))
        return discount
    else:
        return price
price = input('Enter price:')
discount_percent = input('Enter percentage discount:')
result = calculate_discount(price, discount_percent)
print(result)
    