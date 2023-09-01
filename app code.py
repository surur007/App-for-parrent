import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class babyApp(GridLayout):
    def __init__(self,**kwargs):
        super(babyApp, self).__init__()
        self.cols = 3
        self.add_widget(Label(text = 'Baby Name'))
        self.b_name = TextInput ( )
        self.add_widget (self.b_name)

        self.add_widget(Label(text = 'Baby Marks'))
        self.b_marks = TextInput ( )
        self.add_widget(self.b_marks)

        self.add_widget(Label(text = 'Baby Gender'))
        self.b_gender = TextInput ( )
        self.add_widget(self.b_gender)

        self.press = Button(text_= 'Push Me')
        self.press.bind(on_press = self.push_me)
        self.add_widget(self.press)

        def push_me(self, instance):
            print("Name of Baby is "+self.b_name.text)
            print("Marks of Baby is " + self.b_marks.text)
            print("Gender of Baby is " + self.b_gender.text)
            print("")

class parentApp(App):
    def build(self):
        return babyApp()

if __name__ == "__main__":
    parentApp().run()

