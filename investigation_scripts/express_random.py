import sys
from oracle import quote

def main():
    import random
    categories = ["standard", "electronics", "fragile", "books", "clothing", "food"]
    for i in range(1000):
        w = round(random.uniform(0.1, 100), 1)
        d = round(random.uniform(1, 5000), 1)
        c = random.choice(categories)
        pf = quote(w, d, c, False, "")
        pt = quote(w, d, c, True, "")
        if pf != pt:
            print(f"Express effect found! {c}, w={w}, d={d}: False={pf}, True={pt}")
            return
    print("No express effect found after 1000 random probes.")

if __name__ == "__main__":
    main()
