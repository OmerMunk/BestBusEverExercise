import random
import copy


class Ride:

    def __init__(self, departure, arrival, driver=None, delays=[]):
        """
        A constructor for a ride object
        :param departure: The time of the departure
        :param arrival: The time of the arrival
        :param driver: The name of the driver
        :param delays: A list of strings that represent reported delays by passengers
        """
        self.id = str(random.randint(1000,9999))
        self.departure = departure
        self.arrival = arrival
        self.driver = driver
        self.delays = delays

    def get_ride(self):
        """
        :return: The ride as an object
        """
        return self.id, self.departure, self.arrival, self.driver, self.delays

    def ride_no_driver(self):
        """
        A function that creates a copy of the ride without the drivers name, to print it publicly
        :return: a copy of the ride, without the drivers name
        """
        public_ride = copy.deepcopy(self)  # Using deep copy to prevent aliasing
        public_ride.driver = None
        return public_ride

    def add_delay(self, delay):
        """
        A function that adds string with a delay report to the delay's list
        :param delay: A string with a delay details reported by a passenger
        :return: The ride with the added delay
        """
        self.delays.append(delay)
        return self


    def __str__(self):
        """
        A print function for ride
        :return: All the details of a ride for a manager, and all the details of a ride besides the driver's name, for a passenger
        """
        if self.driver is None:  # A private printing to hide the driver's name from the passenger
            return (f"Ride id is: {self.id}, departure time: {self.departure}, arrival time: {self.arrival}, delays: {self.delays}")
        else:  # A public printing for managers
            return f"Ride id is: {self.id}, departue time: {self.departure}, arrival time: {self.arrival}, name of driver: {self.driver}, delays: {self.delays}"

    def __repr__(self):
        return str(self)
