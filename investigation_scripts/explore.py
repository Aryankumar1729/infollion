import sys
from oracle import quote

def main():
    print("--- Exact Weight thresholds ---")
    for w in range(10, 20):
        print(f"w={w}: {quote(w, 100.0, 'standard', False, '')}")

    print("\n--- Exact Distance thresholds ---")
    for d in range(250, 350, 10):
        print(f"d={d}: {quote(1.0, d, 'standard', False, '')}")

    print("\n--- Category Multipliers ---")
    print("w=10, d=100")
    for c in ["standard", "electronics", "fragile"]:
        print(f"{c}: {quote(10.0, 100.0, c, False, '')}")

    print("w=1, d=10")
    for c in ["standard", "electronics", "fragile"]:
        print(f"{c}: {quote(1.0, 10.0, c, False, '')}")

    print("\n--- Express Effect ---")
    print("Maybe express only works with some distances?")
    for d in [10, 100, 500, 1000]:
        price_f = quote(1.0, d, 'standard', False, '')
        price_t = quote(1.0, d, 'standard', True, '')
        print(f"d={d} Express False: {price_f}, True: {price_t}")
        
    for w in [10, 50]:
        price_f = quote(w, 100.0, 'standard', False, '')
        price_t = quote(w, 100.0, 'standard', True, '')
        print(f"w={w} Express False: {price_f}, True: {price_t}")

if __name__ == "__main__":
    main()
