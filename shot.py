import factory
import Image

shot = Image.new('RGB', (400,300), 'white')

for i in range(10):
    c = factory.stitch_print(20, (20,30))
    shot.paste(c, (0, i * 30))
    
shot.show()
shot.save('shot.png')