#Case Study 3: Warehouse Inventory Reconciliation

#1. Problem Statement
'''Compare opening stock, incoming stock, dispatched stock and recorded closing stock for multiple products; detect discrepancies and calculate replenishment needs.'''
#2. Objectives
'''	Compute expected closing stock for each product.
	Compare expected and recorded stock to identify discrepancies.
	Calculate replenishment quantities for a minimum stock level.'''


#3. Assumptions
'''	All stock quantities are non-negative integers.
   Expected closing stock = opening + incoming - dispatched.
	Minimum desired stock is entered for each product.'''


#4. Algorithm
'''Step 1: Read the number of products.
Step 2: For each product, read stock movement and recorded closing stock.
Step 3: Calculate expected stock and discrepancy.
Step 4: Calculate replenishment needed to meet the minimum level.
Step 5: Print a reconciliation report.'''


#5. Flowchart
'''Start -> Read and validate input -> Process calculations and conditions -> Display results -> Stop'''


#6. Pseudocode
'''BEGIN
  READ product count
  FOR each product DO
      READ opening, incoming, dispatched, recorded closing, minimum stock
      expected <- opening + incoming - dispatched
      discrepancy <- recorded closing - expected
      replenishment <- max(0, minimum stock - recorded closing)
      PRINT results
  END FOR
END'''


#7. Python Source Code
n = int(input("Number of products: "))
 
if n <= 0:
    print("Enter at least one product.")
else:
    for i in range(n):
        print(f"\nProduct {i+1}")
        name = input("Product name: ")
        opening = int(input("Opening stock: "))
        incoming = int(input("Incoming quantity: "))
        dispatched = int(input("Dispatched quantity: "))
        closing = int(input("Recorded closing stock: "))
        minimum = int(input("Minimum desired stock: "))
 
        values = [opening, incoming, dispatched, closing, minimum]
        if min(values) < 0 or dispatched > opening + incoming:
            print("Invalid quantities; check this product's data.")
            continue
 
        expected = opening + incoming - dispatched
        discrepancy = closing - expected
        replenish = max(0, minimum - closing)
        print("Expected closing stock:", expected)
        print("Recorded closing stock:", closing)
        print("Discrepancy (recorded - expected):", discrepancy)
        print("Replenishment required:", replenish)
        print("Status:", "MATCH" if discrepancy == 0 else "DISCREPANCY FOUND")


#8. Test Case and Expected Output
'''Example: opening 100,
            incoming 40,
            dispatched 70,
            recorded closing 65,
            minimum stock 80. 
            Expected = 70, 
            discrepancy = -5, 
            replenishment = 15.
'''

#9. Conclusion
'''The program identifies stock-record differences and shows how much stock should be replenished to reach the specified minimum level.'''





 



