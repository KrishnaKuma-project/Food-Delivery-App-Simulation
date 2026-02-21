import login_verification as login 
import random
import time
import small_function as SM
#import main_function as main

order_detail_list=[]
order_count=0

order_detail_earnings=[]
order_earnings=0

def order_detail():
    global order_detail_list
    global order_earnings
    global earning_calculator

    customer_details={
        1:"K. RAJARAMAN, Flat No. 5, Victoria Garden, 106, J.N. Salai,Koyambedu, Chennai - 600107",
        2:"G. RAMAMOORTHY, No.5, 12th Main Road, Vijaya Nagar,Velacheri, Chennai - 600 042",
        3:"P. KRISHNANANDA RAO, No. 17, Velmurugan Colony,Vadapalani , Chennai - 600 026 ",
        4:"K. AIYAPPAN, 21, Sabari Street, Nesapakkam, K.K. Nagar West, Chennai - 600 078"
        } 
    
    restaurants_details={
        1:"R&G - GreenPark Chennai, 183 N.S.K. Salai, Arcot Rd, Vadapalani Hotel Green Park, Chennai (Madras) 600026 India",
        2:"Southern Spice, Mahatma Gandhi Road Lobby Level, Taj Coromandel, Chennai, Chennai (Madras) 600034 India",
        3:"Waterside, 4/129, Mount Poonamallee Road Feathers Hotel, Manappakkam, Chennai (Madras) 600089 India",
        4:"The Reef, 280 ECR, Vadanamelli Sheraton Grand Chennai Resort & Spa, Chennai (Madras) 603104 India"
    }

    cus_detail=random.choice(list(customer_details.values()))
    res_detail=random.choice(list(restaurants_details.values()))
    order_detail_list.append({cus_detail:res_detail})

    print("\n")
    print("Restaurant Details : ".center(68))
    print(res_detail)
    SM.sleep(1.5)

    try:
        restaurants_confirmation=int(input("After You Pick Food From Restaurant Enter 1 : "))
        if restaurants_confirmation==1:
            print("Food Pickup Confirmation Is Accpeted.")
            pickup_confirmation=1

            if pickup_confirmation==1:
                print("\n")
                print("Customer Details : ".center(68))
                print(cus_detail)
                SM.sleep(1.2)

                delivery_comfrimation_input=int(input("If Food Delivery Completed Enter 1 : "))

                if delivery_comfrimation_input==1:
                    for i in range (0, 6):
                        print(f"Please Wait We Checking. {i+1}",end="\r")
                        time.sleep(1)
                    print("Thank You, Your order Marked as Completed.")

                    earning_calculator=random.randint(35,80)
                    order_detail_earnings.append(earning_calculator)
                    order_earnings+=earning_calculator

                    print(f"\nYour Total Earnings In This Order ₹{earning_calculator}")

                    return True
        
        elif restaurants_confirmation!=1:
            print("You Enter The Invalid Input Please Try Again. ")
            SM.sleep(1.5)
            return restaurants_confirmation
        
        else:
            print("Something Went Wrong Please Try Again. ")
            SM.sleep(1)
            return restaurants_confirmation

    except ValueError:
        print ("You Given Wrong Input, only Numbers can be enter .")
        SM.sleep(1)
        return 


def order():
    global order_count
    print("\n")
    print("You Received A order!!!!".center(68))
    print("\n")
    try:
        order_confirmation=int(input("""1 For Accept
2 For Reject 
Enter The Number Here : """))
        
        if order_confirmation==1:
            order_count+=1
            print(f"Thank You For order confirmation {login.name_input}")
            order_detail()
            return True

        elif order_confirmation==2:
            order_count+=1
            print (f"You Are Rejected The Order {login.name_input}\n")
            print ("If You Reject More Order You Will Get Penalty.\n")
            order_time=random.randint(6,13)
            for i in range (0,13):
                if i!=order_time:
                    print(f"Waiting For Order... {i+1}",end="\r")
                    time.sleep(1)
            order()


        else:
            print("Something Went Wrong We Restarting The Task Please Wait. ")
            SM.loading(5)

    except ValueError:
        print("Something Went Wrong We Restarting The Task Please Wait. ")
        SM.loading(5)
        