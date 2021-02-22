from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder


Builder.load_file('update_label.kv')


class MyBoxLayout(Widget):
    def press(self):
        name = self.ids.name_input.text
        # print(name)
        self.ids.name_label.text = f'Hello {name}!'

        self.ids.name_input.text = ''


class AwesomeApp(App):
    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    AwesomeApp().run()
