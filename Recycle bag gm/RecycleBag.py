import pgzrun
import random

HEIGHT = 800
WIDTH = 800
CENTRE_X = 400
CENTRE_Y = 400
CENTRE = ( CENTRE_X , CENTRE_Y)
FINAL_LEVEL = 6
START_SPEED = 7 # seconds
ITEMS = [ "bag" , "battery" , "bottle" , "chips"]
game_over = False
game_complete = False
current_level = 1
items = []
animations = []

def draw():
    global items , current_level , game_complete , game_over
    screen.clear()
    screen.blit("bground" , (0,0))

    if game_over:
        display_message("GAME OVER", "Try again.")
    elif game_complete:
        display_message("YOU WON", "Well Done.")
    else:
        for item in items:
            item.draw()

def update():
    global items
    if len(items) == 0:
        items = make_items(current_level)
    # Item generation based on current level

def make_items(number_of_extra_items):
    items_to_create = get_option_to_create(number_of_extra_items)
    new_items = create_items(items_to_create)
    layout_items(new_items)
    animate_items(new_items)
    return new_items

# Selection of items to create 
def get_option_to_create(number_of_extra_items):
    items_to_create = ["paper_bag"]
    for i in range (0 , number_of_extra_items):
        random_option = random.choice(ITEMS)
        items_to_create.append(random_option)
    return items_to_create

# Creation of Actor Object On each item
def create_items(items_to_create):
    new_items = []
    for pic in items_to_create:
#option
        item = Actor(pic + "img")
        new_items.append(item)
    return new_items


def layout_items(items_to_layout):
    num_of_gaps = len(items_to_layout) + 1
    gap_size = WIDTH / num_of_gaps
    random.shuffle(items_to_layout)
    for index, item in enumerate(items_to_layout):
        new_x_pos = (index + 1) * gap_size
        item.x = new_x_pos

def animate_items(items_to_animate):
    global animations
    for item in items_to_animate:
        duration = START_SPEED - current_level
        item.anchor = ("center" , "bottom")
        animation = animate(item , duration = duration , on_finished = handle_game_over , y=HEIGHT)
        animations.append(animation)


def handle_game_over():
    global game_over
    game_over = True


def on_mouse_down(pos):
    global items , current_level
    for item in items:
        if item.collidepoint(pos):
            if "paper_bag" in item.image:
                handle_game_complete()
            else:
                handle_game_over()

def handle_game_complete():
    global game_complete , animations , items , current_level
    stop_animations(animations)
    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level += 1
        items = []
        animations = []


def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()
            

def display_message(heading_text , sub_heading_text):
    screen.draw.text(heading_text , fontsize = 60 , center=CENTRE , color = "white")
    screen.draw.text(sub_heading_text , fontsize = 40 , center=(CENTRE_X , CENTRE_Y+40) , color = "white")
pgzrun.go()