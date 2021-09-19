import json
from typing import cast
from classes import Car, Client, Driver, Order, Partner
import re


clients = [Client(87463337829,"Mark"),
           Client(58385748334,"Steave")]
cars = [Car("Audi","red", "x 345 xx", "new"),
        Car("Lada","green","a xxx aa", "old")]
drivers = [Driver(4.6,"Nikolay", 8493665582),
           Driver(3.9,"Kostya", 834936573)]
partners = [Partner("Didi"), Partner("Sitymobil")]

orders = [Order(344,"xxxxxx", "high","12.07.2021 13:44",clients[0], drivers[0]),
          Order(323,"xxxxx1x", "avarage","12.07.2020 13:44", clients[0], drivers[0])]

db = {
"db" : {
    "clients":list({"phone":client.phone,
                    "name":client.name} for client in clients),

    "drivers":list({"mark":driver.mark,
                    "name":driver.name,
                    "phone":driver.phone} for driver in drivers),

    "cars":list({"clas":car.clas,
                 "color":car.color,
                 "number":car.number,
                 "repair":car.repair} for car in cars),

    "orders":list({"price":oder.price,
                   "rate":oder.rate,
                   "demand":oder.demand,
                   "time":oder.time,
                   'client':{'phone':oder.client.phone,
                             'name':oder.client.name },
                    'driver':{'mark':oder.driver.mark,
                              'name':oder.driver.name,
                              'phone':oder.driver.phone}} for oder in orders),

    "partner":list({"partner":partner.legal} for partner in partners)
}
}

#data = json.dumps(db)
#print(data)
with open('./data.json', 'w', encoding='utf8') as f:
    json.dump(db, f)
