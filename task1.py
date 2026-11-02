#Case Study 1: Attendance Recovery Computation

#1. Problem Statement
'''Calculate a student's current attendance percentage and determine the minimum consecutive classes that must be attended to reach a target eligibility percentage.'''


#2. Objectives
'''	Calculate attendance percentage from classes attended and conducted.
	Calculate the minimum future classes required to reach the target percentage.
	Compare alternative future attendance scenarios.'''


#3. Assumptions
'''	Attended classes cannot exceed classes conducted.
    Target eligibility is 75% by default.
	The student attends every consecutive future class being calculated.'''


#4. Algorithm
'''Step 1: Read attended classes, conducted classes and target percentage.
   Step 2: Validate the input values.
   Step 3: Calculate current percentage.
   Step 4: Increase future classes one at a time until the percentage reaches the target.
   Step 5: Print current status and required classes for each scenario.'''


#5. Flowchart
'''Start -> Read and validate input -> Process calculations and conditions -> Display results -> Stop'''


#6. Pseudocode
'''BEGIN
  READ attended, conducted, target
  current <- attended / conducted * 100
  FOR each future scenario DO
      future <- 0
      WHILE (attended + future) / (conducted + future) * 100 < target
          future <- future + 1
      PRINT future
  END FOR
END'''


#7. Python Source Code
attended = int(input("Classes attended: "))
conducted = int(input("Classes conducted: "))
target = float(input("Eligibility percentage (e.g. 75): "))
 
if conducted <= 0 or attended < 0 or attended > conducted:
    print("Invalid attendance details.")
elif not 0 < target <= 100:
    print("Target must be greater than 0 and at most 100.")
else:
    current = attended / conducted * 100
    print(f"Current attendance: {current:.2f}%")
    if current >= target:
        print("You already meet the eligibility threshold.")
    else:
        for scenario in [1.0, 0.9, 0.75]:
            future = 0
            while ((attended + future * scenario) /
                   (conducted + future)) * 100 < target:
                future += 1
            # For non-perfect attendance, simulate attended future classes
            # by counting only the assumed proportion as attended.
            print(f"Future attendance rate {scenario*100:.0f}%: "
                  f"about {future} classes to reach target.")

            
#8. Test Case and Expected Output
'''Example: attended = 60, 
         conducted = 80, 
         target = 75. 
         Current attendance = 75.00%; 
         eligibility is already met.'''


#9. Conclusion
'''The program reports the current attendance percentage and evaluates how future attendance patterns affect eligibility. The 100% scenario gives the minimum consecutive classes when every upcoming class is attended.'''

 



 



