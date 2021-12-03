import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

class Grid(GridLayout):
    def __init__(self, **kwargs):
        super(Grid, self).__init__(**kwargs)
        
        self.cols = 1
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        #username
        self.top_grid.add_widget(Label(text="Username:",))
        self.user = TextInput(multiline=True)
        self.top_grid.add_widget(self.user)
        #alamat
        self.top_grid.add_widget(Label(text="Alamat:"))
        self.alamat = TextInput(multiline=True)
        self.top_grid.add_widget(self.alamat)
        
        self.add_widget(self.top_grid)
        #button
        self.btn = Button(text="Submit",
            font_size= 30,
            size_hint_y= None,
            height= 50,
            size_hint_x= None,
            width= 150)
        
        self.btn.bind(on_press=self.hasil)
        self.add_widget(self.btn)
        
    def hasil(self, instance):
        username = self.user.text
        alamat = self.alamat.text
        
        self.add_widget(Label(text=f"Hallo {username}, your addres is {alamat}"))
        
        self.user.text = ""
        self.alamat.text = ""
        
class MyApp(App):
    def build(self):
        return Grid()
if __name__ == '__main__':
    MyApp().run()
