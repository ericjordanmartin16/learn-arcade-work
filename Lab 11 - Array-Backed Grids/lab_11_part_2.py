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
                # Insert a number 0 to the current row.
                self.grid[row].append(0)

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
        # Set to green if the square is white, and vice versa.
        if self.grid[row][column] == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0

        """running_total = 0

        for row in range(ROW_COUNT):
            row_cell_count = 0
            continuous_count = 0
            print(f"Row {row} has {row_cell_count} cells selected.")
            for column in range(COLUMN_COUNT):
                column_cell_count = 0
                if self.grid[row][column] == 1:
                    row_cell_count += 1
                    column_cell_count += 1
                    running_total += 1
                    continuous_count += 1
                elif self.grid[row][column] == 0:
                    if continuous_count > 2:
                        print(f"There are {continuous_count + 1} continuous blocks selected on row {row}.")
            print(f"Column {column} has {column_cell_count} cells selected.")"""

        running_total = 0
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    running_total += 1
            print(f"Running total: {running_total}")

        for row in range(ROW_COUNT):
            row_total = 0
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    row_total += 1
            print(f"Row total: {row_total}")

        for column in range(COLUMN_COUNT):
            column_total = 0
            for row in range(ROW_COUNT):
                if self.grid[row][column] == 1:
                    column_total += 1
            print(f"Column total: {column_total}")

        for row in range(ROW_COUNT):
            continuous_count = 0
            for column in range(COLUMN_COUNT):
                if self.grid[row][column] == 1:
                    continuous_count += 1
                elif self.grid[row][column] == 0:
                    if continuous_count > 2:
                        print(f"There are {continuous_count + 1} continuous blocks selected on row {row}.")
                    continuous_count = 0

            if continuous_count > 2:
                print(f"There are {continuous_count + 1} continuous blocks selected on row {row}.")

        singular_text = "Total of 1 cell is selected."
        plural_text = f"Total of {running_total} cells are selected."

        if running_total == 1:
            print(singular_text)
        else:
            print(plural_text)


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
