import arcade
import random

resolution_width = 1024
resolution_height = 768

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.CORNSILK)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

    def on_update(self, delta_time):
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        pass


def main():
    game = MyGame(resolution_width, resolution_height, "PyCon TW Lightning Talk")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()