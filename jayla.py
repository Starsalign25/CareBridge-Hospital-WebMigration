def calculate_bill():
    base_fee = 100
    lab_test_rate = 10

    # Get valid patient type
    while True:
        patient_type = input("Enter patient type (Subsidised / Private): ").strip().capitalize()
        if patient_type != "Subsidised" and patient_type != "Private":
            print("Error: Invalid patient type.")
        else:
            break

    # Get valid number of lab tests
    while True:
        num_lab_tests_input = input("Enter number of lab tests completed: ").strip()
        if not num_lab_tests_input.isdigit():
            print("Error: Enter a valid whole number.")
        else:
            num_lab_tests = int(num_lab_tests_input)
            break

    # Calculate subtotal
    subtotal = base_fee + (num_lab_tests * lab_test_rate)

    # Apply discount if applicable
    if patient_type == "Subsidised":
        total = round(subtotal * 0.70, 2)
    else:
        total = round(subtotal, 2)

    # Display results
    print("\n----- Bill Summary -----")
    print("Patient Type:", patient_type)
    print(f"Number of Lab Tests: {num_lab_tests}")
    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Total Amount to Pay: ${total:.2f}\n")


if __name__ == "__main__":
    calculate_bill()