def calculate_bill():
    print("\n--- Calculate Bill ---")

    # ---- Fees ----
    BASE_CONSULTATION_FEE = 100
    LAB_TEST_RATE = 10
    SUBSIDISED_DISCOUNT = 0.8   # 20% discount

    # ---- Patient Type ----
    valid_types = ("SUBSIDISED", "PRIVATE")

    while True:
        patient_type = input(
            "Enter patient type (Subsidised / Private): "
        ).strip()

        if patient_type.upper() not in valid_types:
            print(
                "Error: Patient type must be 'Subsidised' or 'Private'. "
                "Please try again."
            )
        else:
            break

    # ---- Number of Lab Tests ----
    while True:
        lab_tests_input = input(
            "Enter number of lab tests completed: "
        ).strip()

        if not lab_tests_input.isdigit():
            print(
                "Error: Number of lab tests must be a whole number. "
                "Please try again."
            )
        else:
            lab_tests = int(lab_tests_input)
            break

    # ---- Calculation ----
    subtotal = BASE_CONSULTATION_FEE + (lab_tests * LAB_TEST_RATE)

    if patient_type.upper() == "SUBSIDISED":
        total = subtotal * SUBSIDISED_DISCOUNT
    else:
        total = subtotal

    # ---- Output ----
    print("\nBill calculated successfully!")
    print(f"Patient Type : {patient_type.title()}")
    print(f"Total to Pay : ${total:.2f}")


if __name__ == "__main__":
    calculate_bill()