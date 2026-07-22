def add_tax(price , rate=0.15):
    return price + price * rate
total = add_tax(1000) # 1150.0(uses ddefault rate)
total + add_tax(1000, rate=0.10) #1100.00 (keyword argument)
print("===tax calculator ===")
