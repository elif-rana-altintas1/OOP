
#!ABSTRUCTİON (soyutlama)
#? OOP konuları arasında en en önenmli olanıdır.Çünkü üst seviyeli yazılım prensiplerine ve tasarım desenlerine uymak istiyorsak " soyutlama kullanmak zorundayız."
#*soyutlama yapısına uymak istiyorsak ilk önce ata sınıfımız abstract olarak işaretlenir daha sınıflarımızın içerisindeki üyeleri abstract member yaparak hem sınıfı hem de sınıf içi üyeler abstraction uyguluyotuz.Böylellikle üst sınıf ile alt sınıf arasında sözleşme imzalamış bir başka değiş ile alt sınıflara kural koymuş oluyor.


from abc import ABC, abstractmethod

class BaseMuzikAleti:
    def __init__(self,model:str,brand:str):
        self.model= model
        self.brand=brand

class Gitar(BaseMuzikAleti)  :
    def __init__(self, model, brand,tel:str):

        super().__init__(model, brand)
        self.tel = tel

class Keman(BaseMuzikAleti):
    def __init__(self,model:str,brand:str , kasa:str):
        super().__init__(model,brand)
        self.kasa= kasa
       



class Muzisyen:
    def __init__(self,firstname:str, lastname=str):

        self.firstname=firstname
        self.lastname=lastname
        self.caldigi_enstrumanlar=list()
#*BaseServise sınıfı "ABC(abstract base class)" sınıfından kalıtım olarak soyut (abstract) bir sınıf olmuştur.
#*aşağıda enstruman_sesi() fonksiyonu "@abstractmethod" dekarotörü ile dkore edilerek ilgili method soyutlaştırılmıştır.ve bu fonksiyon artık alt sınıflarda kullanılmak zorundadır.
#!pyhton da çok fazla sayıda dekoretör vardır kendi ihtiyaçlarınıza göre custom yazılabilir 
#todo burada methodun gövdesini neden boş bıraktık.çünkü bu fonksiyon alt sınıflarda override edilmeye zorunludur.bu bağlamda her alt sınıfın kendi ihtiyaçlarına göre dizayn edilecek bu fonksiyona ata sınıfta gövde yazmak mantıksızdı.

@abstractmethod
class BaseService(ABC):
    def enstruman_sesi(self)->str:
        pass

    @abstractmethod
    def harmonize (self) -> str:
        pass
    def log (self)-> str:
        return "kayıt tutuldu" 

class GitarService(BaseService) :
    def enstruman_sesi(self):
        return "gitar sesi"
    def harmonize(self):
        return " akor edildi"
    
class KemanService(BaseService) :
    def enstruman_sesi(self):
        return "gitar sesi"
    def harmonize(self):
        return " akor edildi" 
    
#! sınıfların kendine has methodları yazılabilir
    def hello_everyone(self):
        return " kimseyi selamlamak istemiyorum"
    
def main(): 
    gitar_service= GitarService()
    keman_service=KemanService()

    gitar = Gitar("fender","classicel gitar", "kaliteli tel")
    keman = Keman ("godrigez","classicel","meşe")


    muzisyen=Muzisyen(" Burak , Yılmaz")
    muzisyen.caldigi_enstrumanlar.append(gitar)
    muzisyen.caldigi_enstrumanlar.append(keman)


    print(
        f"ad: {muzisyen.firstname}\n"
        f"soyad: {muzisyen.lastname}\n"
        f"çaldığı enstrüman: {muzisyen.caldigi_enstrumanlar[0].brand}\n"
        f"çaldığı enstrüman: {muzisyen.caldigi_enstrumanlar[0].model}\n"
        f"çıkardığı ses: {gitar_service.enstruman_sesi()}\n"
            f"akor durumu: {gitar_service.harmonize()}\n"

    ) 
main()









g1=GitarService() 
