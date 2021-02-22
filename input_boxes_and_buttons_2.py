import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 1

        self.topGrid = GridLayout()
        self.topGrid.cols = 2

        self.topGrid.add_widget(Label(text="Name: "))

        self.name = TextInput(multiline=False)

        self.topGrid.add_widget(self.name)

        self.topGrid.add_widget(Label(text="Favorite Pizza: "))

        self.pizza = TextInput(multiline=False)

        self.topGrid.add_widget(self.pizza)

        self.topGrid.add_widget(Label(text="Favorite Color: "))

        self.color = TextInput(multiline=False)

        self.topGrid.add_widget(self.color)

        self.add_widget(self.topGrid)

        self.submit = Button(text="Submit", font_size=32)

        self.submit.bind(on_press=self.press)

        self.add_widget(self.submit)

    def press(self):
        name = self.name.text
        pizza = self.pizza.text
        color = self.color.text

        # print(f"hello {name}, your favorite pizza is {pizza} and you adore {color} the most!")
        self.add_widget(Label(text=f"Hello {name}, your favorite pizza is {pizza} and you adore {color} the most!"))

        self.name.text = ""
        self.pizza.text = ""
        self.color.text = ""


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()


