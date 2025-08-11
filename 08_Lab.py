

from abc import ABC , abstractmethod


class CreditCard:
    def __init__(self):
        self.bank_name=""
        self.card_limit=""
        self.card_type=""
        self.installment_shopping=""


class CreditCardBuilder(ABC):
    def __init__(self):
        self._credit_card = CreditCard()


    @property
    def credit_card(self) -> CreditCard:
        return self.credit_card
    @abstractmethod
    def card_limit_func(self) -> str : pass

    @abstractmethod
    def card_limit_func(self) -> int : pass 

    @abstractmethod
    def card_type_func(self) -> str : pass

    @abstractmethod
    def installment_shopping_func(self) -> bool : pass
 

class AmericanExpressCard(CreditCardBuilder):
    def __init__(self):
        super().__init__()
        self._credit_card=super().credit_card

    def bank_name_func(self) :
        self._credit_card.bank_name = "Garanti"
        return self._credit_card.bank_name
    
    def card_limit_func(self):
        self.credit_card.card_limit=1000000
        return self._credit_card.card_limit
    
    def card_type_func(self):
        self.credit_card.card_type="American express"
        return self._credit_card.card_type
    
    def installment_shopping_func(self):
        self._credit_card.installment_shopping=True
        return self.credit_card.installment_shopping
    



#*MASTER CARD YAPALIM
class VisaCard(CreditCardBuilder):



    def __init__(self):
        super().__init__()
        self._credit_card=super().credit_card

    def bank_name_func(self) :
        self._credit_card.bank_name = "iş bankası"
        return self._credit_card.bank_name
    
    def card_limit_func(self):
        self.credit_card.card_limit=10000000
        return self._credit_card.card_limit
    
    def card_type_func(self):
        self.credit_card.card_type="visa "
        return self._credit_card.card_type
    
    def installment_shopping_func(self):
        self._credit_card.installment_shopping=True
        return self.credit_card.installment_shopping
    




class Creator:
    @staticmethod
    def create_credir_card(credit_card_builder:CreditCardBuilder):
        print(
            f"bank name:{credit_card_builder.bank_name_func()}\n"
            f"card limit:{credit_card_builder.card_limit_func()}\n"
            f"card type:{credit_card_builder.card_type_func()}\n"
            f"installment:{credit_card_builder.installment_shopping_func()}\n"

        )
def main():
    Creator.create_credir_card(AmericanExpressCard)
    Creator.create_credir_card(VisaCard)

main()   