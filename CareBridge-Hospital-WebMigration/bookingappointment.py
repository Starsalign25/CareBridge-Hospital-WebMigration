from datetime import datetime, timedelta

# Ask for department
department = input("Enter department (GP or Specialist): ")

# Ask for appointment date
appointmentDate = input("Enter preferred appointment date (DD/MM/YYYY): ")

# Check if department is valid
validDepartment = (
    department == "GP" or department == "Specialist"
)

# Check if date is valid
try:
    appointment_date = datetime.strptime(
        appointmentDate, "%d/%m/%Y"
    ).date()

    today = datetime.today().date()

    # Appointment must be more than 7 days from today
    validDate = appointment_date > today + timedelta(days=7)

except ValueError:
    validDate = False


# Check the results
if validDepartment == False:
    print("Error: Department must be GP or Specialist.")

elif validDate == False:
    print("Error: Appointment date must be more than 7 days from today.")

else:
    print("Booking Successful!")
    print("Department:", department)
    print("Appointment Date:", appointmentDate)