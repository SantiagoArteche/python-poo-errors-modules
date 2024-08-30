import numpy
import requests

number_handler = numpy.array([2,4,6,7,12,5,6,76])
print(number_handler + 2)
print(number_handler * 2 / 2  ** 4)

getMyApi  = requests.get('https://off-eccom.up.railway.app/api/products/').json()
products = [(prods['name'], prods['price'], prods['stock']) for prods in getMyApi['products']]

for i in products:
    print(f"[Name: {i[0]} Price: {i[1]} Stock: {i[2]}]")






