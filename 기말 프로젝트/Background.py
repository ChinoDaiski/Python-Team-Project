
from gfw.gfw import *


resource = 'resource/'

class Backgrond:

    image = None

    def __init__(self):
        if Backgrond.image == None:
            Backgrond.image = load_image(resource + 'background.png')

    def draw(self):
        self.image.draw(300, 400)

    def update(self):
        pass
    
    def late_update(self):
        pass

    
if __name__ == "__main__":
	print("Running test code ^_^")
