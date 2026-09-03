def assign_triage_room():
    """
    Inputs   : severity of condition (whole number 1-10)
    Process  : 1-4  -> Waiting Room
               5-7  -> Room 1
               8-10 -> Room 2
    Output   : triage summary with severity and assigned room
    """
    print("\n--- Assign Triage Room ---")
 
    while True:
        severity_input = input("Enter severity of condition (1-10): ").strip()
        if not severity_input.isdigit():
            print("Error: Severity must be a whole number between 1 and 10. Please try again.")
            continue
        severity = int(severity_input)
        if severity < 1 or severity > 10:
            print("Error: Severity must be between 1 and 10. Please try again.")
        else:
            break
 
    if 1 <= severity <= 4:
        room = "Waiting Room"
    elif 5 <= severity <= 7:
        room = "Room 1"
    else:  # 8 to 10
        room = "Room 2"
 
    print("\nTriage assigned successfully!")
    print(f"Severity Level  : {severity}")
    print(f"Assigned Room   : {room}")