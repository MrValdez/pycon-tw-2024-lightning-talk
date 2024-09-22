import arcade
import random

resolution_width = 1024
resolution_height = 768

class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.CORNSILK)

    def setup(self):
        self.score = 0
        self.player = arcade.Sprite("python.png")

        self.zoo = arcade.SpriteList()
        animals = ["animal1.png", "animal2.png", "animal3.png"]

        for i in range(30):
            animal = arcade.Sprite(random.choice(animals))
            animal.center_x = random.randrange(resolution_width)
            animal.center_y = random.randrange(resolution_height)
            self.zoo.append(animal)
            

    def on_draw(self):
        self.clear()
        self.zoo.draw()
        self.player.draw()

    def on_update(self, delta_time):
        collisions = arcade.check_for_collision_with_list(self.player, self.zoo)
        for collision in collisions:
            collision.remove_from_sprite_lists()
            self.score += 1
            print(self.score)

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        self.player.center_x = x
        self.player.center_y = y


def main():
    game = MyGame(resolution_width, resolution_height, "PyCon TW Lightning Talk")
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()