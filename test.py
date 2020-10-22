# python OBJECT ORIENTED PROGRAMMING
class Car:
    color =""
    Name=""
    model= 0

    def goForword(self):
        print("the is going forword")
        

    def goBack(self):
        print("the car is going back")

     
        

if __name__ == "__main__":
    car1=Car()
    car1.color="blue"
    car1.Name="mercedes"
    car1.model=2020
    car1.goForword()

    print(car1.color +"car color")

    
