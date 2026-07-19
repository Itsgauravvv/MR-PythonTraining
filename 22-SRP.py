monthly_usage = float(input("Enter monthly usage (hours): "))
missed_payments = int(input("Enter number of missed payments: "))
support_tickets = int(input("Enter number of support tickets: "))
satisfaction_score = float(input("Enter satisfaction score (out of 10): "))

if monthly_usage > 100 and satisfaction_score >= 8:
    print("Prediction: Likely to Renew")
elif monthly_usage < 30 and support_tickets > 5:
    print("Prediction: High Churn Risk")
elif missed_payments > 3:
    print("Prediction: Payment Risk")
else:
    print("Prediction: Moderate Renewal Probability")