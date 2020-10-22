class Car:

    def __init__(self , name , model , color):
        self.color=color
        self.name=name
        self.model=model

    def sshow(self):
        print("the car name is = " ,self.name, "the color = " , self.color , "the model = ", self.model)


if __name__ == '__main__':
    car1=Car("mercedes",2020,"red")
    car1.sshow()

    
