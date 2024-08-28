import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class RegistrationApp(App):
    def build(self):
        self.title = "Registration Form"
        layout = BoxLayout(orientation = 'vertical', padding= 30, spacing=10)

        head_label = Label()

        return layout
    


if __name__ == '__main__':
    RegistrationApp(). run()