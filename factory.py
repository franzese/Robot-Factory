import random
import math
import Image
import ImageDraw

""" global vars """
colors = ['rgb(0, 0, 0)', 'rgb(96, 48, 48)', 'rgb(96, 152, 48)', 'rgb(152, 200, 200)', 'rgb(200, 248, 152)'] #darkest to lightest
x = 0
y = 1
size = (32, 32)


class robo_piece:
    width = 0
    height = 0
    
    def __str__(self):
        return str(self.width) + "px, " + str(self.height) + "px"

class robot:
    head = robo_piece()
    arms = robo_piece()
    body = robo_piece()
    legs = robo_piece()
    
    def __init__(self, size):
        # maximum height is 33% of the canvas
        maxheight = int(math.ceil(size[y]/3.0))
        
        self.arms.width = random.randint(2,3)
        self.arms.height = 1
        
        self.body.width = random.randrange(4, size[x] - self.arms.width + 1, 2)
        self.body.height = random.randint(4, maxheight)
        
        self.legs.width = random.randrange(4, self.body.width + 1, 2)
        self.legs.height = random.randint(3, maxheight)
        
        self.head.width = random.randrange(8, size[x] + 1, 2)
        self.head.height = random.randint(7, maxheight)
        
    def __str__(self):
        return 'head: ' + str(self.head) + '\nbody: ' + str(self.body) + '\narms: ' + str(self.arms) + '\nlegs: ' + str(self.legs)

def factory(colors, size):
    """ init """
    bot = robot(size)
    canvas = Image.new('RGB', size, 'rgb(220,220,220)')
    draw = ImageDraw.Draw(canvas)
    alpha = Image.new('L', size, 0)

    """ legs """
    leg_offset = int(round((size[x] - bot.legs.width)/2))
    leg_left = ((leg_offset, size[y]), (leg_offset, size[y] - bot.legs.height))
    leg_right = ((leg_offset + bot.legs.width - 1, size[y]), (leg_offset + bot.legs.width - 1, size[y] - bot.legs.height))
    draw.line(leg_left, fill=colors[0])
    draw.line(leg_right, fill=colors[0])

    """ body """
    body_offset = int(round((size[x] - bot.body.width)/2))
    body_left = body_offset
    body_right = body_offset + bot.body.width - 1
    body_bottom = size[y] - 1 - bot.legs.height
    body_top = size[y] - bot.legs.height - bot.body.height
    bot_left = (body_offset, size[y] - 1 - bot.legs.height)
    top_right = (body_offset + bot.body.width - 1, size[y] - bot.legs.height - bot.body.height)
    draw.rectangle([bot_left, top_right], fill=colors[2], outline=colors[0])

    """ arms """
    arm_height = size[y] - bot.legs.height - bot.body.height + int(math.ceil(bot.body.height/2))
    arm_offset = (size[x] - bot.body.width - (bot.arms.width * 2))/2
    arm_left = ((arm_offset ,arm_height),(arm_offset + bot.arms.width - 1, arm_height))
    arm_right =  ((body_offset + bot.body.width, arm_height), (body_offset + bot.body.width + bot.arms.width - 1, arm_height))
    draw.line(arm_left, fill=colors[0])
    draw.line(arm_right, fill=colors[0])

    """ head """
    offset = int(round((size[x] - bot.head.width)/2))
    bot_left = (offset, size[y] - 1 - bot.legs.height - bot.body.height + 1)
    top_right = (offset + bot.head.width - 1, size[y] - bot.legs.height - bot.body.height - bot.head.height + 1)
    draw.rectangle([bot_left, top_right], fill=colors[2], outline=colors[0])

    
    del draw
    canvas.show()
    canvas.save('robot.png')
    
    
factory(colors, size)    
    
 
    
