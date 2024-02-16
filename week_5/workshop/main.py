from myStack import Stack
from myQueue import Queue

# Do not modify or delete
testGraph = {
    'A': ('B', 'C'),
    'B': ('A', 'D', 'E', 'F'),
    'C': ('A', 'F'),
    'D': ('B'),
    'E': ('B', 'F'),
    'F': ('B','C', 'E'),
    'G': ()
}

def unvisit_all(graph):
    """
    Inputs:
      - graph: a graph (dictonary of sets)

    Returns:
      - a dictionary where keys are cities and values are False (not visisted)
    """
    visited = {}

    for city in graph.keys():
        visited[city] = False

    return visited

def depth_first_search(graph, src, dest):
    """
    Inputs:
      - graph: a graph (dictonary of sets)
      - src: a source city (string)
      - dest: a destination city (string)

    Returns either/or:
      - a python list representing the path (for example: [A, B, C])
      - None (if no path was found)
    """
    # TODO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    pass

def breath_first_search(graph, src, dest):
    """
    Inputs:
      - graph: a graph (dictonary of sets)
      - src: a source city (string)
      - dest: a destination city (string)

    Returns either/or:
      - a python list representing the path (for example: [A, B, C])
      - None (if no path was found)
    """
    # TODO <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    pass

if __name__ == "__main__":
    # depth-first-search
    result = depth_first_search(testGraph, "A", "E")

    print("Dept First Seach using Stack Result:")
    if result:
        print(f"Path Found: {str(result)}")
    else:
        print("Path not found")


    # breath first search
    result = depth_first_search(testGraph, "A", "E")

    print("Breath First Seach using Queue Result:")
    if result:
        print(f"Path Found: {str(result)}")
    else:
        print("Path not found")
