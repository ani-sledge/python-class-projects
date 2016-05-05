# Memory Card Game

import simplegui
import random

# Global variables

image = simplegui.load_image("https://www.usgamesinc.com/files/detailed_images/ANS108_2.jpg")
image_width = image.get_width()
image_height = image.get_height()
WIDTH = 800
HEIGHT = 80
card_num = 16
card_width = WIDTH / card_num
memory = []
exposed = []
state = 0
c1 = 0
c2 = 0
turns = 0


# Helper functions
def new_game():
    global memory, exposed, state, turns
    memory = range(8) + range(8)
    random.shuffle(memory)
    exposed = [False, False, False, False, False, False, False, False, 
               False, False, False, False, False, False, False, False]
    state, turns = 0, 0
    label.set_text("Turns = " + str(turns))

# Event handlers
def mouseclick(pos):
    global state, c1, c2, turns
    if not exposed[pos[0] / card_width]: 
        exposed[pos[0] / card_width] = True

        if state == 0:
            state = 1
        elif state == 1:
            state = 2
            turns += 1
        else:
            state = 1
            if memory[c1] != memory[c2]:
                exposed[c1], exposed[c2] = False, False
        c2 = c1
        c1 = pos[0] / card_width 
        label.set_text("Turns = " + str(turns))
    
# Draw handler    
def draw(canvas):
    x = 25
    count = 0
    for number in memory: 
        if exposed[count]: 
            canvas.draw_text(str(number), (x - 10, 55), 40, "White") 
        else: 
            canvas.draw_image(image, (image_width / 2, image_height / 2), (image_width, image_height), (x, HEIGHT / 2), (50, HEIGHT))
        x += card_width
        count += 1

# Creates frame and adds a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# Registers event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# Starts game
new_game()
frame.start()

