import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)

        self.cols = 6

        self.add_widget(Label(text="Name: "))

        self.name = TextInput(multiline=False)

        self.add_widget(self.name)

        self.add_widget(Label(text="Favorite Pizza: "))

        self.pizza = TextInput(multiline=False)

        self.add_widget(self.pizza)

        self.add_widget(Label(text="Favorite Color: "))

        self.color = TextInput(multiline=False)

        self.add_widget(self.color)

        self.submit = Button(text="Submit", font_size=32)
        self.add_widget(self.submit)


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()


