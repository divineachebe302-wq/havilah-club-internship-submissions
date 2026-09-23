# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.


# =====================================================================
# Exercise 1: Student Profile
# =====================================================================
#  information about an engineer
engineer_name = "Alex Mercer"       # String
engineer_id = 4042                 # Integer
experience_years = 4.5             # Float
is_active_project = True           # Boolean

# Display values with a descriptive label and their data types
print("--- Exercise 1: Profile Details ---")
print(f"Engineer Name: {engineer_name} | Data Type: {type(engineer_name)}")
print(f"Employee ID: {engineer_id} | Data Type: {type(engineer_id)}")
print(f"Years of Experience: {experience_years} | Data Type: {type(experience_years)}")
print(f"Active Status: {is_active_project} | Data Type: {type(is_active_project)}")
print("\n" + "="*50 + "\n")


# =====================================================================
# Exercise 2: Basic Mathematical Operations
# =====================================================================
print("--- Exercise 2: Basic Calculator ---")

num1 = 15.5
num2 = 4.0

print(f"First Number: {num1}")
print(f"Second Number: {num2}")

# Calculating and printing arithmetic operations with clear labels
print(f"Sum: {num1} + {num2} = {num1 + num2}")
print(f"Difference: {num1} - {num2} = {num1 - num2}")
print(f"Product: {num1} * {num2} = {num1 * num2}")

# Handling division by zero safely
if num2 != 0:
    print(f"Quotient: {num1} / {num2} = {num1 / num2}")
    print(f"Remainder: {num1} % {num2} = {num1 % num2}")
else:
    print("Quotient: Undefined (Cannot divide by zero)")
    print("Remainder: Undefined (Cannot divide by zero)")
print("\n" + "="*50 + "\n")


# =====================================================================
# Exercise 3: Temperature Converter
# =====================================================================
print("--- Exercise 3: Temperature Converter ---")
# temperatures
celsius = 25.0
fahrenheit_input = 77.0

# Part 1: Celsius to Fahrenheit
fahrenheit_output = (celsius * 9 / 5) + 32
print(f"{celsius}°C is equal to {fahrenheit_output}°F")

# Part 2: Fahrenheit to Kelvin
kelvin_output = (fahrenheit_input - 32) * 5 / 9 + 273.15
print(f"{fahrenheit_input}°F is equal to {kelvin_output} K")
print("\n" + "="*50 + "\n")


# =====================================================================
# Exercise 4: Robot Sensor Monitor
# =====================================================================
print("--- Exercise 4: Robot Sensor Monitor Report ---")
# robot sensor data
robot_name = "Robo-Route X1"
robot_id = "R-908"
sensor_name = "LiDAR Pro"
sensor_reading = 45.2
operating_limit = 100.0

# Calculating the difference
reading_difference = operating_limit - sensor_reading

# Displaying a clearly formatted report
print("\n==================================")
print("       ROBOT SENSOR REPORT        ")
print("==================================")
print(f"Robot Name:      {robot_name}")
print(f"Robot ID:        {robot_id}")
print(f"Sensor Name:     {sensor_name}")
print(f"Sensor Reading:  {sensor_reading}")
print(f"Operating Limit: {operating_limit}")
print(f"Difference:      {reading_difference:.2f}")
print("==================================")


