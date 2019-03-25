# Created by: Yusuf Moussa
# Created on: 25 March 2019
# Created for: ICS3U
# Daily Assignment Unit 3-0
# This program Calculates the cost of a pizza

from tkinter import *
import time
root = Tk()

imagelist= ['walk1.png', 'walk2.png', 'walk3.png', 'walk4.png', 'walk5.png', 'walk6.png', 'walk7.png', 'walk8.png', 'walk9.png', 'walk10.png']

photo = PhotoImage(file=imagelist[0])
width = photo.width()
height = photo.height()
canvas = Canvas(width=width, height=height)
canvas.pack()
# create a list of image objects
giflist = []
for imagefile in imagelist:
    photo = PhotoImage(file=imagefile)
    giflist.append(photo)
# loop through the gif image objects for a while
for k in range(0, 200):
    for gif in giflist:
        canvas.delete(ALL)
        canvas.create_image(width/2.0, height/2.0, image=gif)
        canvas.update()
        time.sleep(0.1)

root.mainloop()

