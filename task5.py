#Case Study 5: Multi-Day Water Tank Simulation
#1. Problem Statement
'''Simulate tank levels across intervals with changing inflow and outflow, detect overflow and shortage, and identify the first interval at which a target level is reached.'''
#2. Objectives
'''	Update tank level after every interval.
	Detect overflow and shortage conditions.
	Find the first interval that reaches a target level.'''


#3. Assumptions
'''	Tank level starts between zero and capacity.
	Inflow and outflow are non-negative quantities.
	Overflow is measured above capacity; shortage occurs when net outflow would make the level negative.'''


#4. Algorithm
'''Step 1: Read capacity, initial level, target and number of intervals.
Step 2: For each interval, read inflow and outflow.
Step 3: Calculate tentative level and report overflow or shortage.
Step 4: Clamp the stored level between zero and capacity.
Step 5: Record the first interval that reaches the target.'''

#5. Flowchart
'''Start -> Read and validate input -> Process calculations and conditions -> Display results -> Stop'''


#6. Pseudocode
'''BEGIN
  READ capacity, level, target, intervals
  FOR each interval DO
      READ inflow, outflow
      tentative <- level + inflow - outflow
      IF tentative > capacity THEN report overflow
      IF tentative < 0 THEN report shortage
      level <- min(capacity, max(0, tentative))
      IF target not reached before AND level >= target THEN save interval
  END FOR
  PRINT final level and first target interval
END'''


#7. Python Source Code
capacity = float(input("Tank capacity (litres): "))
level = float(input("Initial water level (litres): "))
target = float(input("Target level (litres): "))
days = int(input("Number of intervals/days: "))
 
if capacity <= 0 or not 0 <= level <= capacity or not 0 <= target <= capacity or days < 0:
    print("Invalid tank details.")
else:
    first_reached = None
    for day in range(1, days + 1):
        inflow = float(input(f"Day {day} inflow (litres): "))
        outflow = float(input(f"Day {day} outflow (litres): "))
        if inflow < 0 or outflow < 0:
            print("Inflow and outflow must be non-negative.")
            continue
        tentative = level + inflow - outflow
        if tentative > capacity:
            print(f"Day {day}: OVERFLOW of {tentative-capacity:.2f} litres.")
        if tentative < 0:
            print(f"Day {day}: SHORTAGE of {-tentative:.2f} litres.")
        level = min(capacity, max(0, tentative))
        print(f"Day {day} ending level: {level:.2f} litres")
        if first_reached is None and level >= target:
            first_reached = day
    print("\nFinal water level:", round(level, 2), "litres")
    if first_reached is None:
        print("Target level was not reached.")
    else:
        print("First interval reaching target:", first_reached)


#8. Test Case and Expected Output
'''Example: capacity 1000 L, 
            initial level 500 L, 
            target 800 L. 
            Day 1 inflow 400 L and outflow 100 L gives 800 L; 
            target is first reached on Day 1.
'''

#9. Conclusion
'''The simulation tracks the tank safely across intervals and reports overflow, shortage and target-level milestones.'''




 



