# Ohm's Law Program with Current Classification

# Taking voltage and resistance as input
voltage = float(input("Enter voltage (V) in volts: "))
resistance = float(input("Enter resistance (R) in ohms: "))

# Calculating current using Ohm's Law: I = V / R
current = voltage / resistance

# Display the calculated current
print(f"\nCalculated Current (I) = {current:.2f} A")

# Determine and display the nature of current
if current < 0.5:
    print("Nature of Current: Low current")
elif 0.5 <= current <= 2:
    print("Nature of Current: Normal current")
else:
    print("Nature of Current: High current")
