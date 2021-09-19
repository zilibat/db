class Driver:
    def __init__(self, mark, name, phone) -> None:
        self.mark = mark
        self.name = name
        self.phone = phone

class Client:
    def __init__(self,phone,name) -> None:
        self.phone = phone
        self.name = name


class Partner:
    def __init__(self,legal) -> None:
        self.legal = legal

class Order:
    def __init__(self,price,rate,demand,time, client, driver) -> None:
        self.driver = driver
        self.client = client
        self.price = price
        self.rate = rate
        self.demand = demand
        self.time = time

class Car:
    def __init__(self,clas,color,number,repair) -> None:
        self.clas = clas
        self.color = color
        self.number = number
        self.repair = repair