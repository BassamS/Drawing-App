from .settings import *


class Button:
    def __init__(self, x, y, width, height, color, text=None, text_color=BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.hight = height
        self.color = color
        self.text = text
        self.text_color = text_color
