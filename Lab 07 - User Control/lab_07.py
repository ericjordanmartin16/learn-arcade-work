""" Lab 7 - User Control """

import arcade
import random

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3


# Functions for drawing background image.
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

    # Draw a square for the body of the house.
    arcade.draw_rectangle_filled(x, y, 40, 40, house_color)

    # Draw a triangle for the roof of the house.
    arcade.draw_triangle_filled(x - 20, y + 20, x + 20, y + 20, x, y + 50, roof_color)

    # Draw windows for each house.
    arcade.draw_rectangle_outline(x - 10, y + 10, 10, 10, (0, 0, 0))
    arcade.draw_rectangle_outline(x + 10, y + 10, 10, 10, (0, 0, 0))

    # Draw a door for each house.
    arcade.draw_rectangle_outline(x, y - 12.5, 10, 15, (0, 0, 0))


def draw_pond(x, y):
    """Draws a pond at point (x, y)"""
    arcade.draw_ellipse_filled(x, y, 100, 60, (0, 0, 255), 0, -1)
    arcade.draw_ellipse_filled(x + 10, y + 5, 50, 30, (150, 150, 255), 0, -1)


def draw_tree(x, y):
    """Draws a tree at point (x, y)"""
    arcade.draw_rectangle_filled(x, y, 10, 25, (150, 50, 50))
    arcade.draw_triangle_filled(x - 15, y + 12.5, x + 15, y + 12.5, x, y + 60, (50, 255, 50))


class Character:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        self.ow_sound = arcade.load_sound("ow.m4a")
        self.ow_sound_player = None

        self.position_x = position_x
        self.position_y = position_y
        self.change_x = 0
        self.change_y = 0
        self.radius = radius
        self.color = color

    def draw(self):
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)
        arcade.draw_text(" :) ", self.position_x - 4, self.position_y + 9, arcade.color.BLACK, font_size=12,
                         font_name="arial", rotation=270)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        # Code to make the object stop at the edges of the screen.
        if self.position_x <= self.radius:
            self.change_x = 0
        if self.position_x <= self.radius:
            if not self.ow_sound_player or not self.ow_sound_player.playing:
                self.ow_sound_player = arcade.play_sound(self.ow_sound)
        if self.position_x >= SCREEN_WIDTH - self.radius:
            self.change_x = 0
        if self.position_y <= self.radius:
            self.change_y = 0
        if self.position_y >= SCREEN_HEIGHT - self.radius:
            self.change_y = 0


class AntiCharacter:
    def __init__(self, position_x, position_y, change_x, change_y, width, height, color):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = 0
        self.change_y = 0
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        arcade.draw_rectangle_filled(self.position_x, self.position_y, self.width, self.height, self.color)
        arcade.draw_text(" :( ", self.position_x - 4, self.position_y + 9, arcade.color.BLACK, font_size=12,
                         font_name="arial", rotation=270)

    def update(self):
        self.position_x += self.change_x
        self.position_y += self.change_y

        # Code to make the object stop at the edges of the screen.
        if self.position_x <= self.width:
            self.change_x = 0
        if self.position_x >= SCREEN_WIDTH - self.width:
            self.change_x = 0
        if self.position_y <= self.height:
            self.change_y = 0
        if self.position_y >= SCREEN_HEIGHT - self.height:
            self.change_y = 0


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self, width, height, title):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.click_sound = arcade.load_sound("click.m4a")

        arcade.set_background_color((52, 168, 50))

        self.character_list = []
        self.anticharacter_list = []

        # Set the object to a random location on the screen, and make the radius and color random.
        x = 10 # random.randrange(SCREEN_WIDTH)
        y = 140 # random.randrange(SCREEN_HEIGHT)
        cx = 2 # random.randrange(-3, 4)
        cy = 2 # random.randrange(-3, 4)
        radius = 10

        # Attributes for the AntiCharacter.
        anti_x = random.randrange(SCREEN_WIDTH)
        anti_y = random.randrange(SCREEN_HEIGHT)
        width = 20
        height = 20

        # Set individual colors that can be inverted for the AntiCharacter.
        color_a = random.randrange(100, 256)
        color_b = random.randrange(100, 256)
        color_c = random.randrange(100, 256)
        color = (color_a, color_b, color_c)
        anticolor = (256 - color_a, 256 - color_b, 256 - color_c)

        self.character = Character(x, y, cx, cy, radius, color)
        self.character_list.append(self.character)

        self.anticharacter = AntiCharacter(anti_x, anti_y, cx, cy, width, height, anticolor)
        self.anticharacter_list.append(self.anticharacter)

    def on_draw(self):
        arcade.start_render()

        # Draw the background image.
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

        draw_tree(50, 50)
        draw_tree(100, 50)
        draw_tree(150, 50)
        draw_tree(200, 50)
        draw_tree(300, 50)
        draw_tree(350, 50)
        draw_tree(400, 50)
        draw_tree(450, 50)

        # Finish drawing
        # arcade.finish_render()

        # Draw a character
        for character in self.character_list:
            self.character.draw()

        for anticharacter in self.anticharacter_list:
            self.anticharacter.draw()

    def on_update(self, delta_time):
        for character in self.character_list:
            self.character.update()

        for anticharacter in self.anticharacter_list:
            self.anticharacter.update()

    def on_mouse_motion(self, x, y, dx, dy):
        self.anticharacter.position_x = x
        self.anticharacter.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        arcade.play_sound(self.click_sound)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.character.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.character.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.character.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.character.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.character.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.character.change_y = 0


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
    arcade.run()


main()
