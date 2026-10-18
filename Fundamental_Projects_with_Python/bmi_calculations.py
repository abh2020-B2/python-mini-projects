# import and global variables


# getting user inputs as height and weight
def get_user_inputs():
    weight = float(input("enter your weight (kg): "))
    height = float(input("enter your height (m): "))
    return height,weight


# calculate BMI 
def calculte_bmi(weight,height):
    return weight / (height ** 2)

# get the BMI result 
def get_bmi_result(bmi):
    print(f"bmi : {bmi}\nresult:")
    if bmi < 18.5:
        print("Under Weight")
    elif  18.5 <= bmi < 25:
        print("Normal")
    elif 25 <= bmi < 30:
        print("Over Weight")
    elif 30 <= bmi < 35:
        print("Obese")
    else:
        print("Extremely Obese")

# create main function runner
def main():
    weight , height = get_user_inputs()
    bmi = calculte_bmi(weight=weight , height=height)
    get_bmi_result(bmi=bmi)

if __name__ == '__main__':
    main()