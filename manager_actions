from route import Route
from ride import Ride


def add_route(num, orig, dest, stops):
    """

    :param num: the number of the line
    :param orig: the origin of the route
    :param dest: the final destination of the route
    :param stops: the stops along the routes
    :return: a route object with the desired parameters
    """
    new_route = Route(num, orig, dest, stops)
    return new_route


def delete_route(num, all_routes={}):
    """
    a function that updates the collection of all the routes created, without the deleted one.
    :param num: the line number of the requested route to delete
    :param all_routes: a collection of all the routes created
    """
    if num in all_routes:
        print(f"line number {num} has deleted.")
        all_routes.pop(num)
    else:
        print(f"line number {num} does not exist" )


def update_route(num, all_routes):
    """
    updates a specific attribute of a selected route
    :param num: the line number of the route
    :param all_routes: a collection of all the routes created
    """
    if num in all_routes:
        print(f"The details of the route you selected are: {all_routes[num]}")
        change = input("""What would you like to change?
                          1 - origin
                          2 - destination
                          3 - stops""")
        while change != '1' and change != '2' and change != '3':
            print("Invalid input, try again")
            change = input("""What would you like to change?
                                      1 - origin
                                      2 - destination
                                      3 - stops""")
        if change == '1':
            new_origin = input("Please enter the new origin")
            changed_route = all_routes[num]
            changed_route.set_origin(new_origin)
            all_routes[num] = changed_route
            print(f"The route after the change: {all_routes[num]}")
        elif change == '2':
            new_dest = input("Please enter the new destination")
            changed_route = all_routes[num]
            changed_route.set_dest(new_dest)
            all_routes[num] = changed_route
            print(f"The route after the change: {all_routes[num]}")
        else:
            new_stops = input("Please enter the stops(ordered, separated by coma)")
            changed_route = all_routes[num]
            changed_route.set_stops(new_stops)
            all_routes[num] = changed_route
            print(f"The route after the change: {all_routes[num]}")
    else:
        print(f"line number {num} does not exist")


def add_scheduled_ride(route, departure, arrival, driver_name):
    """
    creates a new ride for a specific route
    :param route: the selected route for adding a ride
    :param departure: the time of the departure
    :param arrival: the time of the arrival
    :param driver_name: the name of the driver
    :return: the same route given, with the added ride
    """
    new_ride = Ride(departure, arrival, driver_name)
    route.set_rides(new_ride)
    return route
