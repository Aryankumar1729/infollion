import sys
from oracle import quote

def main():
    print("--- Coupon test ---")
    print(f"w=1, d=10, WELCOME10: {quote(1.0, 10.0, 'standard', False, 'WELCOME10')}")
    print(f"w=1, d=10, NO COUPON: {quote(1.0, 10.0, 'standard', False, '')}")
    
    print("\n--- Express with Coupon ---")
    pf = quote(1.0, 10.0, 'standard', False, 'WELCOME10')
    pt = quote(1.0, 10.0, 'standard', True, 'WELCOME10')
    print(f"Express False: {pf}, True: {pt}")

    print("\n--- Exact 10% discount threshold ---")
    for d in [303, 304, 305]:
        p = quote(1.0, d, 'standard', False, "")
        print(f"d={d}, base_price={40 + 2.5*d}, quoted: {p}")

    print("\n--- Test express one more time, explicitly ---")
    # Is it possible express is just a +50 flat fee that gets absorbed by the 10% discount? No.
    print(quote(2.0, 50.0, 'standard', True, ''))

if __name__ == "__main__":
    main()
