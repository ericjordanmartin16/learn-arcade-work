"""
Eric Martin, Intro to Computer Science, Instructor Paul Craven. Lab #3: Drawing with Functions.
"""
import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_streets():
    # Draw east-west streets.
    arcade.draw_lrtb_rectangle_filled(0, 250, 550, 530, (168, 111, 50))  # upper
    arcade.draw_lrtb_rectangle_filled(0, 600, 350, 330, (168, 111, 50))  # middle
    arcade.draw_lrtb_rectangle_filled(0, 525, 150, 130, (168, 111, 50))  # lower

    # Draw north-south streets.
    arcade.draw_lrtb_rectangle_filled(250, 270, 600, 0, (168, 111, 50))  # left
    arcade.draw_lrtb_rectangle_filled(525, 545, 330, 0, (168, 111, 50))  # right


def draw_house(x, y, house_color, roof_color):
    """Draws a house at point (x, y) of color (a, b, c)"""
    arcade.draw_point(x, y, arcade.color.RED, 5)

    # Draw a square for the body of the house.
    arcade.draw_rectangle_filled(x, y, 40, 40, house_color)

    # Draw a triangle for the roof of the house.
    arcade.draw_triangle_filled(x - 20, y + 20, x + 20, y + 20, x, y + 50, roof_color)


def draw_pond(x, y):
    """Draws a pond at point (x, y)"""
    arcade.draw_ellipse_filled(x, y, 100, 60, arcade.csscolor.BLUE, 0, -1)


def main():
    # Open a window
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")

    # Set the background color
    arcade.set_background_color((52, 168, 50))

    # Get ready to draw
    arcade.start_render()

    draw_streets()
    draw_house(30, 180, (100, 200, 300), (140, 140, 140))
    draw_house(90, 180, (11, 22, 33), (200, 200, 100))
    draw_house(150, 180, (44, 55, 66), (47, 98, 12))
    draw_house(210, 180, (77, 88, 99), (214, 89, 111))
    draw_house(310, 180, (206, 4, 0), (0, 255, 62))
    draw_house(370, 180, (193, 88, 99), (46, 2, 3))
    draw_house(430, 180, (8, 58, 199), (236, 236, 13))
    draw_house(490, 180, (255, 222, 163), (3, 108, 200))

    draw_house(30, 380, (300, 200, 100), (140, 140, 140))
    draw_house(90, 380, (33, 22, 11), (100, 200, 200))
    draw_house(150, 380, (66, 55, 44), (12, 98, 47))
    draw_house(210, 380, (99, 88, 77), (111, 89, 214))
    draw_house(310, 380, (0, 4, 206), (62, 255, 0))
    draw_house(370, 380, (99, 88, 193), (3, 2, 46))
    draw_house(430, 380, (199, 58, 8), (13, 236, 236))
    draw_house(490, 380, (163, 222, 255), (200, 108, 3))

    draw_pond(450, 550)

    # Finish drawing
    arcade.finish_render()

    # Keep the window up until someone closes it.
    arcade.run()


main()