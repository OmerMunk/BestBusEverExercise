import copy
import manager_actions
import passenger_actions

# The main script, this script is the user interface, it can launch all the actions for both manager and passenger
if __name__ == '__main__':
    all_routes = {}
    while True:  # The script always running
        print("Welcome to the Best Bus Ever App")
        print("""Choose:
        1 for passenger
        2 for manager
        3 to close the application""")
        identify = input()
        identifiers = ['1', '2', '3']
        while identify not in identifiers:
            print("Invalid input, please try again")
            print("""Choose:
            1 for passenger
            2 for manager
            3 to close the application""")
            identify = input()
        if identify == '1':  # The user chose the passenger menu
            passenger_options = ['0','1','2']
            passenger_option = None
            while passenger_option != '0':
                print("Hello passenger! Welcome aboard")
                print("This is the passenger menu")
                print("""Choose option:
                1 - Search Route
                2 - Report delay
                0 - Back to main menu""")
                passenger_option = input()
                while passenger_option not in passenger_options:
                    print("Invalid input, try again")
                    print("This is the passenger menu")
                    print("""Choose option:
                    1 - Search Route
                    2 - Report delay
                    0 - Back to main menu""")
                    passenger_option = input()
                if passenger_option == '1':
                    search_options = ['1', '2', '3', '4', '0']
                    search_type = input("""How do you want to search route?
                    1 - By line number
                    2 - By origin
                    3 - By destination
                    4 - By bus stop
                    0 - Back to main menu""")
                    while search_type not in search_options:
                        print("Invalid input, try again")
                        search_type = input("""How do you want to search route?
                        1 - By line number
                        2 - By origin
                        3 - By destination
                        4 - By bus stop
                        0 - Back to main menu""")
                    if search_type == '1':
                        num = input("Which is the line number you want to search?")
                        print(passenger_actions.search_route_by_num(num, all_routes))
                    if search_type == '2':
                        orig = input("Which is the origin you want to search?")
                        print(passenger_actions.search_route_by_orig(orig, all_routes))
                    if search_type == '3':
                        dest = input("What is the destination you want to search?")
                        print(passenger_actions.search_route_by_dest(dest, all_routes))
                    if search_type == '4':
                        stop = input("Which is the stop you want to search?")
                        print(passenger_actions.search_route_by_stop(stop, all_routes))
                elif passenger_option == '2':
                    num = input("Which is the line number of the ride you want to report a delay?")
                    rideID = input("What is the ID of the ride you want to report a delay?")
                    delay = input("What do you want to report?")
                    if num in all_routes.keys():
                        delay_change = False
                        for key, value in all_routes[num].scheduled_rides.items():
                            if rideID == key or rideID == value:
                                passenger_actions.report_delay(all_routes[num].scheduled_rides[rideID], delay)
                                print("Delay Reported Successfully")
                                delay_change = True
                        if delay_change == False:
                            print(f"There is not such a ride ID in line number {num}")
                    else:
                        print(f"There is not such a line number {num}")
                else: # Back to main menu
                    continue

        elif identify == '2':  # The user chose the manager menu
            correct_password = "RideWithUs!"
            tries = 0
            print("Please enter the managers password:")
            password = input()
            while tries != 2 and password != correct_password:
                print(f"Wrong password, you have {2-tries} attempts left")
                tries += 1
                password = input("Re-enter password")
            if password!= correct_password:
                exit("You have reached the limit of attempts for entering the correct password,"
                     " the application has locked.")  # closing the program with an exit string
            else:
                manager_option = None
                manager_options = ['0', '1', '2', '3', '4']
                print("Correct password")
                while manager_option != '0':
                    print("Hello manager! Welcome to the manager menu")
                    print("""choose option:
                    1 - Add route
                    2 - Delete route
                    3 - Update route
                    4 - Add scheduled ride
                    0 - Back to main menu""")
                    manager_option = input()
                    while manager_option not in manager_options:
                        print("Invalid input, try again")
                        print("Hello manager! Welcome to the manager menu")
                        print("""Choose option:
                        1 - Add route
                        2 - Delete route
                        3 - Update route
                        4 - Add scheduled ride
                        0 - Back to main menu""")
                        manager_option = input()
                    if manager_option == '1':
                        num = input("Enter the number of the line")
                        orig = input("Enter the origin of the route")
                        dest = input("Enter the destination of the route")
                        stops = input("Enter the stops (ordered"
                                      "ed, separated by coma)")
                        route = manager_actions.add_route(num, orig, dest, stops)
                        route_to_list = copy.deepcopy(route)
                        all_routes.update({num: route_to_list})
                        print(all_routes)
                        continue
                    if manager_option == '2':
                        num = input("Enter the number of the line you want to delete")
                        manager_actions.delete_route(num, all_routes)
                        print(all_routes)
                        continue
                    if manager_option == '3':
                        num = input("Enter the number of the line you want to update")
                        manager_actions.update_route(num, all_routes)
                        continue
                    if manager_option == '4':
                        num = input("Enter the number of the line you want add a scheduled ride to")
                        if num in all_routes:
                            print(f"The current details for the route you chose is: {all_routes[num]}")
                            departure = input("Enter the departure time:")
                            arrival = input("Enter the arrival time:")
                            driver = input("Enter the driver's name:")
                            updated_route = manager_actions.add_scheduled_ride(all_routes[num], departure, arrival, driver)
                            all_routes[num] = updated_route
                            print(f"The route with the added ride:{all_routes[num]}")
                        else:
                            print(f"There is not such a route {num}")
                    if manager_option == '0':  # Back to main menu
                        continue

        else:  # If the user enter's 3 on the main menu
            exit()  # Exit's the script
