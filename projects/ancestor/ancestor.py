
def earliest_ancestor(ancestors, starting_node):
    # initialize the empty dictionary
    graph = {}

    # build the graph but in reverse way (switch the value to be the key)
    for (u, v) in ancestors:
        if v not in graph:
            # it needs to be a list so it will be in order
            graph[v] = []
        graph[v].append(u)

    # check first if the starting node is the ancenstor 
    if starting_node not in graph:
        return -1

    # set the starting node as the current
    curr = starting_node

    # while current is still the key in the graph
    while curr in graph:
        parents = graph[curr]
        # get the first one from the collection
        curr = parents[0]

    return curr