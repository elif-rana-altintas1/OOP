
#! KALITIM
#?Biyolojide olduğu gibi bizler nasıl ebeveynlerimizden kalıtım yoluyla özellikler aldıysan yazılımda da kalıtım vasıtasıyla ata sınıflardan alt sınıflara özellikler aktarılabilir 
#?Kalıtım vasıtasıyla kod tekrarı engellenrek,özellikler tek bir merkeze dağıtılarak kontrol ve yönetim sağlanır .
#*Human sınıfı pyhton da built in olarak bulunan "object" sınıfından kalıtım almaktadır. Pyhton 3.0'dan sonra bunu belirtmeye gerek kalmamış
#*class Human (object):-->bu kullanıma gerek kalmamıştır.


# class Human:
#     def __init__(self , height:float, weight:float):
#         self.height = height
#         self.weight = weight

#     def show_information(self):
#         return self.__dict__ 

# #*Artık knight sınıfımız human sınıfından kalıtım yoluyla özellik kazandı  
# class Knight(Human):
#     pass

# class Rogue(Human):
#     pass
# k1=Knight(height=1.84 , weight=98)
# print(
#     k1.show_information()
# )
# g1=Rogue(height=2.01,weight=185)
# print(
#     g1.show_information()
#     )

# print(
#     dir(g1)
# )

#! Method overriding
#*Ata sınıflarda (parent class)bulunan methodların alt sınıflarda ezilerek onlara yeni işlevler kazandırmaya yada var olan yeteneklerinin yanına yeni yetenekler kazandırmaya denir 
# from uuid import uuid4
# from datetime import datetime
# from socket import gethostname , gethostbyname
# from enum import Enum
# from pprint import pprint

# class status(Enum):
#     Active=1
#     Modified=2
#     Passive=3
#*BaseEntity,CoreEntity,KernelEntity bu isimlendirmeye sahipo sınıflar ata sınıfalardır.Amaçları Kalıtım vermektir ve kalıtım verecekleri alt sınıfların ORTAK ÖZELLİKLERİNİ barındırırlar.
#?Bu örnekte Category ve product olmak üzere iki tane alt sınıfım olacaktır bu alt sınıfların ortak özellikleri nei ise sadece onları burada yazmalıyım
# class BaseEntity:
#     def __init__(self,name:str,description:str):

#         self.id=str(uuid4()) 
#         self.status=status.Active.name
#         self.create_date=datetime.now()
#         self.ip_adress= gethostbyname(gethostname())
#         self.machine_name=gethostname()
#         self.name=name
#         self.description=description
    
#     def show_info (self):
#        print(
#            f"name:{self.name}\n"
#            f"Description:{self.description}"
#        ) 
    
# class Category(BaseEntity):
#     pass

# class Product(BaseEntity):
#     def __init__(self, name, description,stock:int,price:float):
#         super().__init__(name, description) #*otomatik geldi overriding yaptı.
#         self.stock=stock
#         self.price=price
#     def show_info(self):
#          super().show_info()
#          print(
#              f"stock:{self.stock}\n"
#              f"price:{self.price}"
#          )

# c1=Category(
#     name="Boxing equipment",
#     description="best boxing equipment"
# )
# c1.show_info()
# print("============")
# p1=Product(
#     name="everlast training gloves",
#     description="everlast training gloves",
#     stock=100,
#     price=1.14
# )
# p1.show_info()

#*ÖRNEK
#BasePhone adında bir ata sınıfı oluşturalım.İd,brand, model,price object attribute olsun. Phone_ring_sounda()->"genel telefon sesi" string ifadesi dönecek,show_info()
#samsung adında bir sınıf oluşturalım BasePhone kalıtım alınacak.Camera object attribute.Phone_ring_sound()->"samsung telefon sesi" dönecek,shor_info()
#iphone adında bir sınıf oluşturualım BasePhone kalıtım alıcak. operating_system object attribute phone_ring_sound()->"iphone telefon sesi" döncek,show info()

# class BasePhone:
#     def __init__(self, id, brand, model, price):
#         self.id = id
#         self.brand = brand
#         self.model = model
#         self.price = price

#     def phone_ring_sound(self):
#         return "genel telefon sesi" 
    
#     def show_info(self):
#         print(f"ID: {self.id}")
#         print(f"Brand: {self.brand}")
#         print(f"Model: {self.model}")
#         print(f"Price: {self.price}") 

# class Samsung(BasePhone):
#     def __init__(self, id, brand, model, price,camera):
#           super().__init__(id, brand, model, price)
#           self.camera=camera

      
#     def phone_ring_sound(self):
#         return "samsung telefon sesi"

