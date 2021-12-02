class Route:
    """
    A class that represent a route of a bus
    """
    def __init__(self, line_number, origin, destination, list_of_stops, scheduled_rides={}):
        """
        A constructor of a route object
        :param line_number: The number of the route line
        :param origin: The origin of the route
        :param destination: The final destination of the route
        :param list_of_stops: The stops along the route
        :param scheduled_rides: A dictionary that contains the details of the rides schedule
        """
        self.line_number = line_number
        self.origin = origin
        self.destination = destination
        self.list_of_stops = list_of_stops.split(',')
        self.scheduled_rides = scheduled_rides

    def get_route(self):
        """
        :return: The line number of the route
        """
        return self.line_number, self.origin

    def set_origin(self, new_origin):
        """
        Updates he origin of the desired route
        :param new_origin:
        """
        self.origin = new_origin

    def set_dest(self, new_dest):
        """
        Updates the destination of the desired route
        :param new_dest:
        """
        self.destination = new_dest

    def set_stops(self, new_stops):
        """
        Updates the stops list of the desired route
        :param new_stops:
        """
        new_stops= new_stops.split(',')
        self.list_of_stops = new_stops

    def set_rides(self, new_ride):
        """
        Add a new ride to a specific route
        :param new_ride:
        """
        self.scheduled_rides.update({new_ride.id: new_ride})

    def get_rides(self):
        """
        :return: The rides of a specific route
        """
        return self.scheduled_rides

    def __str__(self):
        """
        A print function
        :return: A string with all the details of the route
        """
        if self.scheduled_rides == {}:
            # The print method if the route doesnt have any rides
            return f"The line number is {self.line_number}, \n" \
                   f"the origin is: {self.origin}, the destination is: {self.destination},\n" \
                   f" the list of stops is:{self.list_of_stops}\n" \
                   f"there are no scheduled rides currently.\n"
        else:
            # The print method if the route has at least 1 ride
            return f"The line number is {self.line_number}, \n" \
                   f"the origin is: {self.origin}, the destination is: {self.destination},\n" \
                   f" the list of stops is:{self.list_of_stops}\n" \
                   f" the scheduled rides are: {self.scheduled_rides}\n"

    def __repr__(self):
        """
        A function that enables to print a collection of routes, each route will be printed with the __str__ function.
        """
        return str(self)
