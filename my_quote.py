import math

def quote(weight_kg, distance_km, category, express=False, coupon=""):
    w = math.ceil(weight_kg * 2) / 2
    price = w * 40.0 + distance_km * 2.5
    
    if category == 'electronics':
        price *= 1.3
    elif category == 'fragile':
        price += 150.0
        
    if price > 800:
        price *= 0.9
        
    if coupon == 'WELCOME10':
        price -= 100.0
        
    return round(price, 2)
