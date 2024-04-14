from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.switch import Switch
from kivy.uix.filechooser import FileChooser
from kivy.uix.spinner import Spinner
from random import randint, choice


class MyApp(App):
    def build(self):
        button = Button(text="натисни")
        button1 = Button(text="delete file system32")
        self.label = Label(text="привіт")
        switch = Switch()
        fileChooser = FileChooser()
        spinner = Spinner()

        layout = BoxLayout(orientation="vertical")
        layout.add_widget(button)
        layout.add_widget(button1)
        layout.add_widget(self.label)
        layout.add_widget(switch)
        layout.add_widget(fileChooser)
        layout.add_widget(spinner)
        button.bind(on_press=self.click_button)

        return layout
              
    def click_button(self,instance):
        list1 = ''        
          
        parol = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
       

        for _ in range(8):
            list1 += choice(parol)
        self.label.text = str(list1)  



if __name__ == "__main__":
    MyApp().run()