def get_recommendation(data):
    rec = {"diet": [], "exercise": [], "ayurveda": [], "warnings": []}

    glucose = data["Glucose"]
    bmi = data["BMI"]
    age = data["Age"]
    bp = data["BloodPressure"]

    #High glucose

    if glucose > 140:
        rec["diet"].append("Avoid sugar, sweets, and refined carbs")
        rec["ayurveda"].append("Fenugreek seeds, Bitter gourd juice")
        rec["warnings"].append("High blood sugar detected")



    # High BMI
    if bmi > 25:
        rec["diet"].append("Low-carb, high-fiber diet")
        rec["exercise"].append("30–45 min daily walking")
        rec["ayurveda"].append("Triphala for metabolism")

    # High BP
    if bp > 90:
        rec["diet"].append("Reduce salt intake")
        rec["exercise"].append("Yoga, breathing exercises")
        rec["ayurveda"].append("Ashwagandha for stress")

    #Age Factor
    if age > 45:
        rec["warnings"].append("Age-related risk increased")
        rec["exercise"].append("Regular health checkups")

    return rec