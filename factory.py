import random
import math
import Image
import ImageDraw
import sys

""" global vars """
colors = ['rgb(0, 0, 0)', 'rgb(46, 76, 16)', 'rgb(96, 152, 48)', 'rgb(152, 200, 200)', 'rgb(200, 248, 152)'] #darkest to lightest
size = (20, 32)
x, y = 0, 1


# experimental object
class robo_body: 
    __size = (0,0)

    left = 0 
    right = 0 #should be property
    bottom = 0 #should be property
    top = 0 #should be method

    def __init__(self, size):
        self.__size = size

    def get_width(self):
        return self.__width
        
    def set_width(self, width):
        self.__width = width

    width = property(get_width, set_width)

    def get_height(self):
        return self.__height
        
    def set_height(self, height):
        self.__height = height

    height = property(get_height, set_height)

    def __str__(self):
        return str(self.width) + "px, " + str(self.height) + "px"
        
        
class robo_piece: #http://blog.fedecarg.com/2008/08/17/no-need-for-setget-methods-in-python/
     width = 0 #should be property
     height = 0 #should be property
     left = 0 #should be property
     right = 0 #should be property
     bottom = 0 #should be property
     top = 0 #should be method

     def __str__(self):
         return str(self.width) + "px, " + str(self.height) + "px"   
                      
class robot:
    head = robo_piece()
    arms = robo_piece()
    body = robo_piece()
    legs = robo_piece()
    eyes = robo_accessory()
    tenna = robo_accessory()
    count_eyes = 3
    count_tenna = 5 # 4 different antennaes
    
    
    def __init__(self, size):
        """ random sizes """
        maxheight = int(math.ceil(size[y]/3.0)) #maximum height is 1/3rd of the canvas
        height = 0
        
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
        self.eyes.select = random.randrange(self.count_eyes)
        
        if size[y] - self.body.height - self.legs.height - self.head.height + 1 >= 4:
            self.tenna.width = random.randrange(4, self.head.width + 1, 2)
            self.tenna.height = size[y] - self.body.height - self.legs.height - self.head.height + 1
            self.tenna.select = random.randrange(1, self.count_tenna)
        else:
            self.tenna.select = 0

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
            
        self.tenna.left = int(round((self.size[x] - self.tenna.width)/2))
        self.tenna.right = self.tenna.left + self.tenna.width - 1
        self.tenna.bottom = self.head.top - 1
        self.tenna.top = self.tenna.bottom - self.tenna.height + 1
        
    def __str__(self):
        return 'head: ' + str(self.head) + '\nbody: ' + str(self.body) + '\narms: ' + str(self.arms) + '\nlegs: ' + str(self.legs) + '\nhands: ' + str(self.hands) + '\neyes: ' + str(self.eyes)

    def draw(self, colors, **kwargs):
        """ init """
        canvas = Image.new('RGB', self.size, 'rgb(255,255,255)')
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
        
        """ eyes - 3 selections @ 100%"""
        if self.eyes.select is 0:
            draw.point((self.eyes.left, self.eyes.bottom), fill=colors[3])
            draw.point((self.eyes.left, self.eyes.bottom - 1 ), fill=colors[0])
            draw.point((self.eyes.left, self.eyes.top ), fill=colors[1])  
            draw.point((self.eyes.right, self.eyes.bottom), fill=colors[3])
            draw.point((self.eyes.right, self.eyes.bottom - 1 ), fill=colors[0])
            draw.point((self.eyes.right, self.eyes.top ), fill=colors[1])
        elif self.eyes.select is 1:
            draw.point((self.eyes.left, self.eyes.bottom), fill=colors[1])
            draw.point((self.eyes.left, self.eyes.bottom - 1 ), fill=colors[0])
            draw.point((self.eyes.left, self.eyes.top ), fill=colors[3])  
            draw.point((self.eyes.right, self.eyes.bottom), fill=colors[1])
            draw.point((self.eyes.right, self.eyes.bottom - 1 ), fill=colors[0])
            draw.point((self.eyes.right, self.eyes.top ), fill=colors[3])
        elif self.eyes.select is 2: # and self.eyes.width <= 4 :
            draw.line([(self.eyes.left, self.eyes.bottom - 1),(self.eyes.left + 1, self.eyes.bottom - 1)], fill=colors[0])
            draw.line([(self.eyes.left, self.eyes.bottom),(self.eyes.left + 1, self.eyes.bottom)], fill=colors[3])
            draw.line([(self.eyes.right, self.eyes.bottom - 1),(self.eyes.right - 1, self.eyes.bottom - 1)], fill=colors[0])
            draw.line([(self.eyes.right, self.eyes.bottom),(self.eyes.right - 1, self.eyes.bottom)], fill=colors[3])

        """ antenna - 4 selections @ 60% """
        prob = 0.6
        while random.random() < prob and self.tenna.select is not 0 and self.tenna.height >= 4: # and has at least 4px of space
            if self.tenna.select is 1:
                if self.tenna.width is self.head.width:
                    self.tenna.width -= 2
                    self.tenna.left += 1
                    self.tenna.right -= 1
                self.tenna.height = min(4, self.tenna.height)
                self.tenna.top = self.tenna.bottom - self.tenna.height + 1
                draw.line([(self.tenna.left, self.tenna.bottom),(self.tenna.left, self.tenna.bottom - self.tenna.height + 1)], fill=colors[0])
                draw.point((self.tenna.left, self.tenna.bottom - self.tenna.height + 2), fill=colors[3])
                draw.line([(self.tenna.right, self.tenna.bottom),(self.tenna.right, self.tenna.bottom  - self.tenna.height + 1)], fill=colors[0])        
                draw.point((self.tenna.right, self.tenna.bottom - self.tenna.height + 2), fill=colors[3])
                break
            elif self.tenna.select is 2:
                self.tenna.height = min(4, self.tenna.height)
                self.tenna.top = self.tenna.bottom - self.tenna.height + 1
                draw.line([(self.head.right - 1, self.tenna.bottom),(self.head.right - 1, self.tenna.top)], fill=colors[0])
                break
            elif self.tenna.select is 3:
                self.tenna.height = min(2, self.tenna.height)
                self.tenna.top = self.tenna.bottom - self.tenna.height + 1
                draw.line([(self.head.left, self.tenna.bottom),(self.head.left, self.tenna.top)], fill=colors[0])
                break
            elif self.tenna.select is 4: # rejection constraints
                if self.head.width >= 10:
                    if self.head.width >= 12:
                        self.tenna.width = random.choice((10,12))
                    else:
                        self.tenna.width = 10
                    self.tenna.height = 3
                    self.tenna.left = int(round((self.size[x] - self.tenna.width)/2))
                    self.tenna.right = self.tenna.left + self.tenna.width - 1
                    self.tenna.bottom = self.head.top - 1
                    self.tenna.top = self.tenna.bottom - self.tenna.height + 1
                    draw.line([(self.tenna.left,self.tenna.bottom),(self.tenna.left, self.tenna.top)], fill=colors[0])
                    draw.line([(self.tenna.right,self.tenna.bottom),(self.tenna.right, self.tenna.top)], fill=colors[0])
                    draw.point((self.tenna.left + self.tenna.width/2 - 1, self.tenna.top), fill=colors[2])
                    draw.point((self.tenna.left + self.tenna.width/2 , self.tenna.top + 1), fill=colors[2])
                    draw.point((self.tenna.left + self.tenna.width/2 - 2, self.tenna.top), fill=colors[3])
                    draw.point((self.tenna.left + self.tenna.width/2 - 1, self.tenna.top - 1), fill=colors[3])
                    draw.point((self.tenna.left + self.tenna.width/2 + 1, self.tenna.top), fill=colors[3])
                    break
                else:
                    self.tenna.select = random.randrange(1, self.count_tenna)
                    continue
                    
        
        """ optional keyword arguments """
        if 'palette' in kwargs and kwargs['palette'] is True:
            draw.rectangle([(0,0),(1,1)], fill=colors[0])
            draw.rectangle([(0,2),(1,3)], fill=colors[1])
            draw.rectangle([(0,4),(1,5)], fill=colors[2])
            draw.rectangle([(0,6),(1,7)], fill=colors[3])
            draw.rectangle([(0,8),(1,9)], fill=colors[4])        
        
        del draw
        return canvas

