import image
import random

img = image.Image("luther.jpg")
new_img = image.EmptyImage(img.getWidth(), img.getHeight())
win = image.ImageWin(img.getWidth(), img.getHeight())

for i in range(1, img.getWidth() - 1):
    for j in range(1, img.getHeight() - 1):
        # pick a random neighbor
        nx = random.randint(i-1, i+1)
        ny = random.randint(j-1, j+1)
        
        # set this pixel to neighbor's color
        neighbor_color = img.getPixel(nx, ny)
        new_img.setPixel(i,j, neighbor_color)
        

new_img.draw(win)
win.exitonclick()



