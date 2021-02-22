from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('color.kv')


class MyGridLayout(Widget):

    name = ObjectProperty(None)
    pizza = ObjectProperty(None)
    color = ObjectProperty(None)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # print(f"hello {name}, your favorite pizza is {pizza} and you adore {color} the most!")
        # self.add_widget(Label(text=f"Hello {name}, your favorite pizza is {pizza} and you adore {color} the most!"))
        print(f"Hello {name}, your favorite pizza is {pizza} and you adore {color} the most!")

        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class AwesomeApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    AwesomeApp().run()


