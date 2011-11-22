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
border = random.randint(4, border - 2) # body must be > leg width + 1px and must leave >3px for arms
height = random.randint(3, 8)

print "Body Height: " + str(height) + "\tBody Border: " + str(border)

bot_left = (border,top_left[y])
top_right = (robot.size[x] - 1 - border, top_right[y] - height)

#print "BL: " + str(bot_left) + "\tTR: " + str(top_right)
draw.rectangle([bot_left, top_right], fill=colors[2], outline=colors[0])


""" cleanup """

del draw
robot.show()
robot.save('robot.png')