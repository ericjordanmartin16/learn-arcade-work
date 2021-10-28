""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN = 0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Coin(arcade.Sprite):
    """def reset(self):
        self.bottom = random.randrange(SCREEN_HEIGHT, SCREEN_HEIGHT * 2)
        self.center_x = random.randrange(SCREEN_WIDTH)"""

    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.change_x = 0
        self.change_y = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if self.left < 0:
            self.change_x *= -1
        if self.right > SCREEN_WIDTH:
            self.change_x *= -1
        if self.bottom < 0 :
            self.change_x *= -1
        if self.top > SCREEN_HEIGHT:
            self.change_y *= -1
        """self.center_y -= 1
        if self.top <= 0:
            self.reset()"""


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.player_list = None
        self.coin_list = None

        self.player_sprite = None
        self.score = 0

        # self.set_mouse_visible(False)
        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        for i in range(COIN_COUNT):
            coin = Coin("coin.png", SPRITE_SCALING_COIN)
            coin.center_x = SCREEN_WIDTH / 2
            coin.center_y = 20 * i

            if i % 2 == 0:
                coin.change_x = -7
            else:
                coin.change_x = 7
            coin.change_y = 0
            self.coin_list.append(coin)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.coin_list.draw()

        # output = "Score: " + str(self.score)
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 28)

    def on_mouse_motion(self, x, y, dx, dy):
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def on_update(self, delta_time):
        """ Remove coins from screen upon collision with player; add 1 to the score for every collision. """
        self.coin_list.update()
        coin_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)
        for coin in coin_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
