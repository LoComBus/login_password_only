def access():
    entered_password = input("Enter your password: ").lower()

    with open("database.txt", "r") as db:
        for line in db:
            password = line.strip()
            if password == entered_password:
                print("Access granted.")
                return

    print("Access denied. Incorrect password.")
    access()

access()


