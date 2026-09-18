import sys
from oracle import quote

def main():
    print("--- Detailed Weight ---")
    for w in range(1, 101, 5):
        print(f"w={w:3d}: {quote(w, 100.0, 'standard', False, '')}")

    print("\n--- Detailed Distance ---")
    for d in range(10, 5001, 200):
        print(f"d={d:4d}: {quote(1.0, d, 'standard', False, '')}")

    print("\n--- Detailed Express ---")
    print(f"d=10, express=True: {quote(1.0, 10.0, 'standard', True, '')}")
    print(f"d=100, express=True: {quote(1.0, 100.0, 'standard', True, '')}")
    print(f"d=1000, express=True: {quote(1.0, 1000.0, 'standard', True, '')}")

if __name__ == "__main__":
    main()
