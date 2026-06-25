def login():
    print("===== ADMIN LOGIN =====")

    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username == "admin" and password == "admin123":
        print("Login Successful!")
        return True
    else:
        print("Invalid Username or Password")
        return False

if __name__ == "__main__":
    login()
    