import arcade
# import random

WIDTH = 60
HEIGHT = 60
MARGIN = 5
COLUMN_COUNT = 10
ROW_COUNT = 10

# Always one more margin than number of boxes.
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color((0, 0, 0))

        # Create grid of numbers.
        self.grid = []
        for row in range(ROW_COUNT):
            # For each row, create a list that represents entire row.
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                # Add a number 0 to the current row.
                self.grid[row].append(0)

        # Change the value of row 2 column 1 so that it prints green (in below).
        # self.grid[row][column in that particular row]
        self.grid[2][1] = 1
        #         y  x
        #        row column
        print(self.grid)

        # More efficient way of doing it that is beyond the scope of this class.
        # self.grid = [[0 for x in range(10)] for y in range(10)]

    def on_draw(self):
        """
        Render the screen.
        """

        color = (255, 255, 255)
        arcade.start_render()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = WIDTH / 2 + column * (WIDTH + MARGIN) + MARGIN
                y = HEIGHT / 2 + row * (HEIGHT + MARGIN) + MARGIN
                if self.grid[row][column] == 0:
                    color = (255, 255, 255)
                else:
                    color = (0, 255, 0)
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """

        # Print the row and column where the user clicks.
        row = y // (HEIGHT + MARGIN)
        column = x // (WIDTH + MARGIN)
        print(row, column)
        # Set to green if the square is white, and vice versa.
        if self.grid[row][column] == 0:
            self.grid[row][column] = 1
            self.grid[row + 1][column] = 1
            self.grid[row - 1][column] = 1
            self.grid[row][column + 1] = 1
            self.grid[row][column - 1] = 1
        else:
            self.grid[row][column] = 0


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
