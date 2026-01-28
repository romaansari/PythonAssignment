# Steel Grading Program

# Input steel properties
hardness = float(input("Enter hardness of steel: "))
carbon_content = float(input("Enter carbon content of steel: "))
tensile_strength = float(input("Enter tensile strength of steel: "))

# Check conditions
condition1 = hardness > 50
condition2 = carbon_content < 0.7
condition3 = tensile_strength > 5600

# Determine grade
if condition1 and condition2 and condition3:
    grade = 10
elif condition1 and condition2:
    grade = 9
elif condition2 and condition3:
    grade = 8
elif condition1 and condition3:
    grade = 7
elif condition1 or condition2 or condition3:
    grade = 6
else:
    grade = 5

# Display the result
print(f"\nThe grade of the steel is: {grade}")
