class car:
    def __init__(self,name,color,speed):
        self.name=name
        self.color=color
        self.speed=speed
    def start(self):
        print(self.name,"is starting....")
    def stop(self):
        print(self.name,"is stoping....")
    def details(self):
        print("Name:",self.name)
        print("color:",self.color)
        print("speed:",self.speed,"km/h")
name=input("Enter the name:")
color=input("Enter the color:")
speed=int(input("Enter the speed:"))
c1=car(name,color,speed)
print("===============CAR INFORMATION SYSTEM=================")
c1.start()
c1.details()
c1.stop()
    
