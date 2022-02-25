# class Dad:
#     cricket = 1
# class Son(Dad):
#     dance =1
#     def isdance(self):
#         return f"I dance {self.dance} number of times"
# class GrandSon(Son):
#    dance =6
#    def isdance(self):
#        return f"I dance {self.dance}  more than my father"
# hari = Dad()
# arun = Son()
# shivam = GrandSon()
#
# print(shivam.dance)
class ElectronicsDevice:
    pcb = True
    cpu = True
    price = 5000
    size = "Huge"
    hdmi =  "its in TV"
    brand = "LG"
class PocketDevice(ElectronicsDevice):
    size = "small"
    GPS = True
    price = 350
    headphonejack = True
    brand = "Apple"
class Phone(PocketDevice):
    price = 1500
    size = "Apple_Size"
    headphonejack = False

TV = ElectronicsDevice()
Ipod = PocketDevice()
Iphone = Phone()


print(TV.price)
print(Ipod.cpu)
print(Iphone.brand)
