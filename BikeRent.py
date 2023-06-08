class Customer:
    def __init__(self,name,idnumber,rental,NumofBike):
        self.name=name
        self.idnumber=idnumber
        self.rental=rental
        self.NumofBike=NumofBike
class Bikers():
    def __init__(self,stock=50):
        self.stock=stock
    def display(self):
        print("We have currently {} bikes available to rent.".format(self.stock))
        return self.stock
    def displayUserDetail(self,UserList):
            if len(UserList)<=0:
                print("UserList is emtry and Nothing")
            else:
                for Username in UserList:
                    print("Username : {} idnumber is : {} rental PriceNum : {} of Bike take Rent : {}".format(Username.name,Username.idnumber,Username.rental,Username.NumofBike))
    def rentBikeOnHourlyBasis(self, n,User):
        """
        Rents a bike on hourly basis to a customer.
        """
        if n <= 0:
            print("Number of bikes should be positive!")
            return None
        
        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
        
        else:                      
            print("You have rented a {} bike(s) and Username is -{} and ID - {}".format(n,User.name,User.idnumber))
            print("You will be charged $5 for each hour per bike.")
            print("We hope that you enjoy our service.")
            self.stock -= n
            return True
    def returnBike(self,data):
        """
        1. Accept a rented bike from a customer
        2. Replensihes the inventory
        3. Return a bill
        """
        print(data)
        print("Thanks for returning your bike. Hope you enjoyed our service!")
        print("Username is{} and UserID is {} and Bill is {}".format(data["Username"],data["UserID"],data["UserRental"]*data["UserBike"]))