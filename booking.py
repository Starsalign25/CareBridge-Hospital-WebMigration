from datetime import datetime, timedelta


def book_appointment():
    print("\n--- Book Appointment ---")

    # Ask for department
    while True:
        department = input("Enter department (GP or Specialist): ").strip()

        if department == "GP" or department == "Specialist":
            break
        else:
            print("Error: Please enter GP or Specialist.")

    # Ask for appointment date
    while True:
        appointment_date = input(
            "Enter appointment date (DD/MM/YYYY): "
        ).strip()

        try:
            appointment_date = datetime.strptime(
                appointment_date, "%d/%m/%Y"
            ).date()

            current_date = datetime.now().date()
            maximum_date = current_date + timedelta(days=7)

            if current_date < appointment_date <= maximum_date:
                break
            else:
                print("Error: Appointment must be within the next 7 days.")

        except ValueError:
            print("Error: Please enter the date in DD/MM/YYYY format.")

    # Display booking details
    print("\nAppointment Booked Successfully!")
    print("Department:", department)
    print(
        "Appointment Date:",
        appointment_date.strftime("%d/%m/%Y")
    )


# Run the function
book_appointment()