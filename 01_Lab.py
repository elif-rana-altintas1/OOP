
#?Eğitimimizin bu safhasına kadar pyhton programlama dilinde built-in olarak bulunan objelerin yani nesneleri kullandık.
#*Örneğin int,dict,list,random etc.Artık OOP yaklaşımıyla kendi ihtiyaçlarımız doğrultusunda custom nesneler yaratabileceğiz
#! Pyhton programlama dilinde her şey objedir.Bizde artık kendi objelerimizi yaratabileceğiz.
#? Kendi objelerimizi yaratmak için önce "class" faydalanacağız.
#todo Sınıf (class) içerisinde yaratmak istediğimiz nesnenin(objenin) sahip olmasını istediğimiz özelliklerini yazıyoruz

# class Vehicle:
    #yaratmak istediğimiz objenin özelliklerini buraya yazıyoruz.
    #bu özelliklere attribute-features denir.
#     door_number=""
#     brand=""
#     model=""
#     engine_size=""

#?yukarıda tanımladığımız sınıftan faydalanarak artık objeler yaratabiliriz bu işleme "instance" yani örneklem almak denir

# Vehicle_1=Vehicle() #*şu an instance aldık yani vehicle serisinden örneklem çıkardık


#!artık vehicle_1 objemiz "vehicle" sınıfın sahip olduğu tüm özelliklere sahiptir.
# Vehicle_1.brand="dodge"
# Vehicle_1.model="TRX-1500"
# Vehicle_1.door_number="4"
# Vehicle_1.engine_size="V5.6"

# print(f"vehicle brand :{Vehicle_1.brand}")



#todo artık istediğimiz kadar vehicle yaratabiliriz nasıl ki istediğimiz kadar liste, sözlük, tuple yaratabiliyorsak.
#*örnek 1 
# Vehicle_2=Vehicle()
# Vehicle_2.brand="ford"
# Vehicle_2.model="ranger"
# print(f"vehicle brand :{Vehicle_2.brand}")

#*örnek 2
# class phone:
#     model=""
#     color=""
#     brand=""
#     GB=""
# phone=phone()
# phone.brand="samsung"
# phone.color="pink"
# phone.model="S20"
# phone.GB="128GB"

# print(f"phone brand :{phone.brand}")

#*örnek 3 
    #attribute'lere default değerler atayabiliyoruz.
    #Direk sınıf içerisine yazdığımız özelliklere "class attribute" denir.

# class boxer:
#     defance=80
#     attack=90
#     ring_iq=70


# b1=boxer()
# print(f'ring iq:{b1}')    

#?__init__() special function
#! init fonksiyonu ile sınıfımızı initialize etmeye yarar.Bir diğer görevi dışarıdan gelen değerleri almak ve bu değerlerin atanacağı attributeleri run time yaratmak ve assigned etmektir.

# class product:
#     #*class attribute
#     name=""
#     description=""

#     def __init__(self,price:float,stock:int):
#         #* object attributes
#         self.fiyat = price
#         self.stok = stock
       
# p1=product(price=1000, stock=5000)  
# p1.name="boxing gloves"
# p1.description="boxing goves"     
# print(
#     f"name:{p1.name}\n"
#     f"description:{p1.description}\n"
#     f"price:{p1.fiyat}\n"
#     f"stock:{p1.stok}"
# )
# #*dir()--> fonksiyonu bir yapının tüm özelliklerini ekrana yazdırır 
# print(dir(product)) #sınıfın özellikleri fiyat stok yok 
# print(dir(p1)) #onjenin özellikleri fiyat stok var 


#*örnek
# class make_up:
#     product_name=""
#     color=""

#     def __init__(self,price:float,stock:int):
        
#         self.price=price
#         self.stock=stock

# p1= make_up (price=1500,stock=2850)      
# p1.product_name="beauty gloss"
# p1.color="pink"
# print(
#     f"name:{p1.product_name}\n"
#     f"description:{p1.color}\n"
#     f"price:{p1.price}\n"
#     f"stock:{p1.stock}"
# )


#*örnek
#*circle isminde bir sınıf yaratalım 
#*pi adında bir class attribute olsun
#*r adında bir object olsun
#*area premitter hesaplayan iki ayrı fonksiyon olsun (pi=3.14)

# class circle:
#     pi=3.14

#     def __init__(self,radius:float):

#         self.r=radius
    
#     def area(self):
#         return self.pi * self.r **2
    
#     def premitter(self):
#         return 2*self.pi * self.r        

# c1=circle(radius=1.2)
# print(f"area:{c1.area()}")
# print(f"premitter:{c1.premitter()}")

#*örnek
#*softwareDeveloper adında bir sınıf yaratalım 
#*sınıfın first_name ,last_nem object attribute olsun
#*knowledge_language->list , class attribute olsun 
#*add_new_language(),bu fonksiyona verilecek olan 1 veya 1 den fazla programalama dilini ayrı ayro "knowledge" listesine eklesin
#*show_information() bu fonksiyonda ilgili yazılımcının bilgilerini çıktı versin 


# class softwareDeveloper:
#     knowledge_language=list()

#     def __init__(self, first_name:str,last_name:str):
#         self.first_name=first_name
#         self.last_name=last_name

#     def add_new_language(self, programming_language:str):
        

#         for item in programming_language.split(",") :
#             self.knowledge_language.append(item.strip())

        

#     def show_information(self):
#         return (
#             f"first name: {self.first_name}\n"
#             f"last name : {self.last_name}\n"
#             f"programming skills:{self.knowledge_language}"
#         )
    
# sd_1=softwareDeveloper(first_name="burak",last_name="yılmaz")
# sd_1.add_new_language(programming_language="pyhton")
# print(sd_1.show_information())
# sd_1.add_new_language(programming_language="c#,java,vb.net")    
# print(sd_1.show_information())

#*örnek
#*dikdörtgenin alanını ve çevresini hesaplayan bir sınıf hazırlayın


# class Rectangle:

#     def __init__(self, kısa_kenar:float, uzun_kenar:float):
#         self.kısa_kenar = kısa_kenar
#         self.uzun_kenar = uzun_kenar

#     def alan_hesaplama(self):
#         return self.kısa_kenar * self.uzun_kenar

#     def cevre_hesaplama(self):
#         return 2 * (self.kısa_kenar + self.uzun_kenar)

# r1 = Rectangle(kısa_kenar=3, uzun_kenar=6)

# print("Alan:", r1.alan_hesaplama())
# print("Çevre:", r1.cevre_hesaplama())




