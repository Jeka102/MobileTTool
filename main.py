import kivy
import webbrowser
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout


Builder.load_file('MainLayout.kv')

class MainLayout(FloatLayout):
    def redirect_to_eve(self):
        webbrowser.open_new('https://login.eveonline.com/v2/oauth/authorize/')

class MobileTTool(App):
    def build(self):
        return MainLayout()

if __name__ == '__main__':
    MobileTTool().run()
