""" Homework 6 - needs to be presented before exam day
A car factory requires a class for an iterable object that can be used to keep track of car serial and lot numbers
produced in a certain day. A instance variable called "day" will record the date, in any format/value you prefer.
Lot number and serial number had values of 0 and 0 respectively for the first car produced.
Serial number is incremented with each car produced, lot number is incremented every 20 cars produced.
Each instance of the class will get constructor arguments the starting serial and number of cars produced for that day.
Your instance will need to calculate the lot numbers and serials produced in that specific day.
ex: Instance has start serial 30 and number of cars produced is 30 meaning resulting in serial numbers produced that day
are: 30, 31 ..59, 60 and lot numbers produced that day are 1, 2, 3 (serial 60 is part of lot 3)
Cars with odd serial number are right side driving cars and the cars with even serial number are left side driving cars.
Your instance will have methods for returning serial numbers for right side driving cars and left side driving cars.
Iterating the object will return the lot numbers produced that day
1) Implementation:
    a) Correct implementation of iterable object. 10P
    b) Correct implementation of iterator object. 10P
    c) Correct implementation of methods returning right and left side driving cars. 20P
2) Execution:
    a) Create object from class defined above using start serial 111 and number of cars produced 91. 10P
    b) Print all left hand and right hand serials for the object above: 10P
    c) Iterate the object created above and write the lot numbers on new lines in a file. 20P
3) Document:
   a) Add type hints for all arguments 5P
   a) Add module documentation 5P
   b) Add document all classes 5P
   c) Add document all methods 5P
"""

from datetime import date

class Production:

    def __init__(self, starting_serial_nr, total_cars_produced):
        """
        :param starting_serial_nr: starting serial number of cars produced today
        :param total_cars_produced: the total number of cars produced today
        self.serial -> list with all the serial numbers of cars produced today
        self.lot -> list with all the lot numbers produced today
        self.day -> variable with today's date
        """
        self.serial = list()
        self.lot = list()
        self.day = date.today().strftime('%d/%m/%Y')
        self.starting_serial_nr = starting_serial_nr
        self.total_cars_produced = total_cars_produced
        Production.todays_serial_and_lot_numbers(self)

    def todays_serial_and_lot_numbers(self):
        """
        serial_number -> variable used to get the serial number of each car.
                        It starts from 0 to total_cars_produced+1 and it used to increment the starting_serial_number,
                        which is append then to the serial list.
        copy_total_cars_produced -> copy of total cars produced today
        copy_serial_numbers -> copy of the starting serial number from today
        copy_serial_numbers is also how many cars were produced until today (because the count starts from 0)
        so we check if it is divisible by 20. If it is it means that the lots done were full and the integer division -1
        (because lot numbers starts from 0) is the number of lots done until today and lot_number takes the value of the
        integer division. Then we start to count lots by adding 1 in lot_number and decrese cars produced today by 20 (20 cars in a lot)
        if copy_serial_numbers is not divisible by 20 we check the full lots done by today. the lot number starts so from
        that nr +1 because we start a new lot which is added to te list and then we calculate the remains cars to add to lots
        after the lot is complete.
        """
        for serial_number in range(self.total_cars_produced + 1):
            self.serial.append(self.starting_serial_nr + serial_number)
        print("The serial numbers from today are: ", self.serial)
        copy_total_cars_produced = self.total_cars_produced
        copy_serial_numbers = self.starting_serial_nr
        if copy_serial_numbers % 20 == 0:
            lot_number = copy_serial_numbers / 20 -1
            while copy_total_cars_produced > 0:
                lot_number += 1
                copy_total_cars_produced -= 20
                self.lot.append(lot_number)
                self.lot.sort()
        else:
            full_lots_until_today = (copy_serial_numbers // 20) - 1
            lot_number = full_lots_until_today + 1
            cars_to_complete_lot = self.starting_serial_nr - lot_number * 20
            copy_total_cars_produced = self.total_cars_produced - cars_to_complete_lot
            while copy_total_cars_produced > 0:
                lot_number += 1
                copy_total_cars_produced -= 20
                self.lot.append(lot_number)
                self.lot.sort()
        print("The lot numbers from today are:", self.lot)

    def left_handed_cars(self):
        """
        left_handed_cars is created as an empty list which will later incorporate all even the serial numbers of cars produced today
        We iterate through serial list and extract each car serial number and encapsulate it into car_serial variable.
        car_serial will be checked if it is divisible by 2. If it is it means that the car is left handed so its serial will be appended
        to the left_handed_cars list
        """
        left_handed_cars = []
        for car_serial in self.serial:
            if car_serial % 2 == 0:
                left_handed_cars.append(car_serial)
        print("The serial numbers of left handed cars from today are:", left_handed_cars)

    def right_handed_cars(self):
        """
        right_handed_cars is created as an empty list which will later incorporate all even the serial numbers of cars produced today
        We iterate through serial list and extract each car serial number and encapsulate it into car_serial variable.
        car_serial will be checked if it is not divisible by 2. If it is it means that the car is left handed so its serial will be appended
        to the right_handed_cars list
        """
        right_handed_cars = []
        for car_serial in self.serial:
            if car_serial % 2 != 0:
                right_handed_cars.append(car_serial)
        print("The serial numbers of right handed cars from today are:", right_handed_cars)

    def __iter__(self):
        return self.lot


car_production = Production(111, 92)
car_production.left_handed_cars()
car_production.right_handed_cars()

lot_numb_file = open('File_with_lot_numbers', 'w+')
for lot_numb in car_production.__iter__():
    lot_numb_file.write(str(lot_numb))
    lot_numb_file.write('\n')
lot_numb_file.close()
