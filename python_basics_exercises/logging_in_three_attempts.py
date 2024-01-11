#Program gives user three attempts to log in using correct password.

for i in range(1, 4):
    print("\nLogin attempt no.:", i)
    password = input("Password: ")

    if password == "testpassword":
        print("Hello user!")
        break

    else:
        if 3-i == 0:
            print("Incorrect password, no more attempts :-(")
        else:
            print("Incorrect password. Attempts left:", 3-i)
    
#ending
input("\n\nPress Enter to finish.")