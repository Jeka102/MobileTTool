import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.pagelayout import PageLayout
from kivy.uix.label import Label
from kivy.base import runTouchApp
from kivy.lang import Builder


kv = '''
PageLayout:
    GridLayout:
        canvas:
            Color:
                rgba: 0/255., 0/255., 0/255., 1
            Rectangle:
                pos: self.pos
                size: self.size
        rows: 4
        GridLayout:
            canvas:
                Color:
                    rgba: 0/255., 0/255., 0/255., 1
                Rectangle:
                    pos: self.pos
                    size: self.size
            cols: 1
            AsyncImage:
                source: 'images/unknown.png'
        GridLayout:
            canvas:
                Color:
                    rgba: 0/255., 0/255., 0/255., 1
                Rectangle:
                    pos: self.pos
                    size: self.size
            cols: 2
            Label:
                text: 'Логин'
            TextInput
        GridLayout:
            canvas:
                Color:
                    rgba: 0/255., 0/255., 0/255., 1
                Rectangle:
                    pos: self.pos
                    size: self.size
            cols: 2
            Label:
                text: 'Пароль'
            TextInput        
        GridLayout:
            canvas:
                Color:
                    rgba: 0/255., 0/255., 0/255., 1
                Rectangle:
                    pos: self.pos
                    size: self.size
            cols: 1
            Button:
                text: 'Подключиться'
            TextInput    
    BoxLayout:
        canvas:
            Color:
                rgba: 0/255., 0/255., 0/255., 1
            Rectangle:
                pos: self.pos
                size: self.size

        orientation: 'vertical'
        Label:
            size_hint_y: None
            height: 1.5 * self.texture_size[1]
            text: 'Тут будут настройки и морда капсулера!'
    BoxLayout:
        canvas:
            Color:
                rgba: 109/255., 8/255., 57/255., 1
            Rectangle:
                pos: self.pos
                size: self.size

        orientation: 'vertical'
        Label:
            size_hint_y: None
            height: 1.5 * self.texture_size[1]
            text: 'Тут будет график капитала!'

        Button:
            text: 'test'
            on_press: print("test")
    BoxLayout:
        canvas:
            Color:
                rgba: 109/255., 8/255., 57/255., 1
            Rectangle:
                pos: self.pos
                size: self.size

        orientation: 'vertical'
        Label:
            size_hint_y: None
            height: 1.5 * self.texture_size[1]
            text: 'Тут будет каталог товаров с ценами!'

        Button:
            text: 'test'
            on_press: print("test")            
    BoxLayout:
        orientation: 'vertical'
        canvas:
            Color:
                rgba: 109/255., 8/255., 57/255., 1
            Rectangle:
                pos: self.pos
                size: self.size

        Label:
            text: 'page 2'

        AsyncImage:
            source: 'http://kivy.org/logos/kivy-logo-black-64.png'

    GridLayout:
        canvas:
            Color:
                rgba: 0/255., 0/255., 0/255., 1
            Rectangle:
                pos: self.pos
                size: self.size

        cols: 2
        Label:
            text: 'page 3'
        AsyncImage:
            source: 'http://kivy.org/slides/kivyandroid-thumb.jpg'
        Button:
            text: 'test'
            on_press: print("test last page")
        AsyncImage:
            source: 'http://kivy.org/slides/kivypictures-thumb.jpg'
        Widget
        AsyncImage:
            source: 'http://kivy.org/slides/particlepanda-thumb.jpg'
'''


if __name__ == '__main__':
    runTouchApp(Builder.load_string(kv))
