# algorithm to procedurally generate room patterns and content

# create world class
class World():
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0

    def create_world(self, x_axis, y_axis):



    # define grid size
    # creates height of grid
    self.grid = [None] * y_axis

    # creates width of the grid
    # inserts columns into stacked rows
    for i in range(len(self.grid)):
        self.grid[i] = [None] x_axis

    # begin plot in middle of grid

    if self.grid[0] is None and self.grid[0][0] is None:
        # set starting room to middle of grid
        start_x = math.ceil(len(self.grid[0]) // 2)
        start_y = math.ceil(len(self.grid) // 2)
    
    # create room for insertion
    room = Room("A generic room", "This is a generic room", x, y)

    # insert room into grid
    # inserts into the x-axis list item within the y-axis list
    self.grid[start_x][start_y]
