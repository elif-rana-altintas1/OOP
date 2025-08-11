from abc import ABC, abstractmethod
from datetime import datetime

# Soyut fatura sınıfı
class BaseBill(ABC):
    def __init__(self, bill_name: str, value_add_task: float, amount: float):
        self.bill_name = bill_name
        self.value_add_task = value_add_task
        self.amount = amount

# Su faturası
class WaterBill(BaseBill):
    def __init__(self, bill_name, value_add_task, amount, mill: int):
        super().__init__(bill_name, value_add_task, amount)
        self.mill = mill

# Doğalgaz faturası
class NaturelGasBill(BaseBill):
    def __init__(self, bill_name, value_add_task, amount, m3: int):
        super().__init__(bill_name, value_add_task, amount)
        self.m3 = m3

# Soyut servis sınıfı
class BaseService(ABC):
    @abstractmethod
    def calculate_bill(self, bill: BaseBill) -> float:
        pass

    def create_log(self, bill: BaseBill, bill_amount: float):
        with open("log_bill.txt", "a", encoding="utf-8") as file:
            file.write(
                f"bill name: {bill.bill_name}\n"
                f"total amount: {bill_amount}\n"
                f"payment date: {datetime.now()}\n"
                f"===============================\n"
            )
        print(f"{bill.bill_name} has been paymented...")

# Su servisi
class WaterBillService(BaseService):
    def calculate_bill(self, bill: WaterBill) -> float:
        return bill.amount * bill.value_add_task * bill.mill

# Doğalgaz servisi
class NaturalGasBillService(BaseService):
    def calculate_bill(self, bill: NaturelGasBill) -> float:
        return bill.amount * bill.value_add_task * bill.m3

# Kullanım
water_bill = WaterBill("İSKİ", 0.15, 200, 50)
water_service = WaterBillService()
result = water_service.calculate_bill(water_bill)
water_service.create_log(bill=water_bill, bill_amount=result)
