import sys
sys.path.append('../data_structures')
from dll_queue import Queue

import json
import math
import random


class Room:
    def __init__(self, id, name, description, x, y, n=0, s=0, e=0, w=0):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = n
        self.s_to = s
        self.e_to = e
        self.w_to = w
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.x}"

    def connect_rooms(self, connecting_room, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        if direction == "n":
            self.n_to = connecting_room.id
        elif direction == "s":
            self.s_to = connecting_room.id
        elif direction == "e":
            self.e_to = connecting_room.id
        else:
            self.w_to = connecting_room.id

    def get_room_in_direction(self, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        return getattr(self, f"{direction}_to")


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0
        self.directions = ['n', 's', 'e', 'w']

    def generate_rooms(self, size_x, size_y, num_rooms):
            '''
            Fill up the grid, bottom to top, in a zig-zag pattern
            '''
            # Initialize the grid
            self.grid = [None] * size_y
            self.width = size_x
            self.height = size_y
            for i in range(len(self.grid)):
                self.grid[i] = [None] * size_x
            # Start from middle of grid (0,0)
            x = math.ceil(len(self.grid[0]) / 2)
            y = math.ceil(len(self.grid) / 2)
            room_count = 1
            previous_room = None
            node_directions = []
            nodes = Queue()
            # Check if genesis grid point doesn't exist
            if self.grid[0][0] is None:
                """
                Create genesis grid point/room
                """
                # Generate bewteen 1-4 directions
                direction_amount = math.floor(random.random() * 4 + 1)
                # Shuffle directions, and set starting nodes directions     to create
                node_directions = random.sample(
                    self.directions, direction_amount)
                # Create first room
                room = Room(room_count, "Forsaken Palace",
                            "This is a description", x, y)
                # Add room to queue
                nodes.enqueue(room)
                # Save the room in the World grid
                self.grid[y][x] = room
                # Set previous room
                previous_room = room
                # Increment room amount
                room_count += 1
            while room_count < num_rooms:
                if node_directions is not None:
                    current_room = nodes.dequeue()
                    direction = node_directions[0]
                    if current_room is None:
                        break
                    if direction == "n":
                        room_direction = "n"
                        y = current_room.y + 1
                    elif direction == "s":
                        room_direction = "s"
                        y = current_room.y - 1
                    elif direction == "e":
                        room_direction = "e"
                        x = current_room.x + 1
                    else:
                        room_direction = "w"
                        x = current_room.x - 1
                    room = Room(room_count, "A Generic Room",
                                "This is a generic room.", x, y)
                    # Add room to queue
                    nodes.enqueue(room)
                    # Save the room in the World grid
                    self.grid[y][x] = room
                    # Connect the new room to the previous room
                    if previous_room is not None:
                        previous_room.connect_rooms(room,   room_direction)
                    # Update iteration variables
                    previous_room = room
                    room_count += 1
                else:
                    current_room = Queue.dequeue()
                    if current_room is None:
                        break
                    # Generate bewteen 1-4 directions
                    direction_amount = math.floor(random.random() * 4 +     1)
                    # Shuffle directions, and set starting nodes    directions to create
                    node_directions = random.sample(
                        self.directions, len(direction_amount))
                    # Get next direction to go in
                    direction = node_directions[0]
                    if direction == "n":
                        room_direction = "n"
                        y = current_room.y + 1
                    elif direction == "s":
                        room_direction = "s"
                        y = current_room.y - 1
                    elif direction == "e":
                        room_direction = "e"
                        x = current_room.x + 1
                    else:
                        room_direction = "w"
                        x = current_room.x - 1
                    room = Room(room_count, "A Generic Room",
                                "This is a generic room.", x, y)
                    # Add room to queue
                    nodes.enqueue(room)
                    # Save the room in the World grid
                    self.grid[y][x] = room
                    # Connect the new room to the previous room
                    if previous_room is not None:
                        previous_room.connect_rooms(room,   room_direction)
                    # Update iteration variables
                    previous_room = room
                    room_count += 1

    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''

        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"

        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid)  # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"

        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"

        # Print string
        print(str)

    def gen_fixture(self):
        """
        Generates create_world fixture
        """

        # Flatten grid of rooms
        flat_list = [item for sublist in self.grid for item in sublist]

        formatted_fixture = []

        for i, room in enumerate(flat_list, start=0):
            if room is None:
                continue

            formatted_room = {}

            formatted_room["model"] = 'adventure.room'
            formatted_room["pk"] = room.id
            formatted_room["fields"] = {
                "title": room.name,
                "description": room.description,
                "n_to": room.n_to,
                "s_to": room.s_to,
                "e_to": room.e_to,
                "w_to": room.w_to,
                "x": room.x,
                "y": room.y,
            }

            formatted_fixture.append(formatted_room)

        f = open('generated_world.json', "w+")
        f.write(str(formatted_fixture))
        f.close()


w = World()
num_rooms = 3
width = 8
height = 7
w.generate_rooms(width, height, num_rooms)
w.gen_fixture()


print(
    f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
