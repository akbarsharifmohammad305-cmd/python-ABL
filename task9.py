#Case Study 20: University Admission Decision Engine

#1. Problem Statement
'''Evaluate applicants using subject eligibility, aggregate marks, course-specific thresholds and tie-breaking rules, then produce a ranked list of eligible applicants.'''


#2. Objectives
'''Check subject and aggregate eligibility.
    Apply course-specific cutoffs.
    Rank eligible applicants using aggregate marks and entrance score as tie-breakers.'''


#3. Assumptions
'''	Applicants provide aggregate marks, required subject marks and entrance score out of 100.
	Course cutoffs are sample rules and should be changed to match official admission policy.
	Ranking uses aggregate descending, then entrance score descending, then name alphabetically.'''


#4. Algorithm
'''Step 1: Define course-specific aggregate and subject cutoffs.
Step 2: Read applicant details and preferred course.
Step 3: Check all eligibility conditions.
Step 4: Store eligible applicants with ranking fields.
Step 5: Sort and print the ranked list and rejected applicants' reasons.'''


#5. Flowchart
'''Start -> Read and validate input ->Process calculations and conditions -> Display results ->Stop'''


#6. Pseudocode
'''BEGIN
  DEFINE course cutoff rules
  READ applicants
  FOR each applicant DO
      check subject and aggregate requirements
      IF all conditions met THEN add to eligible list
      ELSE record reason
  END FOR
  SORT eligible by aggregate, entrance score, name
  PRINT ranked eligible list and rejection reasons
END'''


#7. Python Source Code
rules = {
    "CSE": {"aggregate": 75, "subject": 70},
    "ECE": {"aggregate": 65, "subject": 60},
    "MECH": {"aggregate": 55, "subject": 50}
}
n = int(input("Number of applicants: "))
eligible = []
 
for i in range(n):
    print(f"\nApplicant {i+1}")
    name = input("Name: ")
    course = input("Course (CSE/ECE/MECH): ").upper()
    aggregate = float(input("Aggregate percentage: "))
    subject = float(input("Required subject percentage: "))
    entrance = float(input("Entrance score (0-100): "))
 
    if course not in rules:
        print("Rejected: unknown course.")
        continue
    if not (0 <= aggregate <= 100 and 0 <= subject <= 100
            and 0 <= entrance <= 100):
        print("Rejected: marks must be between 0 and 100.")
        continue
 
    cutoff = rules[course]
    reasons = []
    if aggregate < cutoff["aggregate"]:
        reasons.append(f"aggregate below {cutoff['aggregate']}%")
    if subject < cutoff["subject"]:
        reasons.append(f"subject marks below {cutoff['subject']}%")
    if reasons:
        print("Not eligible:", ", ".join(reasons))
    else:
        eligible.append((aggregate, entrance, name, course))
        print("Eligible for ranking.")
 
eligible.sort(key=lambda x: (-x[0], -x[1], x[2].lower()))
print("\n--- Ranked Eligible Applicants ---")
if not eligible:
    print("No eligible applicants.")
else:
    for rank, (aggregate, entrance, name, course) in enumerate(eligible, 1):
        print(f"{rank}. {name} | {course} | Aggregate: {aggregate:.2f}% "
              f"| Entrance: {entrance:.2f}")

        
#8. Test Case and Expected Output
'''Example: CSE applicant with aggregate 82%, 
            subject marks 78% and entrance score 88 is eligible. 
            A CSE applicant with aggregate 70% is rejected under the sample cutoff.'''


#9. Conclusion
'''The decision engine applies transparent course rules and ranks eligible candidates using stated tie-breakers. The cutoff values are illustrative and must be replaced with official requirements.'''




 



