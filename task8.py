#Case Study 8: Multi-Product Shopping Budget Constraint

#1. Problem Statement
'''Evaluate a basket of products and quantities, apply discount rules and determine which purchases should be reduced to fit a fixed budget.'''


#2. Objectives
'''	Calculate line totals and conditional discounts.
	Calculate the total basket value.
	Reduce quantities from lower-priority items until the basket fits the budget.'''


#3. Assumptions
'''	Discount applies when a line subtotal reaches the entered threshold.
	Products are reduced in reverse priority order, starting from the last product entered.
	Quantities are whole numbers and cannot become negative.'''


#4. Algorithm
'''Step 1: Read budget and product details.
Step 2: Calculate subtotal and discount for each product.
Step 3: Compute the total after discounts.
Step 4: If over budget, reduce quantities from the last item backward until within budget.
Step 5: Display final quantities and savings.'''


#5. Flowchart
'''Start -> Read and validate input -> Process calculations and conditions -> Display results -> Stop'''


#6. Pseudocode
'''BEGIN
  READ budget and products
  FOR each product DO
      subtotal <- price * quantity
      IF subtotal >= threshold THEN apply discount
      total <- total + discounted subtotal
  END FOR
  FOR products in reverse order WHILE total > budget
      reduce quantity by one and recalculate line total
  END FOR
  PRINT final basket and total
END'''


#7. Python Source Code
budget = float(input("Shopping budget (Rs): "))
n = int(input("Number of products: "))

items = []

if budget < 0 or n <= 0:
    print("Invalid budget or product count.")

else:
    valid = True

    for i in range(n):
        print("\nProduct", i + 1)

        name = input("Name: ")
        price = float(input("Unit price (Rs): "))
        qty = int(input("Quantity: "))
        threshold = float(input("Discount threshold (Rs): "))
        discount = float(input("Discount percentage: "))

        if price < 0 or qty < 0 or threshold < 0 or not 0 <= discount <= 100:
            print("Invalid product data.")
            valid = False
            break

        items.append({
            "name": name,
            "price": price,
            "qty": qty,
            "threshold": threshold,
            "discount": discount
        })

    if valid:

        def line_total(item):
            subtotal = item["price"] * item["qty"]

            if subtotal >= item["threshold"]:
                subtotal -= subtotal * item["discount"] / 100

            return subtotal

        original = sum(line_total(x) for x in items)

        print("\nOriginal basket total: Rs", round(original, 2))

        # Reduce quantities in reverse order
        for item in reversed(items):
            while sum(line_total(x) for x in items) > budget and item["qty"] > 0:
                item["qty"] -= 1

        final_total = sum(line_total(x) for x in items)

        print("\n--- Final Basket ---")

        for item in items:
            print(item["name"], "Quantity:", item["qty"],
                  "Line Total: Rs", round(line_total(item), 2))

        print("\nFinal total: Rs", round(final_total, 2))
        print("Savings: Rs", round(original - final_total, 2))
        print("Amount within budget: Rs", round(budget - final_total, 2))

        if final_total <= budget:
            print("Shopping is within budget.")
        else:
            print("Budget cannot be met.")


#8. Test Case and Expected Output
'''Example: budget rupees 1,000; 
            basket total rupees 1,250. 
            The program reduces quantities starting with the last product until the recalculated total is within rupees 1,000 or no further reductions are possible.'''


#9. Conclusion
'''The program applies product-level discount rules and uses a clear reduction order to bring the basket within the available budget.'''


