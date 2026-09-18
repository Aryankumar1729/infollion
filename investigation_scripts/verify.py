import random
from oracle import quote as oracle_quote
from my_quote import quote as my_quote

def main():
    categories = ["standard", "electronics", "fragile", "books", "clothing", "food"]
    coupons = ["", "WELCOME10"]
    expresses = [True, False]
    
    match = True
    for _ in range(10000):
        w = round(random.uniform(0.1, 100.0), 2)
        d = round(random.uniform(1.0, 5000.0), 2)
        c = random.choice(categories)
        e = random.choice(expresses)
        coup = random.choice(coupons)
        
        expected = oracle_quote(w, d, c, e, coup)
        actual = my_quote(w, d, c, e, coup)
        
        if expected != actual:
            print(f"Mismatch! w={w}, d={d}, c={c}, e={e}, coup={coup}")
            print(f"Expected: {expected}, Actual: {actual}")
            match = False
            break
            
    if match:
        print("Success! my_quote.py matches oracle.py perfectly over 10000 random test cases.")

if __name__ == "__main__":
    main()
