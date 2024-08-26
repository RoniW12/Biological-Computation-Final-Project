from itertools import product

# Define the states for activators and repressors
activator_order = ["NoActivators", "SomeActivators", "AllActivators"]
repressor_order = ["NoRepressors", "SomeRepressors", "AllRepressors"]

# Generate all possible combinations of activators and repressors
combinations = list(product(repressor_order, activator_order))

# Generate all 512 possible Boolean functions (2^9)
all_possible_functions = list(product([0, 1], repeat=len(combinations)))


# Function to check if a function is monotonic
def is_monotonic(function):
    # Exclude trivial cases where the function is always OFF or always ON
    if all(value == 0 for value in function) or all(value == 1 for value in function):
        return False

    # Check monotonicity by increasing activators
    for repressor_state in repressor_order:
        for i in range(len(activator_order) - 1):
            activator_1 = activator_order[i]
            activator_2 = activator_order[i + 1]
            index_1 = combinations.index((repressor_state, activator_1))
            index_2 = combinations.index((repressor_state, activator_2))
            if function[index_1] > function[index_2]:  # The gene turns off with more activators
                return False

    # Check monotonicity by decreasing repressors
    for activator_state in activator_order:
        for i in range(len(repressor_order) - 1):
            repressor_1 = repressor_order[i]
            repressor_2 = repressor_order[i + 1]
            index_1 = combinations.index((repressor_1, activator_state))
            index_2 = combinations.index((repressor_2, activator_state))
            if function[index_2] > function[index_1]:  # The gene turns off with fewer repressors
                return False

    return True


# Filter monotonic functions
monotonic_functions = [func for func in all_possible_functions if is_monotonic(func)]


# Function to translate binary function to descriptive format
def translate_function(function):
    conditions = []
    for i, value in enumerate(function):
        conditions.append(f"{combinations[i][0]} and {combinations[i][1]} -> {'ON' if value == 1 else 'OFF'}")
    return " | ".join(conditions)


expected_functions = [

    (0, 0, 1, 0, 0, 0, 0, 0, 0),
    (0, 1, 1, 0, 0, 0, 0, 0, 0),
    (0, 0, 1, 0, 0, 1, 0, 0, 0),
    (0, 1, 1, 0, 0, 1, 0, 0, 0),
    (0, 0, 1, 0, 0, 1, 0, 0, 1),
    (0, 1, 1, 0, 0, 1, 0, 0, 1),
    (0, 1, 1, 0, 1, 1, 0, 0, 0),
    (0, 1, 1, 0, 1, 1, 0, 0, 1),
    (0, 1, 1, 0, 1, 1, 0, 1, 1),
    (1, 1, 1, 0, 0, 0, 0, 0, 0),
    (1, 1, 1, 0, 0, 1, 0, 0, 0),
    (1, 1, 1, 0, 1, 1, 0, 0, 0),
    (1, 1, 1, 1, 1, 1, 0, 0, 0),
    (1, 1, 1, 0, 0, 1, 0, 0, 1),
    (1, 1, 1, 0, 1, 1, 0, 0, 1),
    (1, 1, 1, 1, 1, 1, 0, 0, 1),
    (1, 1, 1, 0, 1, 1, 0, 1, 1),
    (1, 1, 1, 1, 1, 1, 0, 1, 1)
    # Add all 18 expected functions in the correct order
]


# Check if the generated monotonic functions match the expected functions
def check_functions():
    for expected_function in expected_functions:
        if expected_function not in monotonic_functions:
            print(
                f"Expected function {translate_function(expected_function)} is not found in the generated monotonic functions.")
            return False
    print("All expected functions match the generated monotonic functions.")
    return True


if __name__ == '__main__':
    # Print the monotonic functions
    print("Monotonic Boolean functions:")
    for i, func in enumerate(monotonic_functions):
        print(f"Function {i + 1}: {translate_function(func)}")

    # Print the number of monotonic functions
    print(f"\nTotal number of monotonic functions: {len(monotonic_functions)}")

    # Run the check
    check_functions()
