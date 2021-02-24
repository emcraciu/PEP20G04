"""
A shoe factory needs an iterable object to keep track of shoes produces by each worker each day.
Each worker has a string name and each shoe has an int serial number.
Object will have an instance variable tha will keep track of workers trying to cheat in the form of a list of names.
Iterating the object will return the serial numbers produced that day by all workers

1) 40p: Definition
    a) 5p: Class with constructor that receives the date in the format you desire
    b) 25p: Method for adding work done by worker
        - 5p: argument: 5p
            - 1 receives worker name as string
            - 2 receives series produced as list of ints
        - 10p: using this method more then once for the same worker allows the worker to add new values but not
            retransmit old values .In case existing value is entered by two workers a specific exception
            (DuplicateDataException - created by you) and inheriting ValueError will be raised.
            (ex name1: 100, 101; name1: 101, 102; results in exception DuplicateDataException) 10p
        - 10p: method validates that series introduced do not already belong to another worker. In case of conflict
            series will be removed from both workers and information will be added to instance variable that tracks
            cheating workers and then ValueError with message: "Conflict series: <series>, Workers: <nume1>, <nume2>"
            will be raised
    c) 10p: Iterating this object will return an instance of in iterator that will have all series produced that day

2) 40p: Execution:
    a) 10p: Create instance of class with date format you selected.
    b) 10p: Add data for the following workers:
        - Joe: 402, 403, 409
        - Ana: 399, 404, 405
        - Tim: 400, 401, 406
        - workerX: 406, 407, 408 - after adding workerX, workerX will have 407, 408 and Tim will have 400, 401
    c) 10p: Add data for Tim: 400, 401 and check that DuplicateDataException is raised
    d) 10p: Iterate the created object and save each value on a new line in a file

3) 20p: Documenting:
   a) 5p: type hints for all arguments (optional for returned values)
   a) 5p: module documentation
   b) 5p: class documentation for all classes
   c) 5p: method documentation for all methods
"""
from datetime import date


class DuplicateDataException(ValueError):
    pass


class Production:

    def __init__(self, date):
        """
        :param date: datetime.date oject
        """
        self.date = date
        self.workers = {}
        self.cheating_workers = []

    def add_work_done(self, new_worker_name: str, shoes_serial_numbers: list):
        """
        :param new_worker_name: string
        :param shoes_serial_numbers: list of shoes serial numbers
        :return:
        """
        if new_worker_name not in self.workers.keys():
            self.workers[new_worker_name] = []
            conflict = False
            for serial_number in shoes_serial_numbers:
                cheating_worker = self.check_conflicting_serial_number(serial_number)
                if not cheating_worker:
                    self.workers[new_worker_name].append(serial_number)
                else:
                    self.remove_serial_number_from_worker(cheating_worker, serial_number)
                    self.add_worker_to_cheaters_list(cheating_worker)
                    self.add_worker_to_cheaters_list(new_worker_name)
                    cheated_serial_number = serial_number
                    cheating_worker_name = cheating_worker
                    conflict = True
            if conflict:
                raise ValueError(
                    "Conflict series: {}, Workers: {}, {}".format(cheated_serial_number, cheating_worker_name,
                                                                  new_worker_name))
        else:
            print("Name already here. Let`s check if there are any duplicate series.")
            for serial_numb in shoes_serial_numbers:
                duplicate_series = self.check_duplicate_series(serial_numb, new_worker_name)
                if duplicate_series:
                    raise DuplicateDataException

    def check_conflicting_serial_number(self, serial_number: int):
        """
        :param serial_number: serial number to check if it was already added to one of the workers
        :return: False in case the serial number is new
                 name of the worker that previously introduced the serial number
        """

        for worker in self.workers.keys():
            if serial_number in self.workers[worker]:
                return worker

        return False

    def check_duplicate_series(self, serial_number: int, worker_name: str):
        """

        :param serial_number: int value of the serial number to look for
        :param worker_name: string that contains the name of the worker
        :return:
        """
        if serial_number in self.workers[worker_name]:
            print("Duplicate serial number found.")
            return True
        return False

    def remove_serial_number_from_worker(self, worker_name: str, serial_number: int):
        """
        :param worker_name: string name of worker that first introduced the conflicting serial number
        :param serial_number: int conflicting serial number
        :return:
        """
        self.workers[worker_name].remove(serial_number)

    def add_worker_to_cheaters_list(self, worker_name: str):
        """
        :param worker_name: name of the cheating worker
        :return:
        """
        if worker_name not in self.cheating_workers:
            self.cheating_workers.append(worker_name)

    def print_cheating_workers(self):
        """
        :return:
        """
        if len(self.cheating_workers):
            print('Cheating workers: ' + ', '.join(self.cheating_workers))
        else:
            print('No cheating workers!')

    def __iter__(self):
        return self.cheating_workers


class CheatingNames:
    def __init__(self, cheating_workers: list):
        self.cheating_workers = cheating_workers
        pass

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.cheating_workers):
            return self.cheating_workers.pop(0)
        else:
            raise StopIteration


shoes_production = Production(date(2020, 12, 1))
shoes_production.add_work_done('Joe', [402, 403, 409])
shoes_production.add_work_done('Ana', [399, 404, 405])
shoes_production.add_work_done('Tim', [400, 401, 406])
try:
    shoes_production.add_work_done('workerX', [406, 407, 408])
except ValueError:
    pass

try:
    shoes_production.add_work_done('Tim', [400, 409])
except DuplicateDataException:
    pass

# shoes_production.print_cheating_workers()

cheaters_name_file = open('File_with_cheaters_names.txt', 'w+')
for cheating_workers_name in shoes_production.__iter__():
    cheaters_name_file.write(str(cheating_workers_name))
    cheaters_name_file.write("\n")

cheaters_name_file.close()
