from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Line
from kivy.clock import Clock

class EdgeLightWidget(Widget):
    def __init__(self, **kwargs):
        super(EdgeLightWidget, self).__init__(**kwargs)
        self.show_border = False
        self.bind(pos=self.update_canvas, size=self.update_canvas)

    def update_canvas(self, *args):
        self.canvas.clear()
        if self.show_border:
            with self.canvas:
                Color(0.9, 0.2, 0.2, 0.8)
                Line(rectangle=(self.x + 5, self.y + 5, self.width - 10, self.height - 10), width=8)

    def trigger_light(self, dt):
        self.show_border = True
        self.update_canvas()

class EdgeLightApp(App):
    def build(self):
        root_widget = EdgeLightWidget()
        Clock.schedule_once(root_widget.trigger_light, 10)
        return root_widget

if __name__ == '__main__':
    EdgeLightApp().run()
