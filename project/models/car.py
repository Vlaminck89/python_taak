# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 22:20:10 2025

@author: thoma
"""


class Car:
    def __init__(self, brand, model, year, license_plate, price):
        self._brand = str(brand)
        self._model = str(model)
        self._year = int(year)
        self._license_plate = str(license_plate)
        self._price = float(price)
        
    def voeg_klant_toe(self, conn):
        try:
            cur = conn.cursor()
            query = '''
            INSERT INTO cars (brand, model, year, license_plate, price)
            VALUES (?, ?, ?, ?, ?)
            '''
            parameters = (self._brand, self._model, self._year, self._license_plate, self._price)
            cur.execute(query, parameters)
            conn.commit()
            print(f'{self._brand} {self._model} met nummerplaat {self._license_plate} is toegevoegd.')
        except Exception as e:
            print(f'Fout bij het toevoegen van de auto: {e}')
            
    def __str__(self):
        return ("Brand: " + self._brand +
        "\nModel: " + self._model +
        "\nYear: " + str(self._year) +
        "\nlicense plate: " + self._license_plate +
        "\nPrice: €" + str(self._price))


if __name__ == '__main__':
    car = Car('BMW', '330E', 2023, '2-DEB-213', 200)

    print(car)
