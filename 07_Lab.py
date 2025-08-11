

# from abc import ABC, abstractmethod


# class BaseService(ABC):
#     @abstractmethod
#     def ship_from(self) -> str:
#         pass

# class SumatraService(BaseService):
#     def ship_from(self):
#         return "from sumatra island"
    
# class ColumbiaService(BaseService):
#     def ship_from(self):
#         return "from colombia"
    
# class SouthAfriicaService(BaseService):
#     def ship_from(self) ->str:
#         return "from sumatra island"


# class DefaultService(BaseService):
#     def ship_from(self) ->str:
#         return "shipment not avaliable"
# #!burada bir tasarım deseni anlattım.Fctory Design patten olarak bilinen ve creational design pattern gruba bulunan bu tasarım deseni bize nesnelerimizin yaratılışına müdahale etme imkanı sunar. hatta nesne otomatize erme fabrika gibi otomatik bir şekilde üretilmesini sağlar.

# class shipment:
#     @staticmethod
#     def shipment_method(month:int)-> BaseService:
#         if 4<= month <=7:
#             return ColumbiaService()
#         elif 8 <=month  <=11:
#             return SumatraService()
#         else:
#             if month == 1 or month ==2 or month ==12:
#                 return SouthAfriicaService()
#             else:
#                 return DefaultService()  
     

# def main ():
#     for month in range(1,13):
#        product_shipment=shipment.shipment_method(month=month)
#        print(f"coffe beans shipment {product_shipment.ship_from()}")

# main()  