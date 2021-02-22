from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window
# from kivy.uix.floatlayout import FloatLayout

Builder.load_file('float.kv')


class MyFloatLayout(Widget):
    pass


class AwesomeApp(App):
    def build(self):
        Window.clearcolor = (66/255, 69/255, 245/255, 1)
        return MyFloatLayout()


if __name__ == '__main__':
    AwesomeApp().run()



