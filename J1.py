while True:
    try:
        severity = int(input("Enter severity (1-10): "))

        if 1 <= severity <= 10:
            break
        else:
            print("Invalid input. Enter a whole number from 1 to 10.")

    except ValueError:
        print("Invalid input. Enter a whole number from 1 to 10.")


if severity <= 4:
    room = "Waiting Room"
elif severity <= 7:
    room = "Room 1"
else:
    room = "Room 2"


print("Severity:", severity)
print("Assigned Room:", room)