# returns a list of 5 colors ordered from darkest -> lightest
def randcolors():
    colors = ['','','','','']
    colors[0] = 'rgb(0,0,0)'
    colors[1] = 'hsl(' + str(random.randrange(0, 360)) + ', ' + str(random.randrange(25, 100)) + '%, ' + str(random.randrange(20, 40)) + '%)'
    colors[2] = 'hsl(' + str(random.randrange(0, 360)) + ', ' + str(random.randrange(25, 100)) + '%, ' + str(random.randrange(40, 60)) + '%)'
    colors[3] = 'hsl(' + str(random.randrange(0, 360)) + ', ' + str(random.randrange(25, 100)) + '%, ' + str(random.randrange(60, 80)) + '%)'
    colors[4] = 'hsl(' + str(random.randrange(0, 360)) + ', ' + str(random.randrange(25, 100)) + '%, ' + str(random.randrange(80, 100)) + '%)'    
    return colors

# prints the given number of robots side by side in 1 image
def stitch_print(count, size):
    c = Image.new('RGB', (size[x] * count, size[y]), 'rgb(220,220,220)')
    for i in range(count):
        r = robot(size)
        c.paste(r.draw(randcolors()), (size[x]* i,0))
    c.save('robot.png')
    c.show()
    
# prints the given number of robots in individual images
def batch_print(count, size):
    for i in range(count):
        r = robot(size)
        c = r.draw(randcolors())
        #c.save("robot.png")
        c.show()

count = 1
if len(sys.argv) >= 2: 
    count = int(sys.argv[1])
stitch_print(count, size)

    

    
