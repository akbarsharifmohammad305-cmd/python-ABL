#Case Study 2: ATM Transaction Sequence Simulation

#1. Problem Statement
'''Process deposits and withdrawals, maintain a simulated account balance, reject invalid transactions and withdrawals that exceed limits, and display a transaction summary.'''


#2. Objectives
'''Process multiple transaction types.
   Prevent negative, invalid or over-limit withdrawals.
   Maintain balance and summarize successful and rejected transactions.'''


#3. Assumptions
'''Opening balance cannot be negative.
   Each withdrawal is limited to rupees 10,000 and cannot exceed the balance.
   Only positive transaction amounts are accepted.'''


#4. Algorithm
'''Step 1: Read opening balance and transaction count.
   Step 2: For each transaction, read type and amount.
   Step 3: Validate amount and apply deposit or withdrawal rules.
   Step 4: Record success or rejection and update totals.
   Step 5: Display closing balance and transaction summary.'''


#5. Flowchart
'''Start -> Read and validate input -> Process calculations and conditions -> Display results -> Stop'''
#6. Pseudocode
'''BEGIN
  READ balance, n
  FOR each transaction DO
      READ type, amount
      IF amount <= 0 THEN reject
      ELSE IF type = DEPOSIT THEN add amount to balance
      ELSE IF type = WITHDRAWAL AND amount <= 10000 AND amount <= balance
          subtract amount from balance
      ELSE reject
  END FOR
  PRINT balance and summary
END'''


#7. Python Source Code
balance = float(input("Opening balance (Rs): "))
n = int(input("Number of transactions: "))
withdrawal_limit = 10000
successful = rejected = 0
deposited = withdrawn = 0.0
 
if balance < 0 or n < 0:
    print("Invalid opening balance or transaction count.")
else:
    for i in range(n):
        kind = input(f"Transaction {i+1} (D=deposit/W=withdrawal): ").upper()
        amount = float(input("Amount (Rs): "))
        if amount <= 0:
            print("Rejected: amount must be positive.")
            rejected += 1
        elif kind == "D":
            balance += amount
            deposited += amount
            successful += 1
            print("Deposit successful.")
        elif kind == "W":
            if amount > withdrawal_limit:
                print("Rejected: withdrawal limit is Rs 10000.")
                rejected += 1
            elif amount > balance:
                print("Rejected: insufficient balance.")
                rejected += 1
            else:
                balance -= amount
                withdrawn += amount
                successful += 1
                print("Withdrawal successful.")
        else:
            print("Rejected: unknown transaction type.")
            rejected += 1
    print("\n--- Transaction Summary ---")
    print(f"Closing balance: Rs {balance:.2f}")
    print(f"Deposited: Rs {deposited:.2f}")
    print(f"Withdrawn: Rs {withdrawn:.2f}")
    print("Successful transactions:", successful)
    print("Rejected transactions:", rejected)


#8. Test Case and Expected Output
'''Example: opening balance rupees 5,000; 
            deposit rupees  1,000; 
            withdraw rupees 2,000;
            withdraw rupees 12,000.
            Closing balance = rupees 4,000;
            2 successful and 1 rejected transaction.
'''

#9. Conclusion
'''The simulation updates the account only when a transaction passes validation and provides a clear summary of the final balance and rejected requests.'''

 
