import random
import math
import Image
import ImageDraw

""" global vars """
colors = ['rgb(0, 0, 0)', 'rgb(96, 48, 48)', 'rgb(96, 152, 48)', 'rgb(152, 200, 200)', 'rgb(200, 248, 152)'] #darkest to lightest
x = 0
y = 1
size = (32, 32)


class robot:
    def __init__(self, size):
        # maximum height is 25% of the canvas
        maxheight = int(math.floor(size[y]/4))
        
        self.head.width = random.randit(8, size[x])
        self.head.height = random.randit(7, maxheight)
        
        self.arms.width = random.randint(2,3)
        self.arms.height = 1
        
        self.body.width = random.randint(4, size[x] - self.arms.width)
        self.legs.height = random.randint(4, maxheight)
        
        self.legs.width = random.randint(4, self.body.width)
        self.legs.height = random.randint(3, maxheight)


def factory1 (colors, size):
    robot = Image.new('RGB', size, 'rgb(220,220,220)')
    draw = ImageDraw.Draw(robot)
    alpha = Image.new('L', size, 0)



def factory2 (colors, size):
    """ init """
    robot = Image.new('RGB', size, 'rgb(220,220,220)')
    draw = ImageDraw.Draw(robot)
    alpha = Image.new('L', size, 0)

    """ legs """
    border = random.randint(5, 14)
    height = random.randint(3, 8)

    print "Leg Height: " + str(height) + "\tLeg Border: " + str(border) + "\tLeg Width: " + str(size[x] - (border * 2))

    bot_left = (border, robot.size[y] - 1)
    top_left = (border, robot.size[y] - height)
    bot_right = (robot.size[x] - 1 - border, robot.size[y] - 1)
    top_right = (robot.size[x] - 1 - border, robot.size[y] - height)

    draw.line((bot_left, top_left), fill=colors[0])
    draw.line((bot_right, top_right), fill=colors[0])


    """ body """
    border = random.randint(4, border) # body must be > leg width + 1px and must leave >3px for arms
    height = random.randint(3, 8)

    print "Body Height: " + str(height) + "\tBody Border: " + str(border)

    bot_left = (border,top_left[y])
    #top_left = (border,)
    top_right = (robot.size[x] - 1 - border, top_right[y] - height)

    #print "BL: " + str(bot_left) + "\tTR: " + str(top_right)
    draw.rectangle([bot_left, top_right], fill=colors[2], outline=colors[0])

    """ head """



    """ cleanup """

    del draw
    robot.show()
    robot.save('robot.png')


factory2(colors, size)

#class robot:
     
