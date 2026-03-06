class Profile:
    name="susmi"
    location="atp"
    password="123456"

    def alert(self):
        print("password is incorrect")
    def create_profile(self,name,password):
        self.name=name
        self.password=password
        

p1=Profile()
p2=Profile()

p1.create_profile("hari","192435")
#p1.name="yamuna"3
p2.name="varsha"
p1.alert()

        
print(p1.name)
print(p1.password)
print(p2.name)
print(p2.password)
    
    
