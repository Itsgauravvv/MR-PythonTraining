issue_severity = input("Enter issue severity (critical/high/medium/low): ").lower()
department = input("Enter department: ")
business_impact = input("Enter business impact (high/medium/low): ").lower()
vip_user = input("Is the user a VIP? (yes/no): ").lower()

if issue_severity == "critical" and vip_user == "yes":
    print("Ticket Priority: P1")
elif issue_severity == "critical" and business_impact == "high":
    print("Ticket Priority: P1")
elif issue_severity == "medium":
    print("Ticket Priority: P3")
elif issue_severity == "low":
    print("Ticket Priority: P4")
else:
    print("Ticket Priority: P2")