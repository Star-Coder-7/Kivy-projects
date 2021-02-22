from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.image import Image

Builder.load_file('image.kv')


class MyBoxLayout(Widget):
    pass


class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (66/255, 69/255, 245/255, 1)
        return MyBoxLayout()


if __name__ == '__main__':
    AwesomeApp().run()



