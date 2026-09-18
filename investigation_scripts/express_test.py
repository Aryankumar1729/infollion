import sys
from oracle import quote

def main():
    print("--- Brute force Express ---")
    categories = ["standard", "electronics", "fragile", "books", "clothing", "food"]
    found = False
    for c in categories:
        for w in [1.0, 10.0]:
            for d in [10.0, 100.0, 1000.0]:
                pf = quote(w, d, c, False, "")
                pt = quote(w, d, c, True, "")
                if pf != pt:
                    print(f"Express effect found! {c}, w={w}, d={d}: False={pf}, True={pt}")
                    found = True
    if not found:
        print("No express effect found in this sample.")

if __name__ == "__main__":
    main()
