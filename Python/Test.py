def calculateBMI(height, weight):
    bmi = int(weight)/(int(height)/100)**2
    return bmi
print("*** BMI Calculation ***")
def getInput():
    print("Enter height(cm) weight(kg) : ",end='')
    return input()

def bmiConclusion(bmi):
    if bmi < 18.5 :
        print("underweight")
    elif 18.5 <= bmi and bmi < 25 :
        print("normal")
    elif 25 <= bmi and bmi < 30 :
        print("overweight")
    elif 30 <= bmi and bmi < 35 :
        print("obase")
    else :
        print("extremely obase")
   
height, weight = getInput().split()
bmi = calculateBMI(height, weight)
print("Your BMI is %.2f" %bmi)
print(bmiConclusion(bmi))