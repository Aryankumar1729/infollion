import sys
from oracle import quote

def main():
    print("--- Weight fractional ---")
    for w in [1.0, 1.1, 1.2, 1.5, 1.9, 2.0]:
        print(f"w={w}, quoted: {quote(w, 10.0, 'standard', False, '')}")

    print("--- Distance fractional ---")
    for d in [10.0, 10.1, 10.5, 10.9, 11.0]:
        print(f"d={d}, quoted: {quote(1.0, d, 'standard', False, '')}")
        
    print("--- Express with fractional ---")
    for w in [1.1]:
        print(f"express=True, w={w}: {quote(w, 10.0, 'standard', True, '')}")

if __name__ == "__main__":
    main()
