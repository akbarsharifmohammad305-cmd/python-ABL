#Case Study 10: Traffic Violation Penalty Calculator

#1. Problem Statement
'''Calculate fines for multiple traffic violations using vehicle category, offence type and repeat-offence status, and identify disqualification conditions.'''


#2. Objectives
'''	Apply fine rules based on offence and vehicle type.
	Increase fines for repeat offences.
	Flag offences that cause a disqualification warning.'''


#3. Assumptions
'''	The fine schedule is illustrative for programming practice and is not legal advice.
	Repeat offences double the base fine.
	Driving without a valid licence and dangerous driving trigger a disqualification warning.'''


#4. Algorithm
'''Step 1: Define sample fine rules by offence and vehicle category.
Step 2: Read each violation and repeat-offence status.
Step 3: Validate the offence and vehicle category.
Step 4: Calculate base and repeat fine; update total.
Step 5: Display itemized fines and disqualification warnings.'''


#5. Flowchart
'''Start -> Read and validate input -> Process calculations and conditions -> Display results -> Stop'''


#6. Pseudocode
'''BEGIN
  DEFINE fine rules and disqualifying offences
  READ violation count
  FOR each violation DO
      READ vehicle, offence, repeat status
      IF rule missing THEN report invalid entry
      ELSE calculate base fine
           IF repeat THEN fine <- fine * 2
           add fine to total
           IF offence is disqualifying THEN show warning
      PRINT violation result
  END FOR
  PRINT total penalty
END'''


#7. Python Source Code
fine_rules = {
    "CAR": {"SPEEDING": 1000, "NO_HELMET": 0,
            "NO_LICENCE": 5000, "DANGEROUS_DRIVING": 5000},
    "BIKE": {"SPEEDING": 1000, "NO_HELMET": 500,
             "NO_LICENCE": 5000, "DANGEROUS_DRIVING": 5000},
    "TRUCK": {"SPEEDING": 2000, "NO_HELMET": 0,
              "NO_LICENCE": 5000, "DANGEROUS_DRIVING": 10000}
}
disqualifying = {"NO_LICENCE", "DANGEROUS_DRIVING"}
n = int(input("Number of violations: "))
total = 0
warnings = []
 
for i in range(n):
    print(f"\nViolation {i+1}")
    vehicle = input("Vehicle (CAR/BIKE/TRUCK): ").upper()
    offence = input("Offence (SPEEDING/NO_HELMET/NO_LICENCE/"
                    "DANGEROUS_DRIVING): ").upper()
    repeat = input("Repeat offence? (Y/N): ").upper()
 
    if vehicle not in fine_rules or offence not in fine_rules[vehicle]:
        print("Invalid vehicle category or offence.")
        continue
    if repeat not in ("Y", "N"):
        print("Invalid repeat-offence value.")
        continue
 
    fine = fine_rules[vehicle][offence]
    if repeat == "Y":
        fine *= 2
    total += fine
    print("Penalty: Rs", fine)
    if offence in disqualifying:
        warning = f"{vehicle}: {offence} - disqualification review required"
        warnings.append(warning)
        print("WARNING:", warning)
 
print("\n--- Penalty Summary ---")
print("Total penalty: Rs", total)
if warnings:
    print("Disqualification conditions:")
    for warning in warnings:
        print("-", warning)
else:
    print("No disqualification warning under these sample rules.")


#8. Test Case and Expected Output
'''Example: BIKE + NO_HELMET (first offence) = rupees 500; 
            CAR + SPEEDING (repeat offence) = rupees 2,000. 
            Total = rupees 2,500. 
            NO_LICENCE triggers a disqualification review warning.'''


#9. Conclusion
'''The calculator produces an itemized penalty summary and highlights serious offences. Its fine amounts are examples for a coding exercise, not a substitute for current offici'''



 



