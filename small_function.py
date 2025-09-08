import time 

def loading(a):
    for i in range (a,-1,-1):
        print(f"Please Wait We Are Loading {i}  Second.",end="\r")
        time.sleep(1)
    print("\n")

def sleep(a):
    time.sleep(a)

