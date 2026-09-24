# Day 12 — Python Logic and Functions
# Task: Build a Python utility using conditionals, loops, and functions.


# Exercise 1 — Grade Calculator
def calculate_grade(score):
    """
    Accepts a score from 0-100 and returns the appropriate letter grade.
    """
    if score >= 70:
        return 'A'
    elif score >= 60:
        return 'B'
    elif score >= 50:
        return 'C'
    elif score >= 40:
        return 'D'
    else:
        return 'F'


# Exercise 2 & 4 — Multiplication Table and Error Handling
def run_multiplication_tests(test_numbers):
    """
    Demonstrates the multiplication table loop using a provided list of test values.
    Includes error handling for non-numerical values.
    """
    print("\n=========================================")
    print("      EXERCISE 2 & 4: MULTIPLICATION      ")
    print("=========================================")
    
    for val in test_numbers:
        print(f"\n--- Processing Input Value: {val} ---")
        try:
            # Exercise 4: Attempt to convert input value to a float
            num = float(val)
            
            # Exercise 2: Print multiplication table 1 to 12
            for i in range(1, 13):
                result = num * i
                print(f"{num} x {i} = {result}")
                
        except ValueError:
            # Handle error gracefully when text is passed instead of a number
            print(f"ValueError Handled successfully: '{val}' is not a valid number.")


# Exercise 3 — Temperature Converter
def celsius_to_fahrenheit(celsius):
    """
    Receives a temperature in Celsius and returns the value converted to Fahrenheit.
    """
    return (celsius * 9 / 5) + 32


# Exercise 5 — Execution Orchestration 
def main():
    """
    Executes the exercises sequentially using pre-defined values to satisfy tasks 1-5.
    """
    # ----------------------------------------------------
    # Test Data Setup
    # ----------------------------------------------------
    test_scores = [85, 64, 52, 45, 30]  # Values targeting A, B, C, D, and F
    test_multiplications = ["7", "abc"]  # One valid integer, one invalid text string to trigger error handling
    test_celsius_temps = [0, 25, 100]    # Freezing, room temp, and boiling point values
    
    # ----------------------------------------------------
    # Run Exercise 1: Grade Calculator
    # ----------------------------------------------------
    print("=========================================")
    print("      EXERCISE 1: GRADE CALCULATOR       ")
    print("=========================================")
    for score in test_scores:
        grade = calculate_grade(score)
        print(f"Score: {score} -> Grade: {grade}")
        
    # ----------------------------------------------------
    # Run Exercise 2 & 4: Multiplication Table & Error Handling
    # ----------------------------------------------------
    run_multiplication_tests(test_multiplications)

    # ----------------------------------------------------
    # Run Exercise 3: Temperature Converter
    # ----------------------------------------------------
    print("\n=========================================")
    print("    EXERCISE 3: TEMPERATURE CONVERTER    ")
    print("=========================================")
    for celsius in test_celsius_temps:
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equivalent to {fahrenheit}°F")


if __name__ == "__main__":
    main()
