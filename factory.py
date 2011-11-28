import random
import math
import Image
import ImageDraw
import sys

""" global vars """
colors = ['rgb(0, 0, 0)', 'rgb(46, 76, 16)', 'rgb(96, 152, 48)', 'rgb(152, 200, 200)', 'rgb(200, 248, 152)'] #darkest to lightest
size = (20, 32)
x, y = 0, 1



class robo_piece:
    width = 0
    height = 0
    left = 0
    right = 0
    bottom = 0
    top = 0

    def __str__(self):
        return str(self.width) + "px, " + str(self.height) + "px"

class robot:

    head = robo_piece()
    arms = robo_piece()
    body = robo_piece()
    legs = robo_piece()
    eyes = robo_piece()
    
    def __init__(self, size):
        """ random sizes """
        maxheight = int(math.ceil(size[y]/3.0)) #maximum height is 1/3rd of the canvas
        self.size = size
        
        self.arms.width = random.randint(2,3)
        
        self.body.width = random.randrange(4, size[x] - (self.arms.width * 2) + 1, 2)
        self.body.height = random.randint(4, maxheight)
        
        self.legs.width = random.randrange(4, self.body.width + 1, 2)
        self.legs.height = random.randint(3, maxheight) 
        
        self.head.width = random.randrange(8, size[x] + 1, 2)
        self.head.height = random.randint(7, maxheight)

        self.eyes.width = random.randrange(4, self.head.width - 3, 2)
        self.eyes.height = 3

        """ additional calcs """
        self.arms.height = self.size[y] - self.legs.height - self.body.height + int(math.ceil(self.body.height/2))
        
        self.body.left = int(round((self.size[x] - self.body.width)/2))
        self.body.right = self.body.left + self.body.width - 1
        self.body.bottom = self.size[y] - 1 - self.legs.height
        self.body.top = self.size[y] - self.legs.height - self.body.height
        
        self.legs.left = int(round((self.size[x] - self.legs.width)/2))
        self.legs.right = self.legs.left + self.legs.width - 1
        self.legs.bottom = self.size[y] - 1
        self.legs.top = self.size[y] - self.legs.height
        
        self.head.left = int(round((self.size[x] - self.head.width)/2))
        self.head.right = self.head.left + self.head.width - 1
        self.head.bottom = self.size[y] - 1 - self.legs.height - self.body.height + 1
        self.head.top = self.head.bottom - self.head.height + 1
        
        self.eyes.left = int(round((self.size[x] - self.eyes.width)/2))
        self.eyes.right = self.eyes.left + self.eyes.width - 1
        if self.head.height > 4 + self.eyes.height:
            self.eyes.bottom = random.randrange(self.head.top + 2 + self.eyes.height - 1, self.head.bottom - 2)
            self.eyes.top = self.eyes.bottom - self.eyes.height + 1
        else:
            self.eyes.bottom = self.head.bottom - 2
            self.eyes.top = self.head.top + 2
        
        """ accessories """
        self.hands = False
        self.antenna = False
        if (size[x] - self.body.width - (self.arms.width * 2) >= 6) and random.choice([True, False]):
            self.hands = True
        
        
        
    def __str__(self):
        return 'head: ' + str(self.head) + '\nbody: ' + str(self.body) + '\narms: ' + str(self.arms) + '\nlegs: ' + str(self.legs) + '\nhands: ' + str(self.hands) + '\neyes: ' + str(self.eyes)

    def __test__(self):
        # check if no robo_pieces have negative values
        i=0

    def draw(self, colors):
        """ init """
        canvas = Image.new('RGB', self.size, 'rgb(220,220,220)')
        draw = ImageDraw.Draw(canvas)
        alpha = Image.new('L', self.size, 0)

        """ legs """
        draw.line([(self.legs.left, self.legs.bottom),(self.legs.left, self.legs.top)], fill=colors[0])
        draw.line([(self.legs.right, self.legs.bottom),(self.legs.right, self.legs.top)], fill=colors[0])

        """ body """
        draw.rectangle([self.body.left, self.body.bottom, self.body.right, self.body.top], fill=colors[2], outline=colors[0])
        draw.line([(self.body.left + 1, self.body.top + 2),(self.body.left + 1, self.body.bottom - 1)], fill=colors[3]) #light shading

        if self.head.width >= self.body.width:
            draw.line([(self.body.left + 2, self.body.top + 1),(self.body.right - 1, self.body.top + 1)], fill=colors[1]) #dark shading
        else:
            draw.line([(self.body.left + 2, self.body.top + 1),(self.head.left, self.body.top + 1)], fill=colors[3]) #light shading
            draw.line([(self.head.left + 1, self.body.top + 1),(self.body.right - 1, self.body.top + 1)], fill=colors[1]) #shadow shading

        """ arms """
        draw.line([(self.body.left - self.arms.width, self.arms.height),(self.body.left - 1, self.arms.height)], fill=colors[0]) #left
        draw.line([(self.body.right + 1, self.arms.height), (self.body.right + self.arms.width, self.arms.height)], fill=colors[0]) #right

        """ head """
        draw.rectangle([self.head.left, self.head.bottom, self.head.right, self.head.top], fill=colors[2], outline=colors[0])
        draw.line([self.head.left + 2, self.head.top + 1, self.head.right - 1, self.head.top + 1], fill=colors[4])
        draw.line([self.head.left + 1, self.head.top + 2, self.head.left + 1, self.head.bottom - 1], fill=colors[3])
        
        """ eyes """
        draw.point((self.eyes.left, self.eyes.bottom), fill=colors[3])
        draw.point((self.eyes.left, self.eyes.bottom - 1 ), fill=colors[0])
        draw.point((self.eyes.left, self.eyes.top ), fill=colors[1])  
        draw.point((self.eyes.right, self.eyes.bottom), fill=colors[3])
        draw.point((self.eyes.right, self.eyes.bottom - 1 ), fill=colors[0])
        draw.point((self.eyes.right, self.eyes.top ), fill=colors[1])
        
        del draw
        return canvas

def randcolor():
    return 'hsl(' + str(random.randrange(0, 360)) + ', ' + str(random.randrange(0, 100)) + '%, ' + str(random.randrange(0, 100)) + '%)'

def randcolors():
    colors = ['','','','','']
    colors[0] = 'rgb(0,0,0)'
    colors[1] = 'hsl(' + str(random.randrange(0, 360)) + ', ' + str(random.randrange(0, 100)) + '%, ' + str(random.randrange(20, 40)) + '%)'
    colors[2] = 'hsl(' + str(random.randrange(0, 360)) + ', ' + str(random.randrange(0, 100)) + '%, ' + str(random.randrange(40, 60)) + '%)'
    colors[3] = 'hsl(' + str(random.randrange(0, 360)) + ', ' + str(random.randrange(0, 100)) + '%, ' + str(random.randrange(60, 80)) + '%)'
    colors[4] = 'hsl(' + str(random.randrange(0, 360)) + ', ' + str(random.randrange(0, 100)) + '%, ' + str(random.randrange(80, 100)) + '%)'    
    return colors


def batch_print(count):
    for i in range(0, count):
        r = robot(size)
        #print str(r) + "\n"
        c = r.draw(randcolors())
        c.show()
        #c.save("robot.png")

count = 1
if len(sys.argv) >= 2: 
    count = int(sys.argv[1])
batch_print(count)

    

    
