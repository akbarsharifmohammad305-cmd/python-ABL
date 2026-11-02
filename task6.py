#Case Study 6: Student Performance Trend Analysis

#1. Problem Statement
'''Compare subject marks across examinations, calculate improvements and declines, identify consistently weak subjects and classify each student.'''


#2. Objectives
'''	Compare first and latest examination marks.
	Identify subjects below the pass mark in every examination.
	Classify performance as Improving, Declining, Consistent or At Risk.'''


#3. Assumptions
'''	Marks are between 0 and 100; pass mark is 40.
	All examinations contain the same subjects in the same order.
	Two or more consistently weak subjects means At Risk; otherwise average change above 5 is Improving and below −5 is Declining.'''


#4. Algorithm
'''Step 1: Define subjects, pass mark and trend margin.
Step 2: Read each student's examination marks.
Step 3: Compare first and last marks subject by subject.
Step 4: Identify consistently weak subjects and calculate average change.
Step 5: Print changes, averages, weak subjects and classification.'''


#5. Flowchart
'''Start -> Read and validate input -> Process calculations and conditions -> Display results -> Stop'''

#6. Pseudocode
'''BEGIN
  SET subjects and pass mark
  FOR each student DO
      compare first and last examination marks
      identify subjects below pass mark in every examination
      change <- last average - first average
      IF weak subjects >= 2 THEN At Risk
      ELSE IF change > 5 THEN Improving
      ELSE IF change < -5 THEN Declining
      ELSE Consistent
      PRINT report
  END FOR
END'''


#7. Python Source Code
subjects = ("Maths", "Physics", "Chemistry", "English", "Python")
PASS_MARK = 40
TREND_MARGIN = 5
 
students = [
    ("Asha", [[55, 60, 48, 70, 65], [62, 66, 52, 72, 70],
              [70, 71, 58, 75, 78]]),
    ("Ravi", [[80, 75, 70, 68, 90], [72, 70, 65, 60, 84],
              [65, 62, 60, 58, 80]]),
    ("Meena", [[35, 38, 50, 60, 45], [30, 36, 55, 62, 48],
               [38, 39, 52, 61, 50]])
]
 
for name, exams in students:
    first, last = exams[0], exams[-1]
    weak = [subjects[i] for i in range(len(subjects))
            if all(exam[i] < PASS_MARK for exam in exams)]
    print("\nStudent:", name)
    print(f"{'Subject':<12}{'First':>7}{'Last':>7}{'Change':>9}")
    for i, subject in enumerate(subjects):
        change = last[i] - first[i]
        print(f"{subject:<12}{first[i]:>7}{last[i]:>7}{change:>+9}")
    first_avg = sum(first) / len(first)
    last_avg = sum(last) / len(last)
    diff = last_avg - first_avg
    if len(weak) >= 2:
        category = "At Risk"
    elif diff > TREND_MARGIN:
        category = "Improving"
    elif diff < -TREND_MARGIN:
        category = "Declining"
    else:
        category = "Consistent"
    print(f"Average: {first_avg:.2f} -> {last_avg:.2f} ({diff:+.2f})")
    print("Consistently weak:", ", ".join(weak) if weak else "None")
    print("Classification:", category)


#8. Test Case and Expected Output
'''Test data includes rising marks, 
   falling marks and consistently weak subjects. 
   Asha is Improving, Ravi is Declining, 
   and Meena is At Risk.'''

#9. Conclusion
'''The program uses lists, loops and conditions to show score trends and highlight students who may need academic support.'''





 



