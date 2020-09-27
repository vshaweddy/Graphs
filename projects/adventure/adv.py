from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

###
visited = {}

# Create an array to track the history of the path
backtrack_path = []

# Have directions as keys and assign the opposite direction as its value
directions = { 'n': 's', 's': 'n', 'e': 'w', 'w': 'e'}

# Get the exits and set as value based on the room id to the visited list
visited[player.current_room.id] = player.current_room.get_exits()
print(f"Visited: {visited}")

while len(visited) < len(room_graph):
    # check the current room in visited list or not
    if player.current_room.id not in visited:
        # Get the exits and set as value based on the room id to the visited list
        visited[player.current_room.id] = player.current_room.get_exits()

        # Set the previous room by getting it from the history array
        previous_room = backtrack_path[-1]

        print("Previous room: ", previous_room)
        print("Backtrack path: ", backtrack_path)
        print("Currently in room: ", player.current_room.id)

        # Remove the previous room from the visited list value
        visited[player.current_room.id].remove(previous_room)
        # {0: [], 1: [n]}
    
    # if there is still exit(s)
    elif len(visited[player.current_room.id]) > 0:
        # Set the next room by getting the direction from the last index in visited array
        next_room = visited[player.current_room.id][-1]

        print("Next room: ", next_room)
        print("Backtrack path: ", backtrack_path)
        print("Currently in room: ", player.current_room.id)

        # Mark the next room as the room you're going to visit
        visited[player.current_room.id].remove(next_room) # visited[player.current_room.id].pop()
 
        # Track our path to the next room
        traversal_path.append(next_room)

        # Track the backward path as a backup to get out
        backtrack_path.append(directions[next_room])

        # Travel to the next room
        player.travel(next_room)
        print("Walking to room: ", next_room)

    elif len(visited[player.current_room.id]) == 0:
        # Set the previous room from the track history
        previous_room = backtrack_path[-1]
        print("Previous room: ", previous_room)
        print("Backtrack path: ", backtrack_path)
        print("Currently in room: ", player.current_room.id)

        # Remove the last item in the backtrack path
        backtrack_path.pop()

        # Add the previous room to the traversal path
        traversal_path.append(previous_room)

        # Travel to the next room
        player.travel(previous_room)
        print("Go back to the previous room: ", previous_room)


####
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
