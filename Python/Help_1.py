def calculateBMI(height, weight):
    return int(weight)/((int(height)/100)**2)
def getInput():
    return input(" *** BMI Calculation ***\nEnter height(cm) weight(kg) : ")
def bmiConclusion(bmi):
    if bmi < 18.5 :
        return "You're underweight."
    elif 18.5 <= bmi < 25 :
        return "You're normal."
    elif 25 <= bmi < 30 :
        return "You're overweight."
    elif 30 <= bmi < 35 :
        return "You're obese."
    else :
        return "You're extremely obese."
height, weight = getInput().split()
bmi = calculateBMI(height, weight)
print("Your BMI is %.2f" %bmi)
print(bmiConclusion(bmi))