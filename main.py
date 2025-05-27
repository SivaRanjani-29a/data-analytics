# main.py
# This file is for testing your calculate function.
# In a Gitpod environment, you would run this file using 'python3 main.py'

from mean_var_std import calculate

def run_tests():
    print("--- Running Tests for calculate() function ---")

    # Test case 1: Valid input (9 digits)
    try:
        example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        print(f"\nInput: {example_list}")
        result = calculate(example_list)
        print("Output:")
        for key, value in result.items():
            print(f"  '{key}': {value}")
        print("\nExpected Output (approximately):")
        print("{'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0], 'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667], 'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611], 'max': [[6, 7, 8], [2, 5, 8], 8], 'min': [[0, 1, 2], [0, 3, 6], 0], 'sum': [[9, 12, 15], [3, 12, 21], 36]}")
    except ValueError as e:
        print(f"Error for valid input: {e}")

    print("\n" + "="*50)

    # Test case 2: Invalid input (less than 9 digits)
    try:
        invalid_list_short = [1, 2, 3, 4, 5]
        print(f"\nInput: {invalid_list_short}")
        calculate(invalid_list_short)
    except ValueError as e:
        print(f"Caught expected error for short list: {e}")

    print("\n" + "="*50)

    # Test case 3: Invalid input (more than 9 digits)
    try:
        invalid_list_long = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print(f"\nInput: {invalid_list_long}")
        calculate(invalid_list_long)
    except ValueError as e:
        print(f"Caught expected error for long list: {e}") # This will also raise ValueError due to reshape

    print("\n" + "="*50)

    # Test case 4: Another valid input
    try:
        another_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        print(f"\nInput: {another_list}")
        result_another = calculate(another_list)
        print("Output:")
        for key, value in result_another.items():
            print(f"  '{key}': {value}")
    except ValueError as e:
        print(f"Error for another valid input: {e}")

    print("\n--- Tests Finished ---")

if __name__ == "__main__":
    run_tests()
