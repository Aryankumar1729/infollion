import sys
from oracle import quote

def test():
    w0, d0, c0, e0, coup0 = 1.0, 100.0, "standard", False, ""
    
    print("--- Base ---")
    print(f"Base (1.0kg, 100km, standard, False, ''): {quote(w0, d0, c0, e0, coup0)}")
    
    print("\n--- Weight ---")
    for w in [0.5, 1.0, 2.0, 2.5, 3.0, 10.0, 50.0]:
        print(f"w={w:4.1f}: {quote(w, d0, c0, e0, coup0)}")
        
    print("\n--- Distance ---")
    for d in [10.0, 50.0, 100.0, 200.0, 1000.0]:
        print(f"d={d:6.1f}: {quote(w0, d, c0, e0, coup0)}")
        
    print("\n--- Category ---")
    categories = ["standard", "electronics", "fragile", "books", "clothing", "food"]
    for c in categories:
        print(f"c={c:15s}: {quote(w0, d0, c, e0, coup0)}")
        
    print("\n--- Express ---")
    print(f"express=True: {quote(w0, d0, c0, True, coup0)}")
    
    print("\n--- Coupon ---")
    print(f"coupon='WELCOME10': {quote(w0, d0, c0, e0, 'WELCOME10')}")

if __name__ == "__main__":
    test()
