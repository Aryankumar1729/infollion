from oracle import quote

def main():
    print("--- Experiment 1: Varying Weight (Distance=100, Category='standard') ---")
    for w in [1.0, 2.0, 3.0, 4.0, 5.0, 10.0]:
        price = quote(weight_kg=w, distance_km=100.0, category="standard", express=False, coupon="")
        print(f"Weight: {w:4.1f} kg -> Price: {price}")

    print("\n--- Experiment 2: Varying Distance (Weight=1.0, Category='standard') ---")
    for d in [10.0, 50.0, 100.0, 200.0, 500.0, 1000.0]:
        price = quote(weight_kg=1.0, distance_km=d, category="standard", express=False, coupon="")
        print(f"Distance: {d:6.1f} km -> Price: {price}")

if __name__ == "__main__":
    main()
