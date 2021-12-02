import copy


def search_route_by_num(num, routes):
    """
    A search function for a passenger to search route by its line number
    :param num: The line number to search
    :param routes: All the routes created
    :return: If it exists, the route with the line number selected
    """
    public_routs = copy.deepcopy(routes)
    if num in public_routs.keys():
        for ride in public_routs[num].scheduled_rides:
            public_routs[num].scheduled_rides[ride] = public_routs[num].scheduled_rides[ride].ride_no_driver()
        return public_routs[num]
    else:
        return f"There is not a route with line number {num}"


def search_route_by_orig(orig, routes):
    """
    A search function for a passenger to search routes with a selected origin
    :param orig:
    :param routes: All the routes created
    :return: if they exist, all the routs with the selected origin
    """
    disired_routes = []
    for num in routes.keys():
        if routes[num].origin == orig:
            disired_routes.append(routes[num])
    for route in disired_routes:
        for ride in route.scheduled_rides:
            route.scheduled_rides[ride] = route.scheduled_rides[ride].ride_no_driver()
    if disired_routes != []:
        return disired_routes
    else:
        return "There is no line with that origin"


def search_route_by_dest(dest, routes):
    """
    a search function for a passenger to search routes with a selected destination
    :param dest:
    :param routes: All the routes created
    :return: If they exist, all the routs with the selected destination
    """
    disired_routes = []
    for num in routes.keys():
        if routes[num].destination == dest:
            disired_routes.append(routes[num])
    for route in disired_routes:
        for ride in route.scheduled_rides:
            route.scheduled_rides[ride] = route.scheduled_rides[ride].ride_no_driver()
    if disired_routes != []:
        return disired_routes
    else:
        return "There is no line with that destination"


def search_route_by_stop(stop, routes):
    """
    A search function for a passenger to search routes with a selected stop
    :param stop: The stop to search
    :param routes: All the routes created
    :return: If they exist, all the routs with the selected stop in their list of stops
    """
    disired_routes = []
    for num in routes.keys():
        if stop in routes[num].list_of_stops:
            disired_routes.append(routes[num])
    for route in disired_routes:
        for ride in route.scheduled_rides:
            route.scheduled_rides[ride] = route.scheduled_rides[ride].ride_no_driver()
    if disired_routes != []:
        return disired_routes
    else:
        return "There is no line with that stop"


def report_delay(ride, delay):
    """
    a function that lets a passenger to report a delay
    :param ride: The id of the ride that the passenger want to report a delay
    :param delay: A string with the details of the delay
    :return: The selected ride with the added delay
    """
    ride.add_delay(delay)
    return ride
