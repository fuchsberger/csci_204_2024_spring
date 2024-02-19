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

    visited = unvisit_all(graph)
    stack = Stack()

    stack.push((src, [src]))
    visited[src] = True

    while len(stack) > 0:
        curr, path = stack.pop()

        for city in graph[curr]:
            if city == dest:
                return path + [city]

            if not visited[city]:
              stack.push((city, path + [city]))
              visited[city] = True

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
