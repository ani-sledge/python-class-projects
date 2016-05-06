# Pong Game
"""Mimics the classic Pong arcade game. Users must move the paddles up and
   down to reflect the ball, and try to bounce the ball into their opponents
   gutter. If the ball hits the gutter, it respawns in the center of the field, 
   moving in the direction of the point scorer. The restart button resets the 
   score and respawns the ball. 
"""
import simplegui
import random

#Global Variables
WIDTH = 600
HEIGHT = 400       
LEFT = False
RIGHT = True
score1 = 0
score2 = 0

PAD_WIDTH = 8
PAD_HEIGHT = 80
paddle1_pos = 100
paddle2_pos = 100
paddle1_vel = 0
paddle2_vel = 0

ball_radius = 10
ball_pos = [300, 200]
ball_vel = [0, 0]

# Helper Functions
def spawn_ball(direction):
    """Respawns the ball toward the upper right or upper left, with a random velocity"""
    
    global ball_pos, ball_vel
    ball_pos = [(WIDTH / 2), (HEIGHT / 2)]    
    
    if direction:
        ball_vel[0] = random.randrange(2, 5) 
        ball_vel[1] = random.randrange(1, 4) * -1
    else: 
        ball_vel[0] = random.randrange(2, 5) * -1
        ball_vel[1] = random.randrange(1, 4) * -1
    
def new_game():
    """Resets the score, paddle positions, and paddle velocity.
       Respawns the ball to the upper right."""
    
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, score1, score2 
    
    paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel = 160, 160, 0, 0
    score1, score2 = 0, 0
    spawn_ball(RIGHT)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # draws mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # updates the balls position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    #reverses ball velocity if the ball touches the top or bottom of the canvas
    if (HEIGHT - 1 - ball_radius) < ball_pos[1] or ball_pos[1] < ball_radius:
        ball_vel[1] = (ball_vel[1] * -1)
    
    #determines whether the ball has hit a paddle1, paddle2, or the gutter
    #ball changes direction and increases speed by 10% if within paddle range
    #if outside the paddle range, the ball respawns and the score increases  
    elif (WIDTH - PAD_WIDTH - ball_radius) <= ball_pos[0]:      
        if (paddle2_pos - ball_radius) < ball_pos[1] < (paddle2_pos + PAD_HEIGHT + ball_radius): 
            ball_vel[0] = (ball_vel[0] * -1.1)       
        else: 	
            score1 += 1
            spawn_ball(LEFT) 
    
    elif ball_pos[0] <= (ball_radius + PAD_WIDTH): 
        if (paddle1_pos - ball_radius) <= ball_pos[1] <= (paddle1_pos + PAD_HEIGHT + ball_radius): 
            ball_vel[0] = (ball_vel[0] * -1.1)        
        else:
            score2 += 1
            spawn_ball(RIGHT)

    #Draws the ball
    canvas.draw_circle(ball_pos, ball_radius, 2, "White", "White")
    
    #Updates the paddle position, if the paddle will remain on the screen
    if (HEIGHT - PAD_HEIGHT - paddle1_vel) >= paddle1_pos >= (-1 * paddle1_vel):
        paddle1_pos += paddle1_vel
    if (HEIGHT - PAD_HEIGHT - paddle2_vel) >= paddle2_pos >= (-1 * paddle2_vel):
        paddle2_pos += paddle2_vel
    
    #Draws the paddles
    canvas.draw_polygon([(0, (PAD_HEIGHT + paddle1_pos)), (0, paddle1_pos), 
                         (PAD_WIDTH, paddle1_pos), (PAD_WIDTH, (PAD_HEIGHT + paddle1_pos))], 
                        2, "White", "White")
    canvas.draw_polygon([((WIDTH - PAD_WIDTH), (PAD_HEIGHT + paddle2_pos)), 
                         ((WIDTH - PAD_WIDTH), paddle2_pos), (WIDTH, paddle2_pos), 
                         (WIDTH, (PAD_HEIGHT + paddle2_pos))], 2, "White", "White") 
       
    #Draws the score
    canvas.draw_text(str(score1), (150, 40), 24, "White") 
    canvas.draw_text(str(score2), (450, 40), 24, "White")

def restart(): 
    """Button handler to restart the game"""
    new_game()
    
def keydown(key):
    """Sets the paddle velocity based on the key pressed"""
    
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -8       
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = 8      
    if key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -8       
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 8    

def keyup(key):
    """Sets the paddle velocity to zero if the appropriate key is released"""
    
    global paddle1_vel, paddle2_vel    
    
    if key == simplegui.KEY_MAP["s"] or key == simplegui.KEY_MAP["w"]:
        paddle1_vel = 0   
    if key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 0
    
#Creates frame, sets event handlers
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart)

#Starts frame
new_game()
frame.start()
