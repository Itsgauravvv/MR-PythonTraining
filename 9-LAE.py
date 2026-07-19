mon_sal = int(input("Enter your monthly salary: "))
cred_score = int(input("Enter your credit score: "))
ela = int(input("Enter your existing loan amount: "))
emp_tpe = input("Enter your employment type: ")

if mon_sal > 80000 and cred_score > 750 and ela < 20000:
    print("Loan Status : Approved Immediately.")
elif mon_sal > 50000 and cred_score > 650:
    print("Loan Status : Approved with caution.")
elif cred_score < 600:
    print("Loan Status : Rejected.")
else: 
    print("Loan Status : Under Manual Review.")
