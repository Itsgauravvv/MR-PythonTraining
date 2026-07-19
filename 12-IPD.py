age = int(input("Enter customer age: "))
smoke = input("Do you smoke? (yes/no): ").lower()
bmi = float(input("Enter BMI: "))
disease = input("Do you have a severe pre-existing disease? (yes/no): ").lower()

if disease == "yes" and age > 60:
    print("Insurance Status: Rejected")
elif smoke == "yes" and age > 50:
    print("Insurance Premium: High Premium")
elif bmi >= 25:
    print("Insurance Premium: Medium Premium")
elif age < 30 and smoke == "no" and bmi < 25 and disease == "no":
    print("Insurance Premium: Low Premium")
else:
    print("Insurance Premium: Standard Premium")