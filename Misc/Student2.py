class Student():

    def  __init__(self, name, hometown, age, height, favorite_icecream_color):
        self.name= name
        self.hometown = hometown
        self.age = age
        self.height= height
        self.favorite_icecream_color= favorite_icecream_color

    def print_summary(self):
        print(" This students name is " + self.name + ".")
        print("He is from" + self.hometown + ".")
        print("He is " + self.age + " Years old.")
        print("His height is " + self.height + " cm.")
        print("His favorite icecream color is " + self.favorite_icecream_color)
              
