#!/usr/bin/python3

import kivy
import kivy.app
import kivy.graphics
import kivy.uix.actionbar
import kivy.uix.button
import kivy.uix.image
import kivy.uix.gridlayout
import kivy.uix.label
import kivy.uix.stacklayout

kivy.require('1.8.0')

# Callback to update the background of a widget when it resizes.
def update_widget_bg(widget, value):
    widget.rect.pos = widget.pos
    widget.rect.size = widget.size

class MenuButton(kivy.uix.button.Button, kivy.uix.actionbar.ActionItem):

    def __init__(self, text, callback, **kargs):
        super().__init__(**kargs)
        self.text = text
        self.bind(on_press=callback)

class TopMenuView(kivy.uix.actionbar.ActionView):

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.action_previous = MenuButton('Back', self.multiply)
        self.padding = [10, 10]
        self.spacing = 10
        self.add_widget(MenuButton('Button', self.boom))

    def multiply(self, instance):
        self.add_widget(MenuButton('Button', self.boom))

    def boom(self, instance):
        self.clear_widgets()

class TopMenu(kivy.uix.actionbar.ActionBar):

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.size_hint = (100, 8)
        self.background_color = (255, 255, 255, 0.7)
        self.add_widget(TopMenuView())

class SelectionView(kivy.uix.stacklayout.StackLayout):

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.size_hint = (70, 100)
        # Add background texture.
        with self.canvas.before:
            self.rect = kivy.graphics.Rectangle(pos=self.pos, size=self.size,
                                                source='example.png')
        self.bind(pos=update_widget_bg, size=update_widget_bg)

class BodyPanel(kivy.uix.gridlayout.GridLayout):

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.size_hint = (100, 80)
        self.cols = 2
        self.add_widget(kivy.uix.label.Label(text='The thingy on the left',
                                             size_hint=(30, 100)))
        self.add_widget(SelectionView())

class FooterLabel(kivy.uix.label.Label):

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.text = 'You can get more games on the mod store or the web.'
        self.color = (0, 0, 0, 1)

class FooterPanel(kivy.uix.stacklayout.StackLayout):

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.size_hint = (100, 15)
        # Set up a background color.
        with self.canvas.before:
            self.color = kivy.graphics.Color(1, 1, 1, 0.7)
            self.rect = kivy.graphics.Rectangle(pos=self.pos, size=self.size)
        self.bind(pos=update_widget_bg, size=update_widget_bg)
        
        self.add_widget(FooterLabel())

class MainWindow(kivy.uix.gridlayout.GridLayout):

    def __init__(self, **kargs):
        super().__init__(**kargs)
        self.rows = 3
        self.add_widget(TopMenu())
        self.add_widget(BodyPanel())
        self.add_widget(FooterPanel())

class Launcher(kivy.app.App):

    def build(self):
        return MainWindow()

if __name__ == '__main__':
    main_app = Launcher()
    main_app.run()
