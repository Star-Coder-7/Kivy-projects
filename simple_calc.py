from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500, 700)

Builder.load_file('simple_calc.kv')


class MyBoxLayout(Widget):
    def clear(self):
        self.ids.calcInput.text = '0'

    def clearEntry(self):
        expression = self.ids.calcInput.text
        expression = expression[:-1]
        self.ids.calcInput.text = expression

    def buttonEntry(self, entry):
        expression = self.ids.calcInput.text

        if "Sorry, Error" in expression:
            expression = ''

        if self.ids.calcInput.text == '0':
            expression = ''

        self.ids.calcInput.text = f'{expression}{entry}'

    def buttonEqual(self):
        expression = self.ids.calcInput.text

        try:
            self.ids.calcInput.text = str(eval(expression))
        except:
            self.ids.calcInput.text = "Sorry, Error"

    def buttonDot(self):
        expression = self.ids.calcInput.text
        numList = expression.split('+')

        if '+' in expression and '.' not in numList[-1]:
            self.ids.calcInput.text = f'{expression}.'

        elif '.' in expression:
            pass
        else:
            self.ids.calcInput.text = f'{expression}.'

    def pos_neg(self):
        expression = self.ids.calcInput.text

        if '-' in expression[0]:
            self.ids.calcInput.text = f'{expression.replace("-", "")}'
        else:
            self.ids.calcInput.text = f'-{expression}'


class CalculatorApp(App):
    def build(self):
        return MyBoxLayout()


if __name__ == '__main__':
    CalculatorApp().run()






