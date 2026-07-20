defect_count = int(input("Enter defect count: "))
machine_temperature = float(input("Enter machine temperature (°C): "))
production_speed = float(input("Enter production speed (units/hour): "))
operator_experience = int(input("Enter operator experience (years): "))
if defect_count > 50:
    print("Batch Status: Rejected")
elif machine_temperature > 80 and production_speed > 100:
    print("Batch Status: Risk")
elif operator_experience < 2 and defect_count > 20:
    print("Batch Status: Warning")
else:
    print("Batch Status: Accepted")