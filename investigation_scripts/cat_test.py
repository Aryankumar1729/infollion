import sys
from oracle import quote

def main():
    print("--- Categories: isolate w and d ---")
    for c in ["standard", "electronics", "fragile"]:
        p1 = quote(1.0, 10.0, c, False, "")
        p2 = quote(2.0, 10.0, c, False, "")
        p3 = quote(1.0, 20.0, c, False, "")
        print(f"[{c}] w=1,d=10: {p1}, w=2,d=10: {p2}, w=1,d=20: {p3}")

    print("\n--- Express with food ---")
    print(f"food express=False: {quote(1.0, 100.0, 'food', False, '')}")
    print(f"food express=True: {quote(1.0, 100.0, 'food', True, '')}")
    print(f"electronics express=True: {quote(1.0, 100.0, 'electronics', True, '')}")

if __name__ == "__main__":
    main()
