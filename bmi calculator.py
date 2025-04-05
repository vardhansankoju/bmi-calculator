print("BMI calculator ")
wegiht=float(input("enter your weigth in kg:"))
height=float(input("enter your heigth in meters:"))
bmi=wegiht/(height*2)
print(f"your BMI is {bmi:.2f}")
if bmi<18.5:
    print("your underweight")
elif bmi<23:
    print("your at normal weight")
elif bmi<27:
    print("your overweigth, I think you need to hit the gym")
else:
    print("your obese")