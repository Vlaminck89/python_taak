# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 11:50:33 2025

@author: thoma
"""


class Customer:
    def __init__(self, first_name, last_name, mail, phone, address):
        self._first_name = str(first_name)
        self._last_name = str(last_name)
        self._mail = str(mail)
        self._phone = str(phone)
        self._address = str(address)

    def voeg_customer_toe(self, conn):
        try:
            cur = conn.cursor()
            query = '''
            INSERT INTO customers (first_name, last_name, mail, phone, address)
                    VALUES (?, ?, ?, ?, ?)
                    '''
            parameters = (self._first_name, self._last_name,
                          self._mail, self._phone, self._address)
            cur.execute(query, parameters)
            conn.commit()
            print(f'Klant {self._first_name} {self._last_name} werd toegevoegd.')
        except Exception as e:
            print(f'Fout bij het toevoegen van de klant: {e}')

    def __str__(self):
        return ("Name: " + self._first_name + " " + self._last_name +
        "\nMail: " + self._mail +
        "\nPhone: " + self._phone +
        "\nAddress: " + self._address)
    
if __name__ == '__main__':
    c = Customer('Thomas', 'Vlaminck', 'thomasvlaminck89@gmail.com', '0473269619', 'Karel-Mestdaghstraat 71')
    print(c)