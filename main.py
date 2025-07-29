import kivy
kivy.require('2.1.0')

from kivy.properties import NumericProperty, BooleanProperty
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.clock import Clock

class BallApp(App):
    def build(self):
        return BallGame()

class BallGame(Widget):
    score = NumericProperty(0)
    has_scored = BooleanProperty(False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1 / 60.0)

    def update(self, dt):
        ball = self.ids.ball
        obstacle = self.ids.obstacle

        #Apply gravity
        ball.velocity_y -= 1
        x, y = ball.pos
        y += ball.velocity_y

        #Stop falling when the ball hits the ground
        ground = self.height / 4 + 25
        if y < ground:
            y = ground
            ball.velocity_y = 0
        ball.pos = ( x, y )

        #Move obstacle left across the screen
        ox, oy = obstacle.pos
        ox -= 4

        if ox + obstacle.width < 0:
            ox = self.width
        obstacle.pos = ( ox, oy )

        self.check_collision()

        if not self.has_scored and ball.x > obstacle.x + obstacle.width:
            self.score += 1
            self.ids.score_label.text = str(self.score)
            self.has_scored = True



    def move_up(self):
        ball = self.ids.ball
        if ball.velocity_y == 0:
            ball.velocity_y = 20

    def check_collision(self):
        ball = self.ids.ball
        obstacle = self.ids.obstacle

        if ball.collide_widget(obstacle):
            pass

class Ball(Widget):
    velocity_y = NumericProperty(0)

class Obstacle(Widget):
    pass

if __name__ == '__main__':
    BallApp().run()