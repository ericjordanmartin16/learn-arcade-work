# Remind Hannah to grab her umbrella!!

"""
Lab 08 - Sprites
due Thursday 11/4/2021
Instructor Paul Craven.
"""

import arcade
import random

# --- Constants ---
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 3
COIN_COUNT = 75
BAD_GUY_COUNT = 25
SPRITE_SCALING_COIN = 0.5


class Coin(arcade.Sprite):
    def reset(self):
        self.bottom = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 5:
            self.change_x *= -1
        if self.right > SCREEN_WIDTH - 5:
            self.change_x *= -1
        if self.bottom < 5 :
            self.change_x *= -1
        if self.top > SCREEN_HEIGHT - 5:
            self.change_y *= -1
        # self.center_y -= 1
        if self.top <= 0:
            self.reset()


class BadGuy(arcade.Sprite):
    def reset(self):
        self.bottom = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)
        self.center_x = random.randrange(SCREEN_WIDTH)

    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 5:
            self.change_x *= -1
        if self.right > SCREEN_WIDTH - 5:
            self.change_x *= -1
        if self.bottom < 5 :
            self.change_x *= -1
        if self.top > SCREEN_HEIGHT - 5:
            self.change_y *= -1
        # self.center_y -= 1
        if self.top <= 0:
            self.reset()


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self, width, height, title):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8 - Sprites and Collisions")

        # Sounds from Arcade Library
        self.coin_sound = arcade.load_sound("coin5.wav")
        self.bad_guy_sound = arcade.load_sound("error1.wav")

        self.player_list = None
        self.coin_list = None
        self.bad_guy_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        arcade.set_background_color((52, 168, 50))
        self.set_mouse_visible(False)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bad_guy_list = arcade.SpriteList()

        # Set up the player
        self.score = 0

        # Image from Arcade Library
        self.player_sprite = arcade.Sprite("maleAdventurer_idle.png")
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 70
        self.player_sprite.bottom = 0
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            # Create the coin instance
            # Coin image from Arcade Library
            coin = Coin("keyYellow.png", SPRITE_SCALING_COIN)

            # Position the coin
            coin.center_x = random.randrange(10, SCREEN_WIDTH - 10)
            coin.center_y = random.randrange(150, SCREEN_HEIGHT)

            if i % 2 == 0:
                coin.change_x = -1
            else:
                coin.change_x = 4
            coin.change_y = 1

            # Add the coin to the lists
            self.coin_list.append(coin)

        for i in range(BAD_GUY_COUNT):
            # Create the bad_guy instance
            # BadGuy image from Arcade Library
            bad_guy = BadGuy("zombie_jump.png", SPRITE_SCALING_COIN)

            # Position the coin
            bad_guy.center_x = random.randrange(10, SCREEN_WIDTH - 10)
            bad_guy.center_y = random.randrange(150, SCREEN_HEIGHT)

            if i == 0 or i == 1:
                bad_guy.change_x = 10
                bad_guy.change_y = 2
            else:
                bad_guy.change_x = 1
                bad_guy.change_y = 1

            # Add the bad_guy to the lists
            self.bad_guy_list.append(bad_guy)

    def on_draw(self):
        arcade.start_render()
        self.coin_list.draw()
        self.player_list.draw()
        self.bad_guy_list.draw()

        if len(self.coin_list) == 0:
            arcade.draw_text("Game over!", SCREEN_WIDTH / 2 - 50, SCREEN_HEIGHT / 2, arcade.color.WHITE, 28)

        arcade.draw_text(f"Score: {self.score}", 10, 20, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        if len(self.coin_list) > 0:
            self.coin_list.update()
            self.bad_guy_list.update()
        else:
            self.set_mouse_visible(True)

        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coin_hit_list:
            arcade.play_sound(self.coin_sound)
            coin.remove_from_sprite_lists()
            self.score += 1

        bad_guy_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.bad_guy_list)
        for bad_guy in bad_guy_hit_list:
            arcade.play_sound(self.bad_guy_sound)
            bad_guy.remove_from_sprite_lists()
            self.score -= 1

    def on_mouse_motion(self, x, y, dx, dy):
        if len(self.coin_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing Example")
    window.setup()
    arcade.run()


main()
