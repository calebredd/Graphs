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

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)
breadcrumb = []
switcher ={'n':'s','e':'w','w':'e','s':'n'}
def loop(current_room=player.current_room):
    print(f"{current_room.id}", end=', ')
    # print(f"({current_room.id}, {len(breadcrumb)}, {len(visited_rooms)}", end='), ')
    if len(visited_rooms) == len(room_graph):
        for b in visited_rooms:
            for k in b.get_exits():
                if k =='n':
                    if b.n_to not in visited_rooms:
                        print(f"missing room {b.n_to.id}")
                elif k =='s':
                    if b.s_to not in visited_rooms:
                        print(f"missing room {b.s_to.id}")
                elif k =='e':
                    if b.e_to not in visited_rooms:
                        print(f"missing room {b.e_to.id}")
                elif k =='w':
                    if b.w_to not in visited_rooms:
                        print(f"missing room {b.w_to.id}")
        return 
    else:
        for d in current_room.get_exits():
            if d == 'n':
                if current_room.n_to not in visited_rooms:
                    current_room = current_room.n_to
                    visited_rooms.add(current_room)
                    traversal_path.append('n')
                    breadcrumb.append(switcher['n'])
                    return loop(current_room)
            elif d == 's':
                if current_room.s_to not in visited_rooms:
                    current_room = current_room.s_to
                    visited_rooms.add(current_room)
                    traversal_path.append('s')
                    breadcrumb.append(switcher['s'])
                    return loop(current_room)
            elif d == 'e':
                if current_room.e_to not in visited_rooms:
                    current_room = current_room.e_to
                    visited_rooms.add(current_room)
                    traversal_path.append('e')
                    breadcrumb.append(switcher['e'])
                    return loop(current_room)
            elif d == 'w':
                if current_room.w_to not in visited_rooms:
                    current_room = current_room.w_to
                    visited_rooms.add(current_room)
                    traversal_path.append('w')
                    breadcrumb.append(switcher['w'])
                    return loop(current_room)
        if len(visited_rooms) != len(room_graph):
            if len(breadcrumb): 
                l = breadcrumb.pop(-1)
                traversal_path.append(l)
                if l =='n':
                    current_room = current_room.n_to
                elif l =='s':
                    current_room = current_room.s_to
                elif l =='e':
                    current_room = current_room.e_to
                elif l =='w':
                    current_room = current_room.w_to
                return loop(current_room)
            return
        return
loop(player.current_room)         
            
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
free = 0
while free == True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
