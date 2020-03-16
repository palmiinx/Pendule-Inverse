from tkinter import *

#Fonctions

def deplacer(can, rect, x, sens) :
    x = x + sens*5
    if x == 40 :
        sens=-1
    if x == -40 :      
        sens=1
    can.move(rect, sens*5, 0)
    can.after(50, deplacer, can, rect, x, sens)

def creer_voiture():
    imgfile = 'Voiture.png'
    img = PhotoImage(file = imgfile)

    gifsdict={}
    gifsdict[imgfile] = img

    picture = img.subsample(5, 5) #reduire echelle de l'image
    return(picture)

#Main

root = Tk()

can = Canvas(root, width=1200, height=600)
can.grid()

picture=creer_voiture()
voiture=can.create_image(500,470,anchor=NW,image=picture)
deplacer(can, voiture, 0, 1)

root.mainloop()