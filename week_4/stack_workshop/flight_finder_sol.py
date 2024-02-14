"""
Given:
- A set of cities that HPAir serves (cityFile.txt)
- Pairs of city names, each pair represents the origin and destination
  of one flight (flightFile.txt)
- Pair of cities names each of which represents a request to fly
  from an origin to a destination (requestFile.txt)

Find whether or not a path exists between two cities requested by a passenger.
"""

from stack import Stack

""" A collection of functions to help the is_path() function to
determine if there is a path between two cities"""

"""These global names are for references only. The assignment will take
place in various functions."""

global visited
global NUM_FLIGHT_RTS
global flight_routes
global NUM_CITIES
global city_names

def unvisit_all():
    """Mark all cities unvisited"""
    global visited
    visited = {}
    for i in range(len(city_names)):
        visited[city_names[i]] = False

def mark_visited(which):
    """Mark a particular city visited"""
    visited[which] = True

def get_next_city(from_city):
    """Get the next city that can be reached from 'from_city'"""
    to_city = 'none'
    for i in range(NUM_FLIGHT_RTS):
        if flight_routes[i][0] == from_city:
            to_city = flight_routes[i][1]
            # print(' in getnextcity from to visited[to]', \
            #      from_city, to_city, visited[to_city])
            if visited[to_city] == False:
                return True, to_city
    return False, to_city

def read_flight_routes():
    """Read the flight route information. The format of the file is following
    n : the number of routes
    from1
    to1
    ...
    fromn
    ton"""
    f = open('flightFile.txt', 'r')
    data = f.read()    # read all lines
    lines = data.split('\n')
    size = int(lines[0])    # number of routes
    global NUM_FLIGHT_RTS
    NUM_FLIGHT_RTS = size
    size *= 2               # each route has two cities, orig, dest
    global flight_routes
    flight_routes = []
    for i in range(1, size+1, 2):
        pair = ['' for i in range(2)]
        pair[0] = lines[i].strip()   # source
        pair[1] = lines[i+1].strip() # destination
        flight_routes.append(pair)
    return flight_routes

def read_city_names():
    """Read a list of n cities"""
    f = open('cityFile.txt', 'r')
    data = f.read()
    lines = data.split('\n')
    size = int(lines[0])
    #print(size)
    global NUM_CITIES
    NUM_CITIES = size
    city_names = []
    for i in range(1, size+1):
        city_names.append(lines[i].strip())
    return city_names

def is_path(orig, destiny):
    """Given an orig and a destiny city, determine if there is a path."""
    my_stack = Stack()

    unvisit_all()

    my_stack.push(orig)
    mark_visited(orig)

    top_city = my_stack.peek()

    while (len(my_stack) > 0 and top_city != destiny):

        success, next_city = get_next_city(top_city)
        # print(' top dest next suc', top_city, destiny, next_city, success)
        if success == False:
            my_stack.pop()
        else:
            my_stack.push(next_city)
            mark_visited(next_city)
            if len(my_stack) > 0:
                top_city = my_stack.peek()

    if len(my_stack) == 0:
        return False, my_stack
    else:
        return True, my_stack

def main():

    global city_names
    city_names = read_city_names()
    global flight_routes
    flight_routes = read_flight_routes()

    global visited
    global NUM_FLIGHT_RTS

    unvisit_all()

    #print(flight_routes)

    f = open('requestFile.txt', 'r')
    data = f.read()
    lines = data.split('\n')
    count = int(lines[0])

    print("Origin           │ Destination      │ Route")
    print("─────────────────┼──────────────────┼──────────────────────────────")

    for i in range(1, 2*count+1, 2):
        src = lines[i].strip()
        dst = lines[i+1].strip()
        # print(' in main src|' + src + '| dest |' + dst + '|')
        found, rt_stack = is_path(src, dst)
        if found:
            print(f"{src:16} │ {dst:16} │ {str(rt_stack)}")
        else:
            print(f"{src:16} │ {dst:16} │ -")

if __name__ == "__main__":
    main()
