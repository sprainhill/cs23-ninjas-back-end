# Algorithm sudo code

- Define size of grid

  - Grid
  - Width
  - Height

  ```
  self.width = x_axis
  self.height = y_axis
  ```

- Create a grid

  ```py
  self.grid = [None] * y_axis

  """
  [None, None, None]
  """

  #

  #

  #
  ```

  ```py
  for i in range(len(a)):
      a[i] = [None]* 3

      """
      [[None, None, None], [None, None, None], [None, None, None]]
      """

      # # #

      # # #

      # # #
  ```

- Plot starting room in middle of grid

  ```py
    """
    Check if genesis grid point exists
    """
    if self.grid[0] is None and self.grid[0][0] is None:
        """
        Set starting room to middle of grid
        """
        starting_x = math.ceil(len(self.grid[0]) / 2)
        starting_y = math.ceil(len(self.grid) / 2)
  ```


        room = Room("A Generic Room", "This is a generic room.", x, y)

        # Insert room into grid
        self.grid[starting_y][starting_x] = room
    ```
        """
        [[(2, 2), None, None], [None, None, None], [None, None, None]]
        """

        # # #

        # ☐ #

        #  #
    ```

### Algorithm to plot the rest of points????

- Start from genesis plot point and randomly calculate 1-4 directions (only for the first block)

  - Add each direction into queue
  - move
  - generate next room
  - randomly calculate 0-3 directions, but cant be a connection dir that exists
  - if it hits end of grid, return
  - if it generates 0 directions, terminate that specific branch

- Rest of nodes in queue
  - Generate random amount direction(s) 0-3
  - Create room in said direction
  - Point room to previous direction

* Convert plotted rooms into fixtures

```py
def gen_fixture(self):
      """
      Generates create_world fixture
      """

      # Flatten grid of rooms
      flat_list = [item for sublist in self.grid for item in sublist]

      formatted_fixture = []

      for i, room in enumerate(flat_list, start=0):
          if room is None:
              break

          formatted_room = {}

          formatted_room["model"] = 'adventure.room'
          formatted_room["pk"] = i + 1
          formatted_room["fields"] = {
              "title": room.name,
              "description": room.description,
              "n_to": room.n_to,
              "s_to": room.s_to,
              "e_to": room.e_to,
              "w_to": room.w_to,
              "x": room.x,
              "w": room.y,
          }

          formatted_fixture.append(formatted_room)

      f = open('generated_world.json', "w+")
      f.write(str(formatted_fixture))
      f.close()

```