#     def show_info(self):
#         super().show_info()
#         print(f"Camera: {self.camera}")
    

# class Iphone(BasePhone):
#         def __init__(self, id, model, price, operating_system):
#             super().__init__(id, "iPhone", model, price)
#             self.operating_system = operating_system

#         def phone_ring_sound(self):
#             return "iphone telefon sesi"

#         def show_info(self):
#             super().show_info()
#             print(f"Operating System: {self.operating_system}")


# s1 = Samsung(id=101, model="Galaxy S21",brand="sas", price=25000, camera="108MP")
# i1 = Iphone(id=102, model="iPhone 14", price=45000, operating_system="iOS 17")

# print(s1.phone_ring_sound())   
# s1.show_info()

# print("=============================================")

# print(i1.phone_ring_sound())  
# i1.show_info()


#BaseBill sınıfımız olsun. bill_name,value_add_task , amount object attribute.
#calculate_bill()->value_add_task*amount
#create_log(),bill name,total amount yani calculate_bill sonucu,payment date bilgilerini log

#Elektrictiy_bill sınıfımız olsun.BaseBill'den kalıtım alsın 
#kw object attribute olsun
#calculate_bill->value_add_task * amount* kw

#NaturelGasBill sınıfımız olsun.BaseBill'den kalıtım alsın 
#m3 object attribute olsun
#calculate_bill->value_add_task * amount* m3

#WaterBill sınıfımız olsun.BaseBill'den kalıtım alsın 
#mill object attribute olsun
#calculate_bill->value_add_task * amount* mill

#Hint:Bu örnekte ata sınıftaki fonksiyonlardan hangileri override edilecek hangileri edilmeyecek bunu düşünerek soruyu çözün . çünkü her fonksiyonu override etmek için bir neden ihtiyacımız var .
from datetime import datetime



class BaseBill:
    def __init__(self, bill_name:str,value_add_task:float, amount:float):
        self.bill_name=bill_name
        self.value_add_task=value_add_task
        self.amount=amount
    def calculate_bill(self):
        return self.value_add_task * self.amount
    
    def show_info(self):
        print(f": bill_name{self.bill_name}")
        print(f"value_add_task: {self.value_add_task}")
        print(f"amount: {self.amount}")
    
    def create_log(self):
        with open(
            file="bill_log.txt",
            mode="a",
            encoding="utf-8"
        ) as file:
        
                file.write(
                    f"bill name: {self.bill_name}\n"
                    f"total amount:{self.calculate_bill}\n"
                    f"payment date:{datetime.now()}\n"
                    f"===============================\n"
            )

        print(f"{self.bill_name} has been paymented...")




class  Elektrictiy_bill(BaseBill):
    def __init__(self, bill_name, value_add_task, amount , kw:float):
        super().__init__(bill_name, value_add_task, amount)
        self.kw=kw

    def calculate_bill(self):
        return self.value_add_task * self.amount *self.kw
    
    def show_info(self):
        print(f": bill_name{self.bill_name}")
        print(f"value_add_task: {self.value_add_task}")
        print(f"amount: {self.amount}")
        print(f"kw:{self.kw}")

class  NaturelGasBill(BaseBill):
    def __init__(self, bill_name, value_add_task, amount,m3:int):
        super().__init__(bill_name, value_add_task, amount)
        self.m3=m3

    def calculate_bill(self):
        return self.value_add_task * self.amount *self.m3
    
    def show_info(self):
        print(f": bill_name{self.bill_name}")
        print(f"value_add_task: {self.value_add_task}")
        print(f"amount: {self.amount}")
        print(f"m3:{self.m3}")

  
class  WaterBill(BaseBill):
    def __init__(self, bill_name, value_add_task, amount,mill:int):
        super().__init__(bill_name, value_add_task, amount)
        self.mill=mill

    def calculate_bill(self):
        return self.value_add_task * self.amount *self.mill
    
    def show_info(self):
        print(f": bill_name{self.bill_name}")
        print(f"value_add_task: {self.value_add_task}")
        print(f"amount: {self.amount}")
        print(f"m3:{self.mill}")


e1=Elektrictiy_bill(
    bill_name="BEDAŞ",
    value_add_task=45.6,
    amount=12.5,
    kw= 34.5
)
e1.create_log


n1=NaturelGasBill(
    bill_name="İGDAŞ",
    value_add_task=56.7,
    amount=98.9,
    m3=12000

)




        
