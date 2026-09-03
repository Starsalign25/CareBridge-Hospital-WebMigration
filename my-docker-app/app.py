from flask import Flask, render_template, request
from datetime import datetime, date

app = Flask(__name__)


# -------------------------
# Home Page
# -------------------------

@app.route("/")
def home():
    return render_template("index.html")


# -------------------------
# Register Patient
# -------------------------

@app.route("/register", methods=["GET", "POST"])
def register_patient():

    if request.method == "GET":
        return render_template("register.html")

    name = request.form["name"].strip()
    age = request.form["age"].strip()
    patient_id = request.form["patient_id"].strip()

    if name == "":
        return render_template(
            "register.html",
            message="Please enter a patient name."
        )

    try:
        age = int(age)

        if age <= 0:
            return render_template(
                "register.html",
                message="Age must be a positive number."
            )

    except ValueError:
        return render_template(
            "register.html",
            message="Age must be a whole number."
        )

    if patient_id == "":
        return render_template(
            "register.html",
            message="Please enter a patient ID."
        )

    return render_template(
        "register.html",
        message=f"Patient registered successfully! "
                f"Name: {name}, Age: {age}, ID: {patient_id}"
    )


# -------------------------
# Book Appointment
# -------------------------

@app.route("/appointment", methods=["GET", "POST"])
def book_appointment():

    if request.method == "GET":
        return render_template("appointment.html")

    department = request.form["department"]
    appointment_date = request.form["appointment_date"]

    if department not in ["GP", "Specialist"]:
        return render_template(
            "appointment.html",
            message="Invalid department."
        )

    try:
        selected_date = datetime.strptime(
            appointment_date,
            "%Y-%m-%d"
        ).date()

    except ValueError:
        return render_template(
            "appointment.html",
            message="Invalid date."
        )

    today = date.today()
    days_difference = (selected_date - today).days

    if days_difference < 0 or days_difference > 7:
        return render_template(
            "appointment.html",
            message="Appointment must be within the next 7 days."
        )

    return render_template(
        "appointment.html",
        message=f"Appointment booked successfully! "
                f"Department: {department}, Date: {appointment_date}"
    )


# -------------------------
# Calculate Bill
# -------------------------

@app.route("/bill", methods=["GET", "POST"])
def calculate_bill():

    if request.method == "GET":
        return render_template("bill.html")

    patient_type = request.form["patient_type"]
    lab_tests = request.form["lab_tests"]

    try:
        lab_tests = int(lab_tests)

        if lab_tests < 0:
            return render_template(
                "bill.html",
                message="Number of lab tests cannot be negative."
            )

    except ValueError:
        return render_template(
            "bill.html",
            message="Lab tests must be a whole number."
        )

    BASE_FEE = 100
    LAB_TEST_RATE = 10

    subtotal = BASE_FEE + (lab_tests * LAB_TEST_RATE)

    if patient_type == "Subsidised":
        total = subtotal * 0.70
    else:
        total = subtotal

    return render_template(
        "bill.html",
        message=f"Patient Type: {patient_type} | "
                f"Total Bill: ${total:.2f}"
    )


# -------------------------
# Assign Triage Room
# -------------------------

@app.route("/triage", methods=["GET", "POST"])
def assign_triage():

    if request.method == "GET":
        return render_template("triage.html")

    severity = request.form["severity"]

    try:
        severity = int(severity)

        if severity < 1 or severity > 10:
            return render_template(
                "triage.html",
                message="Severity must be between 1 and 10."
            )

    except ValueError:
        return render_template(
            "triage.html",
            message="Severity must be a whole number."
        )

    if severity <= 4:
        room = "Waiting Room"

    elif severity <= 7:
        room = "Room 1"

    else:
        room = "Room 2"

    return render_template(
        "triage.html",
        message=f"Triage completed! Severity: {severity} | "
                f"Assigned Room: {room}"
    )


# -------------------------
# Run Website
# -------------------------

# if __name__ == "__main__":
#     app.run(debug=True)

if __name__ == '__main__':
    # Force the server to bind to all network interfaces
    app.run(host='0.0.0.0', port=5000)
