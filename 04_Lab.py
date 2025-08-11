

# #!  Encapsulation (Veri Gizleme)
# #?bir sınıfın her hangi bir üyesini encapsule ettiğimiz zaman iligili üyenin sınıf dışından erişimini engellemiş oluyoruz. Yani ilgili üye sadece sınıf içerisinde kullanılabilir durumda olur 
# #*Peki encapsule edilmiş üyeye değer atamak istersek ne yapacağız? Bu durumda ilgili sınıf üye yada üyelerine dolaylı yoldan erişililebilir. Hata belirli kurallara koyarak erişimi kurala bağlıda yapabiliriz



# from uuid import uuid4
# from datetime import datetime
# from socket import gethostname , gethostbyname
# from enum import Enum
# from pprint import pprint


# class status(Enum):
#     Active=1
#     Modified=2
#     Passive=3



#     class BaseEntity:
#     # __ double underscore sembolü ile işaretlediğiniz üyelere alt sınıflardan erişemeyiz.
#         def _init_(self):
#             self.__id = ''
#             self.__create_date = ''
#             self.__ip_address = ''
#             self.__status = ''
#             self.__computer_name = ''

#     # encapsule edilmiş alanlara değerlerini set ettik yani onlara value atadık.
#     def set_values_private_attribute(self):
#         self.__id = uuid4()
#         self.__create_date = datetime.now()
#         self.__status = Status.Active.name
#         self.__computer_name = gethostname()
#         self.__ip_address = gethostbyname(gethostname())

# class Product(BaseEntity):
#     def __init__(self , name :str , description:str):
#         super().__init__()
#         self.description = description
#         self.name= name
#         self.__price=0.0
#         self.__stock=0


#     def set_product_values(self, price:float , stock:int):
#         #*kuraldoğrultusunda encapsule edilmiş olanlara erişim 
#         if price > 0 and stock > 0:
#             super().set_values_private_attribute()
#             self.__price=price
#             self.__stock=stock
#             print("product has been created..!")
#             pprint(self.__dict__)
#         else:
#             print("invalid price and stock values..!") 

# p1 = Product(name="everlast training gloves", description="everlast training gloves") 
# p1.set_product_values(price=12.99 , stock=100)  



# # b1 = BaseEntity()
# # b1.set_values_private_attribute()

# # # _dict_ ile private alanlar gözükmeyebilir, varsayılan dictionary gösterimi yapılır.
# # print(b1._dict_)



 
        