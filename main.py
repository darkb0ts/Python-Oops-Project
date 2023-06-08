from BikeRent import Bikers ,Customer
def main(data=0):
    lastdata=data
    Userlist=[]
    Hashmap=dict()
    loop=True
    BikersRent=Bikers(100)
    global idnumber
    idnumber=-1
    while loop:
        print("""
        ====== Bike Rental Shop =======
        1. Display available bikes
        2. Request a bike on hourly basis $5
        3. Return a bike
        4. show user detail in display
        5. Exit
        """)
        choice=input("enter the number: ")

        try:
            choice=int(choice)
        except ValueError:
            print("That's not an int!")
            continue
        if choice==1:
            BikersRent.display()
        elif choice==2:
            print("old user or new user: ")
            Old=int(input("Enter the New User[2]/Old user[1]: "))
            if Old==1:
                Oldidnumber=int(input("enter the id number: "))
                if Oldidnumber in Hashmap.keys():
                    fetchdata=Hashmap[Oldidnumber]
                    count=0
                    while True:
                        print("You can Update Your Profile Details")
                        print("""
                        ====== Update Profile =======
                        1. Edit Username
                        2. Edit Number of Bikes
                        3. Exit the Update Profile
                        """)
                        UpdateDetail=int(input("enter the Number you Want edit: "))
                        if count==5:
                            print("Multi Time Entered The Invaild Options")
                            break
                        if UpdateDetail==3:
                            break
                        elif UpdateDetail==1:
                            Username=input("Enter the Username: ")
                            fetchdata["Username"]=Username
                        elif UpdateDetail==2:
                            Num=int(input("enter the Number of Bikes: "))
                            FetchData[NumofBikes]=Num
                        else:
                            print("Invaild Options is Entered")
                            count+=1
                    print("Successfull Update Profile")
                    print(fetchdata)
                else:
                    print("invaild user id")
            elif Old==2:                                         #new user and add userlist and Userid to update detail
                name=input("enter the Username: ")
                NumofBikes=int(input("enter the number of bike: "))
                idnumber+=1
                User=Customer(name,idnumber,5,NumofBikes)
                Userlist.append(User)
                Hashmap[User.idnumber]={"UserID":User.idnumber,"Username":User.name,"UserRental":User.rental,"UserBike":User.NumofBike}
                BikersRent.rentBikeOnHourlyBasis(NumofBikes,User)
            else:
                print("invaild number you enter")  
        elif choice==3:
            idnum=int(input("enter the id number: "))
            if idnum in Hashmap.keys():
                FetchData=Hashmap[idnum]
                BikersRent.returnBike(FetchData)
            else:
                print("Are you sure you rented a bike with us?")
                continue
        elif choice==4:
            BikersRent.displayUserDetail(Userlist)
        elif choice==5:
            loop=False
        else:
            print("Invaild Number Your Entered???")
            continue
if __name__ == "__main__":
    main()






















































# class User:

#     def __init__(self, id, name, rental,time):
#         self.id = id
#         self.name = name
#         self.rental=rental
#         self.time=time

# # Create a list of users
# users = []

# # Create 10 users
# for i in range(1, 11):
#     users.append(User(i, "User " + str(i), "user" + str(i) + "@example.com",i+5))

# # Print the list of users
# # for user in users:
# #     print(user.id, user.name,user.rental, user.time)
