# Oracle Pricing Engine Specifications

Through systematic experimentation and reverse engineering of the `oracle.py` module, the following pricing rules have been identified. The rules are applied in the exact order listed below.

## 1. Weight Calculation
The provided `weight_kg` is rounded up to the nearest 0.5 kg. This rounded weight is then charged at a rate of **$40.00 per kg**.
* **Example**: 
  * `quote(weight_kg=1.1, distance_km=10, category="standard")` returns `85.0`.
  * *Explanation*: 1.1 kg is rounded up to 1.5 kg. (1.5 kg * 40.0) + (10 km * 2.5) = 60.0 + 25.0 = 85.0.

## 2. Distance Calculation
The `distance_km` is charged at a flat rate of **$2.50 per km**. This is added to the weight cost to form the initial base price.
* **Example**:
  * `quote(weight_kg=1.0, distance_km=10, category="standard")` returns `65.0`. (40.0 + 25.0)
  * `quote(weight_kg=1.0, distance_km=50, category="standard")` returns `165.0`. (40.0 + 125.0)

## 3. Category Modifiers
The initial base price is modified depending on the `category`:
* **"electronics"**: Increases the total price by 30% (multiplied by `1.3`).
  * **Example**: `quote(weight_kg=1.0, distance_km=10, category="electronics")` returns `84.5`. (65.0 * 1.3 = 84.5)
* **"fragile"**: Adds a flat fee of **$150.00**.
  * **Example**: `quote(weight_kg=1.0, distance_km=10, category="fragile")` returns `215.0`. (65.0 + 150.0 = 215.0)
* **Other Categories**: ("standard", "books", "clothing", "food") have no modifier.

## 4. High-Value Discount
If the price *after* the category modifiers is **strictly greater than $800.00**, a **10% discount** is applied to the total (multiplied by `0.9`).
* **Example (exactly 800 - no discount)**: `quote(weight_kg=1.0, distance_km=304, category="standard")` returns `800.0`.
* **Example (> 800 - discounted)**: `quote(weight_kg=1.0, distance_km=305, category="standard")` returns `722.25`. 
  * *Explanation*: Initial price is 802.5. Since it's > 800, a 10% discount applies: 802.5 * 0.9 = 722.25.

## 5. Coupon Discount
If the coupon code provided is **"WELCOME10"**, a flat discount of **$100.00** is subtracted from the price. This subtraction occurs *after* the high-value discount is evaluated and applied.
* **Example**: `quote(weight_kg=1.0, distance_km=10, category="standard", coupon="WELCOME10")` returns `-35.0`.
  * *Explanation*: Base price is 65.0. 65.0 - 100.0 = -35.0.

## 6. Express Shipping (Ignored)
The `express` parameter (True/False) is completely ignored by the pricing engine and has no effect on the price under any conditions.
* **Example**: 
  * `quote(weight_kg=1.0, distance_km=10, category="standard", express=False)` returns `65.0`.
  * `quote(weight_kg=1.0, distance_km=10, category="standard", express=True)` returns `65.0`.

## 7. Final Rounding
The final calculated price is rounded to **2 decimal places** before being returned.
