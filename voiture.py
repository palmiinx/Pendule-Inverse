from tkinter import *
 
def deplacement():
    canvas.move(W_image,0,5)
   
    #On repete cette fonction
    root.after(40,deplacement)
 
root = Tk()

#chemin d'acces a l'image:
imgfile = 'Voiture.png'
# Utilisation d'un dictionnaire pour conserver une reference:
gifsdict={}

#Creation de l'image:
img = PhotoImage(file = imgfile)
gifsdict[imgfile] = img

#Creation du canvas:
canvas=Canvas(root,width = 500, height = 400 , bd=0, bg="white")
canvas.pack(padx=10,pady=10)

#Un exemple de reduction de l'image:
img_2 = img.subsample(2, 2)

#On cree le Widget image dans le canvas:
#NW=Nord West, le coin haut guche de l'image sera positionne a (10,10):
W_image=canvas.create_image(50,50,anchor=NW,image=img_2)

root.mainloop()