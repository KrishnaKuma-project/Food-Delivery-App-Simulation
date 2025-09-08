import small_function as SM

id=["kk"]
password=["kk1"]

def login():
    global name_input

    name_input=input("Enter Your Name : ")
    login_id_input=input("Enter The ID : ")
    login_password_input=input("Enter The Password : ")

    if login_id_input in id and login_password_input in password:
        print("Verification Completed. ")
        return True
    else:
        print("You Entered Invalid Input, Please Try Again. ")
        SM.loading(5)
        return login()
    


def create_account():
    create_id_input=input ("Enter Your ID To Confirm : ")
    create_password_input= input ("Enter Your Password To Confirm : ")

    id.append(create_id_input)
    password.append(create_password_input)

    SM.loading(5)
    print("Your ID And Password Created.")
    SM.sleep(0.7)

    return True