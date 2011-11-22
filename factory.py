import random
import Image
import ImageDraw

""" global vars """
colors = ['rgb(0, 0, 0)', 'rgb(96, 48, 48)', 'rgb(96, 152, 48)', 'rgb(152, 200, 200)', 'rgb(200, 248, 152)'] #darkest to lightest
x = 0
y = 1
size = (32, 32)

""" init """
robot = Image.new('RGB', size, 'white')
draw = ImageDraw.Draw(robot)
alpha = Image.new('L', size, 0)



""" legs """
border = random.randint(5, 15)
height = random.randint(3, 8)

bot_left = (0 + border, robot.size[y] - 1)
top_left = (0 + border, robot.size[y] - height)
bot_right = (robot.size[x] - 1 - border, robot.size[y] - 1)
top_right = (robot.size[x] - 1 - border, robot.size[y] - height)

#print "Line 1\nBL: " + str(bot_left) + "\nTL: " + str(top_left)
#print "Line 2\nBR: " + str(bot_right) + "\nTR: " + str(top_right)

draw.line((bot_left, top_left), fill=colors[0])
draw.line((bot_right, top_right), fill=colors[0])


""" body """
border = random.randint() # body must be > leg width + 1px and must leave >3px for arms
height = random.randint(3, 8)

print "Body Offset: " + str(border) + "\nBody Height: " + str(height)

bot_left = (robot.size[1]/2 - border, top_left[0])
bot_right = (robot.size[1]/2 + border, top_right[0])
top_left = (robot.size[1]/2 - border, bot_left[1] + height)
top_right = (robot.size[1]/2 + border, bot_right[1] + height)

#print "\nBL: " + str(bot_left) + "\nTR: " + str(top_right)
draw.rectangle([bot_left, top_right], fill=colors[2], outline=colors[0])


""" cleanup """

del draw
robot.show()
robot.save('robot.png')
print '"robot.png" saved.'