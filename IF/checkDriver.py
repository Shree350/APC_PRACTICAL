dr = input("Enter a married status: ").lower()
if dr == "married" :
    print("Driver is insured")
else:
    gender = input("Enter a gender : ").lower()
    age = int(input("Enter a age : "))
    
    if(gender == "male" and age > 30):
        print("Driver is insured")
    elif(gender == "female" and age > 25):
        print("Driver is insured")
    else :
        print("Driver is not insured")
        
        
        
        