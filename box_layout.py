from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file('box.kv')


class MyBoxLayout(Widget):
    pass


class AwesomeApp(App):
    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    AwesomeApp().run()


