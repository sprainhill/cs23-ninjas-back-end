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
            # Shuffle directions, and set starting nodes directions to create
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
                    previous_room.connect_rooms(room, room_direction)
                # Update iteration variables
                previous_room = room
                room_count += 1
            else:
                current_room = Queue.dequeue()
                if current_room is None:
                    break
                # Generate bewteen 1-4 directions
                direction_amount = math.floor(random.random() * 4 + 1)
                # Shuffle directions, and set starting nodes directions to create
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
                    previous_room.connect_rooms(room, room_direction)
                # Update iteration variables
                previous_room = room
                room_count += 1