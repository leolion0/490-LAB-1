class Person:
    def __init__(self, name, dob, ssn):
        self.name = name
        self._dob = dob
        self.__ssn = ssn


class Employee(Person):
    def __init__(self, name, dob, ssn, emp_num, isWorking, position, hRate):
        super().__init__(name, dob, ssn)
        self.emp_num = emp_num
        self.isWorking = isWorking
        self.position = position
        self.__hRate = hRate


class Passenger(Person):
    def __init__(self, name, dob, ssn, ticket_num, flight_num):
        super().__init__(name, dob, ssn)
        self.ticket_num = ticket_num
        self.flight_num = flight_num


class Flight:
    def __init__(self, arr_time, dep_time, arr_dest, dep_dest, flight_num):
        self.arr_time = arr_time
        self.dep_time = dep_time
        self.arr_dest = arr_dest
        self.dep_dest = dep_dest
        self.flight_num = flight_num
