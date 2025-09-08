import login_verification as login
import small_function as SM
import order_page
import random
import time

shift_value=[]

def shift_booking():

    try:
        shift_input=int(input("""\n1.5AM  - 10AM (RS 400 - RS 600 )
2.10AM - 3PM  (RS 600 - RS 1000)
3.3PM  - 6PM  (RS 300 - RS 500 )
4.6PM  - 11PM (RS 600 - Rs 1000)
5.11PM - 5AM  (RS 550 - RS 950 )
                              
Enter The Shift Number To Book : """))
        
        if shift_input not in shift_value:
            print("Shift booked Sucessfully. ")
            shift_value.append(shift_input)
            
        elif shift_input in shift_value:
            print("You Already Booked the Shift. Same Shift Can't Book For Second Time. ")
            SM.sleep(1)
            shift_booking()
        else:
            print("Soming Thing Went Wrong. Please Try Again. ")
            SM.sleep(1)
            shift_booking()

    except ValueError:
        print("Your Entered Invalid Input. Please Try Again (1-5) : ")
        SM.sleep(1)
        shift_booking()

online_status=[]

def go_online():

    try:
        if shift_value:
            if True not in online_status:
                print("After Going Online You Will Start Getting Orders. \n")
                SM.sleep(1)
                online_input=int(input("Enter 1 For Go online \nIf You Already in online Enter 2. \nEnter Here: "))
                if online_input==1:
                    online_status.append(True)
                    print("Your Now In Online Please Wait To Get Orders. ")
                    order_time=random.randint(6,9)
                    for i in range (0,13):
                        if i!=order_time:
                            print(f"Waiting For Order... {i+1}",end="\r")
                            time.sleep(1)
                            

                        else:
                            order_page.order()
                            while True:
                                try:
                                    input_for_next=int(input("""1. Go Offline and go to main menu 
2. Go For Next Order 
Enter Here : """))
                                    if input_for_next==1:
                                        break
                                    elif input_for_next==2:
                                        SM.loading(6)
                                        order_page.order()
                                    elif input_for_next>2:
                                        print("You Given Invalid Input, Please Try Again.")
                                        return input_for_next
                                    else:
                                        print("Somthing Went Wrong, Please Try Again")
                                except ValueError:
                                    print ("You Given Wrong Format Input, Please Try Again.")
                             
            else:
                print("\nyour Already In Online, Please Wait To Get Order.\n")
                print("We Redirect You Get Order.\n")
                SM.loading(7)
                order_page.order() #last ahh Ethula vitan 

        else:
            print("\nYou Not Booked Shift, So Please First Book The Shift.\nYour Redirecting To Shift Booking.")
            SM.loading(5)
            shift_booking()

    except ValueError:
        print("You Entered Invalid Input Please Try Again. ")
        SM.loading(5)
        go_online()
    

def earnings():
    print(f"\nYour Total Earning Today : {order_page.order_earnings}")
    try:
        earnings_input=int(input("""1.For Get Total Order Detail
2.For Get Total Order Earnings 
\nEnter The Number Here : """))
        if earnings_input==1:
            print(f"\nYour total Order Count : {order_page.order_count} \nYour total Order Detail : \n")
            count_increase=0
            for i in range (len(order_page.order_detail_list)):
                print (order_page.order_detail_list[count_increase])
                count_increase+=1
                print("\n")
            SM.loading(5)
            main()

        elif earnings_input == 2:
            if order_page.order_detail_earnings:
                print("Order Earnings List:")
                for earning in order_page.order_detail_earnings:
                    print(f"₹{earning}")
                print("\nYour Total Earnings =", sum(order_page.order_detail_earnings))
            else:
                print("No earnings yet. Please complete an order first.")
                SM.loading(5)
                main()

            
        
        elif earnings_input>2:
            print("You Entered Incorrect Input. Please Try Again.")
            SM.loading(3)
            main()

        else:
            print("You Entered Incorrect Input. Please Try Again.")
            SM.loading(3)
            main()

    except ValueError:
        print ("You Entered Invalid Input variable. Please Try Again.")
        

def help():
    print ("You are now in help page : ".center(68))
    try:
        help_input=int(input("""1.Contact administrator
2.View booked shift
3.Total order count and order earning

Enter the number here : """))
        if help_input==1:
            print("\nEmail ID : krishnakumar23070@gmail.com \nlinkedin : https://www.linkedin.com/in/krishnakumar-s-551b24322/ \n\nIf any help need please contact. ")
            SM.sleep(1.5)
            return main()
        elif help_input==2:
            if shift_value:
                print(f"Your booked shift number : {shift_value}")
                SM.sleep(1.5)
                return main()
            else:
                print("Your not booked any shift, book shift to get online. ")
                SM.sleep(1.5)
                return shift_booking()
        elif help_input ==3:
            print(f"\nYour total order count : {order_page.order_count} \nYour total order earnings : {order_page.order_earnings}")
            SM.sleep(1.5)
            return main()
        else:
            print("Something went worrng please try again. ")
            SM.sleep(1.5)
            print("\n")
            return help()
    except ValueError:
        print ("You given invalid input, Please try again.")
        SM.sleep(1.5)
        print("\n")
        return help()

def main():
    while True:
        try:
            main_input = int(input("""
1. Shift Booking
2. Go Online
3. Earnings
4. Help
5. Exit
Enter the Number (1-5): """))

            if main_input == 1:
                SM.sleep(0.5)
                shift_booking()

            elif main_input == 2:
                SM.sleep(0.5)
                go_online()

            elif main_input == 3:
                SM.sleep(0.5)
                earnings()

            elif main_input == 4:
                SM.sleep(0.5)
                help()

            elif main_input == 5:
                print("Thank you for using the delivery app. Goodbye!")
                break  

            else:
                print("Invalid input. Please enter a number from 1 to 5.")
                SM.sleep(1)

        except ValueError:
            print("Invalid input. Please enter numbers only (1-5).")
            SM.sleep(1)


def login_detail():

    try:
        print("\nTesting Purpose Default ID: kk, Password: kk1 \n")
        SM.loading(5)
        SM.sleep(0.8)
        detail_input=int(input("""Enter 1 for Login.
Enter 2 for create account : """))
        
        if detail_input==1:
                is_logged=login.login()
                if is_logged==True:
                    SM.sleep(1)
                    main()

        elif detail_input==2:
            SM.sleep(1.5)
            is_created=login.create_account()
            if is_created== True:
                print("Please Enter ID, Password To Login. ")
                is_logged=login.login()
                if is_logged==True:
                    SM.sleep(1)
                    main()
        else:
            print ("you entered Invalid input, Please Try Again. ")
            SM.loading(3)
            return login_detail()
        
    except ValueError:
        print("You Entered Invailed Input, Please enter Number's only (1-2). ")
        SM.loading(3)
        return login_detail()

login_detail()
