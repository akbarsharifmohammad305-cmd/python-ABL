#Case Study 7: Fuel Consumption and Route Comparison

#1. Problem Statement
'''Compare several vehicle options for a journey using distance, mileage, fuel price and reserve requirements, then identify the lowest-cost feasible option.'''


#2. Objectives
'''	Calculate fuel needed and journey cost for each vehicle.
	Include a reserve fuel requirement.
	Reject options that cannot carry enough fuel and select the lowest-cost feasible vehicle.'''


#3. Assumptions
'''	Distance is in kilometres, mileage in km/litre and fuel tank capacity in litres.
	Reserve is added to trip fuel need.
	A vehicle is feasible when required fuel including reserve does not exceed its tank capacity.'''


#4. Algorithm
'''Step 1: Read trip distance, fuel price and reserve percentage.
Step 2: For each vehicle, read mileage and tank capacity.
Step 3: Calculate trip fuel, reserve fuel and total required fuel.
Step 4: Mark feasibility and calculate cost.
Step 5: Choose the feasible option with the lowest journey cost.'''


#5. Flowchart
'''Start -> Read and validate input -> Process calculations and conditions -> Display results -> Stop'''


#6. Pseudocode
'''BEGIN
  READ distance, price, reserve percentage, vehicles
  best <- none
  FOR each vehicle DO
      trip_fuel <- distance / mileage
      required <- trip_fuel * (1 + reserve / 100)
      cost <- trip_fuel * price
      IF required <= tank capacity THEN
          IF cost < best cost THEN best <- vehicle
      END IF
      PRINT vehicle result
  END FOR
  PRINT lowest-cost feasible option or none
END'''


#7. Python Source Code
distance = float(input("Journey distance (km): "))
price = float(input("Fuel price per litre (Rs): "))
reserve_pct = float(input("Reserve percentage (e.g. 10): "))
n = int(input("Number of vehicles to compare: "))
 
if distance <= 0 or price <= 0 or reserve_pct < 0 or n <= 0:
    print("Invalid journey details.")
else:
    best = None
    for i in range(n):
        print(f"\nVehicle {i+1}")
        name = input("Vehicle name: ")
        mileage = float(input("Mileage (km/litre): "))
        tank = float(input("Available fuel capacity (litres): "))
        if mileage <= 0 or tank < 0:
            print("Invalid mileage or capacity; skipped.")
            continue
        trip_fuel = distance / mileage
        required = trip_fuel * (1 + reserve_pct / 100)
        cost = trip_fuel * price
        feasible = required <= tank
        print(f"Trip fuel: {trip_fuel:.2f} L")
        print(f"Fuel including reserve: {required:.2f} L")
        print(f"Estimated cost: Rs {cost:.2f}")
        print("Feasible:", "Yes" if feasible else "No")
        if feasible and (best is None or cost < best[1]):
            best = (name, cost, required)
    if best:
        print(f"\nLowest-cost feasible option: {best[0]}")
        print(f"Estimated journey fuel cost: Rs {best[1]:.2f}")
        print(f"Fuel including reserve: {best[2]:.2f} L")
    else:
        print("\nNo vehicle meets the fuel-capacity requirement.")

#8. Test Case and Expected Output
'''Example: distance 300 km, 
            fuel price rupees 100/L,reserve 10%. 
            A 15 km/L vehicle needs 22 L including reserve; 
            if tank capacity is 30 L, it is feasible and trip fuel cost is rupees 2,000.'''

#9. Conclusion
'''The comparison considers both cost and fuel feasibility, so the recommended vehicle is the cheapest option that can complete the journey with the required reserve.'''



 



