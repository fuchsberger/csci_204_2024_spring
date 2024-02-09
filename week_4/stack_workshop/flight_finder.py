from stack import Stack

## TODO

"""
Given:
- A set of cities that HPAir serves (cityFile.txt)
- Pairs of city names, each pair represents the origin and destination
  of one flight (flightFile.txt)
- Pair of cities names each of which represents a request to fly
  from an origin to a destination (requestFile.txt)

Find whether or not a path exists between two cities requested by a passenger.
"""

# The following globals and helper functions are only a suggestion.
# Feel free to structure differently

global visited
global NUM_FLIGHT_RTS
global flight_routes
global NUM_CITIES
global city_names

def unvisit_all():
    """Mark all cities unvisited"""
    pass

def mark_visited(which):
    """Mark a particular city visited"""
    pass

def get_next_city(from_city):
    """Get the next city that can be reached from 'from_city'"""
    pass

def read_flight_routes():
    """Read the flight route information. The format of the file is following
    n : the number of routes
    from1
    to1
    ...
    fromn
    ton"""
    pass

def read_city_names():
    """Read a list of n cities"""
    pass

def is_path(orig, destiny):
    """Given an orig and a destiny city, determine if there is a path."""
    pass

def main():
    # TODO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    pass

if __name__ == "__main__":
  main()
