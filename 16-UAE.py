exam_score = float(input("Enter entrance exam score: "))
percentage_12 = float(input("Enter 12th percentage: "))
category = input("Enter category (General/OBC/SC/ST): ").lower()
extra_score = float(input("Enter extracurricular score (out of 10): "))

if exam_score >= 90 and percentage_12 >= 85:
    print("Admission Status: Direct Admission")

elif category in ["sc", "st", "obc"] and exam_score >= 80 and percentage_12 >= 75:
    print("Admission Status: Direct Admission (Category Relaxation)")
elif exam_score >= 70 and extra_score >= 8:
    print("Admission Status: Waitlisted")
else:
    print("Admission Status: Rejected")